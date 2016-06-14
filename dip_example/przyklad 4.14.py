#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import test

def output(data, format="text"):
    output_function = getattr(test, "output_%s" % format)
    return output_function(data)