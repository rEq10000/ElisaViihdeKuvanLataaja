import urllib.request
import os
import random

os.system("title ElisaViihdeKuvanLataaja")

f = open("Logo.txt", "r")
print(f.read())

print("Tervetuloa EVKuvanLataajaan")
print("HUOM! Kuvaa ei ladata jos sitä ei ole saatavilla.")
print("HUOM! Tämä ohjelmisto lataa vain pieniä kuvia. Jos haluat ladata isompia kuvia niin käytä EVKLBigPic.py")
print("")


while True:
    numba = input("Kirjoita ohjelman numerot: ")
    print("")

    ran = random.randint(10, 99)
    name = numba + "_" + str(ran) + "small.jpg"

    url = "http://thumbs.elisaviihde.fi/thumbnails/" + numba + ".jpg"

    urllib.request.urlretrieve(url, name)

    print("Valmista!")
    print(" ")