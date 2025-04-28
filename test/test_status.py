import requests
import pytest

def test_statur_code():
    response = requests.get('https://belarusbank.by/api/kredits_info')
    assert response.status_code == 400