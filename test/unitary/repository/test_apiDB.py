from src.repository.apiDB import read_items, read_item

import json
import pytest

@pytest.mark.connectionDatabase
def test_conection_db():

    assert read_items() != None
    assert read_items().status_code == 200
    

def test_read_item():

    assert read_item("+5 Dexterity Vest") == [{"_id": "64124bcb1d1c607ae6239ddd", "name": "+5 Dexterity Vest", "quality": 20, "sell_in": 10}]
