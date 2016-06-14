
import FileInfo
try:
    fsock = open("C:\Users\Monika\Downloads\jutro.mp3", "rb", 0)
    try:
        fsock.seek(-128, 2)
        tagdata = fsock.read(128)
    finally:
        fsock.close()
except IOError:
    pass