from src.repository.apiDB import connection_database

import pytest

@pytest.mark.connectionDatabase
def test_conection_db():
    assert connection_database() != None
    assert connection_database().status_code == 200 