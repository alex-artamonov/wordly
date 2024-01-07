def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200

def test_game(client):
    response = client.get("/game")
    assert response.status_code == 200
