from datetime import datetime
from slowrest import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/")
    assert response.json == "Welcome to slowrest!"


def test_day(client):
    response = client.get("/day/2019-03-10/47894757376282")
    print(f'response.json = {response.json}')
    assert response.json