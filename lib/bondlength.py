#############################################################################################################################
##                                               Bond Length Data Average                                                  ##
##                                                                                                                         ##
##   Bondbtwatom =[[single bond lenght][will decide later][max Weight]]                                                    ##
##                              http://www.wiredchemist.com/chemistry/data/bond_energies_lengths.html                                                                                           ##
#############################################################################################################################

def search(name):
    l=[1.2,3.0,5]
    if name=='CH' or name=='HC':
        l[0]=1.09
    if name=='CC' or name=='CC':
        l[0]=1.54
    if name=='CN' or name=='NC':
        l[0]=1.47
    if name=='CO' or name=='OC':
        l[0]=1.43
    if name=='CS' or name=='SC':
        l[0]=1.82  
    if name=='NO' or name=='ON':
        l[0]=1.40  
    if name=='NN' or name=='NN':
        l[0]=1.45
    if name=='OO' or name=='OO':
        l[0]=1.48
    if name=='SO' or name=='OS':
        l[0]=1.43
    if name=='SN' or name=='NS':
        l[0]=1.8
    if name=='SS' or name=='SS':
        l[0]=1.49
    if name=='PP' or name=='PP':
        l[0]=2.21
    if name=='NH' or name=='HN':
        l[0]=1.01
    if name=='CCL' or name=='CLC':
        l[0]=1.77
    if name=='SO' or name=='OS':
        l[0]=1.43
    if name=='HO' or name=='OH':
        l[0]=0.96
    if name=='PO' or name=='OP':
        l[0]=1.63
    if name=='CP' or name=='PC':
        l[0]=1.84   
    if name=='NP' or name=='PN':
        l[0]=1.7 
    if name=='PH' or name=='HP':
        l[0]=1.44
    if name=='HH':
        l[0]=.74
    if name=='ClC' or name=='CCl':
        l[0]=1.77
    if name=='ClH' or name=='HCl':
        l[0]=1.27
    if name=='ClO' or name=='OCl':
        l[0]=1
    if name=='ClN' or name=='NCl':
        l[0]=1.75
    if name=='ClP' or name=='PCl':
        l[0]=2.03
    return l




