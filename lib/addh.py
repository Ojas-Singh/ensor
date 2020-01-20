def addhvector(Vf,Vm):
    v=


    return x,y,z
def addh(pdbdata,final,Matrix,w):
    new_mol=pdbdata
    new_final=final
    for x in range(len(final)):
        for i in pdbdata[0]:
            if i not in final[x][1]:
                for j in final[x][1]:
                    if Matrix[i-1][j-1] >= W:
                        v1=[pdbdata[1][j-1],pdbdata[2][j-1],pdbdata[3][j-1]]
                        v2=[pdbdata[1][i],pdbdata[2][i],pdbdata[3][i]]
                        num=len(new_mol)
                        h=addhvector(v1,v2)
                        new_final[x][1].append(num)
                        new_mol[0].append(num)
                        new_mol[1].append(h[0])
                        new_mol[2].append(h[1])
                        new_mol[3].append(h[2])
                        new_mol[4].append('H')
    return new_mol,new_final
