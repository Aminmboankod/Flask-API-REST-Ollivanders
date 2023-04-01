from src.repository.apiDB import inventory, item_db
import pytest

@pytest.mark.connectionDB
def test_conection_db():

    assert inventory() != None
    
   