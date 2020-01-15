![](https://ojas-singh.github.io/xxz.png)

Ensor is a python program with advanced partitioning algorithms for optimizing Quantum calculation for large molecules.
> If one can divide a species of interest into fragments, employ some level of ab-initio QM to calculate the wave function, energy, and properties of each fragment, and then combine the results from the fragment calculations to predict the same properties for the whole, the possibility exists that the accuracy of the outcome can approach that which would be obtained from a full non fragmented calculation.

### Table of Contents

* [Partitioning Algorithm](#partitioning-algorithm)
	* [Building Connectivity of Molecule](#build-con-matrix)
	* [Information of optimal cut in Eigen Vector & Eigen Value of Laplacian](#laplacian)
	* [Overlaps Calculation](#overlap)
		* [Using neighbour atom](#neighbour)
		* [Using Fiedler Vector](#fiedler)
		* [Using Third Eigen Vector](#thirdeigh)
	* [Final recursive algorithm](#algorithm)
* [Cardinality Equation For Energies Calculation](#equation)
#### Partitioning Algorithm
To intelligently store and operate on molecule we make a Tensor (array) which contains Connectivity Matrix ,Atoms Co-ordinate,Element info. (we can extract all these info from Protein Data Bank file of molecule) 

##### Building Connectivity of Molecule
We build Connectivity by assigning weight to the Matrix $$C_(n,n)$$ representing connectedness between atoms as. 

* $$w(d)=w_{max}^{\big(1-\frac{d^2}{d^2_0}\big)}$$
![](https://ojas-singh.github.io/gausconw.jpeg)

##### Information of optimal cut in Eigen Vector & Eigen Value of Laplacian

We define Laplacian as
* $$l_(n,n)=D_(n,n)-C_(n,n)$$ where $$D$$ is 
```python
Degree_Matrix =  np.diag(np.ravel(np.sum(C[0],axis=1))) 
```
The Laplacian of any graph $$G$$ have a balanced division knowledge, but the $$G$$ must be a one connected component. Otherwise a balanced division does not occur. 

To calculate Eigen Values and corresponding Eigen Vector of $$l_(n,n)$$ ,we use :

```python
eigenvalues, eigenvectors = np.linalg.eigh(Laplacian_matrix)
```
```math
l_(n,n)=a+b
```
