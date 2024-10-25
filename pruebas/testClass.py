#vista data frama con panda
import pandas as pd
# Columnas: features
data_0 = {'sexo': ['Masculino','Femenino','Otro'], 'codigo': [0,1,2], 'frecuencia': [5,6,2]}
pd_0 = pd.DataFrame(data=data_0)
pd_0

#vista dataframe con matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dias = ["L","M","M","J","V","S","D"]
temperaturas = {'BsAs': [28.5,30.5,31,30,28,27.5,30.5],'SantiagoDelEstero': [35,36,38,49,47,42,31]}
ax.plot(dias,temperaturas['BsAs'],color='tab:purple', label='Buenos Aires', marker="^")
ax.plot(dias,temperaturas['SantiagoDelEstero'],color='tab:green', marker='*',label='SantiagoDelEstero')

#pip install scipy
#pip install statsmodels -> works with panda i think