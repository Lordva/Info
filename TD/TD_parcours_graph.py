## Exercice 1

from collections import deque

from numpy import empty


mat_adj=[[0,1,1,0,0,0,0,0,0,1],
         [1,0,0,0,0,1,0,0,0,0],
         [1,0,0,1,0,0,1,0,0,0],
         [0,0,1,0,1,0,0,0,0,0],
         [0,0,0,1,0,1,1,0,0,0],
         [0,1,0,0,1,0,1,0,0,0],
         [0,0,1,0,1,1,0,1,0,0],
         [0,0,0,0,0,0,1,0,1,1],
         [0,0,0,0,0,0,0,1,0,0],
         [1,0,0,0,0,0,0,1,0,0]]

def verif_symetrie(m):
    assert len(m) == len(m[0])
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != m[j][i]:
                return False
    return True

etiquette=[chr(ord('A') + i) for i in range(len(mat_adj))]

def determination_numero(etiquettes, nom_neud):
    for i in range(len(etiquettes)):
        if etiquettes[i] == nom_neud:
            return i

def recherche_voisins(m,neud_visites,noeud):
    L=[]
    for i in range(len(m)):
        if m[noeud][i] != 0 and i not in neud_visites:
            L += [i]
    return L

## Exercice 2: Parcours en largeur

def parcours_largeur(mat):
    file = deque(mat[0])
    n_visite = [file[0]]
    while len(file) != 0:
        noeud_courant = file.popleft()
        voisins = recherche_voisins(mat,n_visite,noeud_courant)
        file.extend(voisins)
        n_visite.extend(voisins)
    return n_visite

print(parcours_largeur(mat_adj))

def parcour_profondeur(mat):
    pile = deque(mat[0])
    n_visite = [pile[0]]
    while len(pile) !=0:
        noeud_courant = pile.pop()
        voisins = recherche_voisins(mat,n_visite,noeud_courant)
        pile.extend(voisins)
        n_visite.extend(voisins)
    return n_visite

print(parcour_profondeur(mat_adj))
def visiter(u, n_decouverts):
    adj=[]
    if u not in n_decouverts:
        n_decouverts += [u] 
    for i in recherche_voisins(mat_adj, n_decouverts, u):
        adj += [i]
        if i not in n_decouverts:
            visiter(i, n_decouverts)

def parcour_profondeur_recursif(mat, depart):
    noeud_decouverts = [depart]
    visiter(depart, noeud_decouverts)
    return noeud_decouverts

print(parcour_profondeur_recursif(mat_adj, 0))

