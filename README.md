# CEC2008
Optimization in Python for CEC’2008 Benchmark Functions  (Competition on Large Scale Global Optimization)

## Description
See CEC2008_TechnicalReport.pdf

## Requirements
1. Python 3.7
2. Libraries
   - scypy
   - [pigmo](https://esa.github.io/pygmo2/install.html). Installed via Conda packet manager.
   - pandas
   - [opfunu](https://pypi.org/project/opfunu/) 
   Installation from github is recommendened (pip install git+https://github.com/thieunguyen5991/opfunu) as there is a bug fix I've    applied. See [this commit](https://github.com/thieunguyen5991/opfunu/commit/346f86686c38ce14238615165bc7547ced6390eb#diff-0dc1a3a4cb023fa8274168c2035ed91a)

## Run the script
1) Install required libraries
2) Execute **Baseline.py** in a Python 3.7 interpreter
3) Provide the inputs via command line:
   - Problem to solve (1 to 6)
   - Number of dimensions (1 to 500) 
   - Maximum iterations

For any problem with dimension = 2, you'll get a contour plot with the last generation swarm in blue and the best particle in red. For this to work the F_contour_soultion.txt files should be in the same folder as baseline.py,

## Algorithm

Rationale: Given that we're dealing with continuous search spaces, it seemd like PSO would be the best algorithm to go for as it seemed to perfrom better than simmulated annealing.

PSO is an evolutionary algorithm where each individual within the population, known as particle in PSO terminology, adjusts its flying trajectory in the multi-dimensional search space according to its own previous flying experience together with those of the neighbouring particles in the swarm. There are variations in terms the velocities and intitializations which define the variant but also different neighbour topologies to 

## Hyper-parameters

For the parametrization of the algorithm I've followed the recommendations of the following paper:

I've used the *Canonical PSO with inertia weight* variant mainly because that's the one I've seen in class, but it would be very intersting to explore the fully informed methodology.

In terms of topology of the swarm I've chosen and adaptive random topology, in which each particle randomly informs K particles and itself, with K set to 3. In this topology the connections between particles randomly change when the global optimum shows no improvement.

Following the proceedings of : M. Zambrano-Bigiarini, M. Clerc and R. Rojas, "Standard Particle Swarm Optimisation 2011 at CEC-2013: A baseline for future PSO improvements," doi: 10.1109/CEC.2013.6557848 I've defined a swarm of 40 particles with random initialisation of particle positions and velocities

The acceleration coefficients for the best positon of the particle (c1)  and best position of the swarm (c2) are set to to 0.5 + ln(2); 
in an unconstrained particle velocity and a constant inertia weight equal to ω = 1/(2 * ln(2)).


## Stopping criterion
Number of generations (parameter)

## Results
In all cases the best fit approached the global minima. Using D=2 as as an example to show contour plot.

```python

----------------------------------------------

Function:  Shifted Rosenbrock’s Function

Dimensions:  2

Generations:  50

----------------------------------------------

Optimization Running...

{} Problem name: <class '__main__.functions'>
	Global dimension:			2
	Integer dimension:			0
	Fitness dimension:			1
	Number of objectives:			1
	Equality constraints dimension:		0
	Inequality constraints dimension:	0
	Lower bounds: [-100, -100]
	Upper bounds: [100, 100]
	Has batch fitness evaluation: false

	Has gradient: false
	User implemented gradient sparsity: false
	Has hessians: false
	User implemented hessians sparsity: false

	Fitness evaluations: 0

	Thread safety: none
```


**Convergence curve**

![Convergence](https://github.com/mcrimi/CEC2008/blob/master/PSO_convergence.png?raw=true)

**Solution**


![Contour Plot](https://github.com/mcrimi/CEC2008/blob/master/Swarm.png?raw=true)

