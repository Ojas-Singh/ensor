import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D
from random import randint

def plot(G,frag,E,N,Coord,filename):
    Parts=frag[0]
    print "Printing generated Graph to graph.png..."
    pos=[]
    for i in range(len(N)):
        pos.append((Coord[0][i],Coord[1][i]))
    fig = plt.figure(figsize=(50,50))
    labels={}
    n=len(Parts)
    for i in range (0,len(E)):
        labels[i]=E[i]    
    pcolor=[]
    for i in range(n):
        pcolor.append('#%06X' % randint(0, 0xFFFFFF))
    for i in range(n):
        nodes=set(N).intersection(Parts[i][1])
        nodei=[N.index(x) for x in nodes]
        nx.draw_networkx_nodes(G,pos,
            nodelist=nodei,
            node_color=pcolor[i],
            node_size=500,
            alpha=0.8)
    cedi=[]
    for i in range(len(frag[1])):
        cutedge=set(N).intersection(frag[1][i])
        cedi.append(tuple([N.index(x) for x in cutedge]))
    nx.draw_networkx_edges(G,pos,
            edgelist=cedi,
            width=2,alpha=0.5,edge_color='r')
    options = { 
    'node_size': 500,
    'line_color': 'grey',
    'linewidths': 0,
    'width': 2,
    'edge_color':'white',
    'with_labels':True,
    'labels':labels,
    'alpha':0.8,
    'font_size':20,
    'font_color':'grey'
    }
    bonds=list(set(G.edges()).difference(cedi))
    nx.draw_networkx_edges(G,pos,
            edgelist=bonds,
            width=2,alpha=0.5,edge_color='w')
    nx.draw_networkx_labels(G,pos,labels,font_size=16)
    plt.axis('off')
    fig.text(0.95, 0.05, ' ENSOR',
        fontsize=70, color='gray',
        ha='right', va='bottom', alpha=0.5) 
    fig.text(0.05, 0.05, filename,
        fontsize=70, color='gray',
        ha='left', va='bottom', alpha=0.5)    
    fig.set_facecolor("#000000")
    plt.savefig("graph.png",facecolor=fig.get_facecolor())

    print "Graph Saved!"
