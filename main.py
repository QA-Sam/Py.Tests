  #TASKS:
    #1. pokemon create
    #2. change pokemon name 
    #3. catch pokemon


import requests
import json

#Functions
token = '66a6ec073dc3b97a43174e895d064c39'
URL = 'https://pokemonbattle.me'
host = 5000

#PokemonCreate
response = requests.post(f'{URL}:{host}/pokemons', headers={'trainer_token' : token}, json={
        'name' : 'Raichu',
        'photo' : 'https://w7.pngwing.com/pngs/937/801/png-transparent-pokemon-go-pokemon-battle-revolution-computer-icons-video-game-pokemon-go-game-video-game-pokemon.png'
    })

#ChangePokemon
response = requests.put(f'{URL}:{host}/pokemons', headers={'trainer_token' : token}, json={
        'pokemon_id' : 1463,
        'name' : 'Colossus',
        'photo' : 'https://w7.pngwing.com/pngs/937/801/png-transparent-pokemon-go-pokemon-battle-revolution-computer-icons-video-game-pokemon-go-game-video-game-pokemon.png'
    })


#CatchPokemon
response = requests.post(f'{URL}:{host}/trainers/addPokebol', headers={'trainer_token' : token}, json={
        'pokemon_id' : 1463,
        })