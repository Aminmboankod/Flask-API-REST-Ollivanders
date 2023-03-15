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

    dayOne      =   Sulfuras("Hand of Ragnaros", 0, 80)
    dayTwo      =   Sulfuras("Hand of Ragnaros", 0, 80)
    dayThree    =   Sulfuras("Hand of Ragnaros", 0, 80)
    dayFour     =   Sulfuras("Hand of Ragnaros", 0, 80)
    dayFive     =   Sulfuras("Hand of Ragnaros", 0, 80)
    daySix      =   Sulfuras("Hand of Ragnaros", 0, 80)

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



@pytest.mark.sulfurasNegative
def test_sulfurasNegative(store):
    
    #New store object with another properties
    store       =   Sulfuras("Hand of Ragnaros", -1, 80)


    '''
    We reate variables with the different states of the Conjured object 
    over
    '''    
    dayOne      =   Sulfuras("Hand of Ragnaros", -1, 80)
    dayTwo      =   Sulfuras("Hand of Ragnaros", -1, 80)
    dayThree    =   Sulfuras("Hand of Ragnaros", -1, 80)
    dayFour     =   Sulfuras("Hand of Ragnaros", -1, 80)
    dayFive     =   Sulfuras("Hand of Ragnaros", -1, 80)
    daySix      =   Sulfuras("Hand of Ragnaros", -1, 80)

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
