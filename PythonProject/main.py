import requests

host='https://api.pokemonbattle.me:9104'
token='9c9f4c508d82450e1a54f61e7fb2edb5'

response = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, 
    headers={"Content-Type":"application/json","trainer_token":token})

print (response.status_code)
print(response.text)

response = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "12492",
    "name": "generate",
    "photo": "generate"
}, 
    headers={"Content-Type":"application/json","trainer_token":token})

print (response.status_code)
print(response.text)

response = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "12492"
}, 
    headers={"Content-Type":"application/json","trainer_token":token})

print (response.status_code)
print(response.text)
