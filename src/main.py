import os.path
import base64
import re
import pandas as pd
from email import message_from_bytes
from datetime import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_messages(service, query):
    results = service.users().messages().list(userId='me', q=query, maxResults=100).execute()
    messages = results.get('messages', [])
    return messages

def parse_message(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()
    raw_data = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
    mime_msg = message_from_bytes(raw_data)

    subject = mime_msg['Subject'] or ''
    date = mime_msg['Date']
    sender = mime_msg['From']

    payload = mime_msg.get_payload(decode=True)
    body = ''
    if not payload:
        for part in mime_msg.walk():
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode(errors='ignore')
    else:
        body = payload.decode(errors='ignore')

    return {
        'subject': subject,
        'from': sender,
        'date': date,
        'body': body
    }

def extract_info(msg):
    body = msg['body'].lower()
    subject = msg['subject'].lower()

    company_match = re.search(r'at\s+([A-Z][a-zA-Z0-9&\-. ]+)', msg['subject'], re.IGNORECASE)
    company = company_match.group(1).strip() if company_match else msg['from']

    status = 'unknown'
    for keyword, label in {
        'thank you for applying': 'submitted',
        'we received your application': 'submitted',
        'we regret to inform': 'rejected',
        'unfortunately': 'rejected',
        'interview': 'interview',
        'schedule a call': 'interview',
        'move forward': 'interview',
        'offer': 'offer',
        'accepted': 'offer',
        'rejected': 'rejected',
    }.items():
        if keyword in body or keyword in subject:
            status = label
            break

    try:
        date_obj = datetime.strptime(msg['date'][:25], "%a, %d %b %Y %H:%M:%S")
    except Exception:
        date_obj = datetime.now()

    return {
        'Company': company,
        'Submit Date': date_obj.strftime('%Y-%m-%d'),
        'Status': status,
        'Subject': msg['subject']
    }

def main():
    service = authenticate_gmail()
    search_query = 'subject:(application OR interview OR rejected OR offer OR position)'
    messages = get_messages(service, search_query)

    print(f"Found {len(messages)} messages matching the query.")

    extracted_data = []
    for i, msg in enumerate(messages):
        print(f"Parsing message {i+1}/{len(messages)}...")
        parsed = parse_message(service, msg['id'])
        info = extract_info(parsed)
        extracted_data.append(info)

    df = pd.DataFrame(extracted_data)
    df.to_excel('job_applications.xlsx', index=False)
    print("Exported data to job_applications.xlsx")

if __name__ == '__main__':
    main()