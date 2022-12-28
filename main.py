  #TASKS:
    #1. pokemon create
    #2. change pokemon name 
    #3. catch pokemon


import requests
import json
import pytest

#Functions
<<<<<<< HEAD

=======
>>>>>>> dde6f78043234fc934c1a6ef76ccd636e92c46ad
token = '028b145f7c73cfd327622973a500c87d'
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
<<<<<<< HEAD
response = requests.post(f'{URL}:{host}/trainers/add_pokeball', headers={'trainer_token' : token}, json={
        'pokemon_id' : 2780,
        })
print(response)
=======
response = requests.post(f'{URL}:{host}/trainers/addPokebol', headers={'trainer_token' : token}, json={
        'pokemon_id' : 1463,
        })
>>>>>>> dde6f78043234fc934c1a6ef76ccd636e92c46ad
