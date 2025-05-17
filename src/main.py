import base64
import re
from email import message_from_bytes
from datetime import datetime
from tqdm import tqdm

# Local imports
from gmail_client import authenticate_gmail, get_messages
from config import STATUS_KEYWORDS
from exporters.excel import export_to_excel

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
    """Categorize emails with configurable keywords"""
    body = msg['body'].lower()
    subject = msg['subject'].lower()

    company_match = re.search(r'at\s+([A-Z][a-zA-Z0-9&\-. ]+)', 
                            msg['subject'], re.IGNORECASE)
    company = company_match.group(1).strip() if company_match else msg['from']

    status = 'unknown'
    for status_type, keywords in STATUS_KEYWORDS.items():
        if any(keyword in body or keyword in subject for keyword in keywords):
            status = status_type
            break

    return {
        'Company': company,
        'Date': msg['date'],
        'Status': status,
        'Subject': msg['subject']
    }

def main():
    service = authenticate_gmail()
    if not service:
        return  # Exit if auth failed

    query = 'subject:(application OR interview OR rejected OR offer OR position)'
    messages = get_messages(service, query)

    print(f"Found {len(messages)} messages matching the query.")

    extracted_data = []
    for msg in tqdm(messages, desc="Processing emails"):
        parsed = parse_message(service, msg['id'])
        info = extract_info(parsed)
        extracted_data.append(info)

    export_to_excel(extracted_data)
    print("Export completed.")

if __name__ == '__main__':
    main()