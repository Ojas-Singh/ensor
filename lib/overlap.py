import copy 
from copy import deepcopy
import numpy as np
import networkx 
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
            

def overlap(F,A,B,M,pdbdata,l,mol_Matrix,w):

    Con_matrix=M[0]
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
            O=O+[j]
            n=neighbour(j,mol_Matrix,1,l)
            O=O+n
            for t in n:
                    tt=[]
                    p=neighbour(t,mol_Matrix,1,tt)
                    for i in p:
                        
                            
                        if pdbdata[4][i-1]=='H' or pdbdata[4][i-1]=='Cl':
                            O=O+[i]
                        elif pdbdata[4][i-1]=='O':
                            O=O+[i]
                            for k in l:

                                if  i in k:
                                    O=O+list(k)
                            # qqqq=neighbour(i,mol_Matrix,1,l)
                    
                            # for k in qqqq:
                            #     if pdbdata[4][i-1]=='H':
                            #         ad=True
                            #         O=O+[k]
                            #         O=O+[i]
                
            # for qq in n:
            #     O.append(j)
            #     r=neighbour(qq,Con_matrix,1.2,l)
            #     O=O+r
           
            #     for k in r:
            #         p=neighbour(k,Con_matrix,1,l)
                    
            #         for i in p:
            #             if pdbdata[4][i-1]=='H' or pdbdata[4][i-1]=='Cl'or pdbdata[4][i-1]=='O':
            #                 O=O+[i]
            #                 qqqq=neighbour(i,Con_matrix,1,l)
                    
            #                 for i in qqqq:
            #                     if pdbdata[4][i-1]=='H':
            #                         O=O+[i]

 
    Overlap=unique(O)
    Ao=A+Overlap
    Bo=B+Overlap
    pAo=unique(Ao)
    pBo=unique(Bo)
    

    return [pAo,pBo]

def overlap2(F,A,M,pdbdata,l,mol_Matrix,w):

    Con_matrix=M[0]
    bonding_broke=[]

    for i in F:
        if i[0] in A or i[1] in A:
            if Con_matrix[i[0]-1][i[1]-1] >= w:
                bonding_broke.append(i)



    x=listcorrect(bonding_broke)
    O=[]
    Ao=[]
    a=[]
    for i in x:
        for j in i:
            O=O+[j]
            n=neighbour(j,mol_Matrix,1,l)
            O=O+n
            for t in n:
                    tt=[]
                    p=neighbour(t,mol_Matrix,1,tt)
                    for i in p:
                        
                            
                        if pdbdata[4][i-1]=='H' or pdbdata[4][i-1]=='Cl':
                            O=O+[i]
                        elif pdbdata[4][i-1]=='O':
                            O=O+[i]
                            for k in l:

                                if  i in k:
                                    O=O+list(k)
                            # qqqq=neighbour(i,mol_Matrix,1,l)
                    
                            # for k in qqqq:
                            #     if pdbdata[4][i-1]=='H':
                            #         ad=True
                            #         O=O+[k]
                            #         O=O+[i]
                
            # for qq in n:
            #     O.append(j)
            #     r=neighbour(qq,Con_matrix,1.2,l)
            #     O=O+r
           
            #     for k in r:
            #         p=neighbour(k,Con_matrix,1,l)
                    
            #         for i in p:
            #             if pdbdata[4][i-1]=='H' or pdbdata[4][i-1]=='Cl'or pdbdata[4][i-1]=='O':
            #                 O=O+[i]
            #                 qqqq=neighbour(i,Con_matrix,1,l)
                    
            #                 for i in qqqq:
            #                     if pdbdata[4][i-1]=='H':
            #                         O=O+[i]

 
    Overlap=unique(O)
    Ao=A+Overlap
    pAo=unique(Ao)
    

    return pAo