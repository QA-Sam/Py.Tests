  #TASKS:
    #1. pokemon create
    #2. change pokemon name 
    #3. catch pokemon


import requests
import json

#Functions
token = '028b145f7c73cfd327622973a500c87d'
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
