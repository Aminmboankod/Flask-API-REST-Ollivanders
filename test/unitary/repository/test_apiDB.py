from src.repository.apiDB import inventario, item
import pytest

@pytest.mark.connectionDB
def test_conection_db():

    assert inventario() != None
    assert inventario().status_code == 200
    
@pytest.mark.read
def test_read_item():

    assert item("+5 Dexterity Vest") == [{"_id": "64124bcb1d1c607ae6239ddd", 
                                               "name": "+5 Dexterity Vest", 
                                               "quality": 20, 
                                               "sell_in": 10}]