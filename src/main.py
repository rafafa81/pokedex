#libraries imported for the pokeapi
import requests
import json

#libraries imported for the google spread sheet modification
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#miscelanea de modulos importados
import datetime
import time

#variables
pokeNumber=1
response_json={'name':None}
numberOfRows=20
dataPoints=['id','name','base_experience','height','weight']
gspreadSheetName='pokedex'
jsonGoogleKeyName='testSheets-3547a5e53a01.json'
sleepTime=2
gSheetNum=1
pageCounter=1



#configuration for the connection to the sreadsheet
scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name("../{0}".format(jsonGoogleKeyName),scope)
client = gspread.authorize(creds)
sheet = client.open(gspreadSheetName)

#loop to retrieve the information of every pokemon
### important - delete the limiter pokeNumber of the while condition

while response_json['name'] != "": 
    try:
        wsheet=sheet.worksheet('Hoja{0}'.format(gSheetNum))
        time.sleep(sleepTime)
        httpsURL='https://pokeapi.co/api/v2/pokemon/{0}/'.format(pokeNumber)
        response=requests.get(httpsURL)
    except Exception:
        print("hubo un error de timeout con la pokeapi")
    if response.status_code==200 :
        response_json=json.loads(response.text)

        #below information will be changed as needed
        #-------------------------------------------- 
        #sheet.update_cell(1,1,response_json['name'])
        column=1
        actualizarFecha=False
        for ele in dataPoints:
            timeUpdated=str(datetime.datetime.today())
            try:
                    vTmpPoke=str(wsheet.cell(pageCounter+1,column).value)
                    #time.sleep(sleepTime)
            except Exception:
                    print("google spreeadsheet max write limit")
                    break
            if pageCounter == 1:
                try:
                    time.sleep(sleepTime+2)
                    wsheet.update_cell(pageCounter,column,dataPoints[column-1].capitalize())
                    #time.sleep(sleepTime)
                except Exception:
                    print("google spreeadsheet max write limit")
                    break
            if vTmpPoke != str(response_json[ele]) :
                try:                 
                    wsheet.update_cell(pageCounter+1,column,response_json[ele])
                    #time.sleep(sleepTime)                  
                except Exception:
                    print("google spreeadsheet max write limit")
                    break
                actualizarFecha=True
            if actualizarFecha and ele == 'weight':
                if pageCounter == 1:
                    wsheet.update_cell(pageCounter,(len(dataPoints))+1,"Last Update")
                try:
                    wsheet.update_cell(pageCounter+1,(len(dataPoints))+1,timeUpdated)
                    #time.sleep(sleepTime)
                except Exception:
                    print("google spreeadsheet max write limit")
                    break
            column=column+1               
        #-------------------------------------------- 
        pageCounter=pageCounter+1
        if pokeNumber % numberOfRows == 0 :
            gSheetNum=gSheetNum+1
            try:
                time.sleep(sleepTime+2)
                newSheet= sheet.add_worksheet(title='Hoja{0}'.format(gSheetNum),rows=100,cols=100)
                pageCounter=1
            except Exception:
                print("The spreadshet already exist")
                pageCounter=1
        pokeNumber=pokeNumber+1
        time.sleep(sleepTime)
        print(pageCounter)
    else:
        
        #in case the get request fails
        response_json['name']=""
        print("Failed to connect to pokeAPI")



