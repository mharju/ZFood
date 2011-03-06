
.. image:: http://play.taiste.fi/stuf/zfood_screenshot.png

ZFood is a simple service to store what you ate. Basically it's just a list of things with count, unit and description.

The input mechanism supports the following format::
    
    input ::= [metadata;]items
    metadata ::= @date
    date ::= [day.month.]hour[:minutes]
    items ::= item[,items]
    item ::= [count][unit] description

For example, if I ate some porridge, milk and some yoghurt for breakfast, I'd input::

    @8; 1glass milk, porridge, 2dl yoghurt

Data
----

The data is stored as plain-text CSV file that can be loaded to Numbers, Excel or other number crunching tool for
any post processing including graphing, clustering of different entries and such.The purpose of this application is 
to make inputting the data as quickly as possible, including mobile devices.

Further ideas
-------------

This idea can easily be extended in a way that the metadata part could contain a category so I'd be able to do lists of
any type with this. For example::

    @8 #shopping-list; 2l milk, 2 bananas, tomatoes, cucumber

Then there could be multiple views for each type of category (along with a default category).

Licence
-------

Licenced under MIT::

    Copyright (C) 2011 by Mikko Harju

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

