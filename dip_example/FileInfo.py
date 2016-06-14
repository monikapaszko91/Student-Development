class FileInfo(dict):
    u"przechowuje metadane pliku"
    def __init__(self, filename=None):
        dict.__init__(self)
        self["plik"] = filename