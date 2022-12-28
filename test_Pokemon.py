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
    if response.status_code == 200:
        print('okay')
    else:
        print('not ok')

def test_piece_of_body():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params= {'trainer_id' : '1141'})
    assert response.json()['trainer_name'] == 'Sam'

    print(response.text)
