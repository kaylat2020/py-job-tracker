# Job Application Tracker 📊✉️
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![CI Status](https://github.com/kaylat2020/py-job-tracker/actions/workflows/ci.yml/badge.svg)](https://github.com/kaylat2020/py-job-tracker/actions)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

email analyzer that tracks job applications, rejections, and interviews.

## 🚀 quick start

```bash
git clone https://github.com/kaylat2020/py-job-tracker.git
cd py-job-tracker
pip install -e .
py-job-tracker --help
```

## 🤝 help wanted

We welcome contributions! Please read our:

- [Contribution Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

**Maintainer**: @kaylat2020
**Response Time**: I typically review PRs within 3 business days !

## 🛠️ development setup

See the [development guide](docs/DEVELOPMENT.md) for advanced configuration.

## 🌟 contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Ziggens"><img src="https://avatars.githubusercontent.com/u/73198537?v=4?s=100" width="100px;" alt="Zach"/><br /><sub><b>Zach</b></sub></a><br /><a href="https://github.com/kaylat2020/py-job-tracker/commits?author=Ziggens" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!