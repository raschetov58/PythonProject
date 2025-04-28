import requests
import pytest

def test_statur_code():
    response = requests.get('https://belarusbank.by/api/kredits_info')
    assert response.status_code == 200
    print(response.text)

def test_piece_body ():
    response = requests.get('https://belarusbank.by/api/kredits_info', params = {'kredit_type':'потребительский'})
    assert response.json()['kredit_type'] == 'на недвижимость'