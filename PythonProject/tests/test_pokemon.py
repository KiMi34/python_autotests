import requests
import pytest

host='https://api.pokemonbattle.me:9104'
token='9c9f4c508d82450e1a54f61e7fb2edb5'

def test_status_code():
     response=requests.get(f'{host}/trainers', params={'trainer_id':2605})
     assert response.status_code == 200

def test_trainer_name():
     response=requests.get(f'{host}/trainers', params={'trainer_id':2605})
     assert response.json()["trainer_name"]=="KiMi"

