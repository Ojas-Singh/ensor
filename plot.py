from mpl_toolkits.mplot3d import Axes3D 
from lib import pdb2con as chef
from matplotlib import animation
import sys
import subprocess
import os
#For plotting---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'Latin Modern Roman Demi','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('legend', fontsize=10)
plt.rcParams['figure.figsize']=[8,8]
#---
def Laplacian_matrix(M):
    laplacian_matrix=np.zeros(M.shape)
    d=np.sum(M,axis=1)
    for i in range(len(d)):
        for j in range(len(d)):
            if i==j:
                laplacian_matrix[i][j]=1       
            else:
                laplacian_matrix[i][j]=-M[i][j]/np.sqrt(d[i]*d[j])
            
    return laplacian_matrix
def main():
    script=sys.argv[0]
    filename = sys.argv[1]
    frmes=25
    wi=5.
    wf=25.
    h=(wf-wi)/frmes
    fx1=[]
    for i in range(frmes):
        print i+1
        pdbdata= chef.pdb2con(filename,wi+i*h)
        N=pdbdata[0]
        E=pdbdata[4]
        Coord=[pdbdata[1],pdbdata[2],pdbdata[3]]
        Adj_Matrix=np.load('results/Con_matrix.npy')
        L=Laplacian_matrix(Adj_Matrix)
        eigenvalues, eigenvectors = np.linalg.eigh(L)
        index_fnzev = np.argsort(eigenvalues)[1]
        fx = eigenvectors[:,index_fnzev] 
        [x,y,z]=Coord
        x,y,z=np.array(x),np.array(y),np.array(z)
        fx1.append(fx)
        

    
    def init():
        ax = fig.gca(projection='3d')
        ax.grid(False)
        plt.grid(b=None)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        # ax.margins(x=0,y=0,z=0)
        
        # ax.set_aspect('equal', 'box')  
        # Get rid of the panes  
        ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

        # Get rid of the spines
        ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        # ax.set_xlabel('Pressure (Bar)')
        # ax.set_zlabel('Residual subcooling (J*Kg-1*K-1')
        # ax.set_ylabel('Temperaure of LNG (K)')
        # plt.title(filename)
        max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max()
        Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
        Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
        Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z.max()+z.min())
        # Comment or uncomment following both lines to test the fake bounding box:
        for xb, yb, zb in zip(Xb, Yb, Zb):
            ax.plot([xb], [yb], [zb], 'w')
        nme=filename.replace('pdb/','')
        nme=nme.replace('.pdb','')
        # ax.view_init(45, -80) #basepair
        ax.view_init(0,0) #1bna
        # p=ax.scatter(x,y,z, c=fx, cmap='jet')
        # fig.colorbar(p, shrink=.6, orientation="horizontal",pad=-.2).set_label(r'$f_2$', fontsize=12)
        # plt.show()
        # plt.savefig('plot/plot'+nme+str(i+1)+'.png', dpi=600, bbox_inches='tight')
        plt.title(r'$w_0='+str(wi+i*h)+r'$')
        p=ax.scatter(x,y,z, c=fx1[0], cmap='jet')
        fig.colorbar(p, shrink=.6, orientation="horizontal").set_label(r'$f_2$', fontsize=12)
        return fig,

    nme=filename.replace('pdb/','')
    nme=nme.replace('.pdb','')
    fig = plt.figure()
    def animate(i):
        plt.clf()
        ax = fig.gca(projection='3d')
        ax.grid(False)
        plt.grid(b=None)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        # ax.margins(x=0,y=0,z=0)
        
        # ax.set_aspect('equal', 'box')  
        # Get rid of the panes  
        ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

        # Get rid of the spines
        ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        # ax.set_xlabel('Pressure (Bar)')
        # ax.set_zlabel('Residual subcooling (J*Kg-1*K-1')
        # ax.set_ylabel('Temperaure of LNG (K)')
        # plt.title(filename)
        max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max()
        Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
        Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
        Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z.max()+z.min())
        # Comment or uncomment following both lines to test the fake bounding box:
        for xb, yb, zb in zip(Xb, Yb, Zb):
            ax.plot([xb], [yb], [zb], 'w')
        nme=filename.replace('pdb/','')
        nme=nme.replace('.pdb','')
        # ax.view_init(45, -80) #basepair
        # ax.view_init(0,0) #1bna
        ax.view_init(55,-15) #vanco
        # p=ax.scatter(x,y,z, c=fx, cmap='jet')
        # fig.colorbar(p, shrink=.6, orientation="horizontal",pad=-.2).set_label(r'$f_2$', fontsize=12)
        # plt.show()
        # plt.savefig('plot/plot'+nme+str(i+1)+'.png', dpi=600, bbox_inches='tight')
        plt.title(r'$w_0='+str(wi+i*h)+r'$')
        p=ax.scatter(x,y,z, c=fx1[i], cmap='jet')
        fig.colorbar(p, shrink=.6, orientation="horizontal",pad=-.2).set_label(r'$f_2$', fontsize=12)
        return fig,
    anim = animation.FuncAnimation(fig, animate, init_func=init,frames=frmes, interval=1, blit = False)
    anim.save('plot/'+nme+'.gif',writer='imagemagick',fps=10)


