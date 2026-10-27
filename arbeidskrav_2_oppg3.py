# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:32:49 2026

@author: Kadja

Regner om grader til radianer oppgave 3, arbeidskrav 2
"""
import numpy as np

v_grad = float(input("Skriv inn gradtallet:")) #ber brukeren om vinkelen
v_rad = v_grad*np.pi/180 #omregning for radiantallet til vinkelen

print("Radiantallet til vinkelen er", v_rad)