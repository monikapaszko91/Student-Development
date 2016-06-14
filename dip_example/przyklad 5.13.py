import FileInfo
f = FileInfo.FileInfo("C:\Users\Monika\Downloads\jutro.mp3")
f
print f
f.__setitem__("gatunek", 31)
print f
f["gatunek"] = 32
print f