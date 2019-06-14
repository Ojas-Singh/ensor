#############################################################################################################################
##                                               Bond Length Data Average                                                  ##
##                                                                                                                         ##
##   Bondbtwatom =[[single bond lenght, error in it],[double bond lenght, error in it],[Triple bond lenght, error in it]]  ##
##                                                                                                                         ##
#############################################################################################################################

def search(name):
    l=[[0,0],[0,0],[0,0]]
    if name=='CH' or name=='HC':
        l=[[1.10,.05],[0,0],[0,0]]
    if name=='CC' or name=='CC':
        l=[[1.54,.05],[1.34,.05],[1.20,.05]]
    if name=='CN' or name=='NC':
        l=[[1.43,.05],[1.38,.05],[1.16,.05]]
    if name=='CO' or name=='OC':
        l=[[1.43,.05],[1.23,.05],[1.13,.05]]    
    return l



