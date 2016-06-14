#!/usr/bin/env python
# -*- coding: utf-8 -*-
d = {}
d["key"] = "value"
d["key"] = "other value"
d
{'key': 'other value'}
d["Key"] = "third value"
d
{'Key': 'third value', 'key': 'other value'}