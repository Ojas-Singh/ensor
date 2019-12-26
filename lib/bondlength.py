#############################################################################################################################
##                                               Bond Length Data Average                                                  ##
##                                                                                                                         ##
##   Bondbtwatom =[[single bond lenght, error in it],[double bond lenght, error in it],[Triple bond lenght, error in it]]  ##
##                                                                                                                         ##
#############################################################################################################################

def search(name):
    l=[0,2,100]
    if name=='CH' or name=='HC':
        l[0]=1.2
    if name=='CC' or name=='CC':
        l[0]=1.7
    if name=='CN' or name=='NC':
        l[0]=1.6
    if name=='CO' or name=='OC':
        l[0]=1.5
    if name=='CS' or name=='SC':
        l[0]=1.8  
    if name=='NO' or name=='ON':
        l[0]=1.36  
    if name=='NN' or name=='NN':
        l[0]=1.5
    if name=='OO' or name=='OO':
        l[0]=1.7
    if name=='SO' or name=='OS':
        l[0]=1.5
    if name=='SN' or name=='NS':
        l[0]=1.8
    if name=='NN' or name=='NN':
        l[0]=1.5
    if name=='OO' or name=='OO':
        l[0]=1.7
    if name=='SS' or name=='SS':
        l[0]=1.7 
    if name=='PP' or name=='PP':
        l[0]=2
    if name=='NH' or name=='HN':
        l[0]=1.2 
    if name=='CCL' or name=='CLC':
        l[0]=1.8
    if name=='SO' or name=='OS':
        l[0]=1.5
    if name=='HO' or name=='OH':
        l[0]=1.2
    if name=='PO' or name=='OP':
        l[0]=1.65 
    if name=='CP' or name=='PC':
        l[0]=1.7   
    if name=='NP' or name=='PN':
        l[0]=1.7 
    if name=='PP' or name=='PP':
        l[0]=2
       
    return l




