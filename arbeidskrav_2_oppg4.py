# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:48:42 2026

@author: Kadja

Hente data fra dictionary/tabell. Oppgave 4, arbeidskrav 2 
"""
#delopp. a) Dictionary med land som nøkkel, og info om hovedstad med innbyggertall
data = {
        "Norge": ["Oslo", 0.634], 
            "England": ["London", 8.982], 
            "Frankrike": ["Paris", 2.161], 
            "Italia": ["Roma", 2.873] 
            }

#delopp b. Brukeren skriver et land og programmet skrive ut informasjon om hovedstaden
land = input("Hvilket land vil du dra til?")

hovedstad = data[land]
print(hovedstad[0], 'er hovedstad i', land, 'og det er', hovedstad[1], 'innbygerre i', hovedstad[0])

#delopp c. Nytt land, med hovedstad og antall innbyggere

land1 = input("Foreslå et land som ikke er på lista!")
hovedstad1 = input("Hva er hovedstaden i dette landet?")
innbyggere1 = input("Ha er antall innbyggere i dette landet?")

data[0]=land1
data[1]=hovedstad1
data[2]=innbyggere1
print (data)
