#!/bin/python
import urllib

for i in range(1, 252):
    nr = str(i)
    if len(nr) == 1:
        nr = "00"+nr
    if len(nr) == 2:
        nr = "0"+nr
    url = "http://serebii.net/pokemongo/pokemon/"+nr+".png"

    urllib.urlretrieve(url, str(i)+".png")
