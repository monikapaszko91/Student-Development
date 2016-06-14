def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


class Licznik:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count += 5

print type(Licznik)
Licznik = singleton(Licznik)
print type(Licznik)