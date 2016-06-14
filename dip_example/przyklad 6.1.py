fsock = open("/niemapliku", "r")
try:
    fsock = open("C:\Users\Monika\Desktop\Egzamin_Terminy.txt")
except IOError:
    print "Plik nie istnieje"
print "Ta linia zawsze zostanie wypisana"
