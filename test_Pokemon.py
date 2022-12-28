#Tasks
    # 1. request get.trainers == 200
    # 2. response with a name of trainer

#Functions
token = '028b145f7c73cfd327622973a500c87d'

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
