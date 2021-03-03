#libraries imported for the pokeapi
import requests
import json

#libraries imported for the google spread sheet modification
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#variables
pokeNumber=1
response_json={'name':None}
numberOfRows=20
dataPoints=['id','name','base_experience','height','weight']

#configuration for the connection to the sreadsheet
scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name("../testSheets-3547a5e53a01.json",scope)
client = gspread.authorize(creds)
sheet = client.open("pokedex").sheet1

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
        for ele in dataPoints:
            sheet.update_cell(pokeNumber,column,response_json[ele])
            column=column+1                    
        #-------------------------------------------- 
        
        pokeNumber=pokeNumber+1
        
    else:
        
        #in case the get request fails
        response_json['name']=""
        print("Failed to connect to pokeAPI")



