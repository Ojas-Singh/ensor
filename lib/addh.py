import copy
from copy import deepcopy

def addhvector(Vf,Vm):
    h=1.09
    
    d=((Vm[0]-Vf[0])**2 + (Vm[1]-Vf[1])**2 + (Vm[2]-Vf[2])**2)**(0.5)
    if d>0:
        # x=h*(Vm[0]-Vf[0])/d
        # y=h*(Vm[1]-Vf[1])/d
        # z=h*(Vm[2]-Vf[2])/d
        x=Vm[0]
        y=Vm[1]
        z=Vm[2]

    
        return x,y,z
    else :
        return False
def addh(pdbdata,final,Mol,w):
    new_mol=[[],[],[],[],[]]
    N=[i for i in pdbdata[0]]
    X=[i for i in pdbdata[1]]
    Y=[i for i in pdbdata[2]]
    Z=[i for i in pdbdata[3]]
    E=[i for i in pdbdata[4]]
    
    new_final=copy.deepcopy(final)
    for x in range(0,len(final)):
        hlist=[]
        if len(final[x][1])!=0:

            for i in pdbdata[0]:
                if i not in final[x][1]:
                    for j in final[x][1]:
                        if Mol[0][i-1][j-1] == w:
                            v1=[pdbdata[1][j-1],pdbdata[2][j-1],pdbdata[3][j-1]]
                            v2=[pdbdata[1][i-1],pdbdata[2][i-1],pdbdata[3][i-1]]
                            num=len(N)
                            h=addhvector(v1,v2)
                            
                            if h not in hlist:
                                N.append(int(num))
                                # X.append(v1[0]+h[0])
                                # Y.append(v1[1]+h[1])
                                # Z.append(v1[2]+h[2])
                                X.append(h[0])
                                Y.append(h[1])
                                Z.append(h[2])
                                E.append('H')
                                new_final[x][1].append(num+1)
                                hlist.append(h)

    new_mol=[N,X,Y,Z,E]
    new_M=[Mol[0],new_mol[0]]
    return new_mol,new_final,new_M
