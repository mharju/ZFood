# -*- coding: utf-8 -*-
import re
import os.path
import math
import csv
from datetime import datetime

class FoodItem(object):
    def __init__(self, item='', count=1, unit='', at=None, id=0):
        self.item = item
        if math.floor(count) == count:
            count = int(count)
        self.count = count
        self.unit = unit
        self.at = at
        self.id = id

    def as_list(self):
        return [self.at.strftime("%Y-%m-%d %H:%M"), self.count, self.unit.encode('utf-8'), self.item.encode('utf-8')]

    @staticmethod
    def from_list(list):
        self = FoodItem()
        self.at = datetime.strptime(list[0], "%Y-%m-%d %H:%M")
        self.count = float(list[1])
        if math.floor(self.count) == self.count:
            self.count = int(self.count)
        self.unit = unicode(list[2].decode('utf-8'))
        self.item = unicode(list[3].decode('utf-8'))

        return self

class Metadata(object):
    def __init__(self, date):
        self.date = date
        
def parse(str):
    def _process_metadata(meta):
        meta_items = map(unicode.strip, meta.split(' '))
        for meta_item in meta_items:
            if '@' in meta_item:
                year, month, day, hour, minute = datetime.now().timetuple()[:5]
                datestr = meta_item[1:]

                try:
                    hour = int(datestr)
                    minute = 0
                except ValueError:
                    if '.' in datestr:
                        day, month, rest = datestr.split('.')
                        day = int(day)
                        month = int(month)
                        if rest:
                            datestr = rest.strip()
                            
                    if ':' in datestr:
                        hour, minute = map(int, datestr.split(':')) 

                date = datetime(year=year, month=month, day=day, hour=hour, minute=minute)


        return Metadata(date=date)

    def _construct_item(entry):
        data = entry.strip()

        if ' ' in data:
            count, item = data[:data.index(' ')], data[data.index(' ')+1:]
            match = re.match(r'(?P<count>(?:\d|\.)+)(?P<unit>.+)', count)
            if match:
                count = float(match.group('count'))
                unit = match.group('unit')
            else:
                unit = ''
                try:
                    count = float(count)
                except ValueError:
                    item = ' '.join([count, item]) 
                    count = 1
        else:
            count, unit, item = 1, '', data

        return FoodItem(item=item, count=count, unit=unit, at=date)

    date = datetime.now()
    if ';' in str:
        meta, items = str.split(';')
        str = items.strip()
        metadata = _process_metadata(meta)
        if metadata.date:
            date = metadata.date 

    return [_construct_item(entry) for entry in str.split(',')]

def store(items, filename='zfood.csv', mode='a'):
    with open(filename, mode) as f:
        writer = csv.writer(f)
        for index, item in enumerate(items):
            writer.writerow( item.as_list() )
            item.id = index + 1

def read(filename='zfood.csv'):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        items = []
        for index, item in enumerate(reader):
            food = FoodItem.from_list( item )
            food.id = index + 1
            items.append( food ) 

        return items 

def remove(id, filename='zfood.csv'):
    data = open(filename, 'r').readlines()
    data.pop(id - 1)
    with open(filename,'w') as f:
        f.writelines(data)

