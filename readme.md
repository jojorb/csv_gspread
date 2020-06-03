![logo.png](https://miro.medium.com/max/1400/1*ytyKftHFa37Fcc-uEcYA-A.png)

# CSV to Google Spreadsheet ![GitHub][li-badge]

> Simple Python CSV to Google Spreadsheet export on run task

## Highlights

- Google API with service account private key
- Panda
- Add color tab on spreadsheet from hex color
- Bypass the raws data limitations from spreadsheet

## Install

```sh
$ cd csv_gspread
$ pip install -r requirements.txt
```

## Prerequisite

- Have a Google account
- [Create a project on Google Cloud Console](https://console.cloud.google.com/apis/credentials)
  - [Activate a service account credientials Google Cloud console](https://console.cloud.google.com/apis/credentials)
  - [Activate Google Services drive and sheet](https://console.cloud.google.com/apis/library)
  - Save your json private key to `creds/private_key.json`
  - copy your generated email for the private key
  - Inside you Google drive, create a spreadsheet to share with your creds email
  - copy the id of the spreadsheet (from the url)

```
# spreadsheet ID from url inside brackets pair
https://docs.google.com/spreadsheets/d/{4tZdjfPWOjhd4I-adeTe53Sfks9jcRkA3298fjd}/edit#gid=404311
```

## Usage

### Save Informations to `csv_gspread.py`

```js
PATH_TO_URL = "https://www.google.com/earth/outreach/data/sharksightings.csv"; // PATH TO DATA
PATH_TO_CSV = "test.csv"; // PATH TO DATA
SPREADSHEET_ID = "4tZdjfPWOjhd4I-adeTe53Sfks9jcRkA3298fjd"; // YOUR SPREADSHEET ID
WORKSHEET_NAME_1 = "some_test_2"; // YOUR SHEET TAB NAME 1
WORKSHEET_NAME_2 = "some_test_1"; // YOUR SHEET TAB NAME 2
```

### run the script

> No need to authorise the app, perfect for CRON task or cli usage

```sh
$ python3 csv_spread.py
```

## Maintainers

- [Roby Remzy][me]

[me]: https://github.com/RobyRemzy
[li-badge]: https://img.shields.io/github/license/RobyRemzy/csv_gspread
[ci-badge]: https://img.shields.io/circleci/build/github/RobyRemzy/csv_gspread?label=CircleCI
[codesandboxurl]: https://codesandbox.io/s/github/RobyRemzy/csv_gspread
