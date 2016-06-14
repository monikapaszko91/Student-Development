#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open("C:\Users\Monika\Desktop\Egzamin_Terminy.txt")
print f
print f.tell()
print f.seek(-128, 2)
f.tell()
tagData = f.read(128)
print tagData
print f.tell()