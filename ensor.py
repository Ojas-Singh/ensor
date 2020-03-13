import sys
import os
import glob
import subprocess
import numpy as np 
import time
from termcolor import colored
from alive_progress import alive_bar
import datetime
<<<<<<< HEAD
from lib import fragment as fg
=======
from lib import fragrr as fg
from lib import frag2 as fg2
from lib import fragment as fgg
>>>>>>> 2e49609721bae17fc1ba1ea9609f549617dbb479
from lib import pdb2con as chef
from lib import xyzexport_H as xyzH
from lib import xyzexport_M as xyzM
from lib import overlap as op
from lib import intersection as intersection
from lib import Ecal as ec
from lib import addh as h
from lib import inputexport as inputexp
from lib import reducedgraph as rg
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
    rgenable=True
    overw=1
    W=5
    l=[]
    res=4
    for i in range(len(sys.argv)):
        if sys.argv[i]=='-p':
            p=int(sys.argv[i+1])
        if sys.argv[i]=='-g09':
            calc=True
        if sys.argv[i]=='-raw':
            ring=False
        if sys.argv[i]=='-res':
            res=int(sys.argv[i+1])

        if sys.argv[i]=='-overlap':
            overw=float(sys.argv[i+1])
        if sys.argv[i]=='-W':
            W=float(sys.argv[i+1])
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
        pdbdata = chef.pdb2con(filename,W)
        ##########_ Matrices _#########################
        Adj_Matrix = np.load('temp/Con_matrix.npy')
        mol_Matrix = np.load('temp/mol_matrix.npy')
        Dmol_Matrix = np.load('temp/Dmol_matrix.npy')
        nonbonmat = np.load('temp/Adj_matrix.npy')
        ##############################################
        Mol=[Adj_Matrix,pdbdata[0]]
        if rgenable :
            l = list(rg.system(mol_Matrix,Dmol_Matrix))


<<<<<<< HEAD
        frag = fg.fragmenter(Mol,p,pdbdata,l,mol_Matrix,overw,res)
        Parts = frag[0]
=======
        frag=fgg.fragmenter(Mol,p,pdbdata,l,mol_Matrix,overw,res)
        Parts=frag[0]
>>>>>>> 2e49609721bae17fc1ba1ea9609f549617dbb479
        
        final = intersection.func(Parts)


        s=0
        for x in final:
            if len(x[1])!=0:
                s = s + 1
                print colored("Part :", 'blue'),x[0], colored("have :", 'blue'), len(x[1])
        print colored("total frag+overlapfrag :", 'blue'),s
        

        
        ec.func(nonbonmat,final)
        xyzM.export(pdbdata,Mol,final)
        M = [mol_Matrix,Mol[1]]
        qq = h.addh(pdbdata,final,M,1)
        xyzH.export(qq[0],qq[2],qq[1])
        inputexp.export(qq[0],qq[2],qq[1])
        inputexp.export(pdbdata,Mol,final)

        
        if calc:
            com = glob.glob("input/part*.com")
            with alive_bar(len(com),bar='smooth',spinner='dots_waves2') as bar:
                for i in com:
                    t1 = time.time()
                    print colored("Processing :", 'blue'),colored(i, 'cyan')
                    crname=i.replace('input/','')
                    crname=crname.replace('.com','')
                    subprocess.call(['g09',i,crname,'out'])
                    t2=time.time()
                    print colored("Done in :", 'green'),t2-t1,"seconds"
                    bar()


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
            rname=filename.strip(".pdb")+"_p_"+str(p)+str(datetime.datetime.now())+'.log'
            
            r = open("data/"+rname, "a")
            
            r.write("This DATA is generated on "+str(datetime.datetime.now())+"\n")
            r.write("  ______ _   _  _____  ____  _____   "+"\n")
            r.write(" |  ____| \ | |/ ____|/ __ \|  __ \  "+"\n")
            r.write(" | |__  |  \| | (___ | |  | | |__) | "+"\n")
            r.write(" |  __| | . ` |\___ \| |  | |  _  /  "+"\n")
            r.write(" | |____| |\  |____) | |__| | | \ \  "+"\n")
            r.write(" |______|_| \_|_____/ \____/|_|  \_\ "+"\n")
            r.write("                                     "+"\n")
            r.write("https://github.com/Ojas-Singh/ensor  "+"\n")
            r.write("                                     "+"\n")
            r.write("Molecule "+filename.strip(".pdb")+"\n")
            r.write("System arg passed on the run."+"\n")
            r.write("   "+str(sys.argv)+"\n")
            while True:
                try:
                    r.write("Calculated Energy : "+str(totE)+"\n")
                    r.write("Time taken by ENSOR : "+ str(tfinal-t0)+"\n")
                    break
                except ValueError:
                    print("Oops! Try again with -g09 option to generate Valid log.")
            r.close()


files = glob.glob('XYZ/*')
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
