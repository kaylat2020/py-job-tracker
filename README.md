# pyJobTracker

tired of manually filling out spreadsheets to keep track of job applications?
this tool will automate it!

## help needed!

Are you a skilled dev looking to contribute? 

## project structure

```
py-job-tracker/
├── .gitignore             # ignore credentials/token files
├── README.md              # project documentation
├── requirements.txt       # python dependencies
├── credentials.json       # Google API credentials (IGNORE IN VERSION CONTROL)
├── src/
│   ├── __init__.py
│   ├── main.py            # current script
│   ├── gmail_client.py    # Gmail API wrapper
│   ├── config.py          # constants and configurations - TODO
│   └── exporters/         # different export formats - TODO
│       └── excel.py
├── tests/
│   ├── test_parser.py
│   └── test_client.py
└── outputs/               # generated reports
    ├── job_applications.xlsx
    └── historical/
```

## setup & run


