# -*- coding: utf-8 -*-
import re
import os.path
import math
from datetime import datetime

class FoodItem(object):
    def __init__(self, item, count, unit, at=None):
        self.item = item
        if math.floor(count) == count:
            count = int(count)
        self.count = count
        self.unit = unit
        self.at = at

    @staticmethod
    def from_csv(data, at):
        count, unit, item = map(lambda x: x.strip("\n").strip('"'), data.split(','))
        return FoodItem(item=item, count=float(count), unit=unit, at=at)

    def __str__(self):
        return '%f,\"%s\",\"%s\"' % (self.count, self.unit, self.item,)
        
def split_items(str):
    def _construct_item(entry):
        data = entry.strip()
        if ' ' in data:
            count, item = data[:data.index(' ')], data[data.index(' ')+1:]
            match = re.match(r'(?P<count>(?:\d|\.)+)(?P<unit>\w+)', count)
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

        return FoodItem(item=item, count=count, unit=unit)

    return [_construct_item(entry) for entry in str.split(',')]

def store(data, date=None, filename='zfood.csv'):
    if not date:
        date = datetime.now()

    with open(filename, 'a') as f:
        f.write(date.strftime("\"%d.%m.%Y %H:%M:%S\""))
        f.write('\n')
        f.write('\n'.join([ 
            unicode(item).encode('utf-8') for item in split_items(data) ]))
        f.write('\n')

class Timeinfo(object): pass
def read(filename='zfood.csv'):
    timeinfo = Timeinfo()
    def _parse_items(lines):
        items = []
        if not getattr(timeinfo, 'at', None):
            timeinfo.at = lines[0].strip("\n").strip('"')

        try:
            line = lines.pop(0)
            food = FoodItem.from_csv(line, timeinfo.at)
            items.append(food)
        except Exception, e:
            timeinfo.at = line.strip("\n").strip('"')
        finally:
            return items

        return items

    items = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            while len(lines) > 0:
                items.extend( _parse_items(lines) )

    return items
