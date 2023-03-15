from src.domain.items.agedBrie import AgedBrie
import pytest



@pytest.fixture
def store():
    item = AgedBrie("Aged Brie", 2, 0)
    return item

@pytest.mark.agedBrie
def test_agedBrie(store):

    '''
    We reate variables with the different states of the AgedBrie object 
    over the days that are provided in the file report.txt
    '''

    dayOne      =   AgedBrie("Aged Brie", 1, 1)
    dayTwo      =   AgedBrie("Aged Brie", 0, 2)
    dayThree    =   AgedBrie("Aged Brie", -1, 4)
    dayFour     =   AgedBrie("Aged Brie", -2, 6)
    dayFive     =   AgedBrie("Aged Brie", -3, 8)
    daySix      =   AgedBrie("Aged Brie",-4, 10)

    '''
    we update once for each day it spends in the inventory 
    and check that it matches the result of the report.txt
    '''
    # update Day 1
    store.updateQuality()
    assert repr(store) == repr(dayOne)

    # update Day 2
    store.updateQuality()
    assert repr(store) == repr(dayTwo)

    # update Day 3
    store.updateQuality()
    assert repr(store) == repr(dayThree)

    # update Day 4
    store.updateQuality()
    assert repr(store) == repr(dayFour)

    # update Day 5
    store.updateQuality()
    assert repr(store) == repr(dayFive)

    # update Day 6
    store.updateQuality()
    assert repr(store) == repr(daySix)
