import requests
import json

#variables
pokeNumber=1
response_json={'name':None}

#loop to retrieve the information of every pokemon
### important - delete the limiter pokeNumber of the while condition 
while response_json['name'] != "" and pokeNumber <= 10:
    httpsURL='https://pokeapi.co/api/v2/pokemon/{0}/'.format(pokeNumber)
    response=requests.get(httpsURL)
    if response.status_code==200 :
        response_json=json.loads(response.text)

        #below information will be changed as needed
        #--------------------------------------------
        print(response_json['name'])
        #--------------------------------------------

        pokeNumber=pokeNumber+1
        
    else:
        
        #in case the get request fails
        response_json['name']=""
        print("Failed to connect to pokeAPI")



