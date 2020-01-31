#############################################################################################################################
##                                               Bond Length Data Average                                                  ##
##                                                                                                                         ##
##                                                                                                                         ##
##                              http://www.wiredchemist.com/chemistry/data/bond_energies_lengths.html                      ##
#############################################################################################################################

def search(name,W):
    l=[0,0,W]
    if name=='CH' or name=='HC':
        l[0]=1.09
        l[1]=411
    if name=='CC' or name=='CC':
        l[0]=1.54
        l[1]=346
    if name=='CN' or name=='NC':
        l[0]=1.47
        l[1]=305
    if name=='CO' or name=='OC':
        l[0]=1.43
        l[1]=358
    if name=='CS' or name=='SC':
        l[0]=1.82  
        l[1]=272
    if name=='NO' or name=='ON':
        l[0]=1.40  
        l[1]=201
    if name=='NN' or name=='NN':
        l[0]=1.45
        l[1]=167
    if name=='OO' or name=='OO':
        l[0]=1.48
        l[1]=142
    if name=='SO' or name=='OS':
        l[0]=1.43
        l[1]=522
    if name=='SN' or name=='NS':
        l[0]=1.8
        l[1]=300  #gg
    if name=='SS' or name=='SS':
        l[0]=2.05
        l[1]=226
    if name=='PP' or name=='PP':
        l[0]=2.21
        l[1]=201
    if name=='NH' or name=='HN':
        l[0]=1.01
        l[1]=386
    if name=='HO' or name=='OH':
        l[0]=0.96
        l[1]=459
    if name=='PO' or name=='OP':
        l[0]=1.63
        l[1]=335
    if name=='CP' or name=='PC':
        l[0]=1.84   
        l[1]=264
    if name=='NP' or name=='PN':
        l[0]=1.7 
        l[1]=300 #gg
    if name=='PH' or name=='HP':
        l[0]=1.44
        l[1]=322
    if name=='HH':
        l[0]=.74
        l[1]=432
    if name=='ClC' or name=='CCl':
        l[0]=1.77
        l[1]=327
    if name=='ClH' or name=='HCl':
        l[0]=1.27
        l[1]=428
    if name=='ClO' or name=='OCl':
        l[0]=1.42
        l[1]=150 #gg
    if name=='ClN' or name=='NCl':
        l[0]=1.75
        l[1]=313
    if name=='ClP' or name=='PCl':
        l[0]=2.03
        l[1]=326
    
    if name=='ClCl' or name=='ClCl':
        l[0]=2.03
        l[1]=100
    return l
