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

def cutter(M,x,r):
    eigenvalues, eigenvectors = np.linalg.eigh(Laplacian_matrix(M))
    index_fnzev = np.argsort(eigenvalues)[2]
    fx = eigenvectors[:,index_fnzev] 
    # f = nx.linalg.algebraicconnectivity.fiedler_vector(G,weight='weight', normalized=False, tol=1e-08, method='tracemin_pcg', seed=None)
    partition=np.zeros(len(fx))
    p1=np.sort([val for val in fx if val>=0])
    p2=np.sort([-val for val in fx if val<0])
    m1=np.mean([val for val in fx if val>=0])
    m2=np.mean([val for val in fx if val<0])
    e0=0.0

    for i in range(len(fx)):
        if fx[i]<0.0:
            partition[i]=-1
        elif fx[i]>0.0:
            partition[i]=1        
        for j in range(len(fx)/5):
            if fx[i]==p1[j]:
                partition[i]=0
            if fx[i]==-p2[j]:
                partition[i]=0
    # partition = [val >= np.median(fx) for val in fx]  
    # np.savetxt("fidler.txt", eigenvectors,fmt="%s")
    a=[]
    b=[]
    c=[]
    Na=[]
    Nb=[]
    Nc=[]
    for i in range (0,len(partition)):
        if partition[i]==1:
            a.append(i)
        elif partition[i]==-1 :
            b.append(i)
        elif partition[i]==0:
            c.append(i)
    a=a+c
    b=b+c
    A=np.zeros((len(a),len(a)))
        # print "Is_Connected :",nx.is_connected(G)
        # print "Connected Components :",[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
        # print "Nodes and Edges in graph :",fg.nodes_edges(Mol)
        # p=int(sys.argv[2])
        # frag=fg.fragmenter(Mol,p)
        # Parts=frag[0]
        # for i in range (0,len
        # print "Is_Connected :",nx.is_connected(G)
        # print "Connected Components :",[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
        # print "Nodes and Edges in graph :",fg.nodes_edges(Mol)
        # p=int(sys.argv[2])
        # frag=fg.fragmenter(Mol,p)
        # Parts=frag[0]
        # for i in range (0,len(frag[0])):
        #     print "Nodes and edges in part",i+1,"is:",fg.nodes_edges(frag[0][i])
        # print "No. of bond broken :",len(frag[1])/2
        # print "No. of non-bond broken :",len(frag[2])/2(frag[0])):
        #     print "Nodes and edges in part",i+1,"is:",fg.nodes_edges(frag[0][i])
        # print "No. of bond broken :",len(frag[1])/2
        # print "No. of non-bond broken :",len(frag[2])/2
    B=np.zeros((len(b),len(b)))
    C=np.zeros((len(c),len(c)))
    for i in range (0,len(a)):
        Na.append(M[1][a[i]])
        for j in range (0,len(a)):
            A[i][j]=M[0][a[i]][a[j]]
    for i in range (0,len(b)):
        Nb.append(M[1][b[i]])
        for j in range (0,len(b)):
            B[i][j]=M[0][b[i]][b[j]]
    # for i in range (0,len(c)):
    #     Nc.append(M[1][c[i]])
    #     for j in range (0,len(c)):
    #         C[i][j]=M[0][c[i]][c[j]]
    P1=[A,Na]
    P2=[B,Nb]
    # P3=[C,Nc]
    return P1,P2,x
# print cutter(Mol,x)
def nodes_edges(M):
    nodes=len(M[0])
    edges=0
    for i in range (0,len(M[0])):
        for j in range (0,i):
            if M[0][i][j]!=0:
                edges=edges+1
    return nodes,edges

def fragmenter(M,p):
    Fragments=[]
    connections=[]
    x=[]
    r=[]
    matrix=[M]
    def caller(matrix):
        for j in range (0,len(matrix)):
            # print matrix
            # print "for ",j,"len vlaue",len(matrix)
            m=matrix[j]
            c=cutter(m,x,r)
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
        
    return matrix,x,r