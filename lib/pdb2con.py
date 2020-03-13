#PDB Format from https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

import numpy as np
from termcolor import colored
import bondlength as bld
from tempfile import TemporaryFile
from alive_progress import alive_bar

N=[]  #ATOM Number
X=[]  # X Coordinate
Y=[]  # Y Coordinate
Z=[]  # Z Coordiante
A=[]  # Atom Element
pdbdata=[N,X,Y,Z,A]




def pdb2con(filename,W):
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
                    pdbdata[4].append((line[76:78]).strip(" "))
                    i+=1
            o = len(pdbdata[0])
            Connectivity_Matrix = np.zeros((o,o))
            Adj_Matrix = np.zeros((o,o))
            mol_Matrix = np.zeros((o,o))
            Dmol_Matrix = np.zeros((o,o))
            
            
            with alive_bar(len(range(0,o))+1) as bar:
                bar('Computing Connectivity Matrix.')
                for i in range(0,o):
                    
                    for j in range (0,i):
                        x1=pdbdata[1][i]
                        y1=pdbdata[2][i]
                        z1=pdbdata[3][i]
                        x2=pdbdata[1][j] 
                        y2=pdbdata[2][j]
                        z2=pdbdata[3][j]
                        d=((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(0.5)
                        name= str(pdbdata[4][i])+str(pdbdata[4][j])
                        bd= bld.search(name,W)
                        b1=bd[1]
                        b0=bd[0]
                        b2=bd[2]
                        if b0==0:
                            print "Update the Bondlength database for :",name
                        w=b2**(1-(d/b0)**2) #gaussian function
                        
                        if d <= b0+.1 :
                            
                            mol_Matrix[i][j]= 1
                            mol_Matrix[j][i]= 1
                            Connectivity_Matrix[i][j]=w
                            Connectivity_Matrix[j][i]=w

                            if d<=b0-.05:
                                mol_Matrix[i][j]= 2
                                mol_Matrix[j][i]= 2
                                Dmol_Matrix[i][j]= 2
                                Dmol_Matrix[j][i]= 2
                                
                            
                            
                        if d==0:
                            Connectivity_Matrix[i][j]=0 
                            Connectivity_Matrix[j][i]=0



                        else:
                            
                            Connectivity_Matrix[i][j]=w
                            Connectivity_Matrix[j][i]=w

                        if b0 <= d <= 4:
                            Adj_Matrix[i][j]=1
                            Adj_Matrix[j][i]=1 
                    bar() 
                     
            print colored('Total Atom in PDB :', 'blue'),len(pdbdata[0])         
    Con_matrix= TemporaryFile()
    np.save('temp/Con_matrix.npy',Connectivity_Matrix)
    Adj_matrix= TemporaryFile()
    np.save('temp/Adj_matrix.npy',Adj_Matrix)
    mol_matrix= TemporaryFile()
    np.save('temp/mol_matrix.npy',mol_Matrix)
    Dmol_matrix= TemporaryFile()
    np.save('temp/Dmol_matrix.npy',Dmol_Matrix)
    
    return pdbdata
