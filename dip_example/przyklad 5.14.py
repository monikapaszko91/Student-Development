
class FileInfo(dict):
    u"przechowuje metadane pliku"
    def __init__(self, filename=None):
        dict.__init__(self)
        self["plik"] = filename

class MP3FileInfo():
    def setitem (self, key, item):
        if key == "plik" and item:
            self. parse(item)
            FileInfo. setitem (self, key, item)