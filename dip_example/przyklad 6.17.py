import os
print os.path.split("c:\\music\\ap\\mahadeva.mp3")
(filepath, filename) = os.path.split("c:\\music\\ap\\mahadeva.mp3")
print filepath
print filename
(shortname, extension) = os.path.splitext(filename)
print shortname
print extension
