import label


def rselector(f,pdbdata,Con_Matrix,D_Matrix):
    ir = []
    for r in range(int(len(pdbdata[0])/32),int(len(pdbdata[0])/6)):
    
        
        ir.append((Ir(r,f,pdbdata,Con_Matrix,D_Matrix),r))
        print "For r : ",r,"Ir is : ",ir[r-int(len(pdbdata[0])/32)][0]
    sir = sorted(ir,  key=lambda tup: tup[0]) 
    print "Selected R is ",sir[0][1] 
    return sir[0][1]


def Om(pdbdata,fi,Con_Matrix,D_Matrix):
    l = []
    k = [x for x in pdbdata[0] if x not in fi]
    for i in fi:
        for j in k:

            if Con_Matrix[i-1][j-1]>2 and D_Matrix[i-1][j-1] < 4 :
                l.append(j) 
                l.append(i)
    ll = set(l)
    return list(ll)


def Io(Fi,fi,pdbdata,Con_Matrix):
    s = 0.0
    Oi = [x for x in Fi if x not in fi]
    notOi = [ x for x in pdbdata[0] if x not in Oi]
    for i in Oi:
        for j in notOi:
            s = s + Con_Matrix[i-1][j-1]
    return s*(len(Oi))**(2.0/3)

def Fr(f,pdbdata,Con_Matrix,r,D_Matrix):
    F = []
    R = label.SGPW(pdbdata,r,Con_Matrix)
    # R = [R1,R2,R3...,Rr]
    for fi in f:
        Fi = fi
        for i in Om(pdbdata,fi,Con_Matrix,D_Matrix):
            for j in R:
                if i in j:
                    Fi = Fi + j
        F.append(Fi)
    return F

def Ir(r,f,pdbdata,Con_Matrix,D_Matrix):
    Frr = Fr(f,pdbdata,Con_Matrix,r,D_Matrix)
    Itotal = 0
    for Fi in Frr:
        for fi in f:
            Itotal = Itotal + Io(list(set(Fi)),list(set(fi)),pdbdata,Con_Matrix)

    return Itotal


