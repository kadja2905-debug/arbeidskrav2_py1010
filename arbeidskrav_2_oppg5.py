# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:28:35 2026

@author: Kadja
"""

#Oppg 5 - arealet og omkrets

import numpy as np

a = int(input("Skriv inn verdien til variabel a her:"))
b = int(input("Skriv inn verdien til variabel b her:"))

areal_sirkel = int(np.pi*(a/2)**2)
omkrets_sirkel = int(2*np.pi*(a/2))
areal_trekant = int(b*a/2)
omkrets_trekant = int(b + ((a**2 + b**2)**(1/2)))

print("Arealet til figuren er", areal_sirkel/2 + areal_trekant)
print("og omkrestsen er", omkrets_sirkel/2 + omkrets_trekant)
