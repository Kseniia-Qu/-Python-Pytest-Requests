import requests
base_url = 'https://pokemonbattle.me:9104/'
token = 'cd680f7c9e18957a24239c15e4ec0718'
response_add_pokemon = requests.post(f'{base_url}pokemons', headers = {'trainer_token': token}, json = {
    "name": "{{Туц}}",
    "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/114.png"
})
print(response_add_pokemon.text)


response_change_name = requests.put(f'{base_url}pokemons', headers = {'trainer_token': token}, json = {
    "pokemon_id": "8832",
    "name": "Туцтуц"
})
print(response_change_name.text)


response_catch_in = requests.post(f'{base_url}trainers/add_pokeball', headers = {'trainer_token': token}, json = {
    "pokemon_id": "8832",
})
print(response_catch_in.text)