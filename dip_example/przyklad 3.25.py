#!/usr/bin/env python
# -*- coding: UTF-8 -*-

uid = "sa"
pwd = "secret"
print pwd + " nie jest poprawnym haslem dla" + uid
print "%s nie jestpoprawnym haslem dla %s" % (pwd, uid)
userCount = 6
print "Users connected: %d" % (userCount, )
print "Users connected: " + userCount