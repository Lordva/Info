

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

def recherche_voisins(m,neud_visites,neud):
    L=[]
    for i in range(len(mat_adj)):
        if mat_adj[neud][i] != 0 and i not in neud_visites:
            L += [i]
    return L
