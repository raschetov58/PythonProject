import requests
import pytest

def test_piece_body ():
    response = requests.get('https://belarusbank.by/api/kredits_info', params = {'type':'потребительский'})
    assert response.status_code == 200