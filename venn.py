import itertools


from itertools import chain, combinations
def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))


def func(Parts):
    n=len(Parts)
    final=[]
    #Final=[[f1,f2,f3...fn],[f1&f2,f2&f3,f1&fn ...],[f1&f2&f3,f2&f3&f4,...],...[]]
    num=[[i] for i in range(n)]
    x=list(all_subsets(num))
    x.pop(0)
    pl=[]
    for i in range(n):
        of=[]
        for j in range(len(Parts[i][1])):
            of.append(str(Parts[i][1][j]))
        pl.append(set(of))
    for subset in x:
        frag=[subset[i][0] for i in range(len(list(subset)))]
        d=[pl[subset[i][0]] for i in range(len(list(subset)))]
        z = pl[subset[0][0]].intersection(*map(set,d))
        z=map(int, z)
        final.append((frag,list(z)))
    
    return final
        


    
