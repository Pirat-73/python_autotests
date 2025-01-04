import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ea4f4ec9974dd4633e6686280dbfeda9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "prisukhin73@mail.ru",
    "password": "Iloveqa1"
}
body_activation = {
    "trainer_token": TOKEN
}
body_pokemon_create = {
    "name": "КИН Конг",
    "photo_id": 5
}
#response = requests.post(url= f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
#print (response.text)
'''response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email', headers = HEADER, json = body_activation) 
print (response_confirmation.text)'''

response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_pokemon_create) 
print (response_create.text)

message = response_create.json()['message']
print(message)