import pandas as pd

df = pd.read_excel('Aufgabe1_data.xlsx')

import matplotlib.pyplot as plt
import numpy as numpy
import matplotlib as mpl
import math

#### a)

sorted_Aus = sorted(df['Aus']) #descending sorted values

l = []
for i in range(0,1000): #values in thousands
    a = i/1000
    l.append(a)
l_flipped = l[::-1] #flip list



#### b)


lambda1 = 1000/sum(df['Aus'])
print(lambda1) # 4.136426290568794



l = []
for i in range(1000):
    y = math.exp(-lambda1 * (sorted_Aus[i]))
    l.append(y)

print(len(l))

#plot

fig, ax = plt.subplots() 
ax.plot(sorted_Aus, l_flipped) #a
ax.plot(sorted_Aus, l)  #b
ax.set_title("Kaplan-Meier Verteilung")
ax.set_ylabel("Prozentsatz: Überlebensrate")
ax.set_xlabel("Zeit")
plt.show()

#### c)


dfc = pd.read_excel('Aufgabe1_data_cens.xlsx') #data frame with census

dfc_sorted = sorted(dfc["Aus"])

data_filtered = []
for i in range(0,len(dfc_sorted)):
    if dfc_sorted[i]<0.249999:
        data_filtered.append(dfc_sorted[i])
print (len(data_filtered))

l_census = []
const = 661
for i in range(len(l_flipped)):
    if  i < const:
        l_census.append(l_flipped[i])

print(len(l_census))


#### d)

data_census = []
for i in range(1000):
    if i < const:
        data_census.append(data_filtered[i])
    else:
        data_census.append(data_filtered[const-1])
print(len(data_census))

lambda2 = const/(sum(data_filtered) + (1000-const) * 0.25)
print("lambda = "+str(lambda2))

l_lambda2 = []
for j in range (const):
    if j < const:
        erg = math.exp(-lambda2 * (dfc_sorted[j]))
        l_lambda2.append(erg)

# plot

fig, bx = plt.subplots()
bx.plot(data_filtered, l_census) #c
bx.plot(data_filtered, l_lambda2) #d
plt.show() 

