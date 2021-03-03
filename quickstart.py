import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']

creds = ServiceAccountCredentials.from_json_keyfile_name("../testSheets-3547a5e53a01.json",scope)

client = gspread.authorize(creds)

sheet = client.open("pokedex").sheet1



