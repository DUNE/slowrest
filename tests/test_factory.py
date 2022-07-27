from datetime import datetime
from tagrest import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"


def test_hash(client):
    response = client.get("/hash/1.0/sce/5844")
    assert response.data == b'"/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root"\n'
    response = client.get("/hash/2.0/sce/5844")
    assert response.data == b'"/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root"\n'


def test_payload(client):
    response = client.get("/payload/dasflksad")
    decoded = bytes.fromhex(str(response.json)).decode('utf-8')
    assert decoded == '1.542007e+09   94.606321  33.542739  4.918960e+02'


def test_tag_map(client):
    response = client.get("/tagmap/2.0")
    print(f'response.json = {response.json}')
    assert response.json


def test_global_tag(client):
    response = client.get("/globaltag/2.0")
    print(f'response.json = {response.json}')
    assert response.json == {'sce': '4.0', 'lifetime': '2.0'}


def test_fast_tag_map(client):
    response = client.get("/fasttagmap/2.0")
    print(f'response.json = {response.json}')
    assert response.json


def test_fast_and_slow_tag_map(client):
    assert client.get("/tagmap/2.0").json == client.get("/fasttagmap/2.0").json


def test_fast_vs_slow_tag_map(client):
    t_0 = datetime.now()
    slow_response = client.get("/tagmap/2.0")
    print(f'slow resp took {datetime.now()-t_0}')
    t_0 = datetime.now()
    fast_response = client.get("/fasttagmap/2.0")
    print(f'fast resp took {datetime.now()-t_0}')
    assert fast_response.json == slow_response.json