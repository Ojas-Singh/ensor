import sys
import os
import glob
import subprocess
import numpy as np 
import time
from termcolor import colored
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
from lib import congugate 
print colored('', 'yellow')
print colored("  ______ _   _  _____  ____  _____   ", 'yellow')
print colored(" |  ____| \ | |/ ____|/ __ \|  __ \  ", 'yellow')
print colored(" | |__  |  \| | (___ | |  | | |__) | ", 'yellow')
print colored(" |  __| | . ` |\___ \| |  | |  _  /  ", 'yellow')
print colored(" | |____| |\  |____) | |__| | | \ \  ", 'yellow')
print colored(" |______|_| \_|_____/ \____/|_|  \_\ ", 'yellow')
print colored("                                     ", 'yellow')
print colored("https://github.com/Ojas-Singh/ensor  ", 'green')



def main():
    p=0
    calc=False
    ring=True
    overw=1
    for i in range(len(sys.argv)):
        if sys.argv[i]=='-p':
            p=int(sys.argv[i+1])
        if sys.argv[i]=='-g09':
            calc=True
        if sys.argv[i]=='-raw':
            ring=False
        if sys.argv[i]=='-overlap':
            overw=float(sys.argv[i+1])
    if len(sys.argv) == 1:
        print colored("use -help to explore options", 'yellow')
    elif sys.argv[1] == '-help' or sys.argv[1]=='-h':
        print "Options For ENSOR:"
        print "usage: ensor.py PATH-TO-FILE -option1 -option2 ... "
        print "e.g : ensor.py PDB/mol.pdb -p 2 -g09"
        print "You can manipulate the bond length data under bondlength.py"
        print ""
    else:



        t0=time.time()
        script = sys.argv[0]
        filename = sys.argv[1]
        pdbdata= chef.pdb2con(filename)
        ##########_ Matrices #########################
        Adj_Matrix=np.load('results/Con_matrix.npy')
        mol_Matrix=np.load('results/mol_matrix.npy')
        Dmol_Matrix=np.load('results/Dmol_matrix.npy')
        nonbonmat=np.load('results/Adj_matrix.npy')
        ##############################################
        Mol=[Adj_Matrix,pdbdata[0]]
        if ring:
            l=list(congugate.system(mol_Matrix,Dmol_Matrix))

        
        frag=fg.fragmenter(Mol,p,pdbdata,l,mol_Matrix,overw)
        Parts=frag[0]
        
        final=intsection.func(Parts)


        s=0
        for x in final:
            if len(x[1])!=0:
                s=s+1
                print colored("Part :", 'blue'),x[0], colored("have :", 'blue'), len(x[1])
        print colored("total frag+overlapfrag :", 'blue'),s
        

        
        ec.func(nonbonmat,final)
        xyz2.export(pdbdata,Mol,final)
        M=[mol_Matrix,Mol[1]]
        qq=h.addh(pdbdata,final,M,1)
        xyz.export(qq[0],qq[2],qq[1])
        inputexp.export(qq[0],qq[2],qq[1])
        inputexp.export(pdbdata,Mol,final)

        if calc:
            com=glob.glob("input/part*.com")
            for i in com:
                t1=time.time()
                print colored("Processing :", 'blue'),colored(i, 'cyan')
                crname=i.replace('input/','')
                crname=crname.replace('.com','')
                subprocess.call(['g09',i,crname,'out'])
                t2=time.time()
                print colored("Done in :", 'green'),t2-t1


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
            print colored(totE, 'red')
            tfinal=time.time()
            print colored("Total execution time :", 'blue'),colored(tfinal-t0, 'green')        
        


files = glob.glob('results/*')
for f in files:
    os.remove(f)
        
files = glob.glob('input/*')
for f in files:
    os.remove(f)        
files = glob.glob('*.chk')
for f in files:
    os.remove(f)   
files = glob.glob('lib/*.pyc')
for f in files:
    os.remove(f) 


if __name__ == '__main__':
   main()
