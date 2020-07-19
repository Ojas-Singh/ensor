import label

# unioqe
def inflation(f,pdbdata,Con_Matrix):  
    F=[]
    for fi in f:
        ir = []
        
        
        for r in range(5,int(len(pdbdata[0])/4)):
            Fi = []
            Fi = fi
            R = label.SGPW(pdbdata,r,Con_Matrix)
            for i in Om(pdbdata,fi,Con_Matrix):
                for j in R:
                    if i in j:
                        Fi = Fi + j
            
            ir.append((Io(list(set(Fi)),list(set(fi)),pdbdata,Con_Matrix),r))
        sir = sorted(ir,  key=lambda tup: tup[0])
        F.append(fi2Fi(sir[0][1],fi,pdbdata,Con_Matrix))
        print sir[0][1]
    return F

def fi2Fi(r,fi,pdbdata,Con_Matrix):
    Fi = fi 
    R = label.SGPW(pdbdata,r,Con_Matrix)
    for i in Om(pdbdata,fi,Con_Matrix):
        for j in R:
            if i in j:
                Fi = Fi + j

    return Fi



def rselector(f,pdbdata,Con_Matrix):
    ir = []
    for r in range(5,int(len(pdbdata[0])/2)):
        
        ir.append((Ir(r,f,pdbdata,Con_Matrix),r))
        print "For r : ",r,"Ir is : ",ir[r-5][0]
    sir = sorted(ir,  key=lambda tup: tup[0]) 
    print "Selected R is ",sir[0][1] 
    return sir[0][1]


def Om(pdbdata,fi,Con_Matrix):
    l = []
    k = [x for x in pdbdata[0] if x not in fi]
    for i in fi:
        for j in k:

            if Con_Matrix[i-1][j-1] >= 0.1 :
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
    return s*len(Oi)

def Fr(f,pdbdata,Con_Matrix,r):
    F = []
    R = label.SGPW(pdbdata,r,Con_Matrix)
    # R = [R1,R2,R3...,Rr]
    for fi in f:
        Fi = fi
        for i in Om(pdbdata,fi,Con_Matrix):
            for j in R:
                if i in j:
                    Fi = Fi + j
        F.append(Fi)
    return F

def Ir(r,f,pdbdata,Con_Matrix):
    Frr = Fr(f,pdbdata,Con_Matrix,r)
    Itotal = 0
    for Fi in Frr:
        for fi in f:
            Itotal = Itotal + Io(Fi,fi,pdbdata,Con_Matrix)

    return Itotal


