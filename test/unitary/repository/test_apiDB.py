from src.repository.apiDB import read_items

import pytest

@pytest.mark.connectionDatabase
def test_conection_db():

    assert read_items() != None
    assert read_items().status_code == 200 
