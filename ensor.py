#PDB Format from https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html
import matplotlib
matplotlib.use('Agg')
import sys
import numpy as np
from tempfile import TemporaryFile
import bondlength as bld
import networkx as nx
import matplotlib.pyplot as plt

#Test
# import tensorflow as tf
print ""
print "  ______ _   _  _____  ____  _____   "
print " |  ____| \ | |/ ____|/ __ \|  __ \  "
print " | |__  |  \| | (___ | |  | | |__) | "
print " |  __| | . ` |\___ \| |  | |  _  /  "
print " | |____| |\  |____) | |__| | | \ \  "
print " |______|_| \_|_____/ \____/|_|  \_\ "
print "                                     "
print "https://github.com/Ojas-Singh/ensor  "

N=[]  #ATOM Number
X=[]  # X Coordinate
Y=[]  # Y Coordinate
Z=[]  # Z Coordiante
A=[]  # Atom Element
pdbdata=[N,X,Y,Z,A]

def main():
    if len(sys.argv) == 1:
        print "use -help to explore options"
    elif sys.argv[1] == '-help':
        print "Options For ENSOR:"
        print "usage: ensor.py <PDB Filename> <Fragments> <graph> "
        print "e.g : ensor.py PDB/mol.pdb 12 True"
        print "You can manipulate the bond length data under bondlength.py"
        print ""
    else:
        script = sys.argv[0]
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            lines = f.readlines()
            l=[]
            for line in lines:
                if line.startswith("ATOM"):
                    pdbdata[0].append(int(line[4:11]))
                    pdbdata[1].append(float(line[31:38]))
                    pdbdata[2].append(float(line[39:46]))
                    pdbdata[3].append(float(line[47:54]))
                    pdbdata[4].append(line[77:78])
            o = len(pdbdata[0])
            Connectivity_Matrix = np.zeros((o,o))
            Adj_Matrix = np.zeros((o,o))
            print "Computing Adjacency Matrix..."
            for i in range (0,o):
                for j in range (0,i):
                    x1=pdbdata[1][i]
                    y1=pdbdata[2][i]
                    z1=pdbdata[3][i]
                    x2=pdbdata[1][j] 
                    y2=pdbdata[2][j]
                    z2=pdbdata[3][j]
                    d=((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(0.5)
                    name= str(pdbdata[4][i])+str(pdbdata[4][j])
                    bd= bld.search(name)
                    
                    if np.subtract(bd[0][0],bd[0][1]) <= d <= np.add(bd[0][0],bd[0][1]):
                        Connectivity_Matrix[i][j]=1
                        Connectivity_Matrix[j][i]=1
                        
                    if np.subtract(bd[1][0],bd[1][1]) <= d <= np.add(bd[1][0],bd[1][1]):
                        Connectivity_Matrix[i][j]=2
                        Connectivity_Matrix[j][i]=2
                        
                    if np.subtract(bd[2][0],bd[2][1]) <= d <= np.add(bd[2][0],bd[2][1]):
                        Connectivity_Matrix[i][j]=3
                        Connectivity_Matrix[j][i]=3
                        
                    if d==0:
                        Connectivity_Matrix[i][j]=0 
                        Connectivity_Matrix[j][i]=0
                        

                    #Resonance Correction 
                    if np.subtract(bd[2][0],bd[2][1]) <= d <= np.add(bd[0][0],bd[0][1]):
                        Adj_Matrix[i][j]=1
                        Adj_Matrix[j][i]=1
            
            def Laplacian_matrix(Adjacency_Matrix):
                Degree_Matrix =  np.diag(np.ravel(np.sum(Adjacency_Matrix,axis=1))) 
                laplacian_matrix = Degree_Matrix - Adjacency_Matrix
                return laplacian_matrix
            def check_symm(matrix):
                for i in range (0,len(matrix)):
                    x=True
                    for j in range (0,len(matrix)):
                        if matrix[i][j] != matrix[j][i] :
                            x=False
                return x

            def cutter(Adjacency_Matrix,x):
                eigenvalues, eigenvectors = np.linalg.eigh(Laplacian_matrix(Adjacency_Matrix))
                index_fnzev = np.argsort(eigenvalues)[1]
                fx = eigenvectors[:,index_fnzev] 
                # f = nx.linalg.algebraicconnectivity.fiedler_vector(G,weight='weight', normalized=False, tol=1e-08, method='tracemin_pcg', seed=None)
                partition = [val >= 0 for val in fx]
                a=[]
                b=[]
                for i in range (0,len(partition)):
                    if partition[i]==True:
                        a.append(i)
                    else :
                        b.append(i)
                    for j in range (0,i):
                        if Adjacency_Matrix[i][j]==1 and partition[i]!=partition[j]:
                            x.append([i,j])
                A=np.zeros((len(a),len(a)))
                B=np.zeros((len(b),len(b)))
                for i in range (0,len(a)):
                    for j in range (0,len(a)):
                        A[i][j]=Adjacency_Matrix[a[i]][a[j]]
                for i in range (0,len(b)):
                    for j in range (0,len(b)):
                        B[i][j]=Adjacency_Matrix[b[i]][b[j]]
                
                return A,B,x

            def nodes_edges(Adjacency_Matrix):
                nodes=len(Adjacency_Matrix)
                edges=0
                for i in range (0,len(Adjacency_Matrix)):
                    for j in range (0,i):
                        if Adjacency_Matrix[i][j]==1:
                            edges=edges+1
                return nodes,edges
            
            def fragmenter(p):
                Fragments=[]
                connections=[]
                x=[]
                matrix=[Adj_Matrix]
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
            
            
            G=nx.from_numpy_matrix(Adj_Matrix)
            print "Is_Connected :",nx.is_connected(G)
            print "Connected Components :",[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
            print "Nodes and Edges in graph :",nodes_edges(Adj_Matrix)
            
            p=int(sys.argv[2])
            frag=fragmenter(p)
            for i in range (0,len(frag[0])):
                print "Nodes and edges in part:",i,"is",nodes_edges(frag[0][i])
            print "Edges between partitions :",frag[1]
            x=[]
            print cutter(Adj_Matrix,x)[2]

            if str(sys.argv[3])=='True':
                print "Printing generated Graph to graph.png..."
                pos=nx.spring_layout(G) 
                fig = plt.figure(figsize=(50,50))
                labels={}
                for i in range (0,len(pdbdata[4])):
                    labels[i]=pdbdata[4][i]
                options = {
                'node_color': 'white',
                'node_size': 500,
                'line_color': 'grey',
                'linewidths': 0,
                'width': 2,
                'edge_color':'white',
                'with_labels':True,
                'alpha':0.8,
                'labels':labels,
                'font_size':20,
                'font_color':'grey'
                }
                nx.draw(G, **options)
                plt.axis('off')
                fig.set_facecolor("#000000")
                plt.savefig("graph.png",facecolor=fig.get_facecolor())

                print "Graph Saved!"
        
        print "All Done glhf ;)"
                  
        # Con_matrix= TemporaryFile()
        # np.save('results/Con_matrix.npy',m)
        
        
        
            


if __name__ == '__main__':
   main()




