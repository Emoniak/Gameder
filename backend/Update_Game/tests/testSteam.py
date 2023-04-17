import json
import pytest

from api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_ListGame(client):
    response = client.get('/steam/ListGame/12345')
    assert response.status_code == 200
    assert b"games" in response.data

def test_SetGameToFirestore(client):
    data = {
        "steamid": "12345",
        "userid": "user1"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = client.post('/steam/UpdateGame', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert b"Data update with sucess" in response.data
