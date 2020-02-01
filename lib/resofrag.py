import numpy as np 
from lib import resolution as rs
def Laplacian_matrix(M):
    Degree_Matrix =  np.diag(np.ravel(np.sum(M[0],axis=1))) 
    laplacian_matrix = Degree_Matrix - M[0]
    return laplacian_matrix
# def Laplacian_matrix(M):
#     M=M[0]
#     laplacian_matrix=np.zeros((len(M[0]),len(M[0])))
#     D=np.sum(M,axis=1)
#     for i in range(len(M)):
#         for j in range(len(M)):
#             if i==j:
#                 laplacian_matrix[i][j]=1
#             else:
#                 laplacian_matrix[i][j]=-M[i][j]/np.sqrt(D[i]*D[j])
#     print laplacian_matrix           
#     return laplacian_matrix
def check_symm(matrix):
    for i in range (0,len(matrix)):
        x=True
        for j in range (0,len(matrix)):
            if matrix[i][j] != matrix[j][i] :
                x=False
    return x

def cutter(M,X,main,pdbdata,l,mol_Matrix,w,res):
    x=[]
    eigenvalues, eigenvectors = np.linalg.eigh(Laplacian_matrix(M))
    index_fnzev = np.argsort(eigenvalues)[1]
    fx = eigenvectors[:,index_fnzev] 
    gx=eigenvectors[index_fnzev] 
    # f = nx.linalg.algebraicconnectivity.fiedler_vector(G,weight='weight', normalized=False, tol=1e-08, method='tracemin_pcg', seed=None)
    partition = [val >= 0 for val in fx]
    a=[]
    aa=[]
    b=[]
    bb=[]
    Na=[]
    Nb=[]
    for i in range (0,len(partition)):
        if partition[i]==True:
            a.append(i)
            aa.append(M[1][i])
        else :
            b.append(i)
            bb.append(M[1][i])
        for j in range (0,i):
            if M[0][i][j]!=0 and partition[i]!=partition[j]:
                x.append([M[1][i],M[1][j]])
    # OO=op.overlap(x,aa,bb,main,pdbdata,l,mol_Matrix,w)
    OO=rs.overlap(M,res,x,w,main,aa,bb,l)
    Na=OO[0]
    Nb=OO[1]
    A=np.zeros((len(Na),len(Na)))
    B=np.zeros((len(Nb),len(Nb)))

    for i in range (0,len(Na)):
        for j in range (0,len(Na)):
            A[i][j]=main[0][Na[i]-1][Na[j]-1]
    for i in range (0,len(Nb)):
        for j in range (0,len(Nb)):
            B[i][j]=main[0][Nb[i]-1][Nb[j]-1]
    


    P1=[A,Na]
    P2=[B,Nb]
    for k in x:
        X.append(k)
    return P1,P2,X
# print cutter(Mol,x)
def nodes_edges(M):
    nodes=len(M[0])
    edges=0
    for i in range (0,len(M[0])):
        for j in range (0,i):
            if M[0][i][j]==1:
                edges=edges+1
    return nodes,edges

def fragmenter(M,p,pdbdata,l,mol_Matrix,w,res):
    Fragments=[]
    connections=[]
    X=[]
    matrix=[M]
    def caller(matrix):
        for j in range (0,len(matrix)):
            # print matrix
            # print "for ",j,"len vlaue",len(matrix)
            m=matrix[j]
            c=cutter(m,X,M,pdbdata,l,mol_Matrix,w,res)
            matrix[j]=[]
            matrix[j].append(c[0])
            matrix[j].append(c[1])
        for j in range (0,len(matrix)):
            s1=matrix[j][0]
            s2=matrix[j][1]
            Fragments.append(s1)
            Fragments.append(s2)
       
    for i in range (0,p):
        caller(matrix)
        matrix=Fragments
        Fragments=[]
        
    return matrix,X