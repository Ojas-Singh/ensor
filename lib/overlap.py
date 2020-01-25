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
def neighbour(atom,Con_matrix,w,l):
    ll=[]
    for j in range(len(Con_matrix[atom-1])):
        if Con_matrix[atom-1][j]>=w:
            ll.append(j+1)
    for i in ll:
        ll=ll+addring(i,l)
    return ll

def addring(n,l):
    a=[]
    for i in l:
        if n in i:
            a=a+list(i)
    return a
            

def overlap(F,A,B,M,pdbdata,l):

    Con_matrix=M[0]
    w=.1
    bonding_broke=[]
    for i in F:
        if Con_matrix[i[0]-1][i[1]-1] >= w:
            bonding_broke.append(i)


    x=listcorrect(bonding_broke)
    print x
    O=[]
    Ao=[]
    Bo=[]
    a=[]
    b=[]

    for i in x:
        for j in i:
            O.append(j)
            n=neighbour(j,Con_matrix,.9,l)
            O=O+n
            for qq in n:
                O.append(j)
                r=neighbour(qq,Con_matrix,1.3,l)
                O=O+r
           
                for k in r:
                    p=neighbour(k,Con_matrix,1,l)
                    
                    for i in p:
                        if pdbdata[4][i-1]=='H':
                            O=O+[i]


    # for i in x:
    #     for j in i:
    #         O.append(j)
    #         n=neighbour(j,Con_matrix,1)
    #         O=O+n
    #         for q in n:
    #             w=neighbour(q,Con_matrix,1)
    #             O=O+w
    #             for i in w:
    #                 if pdbdata[4][i-1]=='H':
    #                     O=O+[i]
    #             for e in w:
    #                 r=neighbour(e,Con_matrix,1.2)
    #                 O=O+r
    #                 for i in r:
    #                     if pdbdata[4][i-1]=='H':
    #                         O=O+[i]
    #                 for k in r:
    #                     p=neighbour(k,Con_matrix,1)
                        
    #                     for i in p:
    #                         if pdbdata[4][i-1]=='H':
    #                             O=O+[i]
    # for i in x:
    #     for j in i:
    #         O.append(j)
    #         n=neighbour(j,Con_matrix,1)
    #         O=O+n
    #         for q in n:
    #             w=neighbour(q,Con_matrix,1.5)
    #             ww=neighbour(q,Con_matrix,1)
    #             O=O+w
    #             for i in ww:
    #                     if pdbdata[4][i-1]=='H':
    #                         O=O+[i]    
    #             for e in w:
    #                 r=neighbour(e,Con_matrix,1)
                   
    #                 for i in r:
    #                     if pdbdata[4][i-1]=='H':
    #                         O=O+[i]    
    Overlap=unique(O)
    Ao=A+Overlap
    Bo=B+Overlap
    pAo=unique(Ao)
    pBo=unique(Bo)
    

    return [pAo,pBo]
