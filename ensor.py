import sys,os,glob,subprocess,time,datetime
import numpy as np 
import ensor_core as core
import config as config
from termcolor import colored
from alive_progress import alive_bar


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

    for i in range(len(sys.argv)):
        if sys.argv[i]=='-p':
            p=int(sys.argv[i+1])
        if sys.argv[i]=='-g09':
            calc=True
        if sys.argv[i]=='-raw':
    if len(sys.argv) == 1:
        print colored("use -help to explore options", 'yellow')
    elif sys.argv[1] == '-help' or sys.argv[1]=='-h':
        print "Options For ENSOR:"
        print "usage: ensor.py PATH-TO-FILE -option1 -option2 ... "
        print "e.g : ensor.py PDB/mol.pdb -p 2 -g09"
        print "You can manipulate the bond length data under bondlength.py"
        print ""
    else:

        Q = core.process(sys.argv[1])  # Q[0] =  , Q[1] = , Q[2] = 

        t0=time.time()
        


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
files = glob.glob('*.pyc')
for f in files:
    os.remove(f) 


if __name__ == '__main__':
   main()
