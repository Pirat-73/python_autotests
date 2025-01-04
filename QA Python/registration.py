import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '235f4c69def02ada6473a4ff2ff705e4'
HEADER = {'Content-Type' : 'application/json'}
body_registration = {
    "trainer_token": TOKEN,
    "email": "mail",
    "password": "password"
}

response = requests.post(url= f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print (response)