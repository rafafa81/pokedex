import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']

creds = ServiceAccountCredentials.from_json_keyfile_name("../testSheets-3547a5e53a01.json",scope)

client = gspread.authorize(creds)

'''service = build('sheets', 'v4', credentials=creds)

spreadsheet = {
    'properties': {
        'title': 'pokedex' 
    }
}
spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                    fields='spreadsheetId').execute()'''

sheet = client.open("pokedex")

try:
    newSheet = sheet.add_worksheet(title='new', rows='100',cols='100')
except gspread.exceptions.APIError as e:
        print(e)
wsheet = sheet.worksheet('new')
wsheet.update_cell(1,1,"volv")





