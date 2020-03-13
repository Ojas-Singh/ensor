import copy 
from copy import deepcopy
import numpy as np
import networkx 

def Laplacian_matrix(M):
    Degree_Matrix =  np.diag(np.ravel(np.sum(M,axis=1))) 
    laplacian_matrix = Degree_Matrix - M
    return laplacian_matrix

def degreeofnode(node,frag,Molecule,Con_matrix):
    degree = Laplacian_matrix(Con_matrix)[node-1][node-1]
    for i in frag:
        degree = degree - Con_matrix[node-1][i-1]
    return float((Laplacian_matrix(Con_matrix)[node-1][node-1]-degree)/Laplacian_matrix(Con_matrix)[node-1][node-1])

def looper(Overlap,frag,Molecule,Wn,r,Rg,Con_matrix):
    N=[]
    NN=[]
    for i in Overlap:
        N = N + neighbour(i,Con_matrix,Wn,Rg)
    Overlap = Overlap + N + NN
    fragintMolecule = [item for item in Molecule if item not in frag]
    for i in fragintMolecule:
        if degreeofnode(i,frag+Overlap,Molecule,Con_matrix) > r :
            NN = NN + [i]
        Overlap = Overlap + NN 
        Overlap = unique(Overlap)

    return Overlap        

def overlap(F,A,M,pdbdata,l,mol_Matrix,w):
    bonding_broke=[]
    Con_matrix=M[0]
    frag = A
    Molecule = M[1]
    fragintMolecule = [item for item in Molecule if item not in frag]
    Overlap = []
    FragmentwithOverlap = frag + Overlap
    for i in F:
        if i[0] in A or i[1] in A:
            if Con_matrix[i[0]-1][i[1]-1] >= w:
                bonding_broke.append(i)
    x = listcorrect(bonding_broke)
    Overlap = [item[0] for item in x] + [item[1] for item in x]
    Overlap = looper(Overlap,frag,Molecule,.9,.5,l,Con_matrix)
    # Overlap = looper(Overlap,frag,Molecule,.9,.5,l,Con_matrix)
    Overlap = unique(Overlap)
    FragmentwithOverlap = unique(FragmentwithOverlap)
    FragmentwithOverlap = frag + Overlap
    
    return FragmentwithOverlap




def bonding_list(F,Con_matrix):
    w=1
    bonding_broke=[]
    for i in F:
        if Con_matrix[i[0]][i[1]] >= w:
            bonding_broke.append(i)
    return bonding_broke

def unique(list): 
   
    unique_list = [] 
    for x in list: 
        if x not in unique_list: 
            unique_list.append(x) 
    
    return unique_list

def gg(l):
    x=[]
    for i in l:
        x.append(i[0])
        x.append(i[1])
    return x

def listcorrect(l):
    x=[]
    for i in l:
        if i[0]>i[1]:
            x.append(i)
    return x
def neighbour(atom,matrix,w,l):
    ll=[]
    # G=networkx.Graph(matrix)
    # ll=list(G.neighbors(atom-1))
    for j in range(len(matrix[atom-1])):   #need update using networkx
        if matrix[atom-1][j]>=w:
            ll.append(j+1)
    l2=deepcopy(ll)
    for i in l2:
        ll=ll+addring(i,l)

    return ll

def addring(n,l):
    a=[]
    for i in l:
        if n in i:
            a=a+list(i)
    return a
