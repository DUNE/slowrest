from tagrest import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"


def test_hash(client):
    response = client.get("/1.0/sce/50848")
    assert response.data == b'"HASH"\n'
