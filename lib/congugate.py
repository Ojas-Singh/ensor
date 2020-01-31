import networkx 
from networkx.algorithms.components.connected import connected_components

def to_graph(l):
    G = networkx.Graph()
    for part in l:
        # each sublist is a bunch of nodes
        G.add_nodes_from(part)
        # it also imlies a number of edges:
        G.add_edges_from(to_edges(part))
    return G

def to_edges(l):
    """ 
        treat `l` as a Graph and returns it's edges 
        to_edges(['a','b','c','d']) -> [(a,b), (b,c),(c,d)]
    """
    it = iter(l)
    last = next(it)

    for current in it:
        yield last, current
        last = current    

def system(mol_Matrix,Dmol_Matrix):
    G=networkx.Graph(mol_Matrix)
    D=networkx.Graph(Dmol_Matrix)
    ringl= list(networkx.cycle_basis(D))
    rings=[]
    for i in ringl:
        if len(i) < 9:
            rings.append(i)
            for j in i:
                rings.append(list(G.neighbors(j))+[j])
    
    d=[]
    l=[]
    for i in range(len(mol_Matrix[0])):
        for j in range(0,i):
            if mol_Matrix[i][j]==2 :
                d.append([i+1,j+1])
    l=l+d
   
    for i in range(len(rings)):
        a=[]
        for j in rings[i]:
            a.append(j+1)
        l.append(a)
    
    X = to_graph(l)
    return list(connected_components(X))


