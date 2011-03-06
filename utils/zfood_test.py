# -*- coding: utf-8 -*-

import zfood    
from datetime import datetime, timedelta

def test_item_split():
    items = zfood.parse(u'leipä, 2dl olutmainen juomasekoitus')
    assert len(items) == 2
    assert items[0].item == u'leipä'

    assert items[1].item == u'olutmainen juomasekoitus', 'invalid items'
    assert items[1].count == 2, 'invalid count'
    assert items[1].unit == u'dl', 'invalid unit'

def test_item_format():
    items = zfood.parse(u'1 leipä')

    assert len(items) == 1
    assert items[0].item == u'leipä', 'invalid item'
    assert items[0].count == 1, 'invalid count'
    assert items[0].unit == u'', 'invalid unit'

    items = zfood.parse(u'2m laku')
    assert len(items) == 1, 'invalid number of items'
    assert items[0].item == u'laku', 'invalid item'
    assert items[0].count == 2, 'invalid count'
    assert items[0].unit == u'm', 'invalid unit'

    items = zfood.parse(u'chicken tikka masala')
    assert len(items) == 1, 'invalid number of items'
    assert items[0].item == u'chicken tikka masala', 'invalid item'
    assert items[0].count == 1, 'invalid count'
    assert items[0].unit == u'', 'invalid unit'
    
def test_date_time():
    def _base_assertions(items):
        assert len(items) == 2, 'invalid number of items'
        assert items[0].item == u'leipä', 'invalid first item'
        assert items[1].item == u'kalaa', 'invalid second item'

        for item in items:
            assert item.at == expected_date, 'invalid date. expected %s got %s' % (expected_date, item.at)

    items = zfood.parse(u'@12; 1 leipä, 2 kalaa')
    today = datetime.now()
    expected_date = datetime(year=today.year, month=today.month, day=today.day, hour=12)

    _base_assertions(items)

    items = zfood.parse(u'@12:30; 1 leipä, 2 kalaa')

    expected_date = expected_date + timedelta(minutes=30)
    _base_assertions(items)

    expected_date = expected_date + timedelta(days=-1)
    items = zfood.parse(u'@%d.%d.12:30; 1 leipä, 2 kalaa' % (expected_date.day, expected_date.month,))
    _base_assertions(items)

def test_store_and_read():
    today = datetime.now()
    expected_date = datetime(year=today.year, month=today.month, day=today.day, hour=12)
    items = zfood.parse(u'@12; 1 leipä, 2 kalaa, 33cl olutta, 1plo viiniä')

    zfood.store(items, filename='zfood_test.csv', mode='w')
    items = zfood.read(filename='zfood_test.csv') 

    assert len(items) == 4, 'invalid item count expected 4 got %d' % (len(items),)
    assert items[0].item == u'leipä', 'invalid first item %s' % (items[0].item,)
    assert items[1].item == u'kalaa', 'invalid second item'
    assert items[2].item == u'olutta', 'invalid second item'
    assert items[3].item == u'viiniä', 'invalid second item'
    for item in items:
        assert item.at == expected_date

def test_store_and_remove():
    items = zfood.parse(u'leipä, olut')
    assert items[0].id == 0

    zfood.store( items, filename='zfood_test.csv', mode='w')
    assert items[0].id == 1, 'invalid id'
    assert items[1].id == 2, 'invalid id'

    zfood.remove(items[0].id, filename='zfood_test.csv')
    items = zfood.read( filename='zfood_test.csv' )

    assert len(items) == 1
    assert items[0].item == u'olut'
