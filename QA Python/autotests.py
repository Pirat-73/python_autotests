import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ea4f4ec9974dd4633e6686280dbfeda9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
Trainer_ID = '24120'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_ID} )
    assert response.status_code == 200

def test_trainer_id ():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_ID} )
    assert response_get.json()["data"][0]["trainer_id"] == Trainer_ID


#def test_status_code():
 #   response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_ID} )

  #  assert response.status_code == 200

#'{"status":"success","data":[{"id":"175746","name":"BIG BOY","stage":"1","photo_id":3,"attack":1,"trainer_id":"24120","status":0,"in_pokeball":0},{"id":"175744","name":"Фрэнк","stage":"1","photo_id":9,"attack":1,"trainer_id":"24120","status":1,"in_pokeball":0},{"id":"175515","name":"КИН Конг","stage":"1","photo_id":5,"attack":1,"trainer_id":"24120","status":1,"in_pokeball":0},{"id":"175514","name":"КИН Конг","stage":"1","photo_id":5,"attack":1,"trainer_id":"24120","status":0,"in_pokeball":0},{"id":"175513","name":"КИН Конг","stage":"1","photo_id":5,"attack":1,"trainer_id":"24120","status":0,"in_pokeball":0},{"id":"175512","name":"КИН Конг","stage":"1","photo_id":5,"attack":1,"trainer_id":"24120","status":0,"in_pokeball":0},{"id":"175511","name":"КИН Конг","stage":"1","photo_id":5,"attack":1,"trainer_id":"24120","status":0,"in_pokeball":0},{"id":"175508","name":"КИН Конг","stage":"1","photo_id":5,"attack":1,"trainer_id":"24120","status":1,"in_pokeball":0}],"next_page":false}'