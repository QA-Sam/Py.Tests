#Tasks
    # 1. request get.trainers == 200
    # 2. response with a name of trainer

#Functions
token = 'token'

import requests
import pytest
import json


def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    print(response)

def test_piece_of_body():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params= {'trainer_id' : '1602'})
    assert response.json()['trainer_name'] == 'Sam'

    print(response)
