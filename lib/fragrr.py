import numpy as np 

def Laplacian_matrix(M):
    Degree_Matrix =  np.diag(np.ravel(np.sum(M[0],axis=1))) 
    laplacian_matrix = Degree_Matrix - M[0]
    return laplacian_matrix
def check_symm(matrix):
    for i in range (0,len(matrix)):
        x=True
        for j in range (0,len(matrix)):
            if matrix[i][j] != matrix[j][i] :
                x=False
    return x

def cutter(M,x):
    eigenvalues, eigenvectors = np.linalg.eigh(Laplacian_matrix(M))
    index_fnzev = np.argsort(eigenvalues)[1]
    fx = eigenvectors[:,index_fnzev] 
    # f = nx.linalg.algebraicconnectivity.fiedler_vector(G,weight='weight', normalized=False, tol=1e-08, method='tracemin_pcg', seed=None)
    partition = [val >= 0 for val in fx]
    a=[]
    b=[]
    Na=[]
    Nb=[]
    for i in range (0,len(partition)):
        if partition[i]==True:
            a.append(i)
        else :
            b.append(i)
        for j in range (0,i):
            if M[0][i][j]==1 and partition[i]!=partition[j]:
                x.append([M[1][i],M[1][j]])
    A=np.zeros((len(a),len(a)))
    B=np.zeros((len(b),len(b)))
    for i in range (0,len(a)):
        Na.append(M[1][a[i]])
        for j in range (0,len(a)):
            A[i][j]=M[0][a[i]][a[j]]
    for i in range (0,len(b)):
        Nb.append(M[1][b[i]])
        for j in range (0,len(b)):
            B[i][j]=M[0][b[i]][b[j]]
    P1=[A,Na]
    P2=[B,Nb]
    return P1,P2,x
# print cutter(Mol,x)
def nodes_edges(M):
    nodes=len(M[0])
    edges=0
    for i in range (0,len(M[0])):
        for j in range (0,i):
            if M[0][i][j]==1:
                edges=edges+1
    return nodes,edges

def fragmenter(M,p):
    Fragments=[]
    connections=[]
    x=[]
    matrix=[M]
    def caller(matrix):
        for j in range (0,len(matrix)):
            # print matrix
            # print "for ",j,"len vlaue",len(matrix)
            m=matrix[j]
            
            matrix[j]=[]
            matrix[j].append(cutter(m,x)[0])
            matrix[j].append(cutter(m,x)[1])
        for j in range (0,len(matrix)):
            s1=matrix[j][0]
            s2=matrix[j][1]
            Fragments.append(s1)
            Fragments.append(s2)
    
    for i in range (0,p/2):
        caller(matrix)
        matrix=Fragments
        Fragments=[]
        
    return matrix,x