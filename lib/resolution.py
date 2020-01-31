import numpy as np
import copy 
from copy import deepcopy
import networkx 
from networkx.algorithms.components.connected import connected_components

def to_graph(l):
    G = networkx.Graph()
    for part in l:
        # each sublist is a bunch of nodes
        G.add_nodes_from(part)
        # it also imlies a number of edges:
        G.add_edges_from(to_edges(part))
    return G

def to_edges(l):
    """ 
        treat `l` as a Graph and returns it's edges 
        to_edges(['a','b','c','d']) -> [(a,b), (b,c),(c,d)]
    """
    it = iter(l)
    last = next(it)

    for current in it:
        yield last, current
        last = current  
def Laplacian_matrix(M):
    Degree_Matrix =  np.diag(np.ravel(np.sum(M,axis=1))) 
    laplacian_matrix = Degree_Matrix - M
    return laplacian_matrix

def into2(M,l,main):
    eigenvalues, eigenvectors = np.linalg.eigh(Laplacian_matrix(M))
    index_fnzev = np.argsort(eigenvalues)[1]
    fx = eigenvectors[:,index_fnzev] 
    partition = [val >= 0 for val in fx]
    a=[]
    b=[]
    for i in range (0,len(partition)):
        if partition[i]==True:
            a.append(l[i])
        else :
            b.append(l[i])
    A=np.zeros((len(a),len(a)))
    B=np.zeros((len(b),len(b)))
    for i in range (0,len(a)):
        for j in range (0,len(a)):
            A[i][j]=main[0][a[i]-1][a[j]-1]
    for i in range (0,len(b)):
        for j in range (0,len(b)):
            B[i][j]=main[0][b[i]-1][b[j]-1]
    return [[A,a],[B,b]]

def grid(M,n,main):
    Fragments=[]
    X=[]
    pixel=[M]
    def caller(pixel):
        for j in range (0,len(pixel)):
            m=pixel[j]
            c=into2(m[0],m[1],main)
            pixel[j]=[]
            pixel[j].append(c[0])
            pixel[j].append(c[1])
        for j in range (0,len(pixel)):
            s1=pixel[j][0]
            s2=pixel[j][1]
            Fragments.append(s1)
            Fragments.append(s2)
       
    for i in range (0,n):
        caller(pixel)
        pixel=Fragments
        Fragments=[]
        
    return pixel

def overlap(M,n,F,w,main,a,b,l):
    
    Con_matrix=main[0]
    bonding_broke=[]

    for i in F:
        if Con_matrix[i[0]-1][i[1]-1] >= w:
            bonding_broke.append(i)
    x=listcorrect(bonding_broke)
    pixel=grid(M,5,main)
    pAo=[]
    pBo=[]
    o=[]
    pixellist=[]
    for i in pixel:
        pixellist.append(i[1])
    finallist=list(connected_components(to_graph(l+pixellist)))
    for i in x:
        for j in i:
            o=o+[j]
            p=neighbour(j,Con_matrix,1,finallist)
            o=o+p
            # for k in p:
            #     t=neighbour(k,Con_matrix,1,pixellist+l)
            #     o=o+t
           
    pAo=a+o
    pBo=b+o
    pAo=unique(pAo)
    pBo=unique(pBo)
    return [pAo,pBo]

def unique(list): 
   
    unique_list = [] 
    for x in list: 
        if x not in unique_list: 
            unique_list.append(x) 
    
    return unique_list

def neighbour(atom,matrix,w,l):
    ll=[]
    for j in range(len(matrix[atom-1])): 
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
def listcorrect(l):
    x=[]
    for i in l:
        if i[0]>i[1]:
            x.append(i)
    return x