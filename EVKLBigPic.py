import urllib.request
import os
import random

os.system("title ElisaViihdeKuvanLataaja")

f = open("Logo.txt", "r")
print(f.read())

print("Tervetuloa EVKuvanLataajaan")
print("HUOM! Kuvaa ei ladata jos sitä ei ole saatavilla.")
print("HUOM! Tämä ohjelmisto lataa vain isoja kuvia. Jos haluat ladata pieniä kuvia niin käytä EVKL.py")
print("")


while True:
    numba = input("Kirjoita ohjelman numerot: ")
    print("")

    ran = random.randint(10, 99)
    name = numba + "_" + str(ran) + "big.jpg"

    url = "http://thumbs.elisaviihde.fi/thumbnails/" + numba + "_655x368.jpg"

    
    try:
        urllib.request.urlretrieve(url, name)
    except:
        print("Kuvan lataus epäonnistui. Tarkista että numerot ovat oikein.")
        print("")
    else:
        print("Valmista!")
        print(" ")