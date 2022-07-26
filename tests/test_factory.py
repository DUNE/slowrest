from tagrest import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"


def test_hash(client):
    response = client.get("/1.0/sce/5844")
    assert response.data == b'"/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root"\n'
    response = client.get("/2.0/sce/5844")
    assert response.data == b'"/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root"\n'


def test_payload(client):
    response = client.get("/payload/dasflksad")
    assert response.data == b'0\n'
