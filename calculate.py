
import sys
import os
import glob

out=glob.glob('input/part*.log')
l=[]
totE=0
for i in out:
    with open(i, 'r') as f:
        ok=[]
        lines = f.readlines()
        for line in lines:
            if line.startswith(" SCF Done:"):
                ok=[i,line]
        l.append(ok)
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
