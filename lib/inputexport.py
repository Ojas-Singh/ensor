
def name(l):
    res='_'.join(str(x) for x in l)
    return res
def e(E):
    if E=='H':
        return 1
    if E=='C':
        return 6
    if E=='O':
        return 8
    if E=='P':
        return 15
    if E=='S':
        return 16
    if E=='N':
        return 7
    if E=='CL':
        return 17
    
    # if E=='':
    #     return 
    # if E=='':
    #     return 
    # if E=='':
    #     return 
    # if E=='':
    #     return 
    # if E=='':
    #     return 
def multi(pdbdata,frag):
    s=0
    for i in frag:
        s=s+e(pdbdata[4][i-1])
    if s%2==0:
        return 1
    else :
        return 2
def export(pdbdata,G,F):
    f= open("input/molecule.com","w+")
    f.write("%chk=molecule.chk"+"\n")
    f.write("%nproc=4\n")
    f.write("# hf/3-21g force \n")
    f.write("\n")
    f.write("The Molecule\n")
    f.write("\n")
    f.write("0 "+str(multi(pdbdata,G[1]))+"\n")
    for i in G[1]:
        A=str(pdbdata[4][i-1])
        X='{: f}'.format(pdbdata[1][i-1])
        Y='{: f}'.format(pdbdata[2][i-1])
        Z='{: f}'.format(pdbdata[3][i-1])
        f.write("{:9} {:14} {:14} {}\n".format(A,X,Y,Z))
    f.write("\n")
    for x in range(len(F)):
        if len(F[x][1])!=0:
            p= open("input/part"+name(F[x][0])+".com","w+")
            p.write("%chk=part"+name(F[x][0])+".chk"+"\n")
            p.write("%nproc=6\n")
            p.write("# hf/3-21g force \n")
            p.write("\n")
            p.write("Part"+str(F[x][0])+"Frag\n")
            p.write("\n")
            p.write("0 "+str(multi(pdbdata,F[x][1]))+"\n")
            
            for i in F[x][1]:
                A=str(pdbdata[4][i-1])
                X='{: f}'.format(pdbdata[1][i-1])
                Y='{: f}'.format(pdbdata[2][i-1])
                Z='{: f}'.format(pdbdata[3][i-1])
                p.write("{:9} {:14} {:14} {}\n".format(A,X,Y,Z))
            p.write("\n")

            