# Rot

    # frmes=50
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # pdbdata= chef.pdb2con(filename,3)
    # N=pdbdata[0]
    # E=pdbdata[4]
    # Coord=[pdbdata[1],pdbdata[2],pdbdata[3]]
    # Adj_Matrix=np.load('results/Con_matrix.npy')
    # L=Laplacian_matrix(Adj_Matrix)
    # eigenvalues, eigenvectors = np.linalg.eigh(L)
    # index_fnzev = np.argsort(eigenvalues)[1]
    # fx = eigenvectors[:,index_fnzev] 
    # [x,y,z]=Coord
    # x,y,z=np.array(x),np.array(y),np.array(z)
    # def init():
    #     ax = fig.gca(projection='3d')
    #     ax.grid(False)
    #     plt.grid(b=None)
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #     ax.set_zticks([])
    #     # ax.margins(x=0,y=0,z=0)
        
    #     # ax.set_aspect('equal', 'box')  
    #     # Get rid of the panes  
    #     ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    #     ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    #     ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    #     # Get rid of the spines
    #     ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    #     ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    #     ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    #     # ax.set_xlabel('Pressure (Bar)')
    #     # ax.set_zlabel('Residual subcooling (J*Kg-1*K-1')
    #     # ax.set_ylabel('Temperaure of LNG (K)')
    #     # plt.title(filename)
    #     max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max()
    #     Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
    #     Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
    #     Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z.max()+z.min())
    #     # Comment or uncomment following both lines to test the fake bounding box:
    #     for xb, yb, zb in zip(Xb, Yb, Zb):
    #         ax.plot([xb], [yb], [zb], 'w')
    #     nme=filename.replace('pdb/','')
    #     nme=nme.replace('.pdb','')
    #     # ax.view_init(45, -80) #basepair
    #     ax.view_init(0,0) #1bna
    #     # p=ax.scatter(x,y,z, c=fx, cmap='jet')
    #     # fig.colorbar(p, shrink=.6, orientation="horizontal",pad=-.2).set_label(r'$f_2$', fontsize=12)
    #     # plt.show()
    #     # plt.savefig('plot/plot'+nme+str(i+1)+'.png', dpi=600, bbox_inches='tight')
    #     # plt.title(r'$w_0='+str(wi+i*h)+r'$')
    #     p=ax.scatter(x,y,z, c=fx, cmap='jet')
    #     fig.colorbar(p, shrink=.6, orientation="horizontal",pad=-.2).set_label(r'$f_2$', fontsize=12)
    #     return fig,

    # nme=filename.replace('pdb/','')
    # nme=nme.replace('.pdb','')
    # def animate(i):
    #     ax.view_init(elev=20,azim=i*360/frmes)
    #     return fig,
    # anim = animation.FuncAnimation(fig, animate, init_func=init,frames=frmes, blit = True)
    # anim.save('plot/'+nme+'rot.gif',writer='imagemagick',fps=24)
if __name__ == '__main__':
   main()