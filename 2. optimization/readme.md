# Mathematical Optimization

### Simple Optimization

Mathematical optimization (alternatively spelled optimisation) or mathematical programming is the selection of a best element, 
with regard to some criterion, from some set of available alternatives. Optimization problems of sorts arise in all quantitative 
disciplines from computer science and engineering to operations research and economics, and the development of solution methods 
has been of interest in mathematics for centuries.

In the simplest case, an optimization problem consists of maximizing or minimizing a real function by systematically choosing 
input values from within an allowed set and computing the value of the function. The generalization of optimization theory and 
techniques to other formulations constitutes a large area of applied mathematics. M
ore generally, optimization includes finding "best available" values of some objective function given a defined domain (or input), 
including a variety of different types of objective functions and different types of domains.
    
Source : https://en.wikipedia.org/wiki/Mathematical_optimization 

### Constrained Optimization

In mathematical optimization, constrained optimization (in some contexts called constraint optimization) is the process 
of optimizing an objective function with respect to some variables in the presence of constraints on those variables. 
The objective function is either a cost function or energy function, which is to be minimized, or a reward function or 
utility function, which is to be maximized. Constraints can be either hard constraints, which set conditions for the 
variables that are required to be satisfied, or soft constraints, which have some variable values that are penalized 
in the objective function if, and based on the extent that, the conditions on the variables are not satisfied. 
    
Source :  https://en.wikipedia.org/wiki/Constrained_optimization
### Convex Optimization

Convex optimization is a subfield of mathematical optimization that studies the problem of minimizing convex functions over convex sets.
Many classes of convex optimization problems admit polynomial-time algorithms, whereas mathematical optimization is in general NP-hard.

Convex optimization has applications in a wide range of disciplines, such as automatic control systems, estimation and signal processing, 
communications and networks, electronic circuit design, data analysis and modeling, finance, statistics (optimal experimental design), 
and structural optimization, where the approximation concept has proven to be efficient. With recent advancements in computing and 
optimization algorithms, convex programming is nearly as straightforward as linear programming.

Source : https://en.m.wikipedia.org/wiki/Convex_optimization

### Combinatorial Optimization

Combinatorial optimization is a subfield of mathematical optimization that is related to operations research, 
algorithm theory, and computational complexity theory. It has important applications in several fields, 
including artificial intelligence, machine learning, auction theory, software engineering,
applied mathematics and theoretical computer science.

Combinatorial optimization is a topic that consists of finding an optimal object from a finite set of objects. 
In many such problems, exhaustive search is not tractable. It operates on the domain of those optimization 
problems in which the set of feasible solutions is discrete or can be reduced to discrete, 
and in which the goal is to find the best solution. Typical problems are the travelling salesman problem ("TSP"), 
the minimum spanning tree problem ("MST"), and the knapsack problem.

Some research literature considers discrete optimization to consist of integer programming together 
with combinatorial optimization (which in turn is composed of optimization problems dealing with graph structures) 
although all of these topics have closely intertwined research literature. 
It often involves determining the way to efficiently allocate resources used to find solutions to mathematical problems. 
    
Source : https://en.wikipedia.org/wiki/Combinatorial_optimization

## Search Space

In mathematical optimization, a feasible region, feasible set, search space, or solution space is the set of all possible points 
(sets of values of the choice variables) of an optimization problem that satisfy the problem's constraints, 
potentially including inequalities, equalities, and integer constraints. 
This is the initial set of candidate solutions to the problem, before the set of candidates has been narrowed down.

For example, consider the problem

    Minimize x**2 + y**2

with respect to the variables x  and y 

subject to

    1 ≤ x ≤ 10 

and

    5 ≤ y ≤ 12.

Here the feasible set is the set of pairs (x, y) in which the value of x is at least 1 and at most 10 and the 
value of y is at least 5 and at most 12. Note that the feasible set of the problem is separate from the objective function,
which states the criterion to be optimized and which in the above example is x 2 + y 4 .

In many problems, the feasible set reflects a constraint that one or more variables must be non-negative. 
In pure integer programming problems, the feasible set is the set of integers (or some subset thereof). 
In linear programming problems, the feasible set is a convex polytope: a region in multidimensional space whose boundaries are formed 
by hyperplanes and whose corners are vertices.

Constraint satisfaction is the process of finding a point in the feasible region.
    
Source : https://en.wikipedia.org/wiki/Feasible_region
