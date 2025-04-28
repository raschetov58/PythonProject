import requests
import pytest

'''response = requests.get('https://belarusbank.by/api/kredits_info')

print(response.text)'''

def test_statur_code():
    response = requests.get('https://belarusbank.by/api/kredits_info')
    assert response.status_code == 400
    print(response.text)

def test_piece_body ():
    response = requests.get('https://belarusbank.by/api/kredits_info', params = {'type':'потребительский'})
    assert response.status_code == 200

    '''assert response.json()['type'] == 'потребительский'''

'''@pytest.mark.parametrize('key, value', [('type','потребительский'),('val_key', 'BYN')])'''