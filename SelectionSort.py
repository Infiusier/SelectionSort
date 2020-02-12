import matplotlib.pyplot as plt
import numpy as np
import random
import time

lista=[]
tamanhos=[1000,10000,30000,60000]
tempos=[]
def geraLista(tamanho):
  x=[]
  while(len(x)<tamanho):
    j=random.randrange(tamanho)
    if j not in x:
      x.append(j)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def selectionsort(lista):
    now=time.time()
    n = len(lista)
    for i in range(n):
        x=lista[i]
        menor=x
        for j in range(i,n,1):
          if menor>lista[j]:
            menor=lista[j]
        if(menor<x):
          lista[lista.index(menor)]=x
          lista[i]=menor
    then=time.time()
    return (then-now)


for i in tamanhos:
  lista=geraLista(i)
  #lista=geraListaPiorCaso(i)
  tempo=selectionsort(lista)
  tempos.append(tempo)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
plt.savefig("CasoMedio")

