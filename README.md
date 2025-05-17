# py-job-tracker

tired of manually filling out spreadsheets to keep track of job applications? this tool will automate it!

## project structure

```
job-tracker/
├── .gitignore             # ignore credentials/token files
├── README.md              # project documentation
├── requirements.txt       # python dependencies
├── credentials.json       # Google API credentials (IGNORE IN VERSION CONTROL)
├── src/
│   ├── __init__.py
│   ├── main.py            # current script
│   ├── email_parser.py    # Email parsing logic - TODO
│   ├── gmail_client.py    # Gmail API wrapper - TODO
│   ├── data_processor.py  # data analysis & categorization - TODO
│   └── exporters/         # different export formats - TODO
│       ├── excel.py
│       └── json.py
├── tests/
│   ├── test_parser.py
│   └── test_client.py
└── outputs/               # generated reports
    ├── job_applications.xlsx
    └── historical/
```
