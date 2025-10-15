"""
MostOften


__init__
-> instantiates and gives the starting list
-> is starting_list a list? []
-> what type is each item?


add_new
-> check what the new item is // is it a valid item? 
-> len(list) before == 1 less than len(list) after
-> validate new_item == item_list[-1]

get_most_often
-> store a list
-> goes through the hole list -> loop test
-> needs a place to store the count -> is the output the 
same as the expected output 
outputs 
    1) the highest 
    2) "no clear winner"
"""
from lib.most_often import *

#__init__
def test_MostOften_initantiates():
    list = []
    mo = MostOften(list)
    assert isinstance(mo, MostOften)

def test_MostOften_starting_list_is_a_list():
    test_list = []
    mo = MostOften(test_list)
    assert isinstance(mo.starting_list, list)

def test_MostOften_start_state():
    test_list = [1, 2, 3]
    mo = MostOften(test_list)
    assert len(mo.starting_list) == 3


#add_new
def test_MostOften_add_new_one_more():
    test_list = [1, 2, 3]
    new_item = [4]
    mo = MostOften(test_list)
    mo.add_new(new_item)
    assert len(test_list) == 4

def test_MostOften_add_new_several_more():
    test_list = [1, 2, 3]
    new_item = 4
    new_item2 = 5


    mo = MostOften(test_list)

    mo.add_new(new_item)

    mo.add_new(new_item2)

    assert len(test_list) == 5