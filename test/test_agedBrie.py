from src.domain.items.agedBrie import AgedBrie
import pytest



@pytest.fixture
def store():
    item = AgedBrie("Aged Brie", 2, 0)
    return item

@pytest.mark.agedBrie
def test_aged_brie(store):

    '''
    We reate variables with the different states of the AgedBrie object 
    over the days that are provided in the file report.txt
    '''

    day_one      =   AgedBrie("Aged Brie", 1, 1)
    day_two      =   AgedBrie("Aged Brie", 0, 2)
    day_three    =   AgedBrie("Aged Brie", -1, 4)
    day_four     =   AgedBrie("Aged Brie", -2, 6)
    day_five     =   AgedBrie("Aged Brie", -3, 8)
    day_six      =   AgedBrie("Aged Brie",-4, 10)

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