import sys,os,glob,subprocess,time,datetime
import numpy as np 
import config as config 
from lib import *
from termcolor import colored



def process(filename,n):
    #phase 1
    pdbdata= pdb2con.do(filename,config.weight)
    # N=[]  #ATOM Number
    # X=[]  # X Coordinate
    # Y=[]  # Y Coordinate
    # Z=[]  # Z Coordiante
    # A=[]  # Atom Element
    # pdbdata=[N,X,Y,Z,A]
    Con_Matrix = np.load('temp/Con_matrix.npy')
    Mol_Matrix = np.load('temp/mol_matrix.npy')

    # algo to decide n 

    f = label.SGP(pdbdata,n,Con_Matrix)
    # f = [f1,f2,f3,f4...,fn]
    overlap.rselector(f,pdbdata,Con_Matrix)
    rinput = int(raw_input("Which R to use : "))
    F = overlap.Fr(f,pdbdata,Con_Matrix,rinput)  # need idea !
    # F = [F1,F2,F3,F4...,Fn]

    final = intersection.func(F)
    # final = [[F1,F2,F3...Fn],[F1&F2,F2&F3,F1&Fn ...],[F1&F2&F3,F2&F3&F4,...],...[]]


    #phase 2 
    s=0
    for x in final:
        if len(x[1])!=0:
            s=s+1
            print colored("Part :", 'blue'),x[0], colored("have :", 'blue'), len(x[1])
    print colored("total frag+overlapfrag :", 'blue'),s

    Mol=[Mol_Matrix,pdbdata[0]]
    xyzexport_M.export(pdbdata,Mol,final)
    M=[Mol_Matrix,pdbdata[0]]
    qq=addh.addh(pdbdata,final,M,1)
    xyzexport_H.export(qq[0],qq[2],qq[1])
    
    
    return qq



















