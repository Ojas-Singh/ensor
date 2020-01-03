#PDB Format from https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

import numpy as np
import bondlength as bld
from tempfile import TemporaryFile
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength
N=[]  #ATOM Number
X=[]  # X Coordinate
Y=[]  # Y Coordinate
Z=[]  # Z Coordiante
A=[]  # Atom Element
pdbdata=[N,X,Y,Z,A]

def pdb2con(filename):
    with open(filename, 'r') as f:
            lines = f.readlines()
            l=[]
            i=1
            for line in lines:
                if line.startswith("ATOM"):
                    # pdbdata[0].append(int(line[4:11]))
                    pdbdata[0].append(i)
                    pdbdata[1].append(float(line[31:38]))
                    pdbdata[2].append(float(line[39:46]))
                    pdbdata[3].append(float(line[47:54]))
                    pdbdata[4].append(line[77:78])
                    i+=1
            o = len(pdbdata[0])
            widgets = [Percentage(),' ', Bar(),' ', ETA(),' ', AdaptiveETA()]
            pbar = ProgressBar(widgets=widgets, maxval=o)
            Connectivity_Matrix = np.zeros((o,o))
            Adj_Matrix = np.zeros((o,o))
            print "Computing Adjacency Matrix..."
            pbar.start()
            for i in range (0,o):
                pbar.update(i+1)
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
                    if d <= bd[0] and d>=0:
                        w=-1*d**2*(bd[2]-1)/bd[0]**2 + bd[2]
                        Connectivity_Matrix[i][j]= w
                        Connectivity_Matrix[j][i]= w

#                     if d>bd[1]:

                        
                    if bd[0] < d <= bd[1]:
                        # Connectivity_Matrix[i][j]=np.exp(-1*d-bd[1])-1
                        # Connectivity_Matrix[j][i]=np.exp(-1*d-bd[1])-1
                        w= .01
                        Connectivity_Matrix[i][j]=w
                        Connectivity_Matrix[j][i]=w

                        
                        
                    if d==0:
                        Connectivity_Matrix[i][j]=0 
                        Connectivity_Matrix[j][i]=0
                        
                    if d <= np.add(bd[0],bd[1]):
                        Adj_Matrix[i][j]=1
                        Adj_Matrix[j][i]=1
            pbar.finish()            
    Con_matrix= TemporaryFile()
    np.save('results/Con_matrix.npy',Connectivity_Matrix)
    Adj_matrix= TemporaryFile()
    np.save('results/Adj_matrix.npy',Adj_Matrix)
    
    return pdbdata
