import sys
import os
import glob
import subprocess
import numpy as np 
import time
import networkx as nx
from networkx.algorithms.components.connected import connected_components
from lib import fragrr as fg
from lib import pdb2con as chef
from lib import plotter as plotter
from lib import xyzexport as xyz
from lib import xyzexport2 as xyz2
from lib import overlap as op
from lib import venn as intsection
from lib import Ecal as ec
from lib import mathfrag as mfg
from lib import addh as h
from lib import inputexport as inputexp
print " "
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
        t0=time.time()
        script = sys.argv[0]
        filename = sys.argv[1]
        pdbdata= chef.pdb2con(filename)
        N=pdbdata[0]
        E=pdbdata[4]
        Coord=[pdbdata[1],pdbdata[2],pdbdata[3]]
        Adj_Matrix=np.load('results/Con_matrix.npy')
        mol_Matrix=np.load('results/mol_matrix.npy')
        Mol=[Adj_Matrix,N]
        x=[]
        
        G=nx.Graph(mol_Matrix)
        # rings=nx.minimum_cycle_basis(G)
        rings= list(nx.cycle_basis(G))

        def to_graph(l):
            G = nx.Graph()
            for part in l:
                # each sublist is a bunch of nodes
                G.add_nodes_from(part)
                # it also imlies a number of edges:
                G.add_edges_from(to_edges(part))
            return G

        def to_edges(l):
            """ 
                treat `l` as a Graph and returns it's edges 
                to_edges(['a','b','c','d']) -> [(a,b), (b,c),(c,d)]
            """
            it = iter(l)
            last = next(it)

            for current in it:
                yield last, current
                last = current    

        G = to_graph(rings)
        connectedrings=list(connected_components(G))
        
        # for i in range(len(connectedrings)):
        #     for j in connectedrings[i]:
        #         mol_Matrix[j-1][j-1]=i
        l=[]
        d=[]
        for i in range(len(mol_Matrix[0])):
            for j in range(0,i):
                if mol_Matrix[i][j]==2 or mol_Matrix[j][i]==2:
                    d.append([i,j])
        l=l+d
        for i in range(len(connectedrings)):
            a=[]
            for j in connectedrings[i]:
                a.append(j+1)
            l.append(a)
        
        

        p=int(sys.argv[2])
        frag=fg.fragmenter(Mol,p,pdbdata,l)
        Parts=frag[0]
        
        final=intsection.func(Parts)


        s=0
        for x in final:
            if len(x[1])!=0:
                s=s+1
                print "Part :",x[0],"have :", len(x[1])
        print "total frag+overlapfrag :",s
        xyz2.export(pdbdata,Mol,final)

        nonbonmat=np.load('results/Adj_matrix.npy')
        ec.func(nonbonmat,final)


        M=[mol_Matrix,Mol[1]]
        qq=h.addh(pdbdata,final,M,1)
        xyz.export(qq[0],qq[2],qq[1])
        inputexp.export(qq[0],qq[2],qq[1])
        inputexp.export(pdbdata,Mol,final)


        com=glob.glob("input/part*.com")
        for i in com:
            t1=time.time()
            print "Processing :",i
            crname=i.replace('input/','')
            crname=crname.replace('.com','')
            subprocess.call(['g09',i,crname,'out'])
            t2=time.time()
            print "Done in :",t2-t1


        out=glob.glob('input/part*.log')
        l=[]
        totE=0
        for i in out:
            with open(i, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith(" SCF Done:"):
                        l.append([i,line])
        for i in l:
            s=i[1]
            r=i[0]
            p=r.count("_")
            res = [i for i in s.split()] 
            magE=float(res[4])
            print p,magE,totE
            if p%2==0:
                totE+=magE
            else:
                totE-=magE
        print totE
        tfinal=time.time()
        print "Total execution time :",tfinal-t0        
      


files = glob.glob('results/*')
for f in files:
    os.remove(f)
        
files = glob.glob('input/*')
for f in files:
    os.remove(f)        
files = glob.glob('*.chk')
for f in files:
    os.remove(f)   


if __name__ == '__main__':
   main()
