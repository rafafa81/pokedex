#libraries imported for the pokeapi
import requests
import json

#libraries imported for the google spread sheet modification
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#miscelanea de modulos importados
import datetime

#variables
pokeNumber=1
response_json={'name':None}
numberOfRows=20
dataPoints=['id','name','base_experience','height','weight']
gspreadSheetName='pokedex'
jsonGoogleKeyName='testSheets-3547a5e53a01.json'

#configuration for the connection to the sreadsheet
scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name("../{0}".format(jsonGoogleKeyName),scope)
client = gspread.authorize(creds)
sheet = client.open(gspreadSheetName).sheet1

#loop to retrieve the information of every pokemon
### important - delete the limiter pokeNumber of the while condition 
while response_json['name'] != "" and pokeNumber <= numberOfRows:
    httpsURL='https://pokeapi.co/api/v2/pokemon/{0}/'.format(pokeNumber)
    response=requests.get(httpsURL)
    if response.status_code==200 :
        response_json=json.loads(response.text)

        #below information will be changed as needed
        #-------------------------------------------- 
        #sheet.update_cell(1,1,response_json['name'])
        column=1
        actualizarFecha=False
        for ele in dataPoints:
            timeUpdated=str(datetime.datetime.today())
            if pokeNumber == 1:
                sheet.update_cell(pokeNumber,column,dataPoints[column-1])
            if sheet.cell(1,2).value != response_json[ele]:
                sheet.update_cell(pokeNumber+1,column,response_json[ele])
                column=column+1
                actualizarFecha=True
            if actualizarFecha and pokeNumber != 1:
                sheet.update_cell(pokeNumber,(len(dataPoints))+1,timeUpdated)
            
        #-------------------------------------------- 
        
        pokeNumber=pokeNumber+1
        
    else:
        
        #in case the get request fails
        response_json['name']=""
        print("Failed to connect to pokeAPI")



