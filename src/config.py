# all constants and configurations in one place
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

STATUS_KEYWORDS = {
    'submitted': ['thank you for applying', 'we received your application'],
    'rejected': ['we regret to inform', 'unfortunately', 'rejected'],
    'interview': ['interview', 'schedule a call', 'move forward'],
    'offer': ['offer', 'accepted']
}

# TODO: add other configs like date formats, regex patterns etc here