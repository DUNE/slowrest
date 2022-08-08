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
    assert type(response.json) is dict


def test_sensor_dict(client):
    response = client.get("/sensor-dict")
    assert type(response.json) is dict


def test_sensor_name(client):
    sensor_dict = client.get("/sensor-dict").json
    sensor_name = client.get("/sensor-name/47894757376282").json
    assert type(sensor_name) is str
    assert sensor_dict['47894757376282'] == sensor_name
