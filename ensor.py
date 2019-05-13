#PDB Format by https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

import sys
import numpy as np
from tempfile import TemporaryFile
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
        print "usage: ensor.py <PDB Filename> <singlebondlength> <delta_singlebondlength> <doublebondlength> <delta_doublebondlength> <triplebondlength> <delta_triplebondlength>"
    elif sys.argv[1] == '-help':
        print "Help Menu For ENSOR:"
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
            # for i in range (0,o):
            #     print pdbdata[0][i],pdbdata[1][i],pdbdata[2][i],pdbdata[3][i],pdbdata[4][i]
            m = np.zeros((o,o))
            d_single= float(sys.argv[2])
            delta_single=float(sys.argv[3])
            d_double=float(sys.argv[4])
            delta_double=float(sys.argv[5])
            d_triple=float(sys.argv[6])
            delta_triple=float(sys.argv[7])
            for i in range (0,o):
                for j in range (0,o):
                    x1=pdbdata[1][i]
                    y1=pdbdata[2][i]
                    z1=pdbdata[3][i]
                    x2=pdbdata[1][j]
                    y2=pdbdata[2][j]
                    z2=pdbdata[3][j]
                    d=((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(0.5)
                    # m[i][j]=d  
                    
                    
                    if d < np.add(d_single,delta_single) and d> np.subtract(d_single,delta_single) :
                        m[i][j]=1
                    if d< np.add(d_double,delta_double) and d> np.subtract(d_double,delta_double) :
                        m[i][j]=2
                    if d< np.add(d_triple,delta_triple) and d> np.subtract(d_triple,delta_triple) :
                        m[i][j]=3
                    
            Con_matrix= TemporaryFile()
            np.save('Con_matrix.npy',m)
            # np.savetxt('Con_matrix.txt',m)      
            print m
            print 'Connectivity Matrix saved as Con_matrix.npy'
            


if __name__ == '__main__':
   main()




