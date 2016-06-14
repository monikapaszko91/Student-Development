#!/usr/bin/env python
# -*- coding: utf-8 -*-
d = {"server":"mpilgrim", "database":"master"}
d
{'bazadanych': 'pubs', 'server': 'mpilgrim', 'uid': 'sa'}
d["licznik"] = 3
d
{'bazadanych': 'pubs', 'server': 'mpilgrim', 'licznik': 3,'uid': 'sa'}
d[42] = "douglas"
d
{42: 'douglas','bazadanych': 'pubs', 'server': 'mpilgrim', 'licznik': 3,'uid': 'sa'}

d
{'licznik': 3, 'bazadanych': 'master', 'server': 'mpilgrim', 42: 'douglas', 'uid': 'sa'}
del d[42]
d
{'licznik': 3, 'bazadanych': 'master', 'server': 'mpilgrim', 'uid': 'sa'}
d.clear()
d


