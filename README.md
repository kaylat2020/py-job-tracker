# Job Application Tracker 📊✉️

Email analyzer that tracks and exports job applications, rejections, interviews, and offers.
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![CI Status](https://github.com/kaylat2020/py-job-tracker/actions/workflows/ci.yml/badge.svg?style=flat-square)](https://github.com/kaylat2020/py-job-tracker/actions)
[![License](https://img.shields.io/github/license/kaylat2020/py-job-tracker)](https://github.com/kaylat2020/py-job-tracker/blob/main/LICENSE)
![Commit Activity](https://img.shields.io/github/commit-activity/w/kaylat2020/py-job-tracker?logo=git)

*\*\*some links will be broken/blank for a bit, I'm working on it chief 🫡*


## 🚀 Quick Start

```bash
# install in dev mode
pip install -e .

# run the tool
job-tracker --help
```

## 🤝 Help Wanted

Contributions are welcome!

(I'm still learning so suggestions are welcome too)

- [Contribution Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

**Maintainer**: @kaylat2020

**Response Time**: I typically review PRs within 3 business days

## 🛠️ Development Setup

See the [development guide](docs/DEVELOPMENT.md) for advanced configuration. **

## Project Structure

```tree
py-job-tracker/
├── .gitignore             # ignore credentials/token files
├── docs                   # dev documentation - TODO
├── README.md              # project documentation
├── requirements.txt       # python dependencies
├── credentials.json       # Google API credentials (ignore)
├── src/
│   ├── __init__.py
│   ├── main.py            # current script
│   ├── gmail_client.py    # Gmail API wrapper
│   ├── config.py          # constants and configurations - TODO
│   └── exporters/         # different export formats
│       └── excel.py
│       └── csv.py
├── tests/
│   ├── test_parser.py     # pytests - TODO
│   └── test_client.py
└── outputs/               # generated reports
    ├── job_applications.xlsx
    └── historical/
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Ziggens"><img src="https://avatars.githubusercontent.com/u/73198537?v=4?s=100" width="100px;" alt="Zach"/><br /><sub><b>Zach</b></sub></a><br /><a href="https://github.com/kaylat2020/py-job-tracker/commits?author=Ziggens" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Sky313"><img src="https://avatars.githubusercontent.com/u/70432145?v=4?s=100" width="100px;" alt="Surya Govindarajan"/><br /><sub><b>Surya Govindarajan</b></sub></a><br /><a href="https://github.com/kaylat2020/py-job-tracker/commits?author=Sky313" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!
