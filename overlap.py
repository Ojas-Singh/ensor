import numpy as np
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
def neighbour(atom,Con_matrix):
    l=[]
    w=1
    for j in range(len(Con_matrix[atom-1])):
        if Con_matrix[atom-1][j]>=w:
            l.append(j+1)
    return l

def overlap(F,A,B,M,pdbdata):

    Con_matrix=M[0]
    w=.1
    bonding_broke=[]
    for i in F:
        if Con_matrix[i[0]-1][i[1]-1] >= w:
            bonding_broke.append(i)


    x=listcorrect(bonding_broke)
    O=[]
    Ao=[]
    Bo=[]
    a=[]
    b=[]





    for i in x:
        for j in i:
            O.append(j)
            n=neighbour(j,Con_matrix)
            O=O+n
            for q in n:
                w=neighbour(q,Con_matrix)
                O=O+w
                for e in w:
                    r=neighbour(e,Con_matrix)
                    O=O+r
                    for k in r:
                        p=neighbour(k,Con_matrix)
                        for i in p:
                            if pdbdata[4][i-1]=='H':
                                O=O+[i]
    Overlap=unique(O)
    Ao=A+Overlap
    Bo=B+Overlap
    pAo=unique(Ao)
    pBo=unique(Bo)
    

    return [pAo,pBo]


