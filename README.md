# ENSOR

Ensor is a python program with advanced partitioning algorithms for optimizing Quantum calculation for large molecules.
> If one can divide a species of interest into fragments, employ some level of ab-initio QM to calculate the wave function, energy, and properties of each fragment, and then combine the results from the fragment calculations to predict the same properties for the whole, the possibility exists that the accuracy of the outcome can approach that which would be obtained from a full non fragmented calculation.

### Table of Contents

* [Partitioning Algorithm](#partitioning-algorithm)
	* [Building Connectivity of Molecule](#building-connectivity-of-molecule)
	* [Information of optimal cut in Eigen Vector & Eigen Value of Laplacian](#information-of-optimal-cut-in-Eigen-vector-&-eigen-value-of-laplacian)
	* [Overlaps Calculation](#overlaps-calculation)
		* [Using neighbour atom](#using-neighbour-atom)
		* [Using Fiedler Vector](#fiedler)
		* [Using Third Eigen Vector](#thirdeigh)
	* [Final recursive algorithm](#algorithm)
* [Cardinality Equation For Energies Calculation](#equation)
#### Partitioning Algorithm


##### Building Connectivity of Molecule
We build Connectivity by assigning weight to the Matrix $$C_(n,n)$$ representing connectedness between atoms as. 

* $$w(d)=w_{max}^{\big(1-\frac{d^2}{d^2_0}\big)}$$
![](https://ojas-singh.github.io/gausconw.jpeg)

So, weighted connectivity $$C$$ is 
$$C_{i,j}=w(d)$$ where $$d$$ is the distance between $$i$$ and $$j$$ atom.

##### Information of optimal cut in Eigen Vector & Eigen Value of Laplacian

We define Laplacian $$L$$ as
* $$L=D-C$$  where $$D=diag(D_1,D_2,..,D_n)$$ with $$D_i=\sum_{j=1}^{n} C_{i,j}$$

  >The Laplacian of any graph $$G$$ have a balanced division knowledge, but the $$G$$ must be a one connected component. Otherwise a balanced division does not occur. 

Because $$L$$ is a symmetric matrix, its eigenvalues are real, and its eigenvectors are orthogonal to each other. Calculating eigenvalues and eigenvector using  $$Lv={\lambda} v$$, the eigenvector corresponding to the second smallest eigenvalue of L(G) is known as the Fiedler vector.

​                        $$v=\begin{bmatrix}v_0 & v_1 & v_2\\. & . & .\\. & . & .\\. & . & .\end{bmatrix}$$      ,        $${\lambda}=\begin{bmatrix}{\lambda}_0 & {\lambda}_1 & {\lambda}_2\\. & . & .\\. & . & .\\. & . & .\end{bmatrix}$$

here $$v_1$$ is Fiedler vector.

we can partition the molecule in two parts using these eigenvectors.

>if ${\lambda}^n_i>median({\lambda}_i)$  than node n is in $part_A$ else in $part_B$

Partition of 804 atom nanotube using eigenvector corresponding to first, second, third, fourth eigen values.

![](https://ojas-singh.github.io/Untitled-2.png )

