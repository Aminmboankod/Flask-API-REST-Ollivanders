from src.domain.items.sulfuras import Sulfuras
import pytest



@pytest.fixture
def store():
    item = Sulfuras("Hand of Ragnaros", 0, 80)
    return item

@pytest.mark.sulfuras
def test_sulfuras(store):

    '''
    We reate variables with the different states of the Sulfuras object 
    over the days that are provided in the file report.txt
    '''

    day_one      =   Sulfuras("Hand of Ragnaros", 0, 80)
    day_two      =   Sulfuras("Hand of Ragnaros", 0, 80)
    day_three    =   Sulfuras("Hand of Ragnaros", 0, 80)
    day_four     =   Sulfuras("Hand of Ragnaros", 0, 80)
    day_five     =   Sulfuras("Hand of Ragnaros", 0, 80)
    day_six      =   Sulfuras("Hand of Ragnaros", 0, 80)

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



@pytest.mark.sulfurasNegative
def test_sulfuras_negative():
    
    #New store object with another properties
    store       =   Sulfuras("Hand of Ragnaros", -1, 80)


    '''
    We reate variables with the different states of the Conjured object 
    over
    '''    
    day_one      =   Sulfuras("Hand of Ragnaros", -1, 80)
    day_two      =   Sulfuras("Hand of Ragnaros", -1, 80)
    day_three    =   Sulfuras("Hand of Ragnaros", -1, 80)
    day_four     =   Sulfuras("Hand of Ragnaros", -1, 80)
    day_five     =   Sulfuras("Hand of Ragnaros", -1, 80)
    day_six      =   Sulfuras("Hand of Ragnaros", -1, 80)

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
