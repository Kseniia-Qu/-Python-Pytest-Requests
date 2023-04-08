import requests
import pytest
def test_trainers():
    token = 'cd680f7c9e18957a24239c15e4ec0718'
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id': 3422
    })
    assert response.status_code == 200


def test_name_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id': 3422
    })
    assert response.json()['trainer_name'] == 'Pola'
