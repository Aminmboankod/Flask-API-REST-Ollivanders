from src.domain.items.conjured import Conjured
import pytest



@pytest.fixture
def store():
    item = Conjured("Conjured Mana Cake", 3, 6)
    return item

@pytest.mark.conjured
def test_conjured(store):

    '''
    We reate variables with the different states of the Conjured object 
    over the days that are provided in the file report.txt
    '''

    dayOne      =   Conjured("Conjured Mana Cake", 2, 4)
    dayTwo      =   Conjured("Conjured Mana Cake", 1, 2)
    dayThree    =   Conjured("Conjured Mana Cake", 0, 0)
    dayFour     =   Conjured("Conjured Mana Cake", -1, 0)
    dayFive     =   Conjured("Conjured Mana Cake", -2, 0)
    daySix      =   Conjured("Conjured Mana Cake", -3, 0)

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
