
def name(l):
    res='_'.join(str(x) for x in l)
    return res
def export(pdbdata,G,F):
    f= open("XYZ/molecule.xyz","w+")
    num=str(len(G[1]))
    f.write(num+"\n")
    f.write("The Molecule\n")
    for i in G[1]:
        A=str(pdbdata[4][i-1])
        X='{: f}'.format(pdbdata[1][i-1])
        Y='{: f}'.format(pdbdata[2][i-1])
        Z='{: f}'.format(pdbdata[3][i-1])
        f.write("{:9} {:14} {:14} {}\n".format(A,X,Y,Z))
    for x in range(len(F)):
        if len(F[x][1])!=0:
            p= open("XYZ/part"+name(F[x][0])+".xyz","w+")
            num=str(len(F[x][1]))
            p.write(num+"\n")
            p.write("Part"+str(F[x][0])+"Frag\n")
            for i in F[x][1]:
                A=str(pdbdata[4][i-1])
                X='{: f}'.format(pdbdata[1][i-1])
                Y='{: f}'.format(pdbdata[2][i-1])
                Z='{: f}'.format(pdbdata[3][i-1])
                p.write("{:9} {:14} {:14} {}\n".format(A,X,Y,Z))

            
        