import os
from .Google import Create_Service
from googleapiclient.http import MediaFileUpload

# FOLDER_PATH = 'googleclient.json'
CLIENT_SECRET_FILE = 'batch/googleclient.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

spreadsheet_id = '1G-91sja7vMo0-WashgDteDZUlC4f5FDOKU_7PW3H5_0'
mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
# print(mySpreadsheets)
worksheet_name = 'Sheet1'
cell_range_insert = 'B1'
def writedata(b):
    b = list(map(str, b))
    values = [b]
    print(values)
    value_range_body = {
        'majorDimension': 'ROWS',
        'values': values
    }

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        valueInputOption='USER_ENTERED',
        range=worksheet_name,
        body=value_range_body
    ).execute()




