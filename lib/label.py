from sklearn.cluster import SpectralClustering
import numpy as np


def SGP(pdbdata,n):
    # pdbdata=[N,X,Y,Z,A]
    o = len(pdbdata[1])
    molecule = []
    for i in range(o):
        molecule.append([pdbdata[1][i],pdbdata[2][i],pdbdata[3][i]])
    molecule=np.array(molecule)
    clustering = SpectralClustering(n_clusters=n,assign_labels="discretize",random_state=0).fit(molecule)
    labels = clustering.labels_
    f=[]
    for i in range(n):
        f.append([])
        for j in range(len(labels)):
            if labels[j]==i :
                f[i].append(pdbdata[0][j])

    return f
     
