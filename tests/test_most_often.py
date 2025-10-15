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
-> needs a place to store the count -> is the output the same as the expected output 
outputs 
    1) the highest 
    2) "no clear winner"
"""
from lib.most_often import *

def test_MostOften_initantiates():
    list = []
    mo = MostOften(list)
    assert isinstance(mo, MostOften)

def test_MostOften_
