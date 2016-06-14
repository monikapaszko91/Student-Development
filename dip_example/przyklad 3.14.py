#!/usr/bin/env python
# -*- coding: utf-8 -*-
li = ['a', 'b', 'c']
li.extend(['d', 'e', 'f'])
print li
['a', 'b', 'c', 'd', 'e', 'f']
print len(li)

print li[-1]
li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])
print li
print len(li)
print li[-1]
