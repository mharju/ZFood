# -*- coding: utf-8 -*-

import zfood    

def test_item_split():
    items = zfood.split_items(u'leipä, 2dl olutmainen juomasekoitus')
    assert len(items) == 2
    assert items[0].item == u'leipä'

    assert items[1].item == u'olutmainen juomasekoitus', 'invalid items'
    assert items[1].count == 2, 'invalid count'
    assert items[1].unit == u'dl', 'invalid unit'

def test_item_format():
    items = zfood.split_items(u'1 leipä')

    assert len(items) == 1
    assert items[0].item == u'leipä', 'invalid item'
    assert items[0].count == 1, 'invalid count'
    assert items[0].unit == u'', 'invalid unit'

    items = zfood.split_items(u'2m laku')
    assert len(items) == 1, 'invalid number of items'
    assert items[0].item == u'laku', 'invalid item'
    assert items[0].count == 2, 'invalid count'
    assert items[0].unit == u'm', 'invalid unit'

    items = zfood.split_items(u'chicken tikka masala')
    assert len(items) == 1, 'invalid number of items'
    assert items[0].item == u'chicken tikka masala', 'invalid item'
    assert items[0].count == 1, 'invalid count'
    assert items[0].unit == u'', 'invalid unit'
    
def test_store():
    data = u'chicken tikka masala, intialainen tee, salaatti, ananas, herne, 2kpl leipä'
    zfood.store(data, filename='zfood_test.csv')
