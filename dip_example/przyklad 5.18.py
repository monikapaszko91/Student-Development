class counter(object):
    count = 0 #(1)
    def __init__(self):
        self.__class__.count += 1
print counter
print  counter.count
c = counter()
print c.count
print counter.count
d = counter()
print d.count
print c.count
print counter.count