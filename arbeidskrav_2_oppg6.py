# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:30:16 2026

@author: Kadja
"""

#Plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10], med 200 punkter jevnt fordelt

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,200)
y = -x*2 - 5

plt.plot(x,y,color="red", linestyle="--")
plt.grid()
plt.xlabel("𝑓(𝑥) = −𝑥2 − 5")
plt.title("Arbeidskrav 2, oppgave 6")

