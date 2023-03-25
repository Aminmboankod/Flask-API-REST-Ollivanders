from src.domain.normalItem import NormalItem
import pytest



@pytest.fixture
def store():
    item = NormalItem("+5 Dexterity Vest", 10, 20)
    return item

@pytest.mark.normalItem
def test_normal_item(store):

    '''
    We reate variables with the different states of the normal object 
    over the days that are provided in the file report.txt
    '''

    day_one      =   NormalItem("+5 Dexterity Vest", 9, 18)
    day_two      =   NormalItem("+5 Dexterity Vest", 8, 16)
    day_three    =   NormalItem("+5 Dexterity Vest", 7, 14)
    day_four     =   NormalItem("+5 Dexterity Vest", 6, 12)
    day_five     =   NormalItem("+5 Dexterity Vest", 5, 10)
    day_six      =   NormalItem("+5 Dexterity Vest", 4, 8)

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
