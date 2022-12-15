# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:59:52 2022

@author: fariz
"""
import pandas as p

data = p.read_csv("Negara.csv")

df=p.DataFrame(data)
m= df.groupby(["Benua"]).mean()
s=df.groupby(["Benua"]).std()

print(df)
print(m)
print(s)