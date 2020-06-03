from creds_google import G_Service
import pandas as pd
import numpy as np
import re

# https://docs.google.com/spreadsheets/d/1rQ6zZKcRX25EEcdjI-adiG15go4XxmdTnoYZtXHTkKM/edit#gid=1456502765

SERVICE_ACCOUNT_FILE = 'creds/private_key.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

PATH_TO_URL = 'https://files.digital.nhs.uk/publicationimport/pub20xxx/pub20188/ccg-pres-data-oct-dec-2015-un-dat.csv'
PATH_TO_CSV = 'test.csv'
SPREADSHEET_ID = '1rQ6zZKcRX25EEcdjI-adiG15go4XxmdTnoYZtXHTkKM'
WORKSHEET_NAME_1 = 'some_test_2'
WORKSHEET_NAME_2 = 'some_test_1'

service = G_Service(SERVICE_ACCOUNT_FILE,
                    API_SERVICE_NAME, API_VERSION, SCOPES)

spreadsheets = service.spreadsheets()


def add_sheets(sheet_id, sheet_name, hx2rgb):
    def hex_to_rgb(hx):
        if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
            div = 255.0
            if len(hx) <= 4:
                return tuple(int(hx[i]*2, 16) / div for i in (1, 2, 3))
            else:
                return tuple(int(hx[i:i+2], 16) / div for i in (1, 3, 5))
        else:
            raise ValueError(f'"{hx}" is not a valid HEX code.')
    hls = hex_to_rgb(hx2rgb)
    try:
        request_body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': sheet_name,
                        'tabColor': {
                            'red': hls[0],
                            'green': hls[1],
                            'blue': hls[2]
                        }
                    }
                }
            }]
        }

        response = spreadsheets.batchUpdate(
            spreadsheetId=sheet_id,
            body=request_body
        ).execute()

        return response
    except Exception as e:
        print(e)


def df_sheets(file_path, sheet_id, sheet_name, sheet_cell):
    df = pd.read_csv(file_path)
    df.replace(np.nan, '', inplace=True)
    # using pasteData from the example above, you will have to use a combination of validate, update and append
    response_date = service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        valueInputOption='RAW',
        range=f"{sheet_name}!{sheet_cell}",
        body=dict(
            majorDimension='ROWS',
            values=df.T.reset_index().T.values.tolist())
    ).execute()


add_sheets(SPREADSHEET_ID, WORKSHEET_NAME_1, '#FF0000')
add_sheets(SPREADSHEET_ID, WORKSHEET_NAME_2, '#6495ED')

df_sheets(PATH_TO_URL, SPREADSHEET_ID, WORKSHEET_NAME_1, 'A1')
df_sheets(PATH_TO_CSV, SPREADSHEET_ID, WORKSHEET_NAME_2, 'A1')
