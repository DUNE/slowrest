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
    assert type(response.json) is dict


def test_sensor_dict(client):
    response = client.get("/sensor-dict")
    assert type(response.json) is dict


def test_sensor_name(client):
    sensor_dict = client.get("/sensor-dict").json
    sensor_name = client.get("/sensor-name/47361543925275").json
    assert type(sensor_name) is str
    assert sensor_dict['47361543925275'] == sensor_name

def test_range(client):
    range_dict = client.get("/range/2021-10-10T07:42:12/2021-10-10T12:06:52/47363708158235")
    assert isinstance(range_dict.json, dict)
