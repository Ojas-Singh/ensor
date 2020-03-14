import sys,os,glob,subprocess,time,datetime
import numpy as np 
import config as config 
from lib import *
from termcolor import colored



def process(filename):
    pdbdata= pdb2con.do(filename,config.weight)
    # N=[]  #ATOM Number
    # X=[]  # X Coordinate
    # Y=[]  # Y Coordinate
    # Z=[]  # Z Coordiante
    # A=[]  # Atom Element
    # pdbdata=[N,X,Y,Z,A]
    Con_Matrix = np.load('temp/Con_matrix.npy')
    Mol_Matrix = np.load('temp/mol_matrix.npy')
    Dmol_Matrix = np.load('temp/Dmol_matrix.npy')
    NB_Matrix = np.load('temp/NB_matrix.npy')

    Mol=[Con_Matrix,pdbdata[0]]
    l=[]
    if config.rg_enable :
        l = list(reducedgraph.system(Mol_Matrix,Dmol_Matrix))
    final = intersection.func(fragment.fragmenter(Mol,config.parts,pdbdata,l,Mol_Matrix,config.overlap,config.res)[0])

    s=0
    for x in final:
        if len(x[1])!=0:
            s=s+1
            print colored("Part :", 'blue'),x[0], colored("have :", 'blue'), len(x[1])
    print colored("total frag+overlapfrag :", 'blue'),s


    xyzexport_M.export(pdbdata,Mol,final)
    M=[Mol_Matrix,Mol[1]]
    qq=addh.addh(pdbdata,final,M,1)
    xyzexport_H.export(qq[0],qq[2],qq[1])

    return qq



















