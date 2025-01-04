import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ea4f4ec9974dd4633e6686280dbfeda9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
body_create = {
    "name": "Фрэнк",
    "photo_id": 9
}
body_change = {
    "pokemon_id": "175746",
    "name": "BIG BOY",
    "photo_id": 3
}
body_catch = {
    "pokemon_id": "175746"
}
#1)response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
#1)print (response_create.json)

#2)response_change = requests.put (url = f'{URL}/pokemons', headers= HEADER, json =body_change )
#2)print (response_change.json)

response_catch = requests.post ( url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_catch )
print( response_catch.text)