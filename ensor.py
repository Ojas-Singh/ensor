import sys
import os
import glob

import networkx as nx
import numpy as np 
from lib import fragerrr as fgr
from lib import fragrr as fg
from lib import pdb2con as chef
from lib import plotter as plotter
from lib import xyzexport as xyz


print ""
print "  ______ _   _  _____  ____  _____   "
print " |  ____| \ | |/ ____|/ __ \|  __ \  "
print " | |__  |  \| | (___ | |  | | |__) | "
print " |  __| | . ` |\___ \| |  | |  _  /  "
print " | |____| |\  |____) | |__| | | \ \  "
print " |______|_| \_|_____/ \____/|_|  \_\ "
print "                                     "
print "https://github.com/Ojas-Singh/ensor  "



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
        pdbdata= chef.pdb2con(filename)
        N=pdbdata[0]
        E=pdbdata[4]
        Coord=[pdbdata[1],pdbdata[2],pdbdata[3]]
        Adj_Matrix=np.load('results/Con_matrix.npy')
        # Adj_Matrix=np.load('results/Adj_matrix.npy')
        Mol=[Adj_Matrix,N]
        x=[]
        
        
        G=nx.from_numpy_matrix(Mol[0])
        print "Is_Connected :",nx.is_connected(G)
        print "Connected Components :",[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
        print "Nodes and Edges in graph :",fg.nodes_edges(Mol)
        p=int(sys.argv[2])
        frag=fg.fragmenter(Mol,p)
        Parts=frag[0]
        for i in range (0,len(frag[0])):
            print "Nodes and edges in part",i+1,"is:",fg.nodes_edges(frag[0][i])
        print "No. of bond broken :",len(frag[1])/2l
        print "No. of non-bond broken :",len(frag[2])/2
        plotter.plot(G,frag,E,N,Coord,filename)

        xyz.export(pdbdata,Mol,Parts)



files = glob.glob('results/*')
for f in files:
    os.remove(f)
        
        
            


if __name__ == '__main__':
   main()
