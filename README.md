# pokedex
Hello everyone with this software helps you to fill a google spreadsheet with the information of de first 20 pokemons fetched with information from the pokeAPI

configure your token from the google project and create a new spreadsheet in google to fill it, once you have your token paste it on the current folder (where the dockerfile is ) to copy it on the container /var/tmp/src folder as key.json and rebuild from the image **rafafa81/pokedex** with the below dockerfile

Dockerfile:
```
FROM rafafa81/pokedex
COPY key.json /var/tmp/src/key.json
```
Command to run the script on creation:
```
sudo docker run pokedex python3 /var/tmp/src/main.py
```
