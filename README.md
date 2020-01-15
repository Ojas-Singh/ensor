![](https://ojas-singh.github.io/xxz.png)

Ensor is a python program with advanced partitioning algorithms for optimizing Quantum calculation for large molecules.
> If one can divide a species of interest into fragments, employ some level of ab-initio QM to calculate the wave function, energy, and properties of each fragment, and then combine the results from the fragment calculations to predict the same properties for the whole, the possibility exists that the accuracy of the outcome can approach that which would be obtained from a full non fragmented calculation.

## Table of Contents

* [Partitioning Algorithm](#partitioning-algorithm)
	* [Building Connectivity of Molecule](#build-con-matrix)
	* [Information of optimal cut in Eigen Vector & Eigen Value of Laplacian](#laplacian)
	* [Overlaps Calculation](#overlap)
		* [Using neighbour atom](#neighbour)
		* [Using Fiedler Vector](#fiedler)
		* [Using Third Eigen Vector](#thirdeigh)
	* [Final recursive algorithm](#algorithm)
* [Cardinality Equation For Energies Calculation](#equation)
