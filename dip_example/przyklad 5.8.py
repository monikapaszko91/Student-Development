import FileInfo
def leakmem():
    f = FileInfo.FileInfo("C:\Users\Monika\Downloads\jutro.mp3")
    for i in range(100):
        leakmem()