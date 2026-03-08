# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 14:39:53 2026

@author: EL RAY KABSO
"""

import kagglehub
import pandas as pd 

diff = pd.read_csv("Smartphone_Usage_Productivity_Dataset_50000.csv")
print(diff.columns)
print(diff['Occupation'])
#nettoie la dataset