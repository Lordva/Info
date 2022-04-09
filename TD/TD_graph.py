import numpy as np
import matplotlib.pyplot as plt

M=[[0.94,0.05,0.01,0.1],
   [0.07,0.87,0.03,0.03],
   [0.02,0.04,0.92,0.02],
   [0,0,0,1]]

M2=np.array([[0.94,0.05,0.01,0.1],
   [0.07,0.87,0.03,0.03],
   [0.02,0.04,0.92,0.02],
   [0,0,0,1]])

P0=np.array([1.081,1.076,0.327,64.516])
P1=P0*M2

Pn=P0*np.linalg.matrix_power(M,200)
print(Pn)


P=0
for i in range(1,201):
    P = np.dot(P0,np.linalg.matrix_power(M,i))
    print(P)

def produit_matriciel(M1,M2):
    assert len(M1) == len(M2[0])
    c=[]
    l=[]
    for i in range(len(M1)):
        for j in M1[i]:
            c[i]+=j
    for k in range(len(M2)):
        for l in range()

