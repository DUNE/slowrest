from datetime import datetime
from slowrest import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/")
    assert response.json == "Welcome to slowrest!"


#def test_hash(client):
#    response = client.get("/hash/sce/1.0/5844")
#    assert response.json == "/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root"
#    response = client.get("/hash/sce/4.0/5844")
#    assert response.json == "/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root"





