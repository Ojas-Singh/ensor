import time
import sys
import os
import glob
import subprocess
print "----------------------[G09 Benchmark]----------------------"
print "-----------------------------------------------------------"
t0=time.time() 
i=''
crname=i.replace('input/','')
crname=crname.replace('.com','')
subprocess.call(['g09',i,crname,'out'])
t1=time.time()
print 