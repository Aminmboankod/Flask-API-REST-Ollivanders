from src.domain.items.backstage import Backstage
import pytest



@pytest.fixture
def store():
    item_name_backstage = "Backstage passes to a TAFKAL80ETC concert"
    item = Backstage(item_name_backstage, 15, 20)
    return item

@pytest.mark.backstage
def test_backstage(store):

    '''
    We reate variables with the different states of the Backstage object 
    over the days that are provided in the file report.txt
    '''

    day_one      =   Backstage("Backstage passes to a TAFKAL80ETC concert", 14, 21)
    day_two      =   Backstage("Backstage passes to a TAFKAL80ETC concert", 13, 22)
    day_three    =   Backstage("Backstage passes to a TAFKAL80ETC concert", 12, 23)
    day_four     =   Backstage("Backstage passes to a TAFKAL80ETC concert", 11, 24)
    day_five     =   Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 25)
    day_six      =   Backstage("Backstage passes to a TAFKAL80ETC concert",  9, 27)

    '''
    we update once for each day it spends in the inventory 
    and check that it matches the result of the report.txt
    '''
    # update Day 1
    store.update_quality()
    assert repr(store) == repr(day_one)

    # update Day 2
    store.update_quality()
    assert repr(store) == repr(day_two)

    # update Day 3
    store.update_quality()
    assert repr(store) == repr(day_three)

    # update Day 4
    store.update_quality()
    assert repr(store) == repr(day_four)

    # update Day 5
    store.update_quality()
    assert repr(store) == repr(day_five)

    # update Day 6
    store.update_quality()
    assert repr(store) == repr(day_six)