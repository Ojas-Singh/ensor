#############################################################################################################################
##                                               Bond Length Data Average                                                  ##
##                                                                                                                         ##
##                                                                                                                         ##
##                              http://www.wiredchemist.com/chemistry/data/bond_energies_lengths.html                      ##
#############################################################################################################################
import math
import numpy

def wf(x,a,b):
    w=a**(1-(x/b)**2)
    return w

def weight(name,a,d):
    l=search(name)
    if l[0][0]==0:
        W=l[1][1]
        b=l[1][0]
    elif l[1][0]==0:    
        W=l[0][1]
        b=l[0][0]
    else:
        W=l[0][1]
        b=l[0][0]
    if b==0:
        return 0
    wg=0
    if d<l[2]:
        wg=wf(d,a,b)
    return W*wg
def search(name):
    l=[[0,0],[0,0],2]
    if name=='CH' or name=='HC':
        l[0][0]=1.09
        l[0][1]=411
        l[1][0]=0
        l[1][1]=0
        l[2]=2
    if name=='CC' or name=='CC':
        l[0][0]=1.54
        l[0][1]=346
        l[1][0]=1.34
        l[1][1]=602
        l[2]=2
    if name=='CN' or name=='NC':
        l[0][0]=1.47
        l[0][1]=305
        l[1][0]=1.29
        l[1][1]=615
        l[2]=2
    if name=='CO' or name=='OC':
        l[0][0]=1.43
        l[0][1]=358
        l[1][0]=1.20
        l[1][1]=799
        l[2]=2
    if name=='CS' or name=='SC':
        l[0][0]=1.82
        l[0][1]=272
        l[1][0]=1.60
        l[1][1]=573
        l[2]=2.2
    if name=='NO' or name=='ON':
        l[0][0]=1.40
        l[0][1]=201
        l[1][0]=1.21
        l[1][1]=607
        l[2]=2
    if name=='NN' or name=='NN':
        l[0][0]=1.45
        l[0][1]=167
        l[1][0]=1.25
        l[1][1]=418
        l[2]=2
    if name=='OO' or name=='OO':
        l[0][0]=1.48
        l[0][1]=142
        l[1][0]=121
        l[1][1]=494
        l[2]=2
    if name=='SO' or name=='OS':
        l[0][0]=0
        l[0][1]=0
        l[1][0]=1.43
        l[1][1]=522
        l[2]=2
    if name=='SN' or name=='NS':
        l[0][0]=0
        l[0][1]=0
        l[1][0]=0
        l[1][1]=0
    if name=='SS' or name=='SS':
        l[0][0]=2.05
        l[0][1]=226
        l[1][0]=1.49
        l[1][1]=425
        l[2]=2.5
    if name=='PP' or name=='PP':
        l[0][0]=2.21
        l[0][1]=201
        l[1][0]=0
        l[1][1]=0
        l[2]=2.5
    if name=='NH' or name=='HN':
        l[0][0]=1.01
        l[0][1]=386
        l[1][0]=0
        l[1][1]=0
        l[2]=4
    if name=='HO' or name=='OH':
        l[0][0]=0.96
        l[0][1]=459
        l[1][0]=0
        l[1][1]=0
        l[2]=4
    if name=='PO' or name=='OP':
        l[0][0]=1.63
        l[0][1]=335
        l[1][0]=1.50
        l[1][1]=544
        l[2]=2
    if name=='CP' or name=='PC':
        l[0][0]=1.84
        l[0][1]=264
        l[1][0]=0
        l[1][1]=0
        l[2]=2
    if name=='NP' or name=='PN':
        l[0][0]=0
        l[0][1]=0
        l[1][0]=0
        l[1][1]=0
    if name=='PH' or name=='HP':
        l[0][0]=1.44
        l[0][1]=322
        l[1][0]=0
        l[1][1]=0
        l[2]=2
    if name=='HH':
        l[0][0]=0.74
        l[0][1]=432
        l[1][0]=0
        l[1][1]=0
        l[2]=1
    if name=='ClC' or name=='CCl':
        l[0][0]=1.77
        l[0][1]=327
        l[1][0]=0
        l[1][1]=0
        l[2]=2
    if name=='ClH' or name=='HCl':
        l[0][0]=1.27
        l[0][1]=428
        l[1][0]=0
        l[1][1]=0
        l[2]=2
    if name=='ClO' or name=='OCl':
        l[0][0]=0
        l[0][1]=0
        l[1][0]=0
        l[1][1]=0
        l[2]=2
    if name=='ClN' or name=='NCl':
        l[0][0]=1.75
        l[0][1]=313
        l[1][0]=0
        l[1][1]=0
        l[2]=2
    if name=='ClP' or name=='PCl':
        l[0][0]=2.03
        l[0][1]=326
        l[1][0]=0
        l[1][1]=0
        l[2]=2.5
    if name=='ClCl' or name=='ClCl':
        l[0][0]=1.99
        l[0][1]=240
        l[1][0]=0
        l[1][1]=0
        l[2]=2.5
    return l
