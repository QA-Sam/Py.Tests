import requests
import json
import pytest

#Functions

token = 'token'
URL = 'https://pokemonbattle.me'
host = 5000

#PokemonCreate
response = requests.post(f'{URL}:{host}/pokemons', headers={'trainer_token' : token}, json={
        'name' : 'Bulba',
        'photo' : 'https://static.wikia.nocookie.net/pokemon/images/6/60/588Karrablast.png/revision/latest?cb=20140329051922'
    })
print(response)

#ChangePokemon
response = requests.put(f'{URL}:{host}/pokemons', headers={'trainer_token' : token}, json={
        'pokemon_id' : 2780,
        'name' : 'Kluben',
        'photo' : 'https://static.wikia.nocookie.net/pokemon/images/d/d3/049Venomoth.png/revision/latest?cb=20140328194046'
    })
print(response)

#CatchPokemon
response = requests.post(f'{URL}:{host}/trainers/add_pokeball', headers={'trainer_token' : token}, json={
        'pokemon_id' : 2780,
        })
print(response)
