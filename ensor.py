#PDB Format by https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

import sys
import numpy as np
from tempfile import TemporaryFile
import bondlength as bld
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
        print "usage: ensor.py <PDB Filename>"
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
            m = np.zeros((o,o))
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
                        m[i][j]=1
                        m[j][i]=1
                    if np.subtract(bd[1][0],bd[1][1]) <= d <= np.add(bd[1][0],bd[1][1]):
                        m[i][j]=2
                        m[j][i]=2
                    if np.subtract(bd[2][0],bd[2][1]) <= d <= np.add(bd[2][0],bd[2][1]):
                        m[i][j]=3
                        m[j][i]=3
                    if d==0:
                        m[i][j]=0 
                        m[j][i]=0
            deg = np.zeros((o,o))
            for i in range (0,o):
                x=0
                for j in range (0,o):
                    if m[i][j] != 0:
                        x=x+1
                deg[i][i] = x
        Lap = deg - m
        
                  
        # Con_matrix= TemporaryFile()
        # np.save('results/Con_matrix.npy',m)
        
        
        
            


if __name__ == '__main__':
   main()
