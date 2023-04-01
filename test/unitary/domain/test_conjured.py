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

    day_one      =   Conjured("Conjured Mana Cake", 2, 4)
    day_two      =   Conjured("Conjured Mana Cake", 1, 2)
    day_three    =   Conjured("Conjured Mana Cake", 0, 0)
    day_four     =   Conjured("Conjured Mana Cake", -1, 0)
    day_five     =   Conjured("Conjured Mana Cake", -2, 0)
    day_six      =   Conjured("Conjured Mana Cake", -3, 0)

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
