# Mathematical Optimization

![alt text](https://github.com/CatalaniCD/computer_science/blob/main/2.%20optimization/optz.png)

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

## Line Search

In optimization, the line search strategy is one of two basic iterative approaches to find a local minimum x∗ of an objective function f : R n → R . 
The other approach is trust region.

The line search approach first finds a descent direction along which the objective function f will be reduced and then computes a step size 
that determines how far x should move along that direction. The descent direction can be computed by various methods, 
such as gradient descent or quasi-Newton method. The step size can be determined either exactly or inexactly. 

Source : https://en.wikipedia.org/wiki/Line_search

## Vector Calculus

Vector calculus, or vector analysis, is concerned with differentiation and integration of vector fields, primarily in 3-dimensional Euclidean space R 3. 
The term "vector calculus" is sometimes used as a synonym for the broader subject of multivariable calculus, which spans vector calculus as well as 
partial differentiation and multiple integration. Vector calculus plays an important role in differential geometry and in the study 
of partial differential equations. It is used extensively in physics and engineering, especially in the description of electromagnetic fields, 
gravitational fields, and fluid flow. 

### Basic objects
#### Scalar fields
A scalar field associates a scalar value to every point in a space. The scalar is a mathematical number representing a physical quantity. 
Examples of scalar fields in applications include the temperature distribution throughout space, the pressure distribution in a fluid, 
and spin-zero quantum fields (known as scalar bosons), such as the Higgs field. These fields are the subject of scalar field theory.

#### Vector fields
A vector field is an assignment of a vector to each point in a space. A vector field in the plane, for instance, can be visualized as 
a collection of arrows with a given magnitude and direction each attached to a point in the plane. Vector fields are often used to model, 
for example, the speed and direction of a moving fluid throughout space, or the strength and direction of some force, such as the magnetic 
or gravitational force, as it changes from point to point. This can be used, for example, to calculate work done over a line.

#### Vectors and pseudovectors
In more advanced treatments, one further distinguishes pseudovector fields and pseudoscalar fields, which are identical to vector fields 
and scalar fields, except that they change sign under an orientation-reversing map: for example, the curl of a vector field is a pseudovector field, 
and if one reflects a vector field, the curl points in the opposite direction. This distinction is clarified and elaborated in geometric algebra, 
as described below.

#### Differential operators
Vector calculus studies various differential operators defined on scalar or vector fields, which are typically expressed in terms of the del operator ( ∇ ) also known as "nabla". The three basic vector operators are:

##### Differential operators in vector calculus 

    Operation :Notation
    Description
    Notational Analogy
    Domain / Range

Gradient : grad ⁡ ( f ) = ∇ f

    - Measures the rate and direction of change in a scalar field. 	
    - Scalar multiplication 	
    - Maps scalar fields to vector fields.

Divergence : div ⁡ ( F ) = ∇ ⋅ F

    - Measures the scalar of a source or sink at a given point in a vector field. 	
    - Dot product 	
    - Maps vector fields to scalar fields.

Curl : curl ⁡ ( F ) = ∇ × F 

    - Measures the tendency to rotate about a point in a vector field in R 3.
    - Cross product
    - Maps vector fields to (pseudo)vector fields.

*f denotes a scalar field and F denotes a vector field 

###### Laplace operators in vector calculus 

Laplacian :	Δ f = ∇ 2 f = ∇ ⋅ ∇ f

    - Measures the difference between the value of the scalar field with its average on infinitesimal balls. 	
    - Maps between scalar fields.

Vector Laplacian : ∇ 2 F = ∇ ( ∇ ⋅ F ) − ∇ × ( ∇ × F ) 

    - Measures the difference between the value of the vector field with its average on infinitesimal balls. 	
    - Maps between vector fields. 

#### Integral theorems

The three basic vector operators have corresponding theorems which generalize the fundamental theorem of calculus to higher dimensions:

##### Integral theorems of vector calculus 

    Theorem
    Statement
    Description

Gradient theorem 	∫ L ⊂ R n ∇ φ ⋅ d r   =   φ ( q ) − φ ( p )      for      L = L [ p → q ] 

    The line integral of the gradient of a scalar field over a curve L is equal to the change in the scalar field 
    between the endpoints p and q of the curve.

Divergence theorem 	∫ ⋯ ∫ V ⊂ R n ⏟ n ( ∇ ⋅ F ) d V   =   ∮ ⋯ ∮ ∂ V ⏟ n − 1 F ⋅ d S 

    The integral of the divergence of a vector field over an n-dimensional solid V is equal to the flux of the 
    vector field through the (n−1)-dimensional closed boundary surface of the solid.

Curl (Kelvin–Stokes) theorem 	∬ Σ ⊂ R 3 ( ∇ × F ) ⋅ d Σ   =   ∮ ∂ Σ F ⋅ d r 

    The integral of the curl of a vector field over a surface Σ in R 3 is equal to the circulation of the vector 
    field around the closed curve bounding the surface.φ denotes a scalar field and F denotes a vector field

##### Green's theorem of vector calculus 
In two dimensions, the divergence and curl theorems reduce to the Green's theorem:

    Theorem 	
    Statement 	
    Description

Green's theorem 	∬ A ⊂ R 2 ( ∂ M ∂ x − ∂ L ∂ y ) d A   =   ∮ ∂ A ( L d x + M d y ) 

    The integral of the divergence (or curl) of a vector field over some region A in R 2 equals the flux 
    (or circulation) of the vector field over the closed curve bounding the region.

*For divergence, F = (M, −L). For curl, F = (L, M, 0). L and M are functions of (x, y).

#### Applications

##### Linear approximations

Linear approximations are used to replace complicated functions with linear functions that are almost the same. Given a differentiable function f(x, y) with real values, one can approximate f(x, y) for (x, y) close to (a, b) by the formula

    f ( x , y )   ≈   f ( a , b ) + ∂ f ∂ x ( a , b ) ( x − a ) + ∂ f ∂ y ( a , b ) ( y − b )
    
The right-hand side is the equation of the plane tangent to the graph of z = f(x, y) at (a, b).

##### Optimization

For a continuously differentiable function of several real variables, a point P (that is, a set of values for the input variables, which is viewed as 
a point in Rn) is critical if all of the partial derivatives of the function are zero at P, or, equivalently, if its gradient is zero. 
The critical values are the values of the function at the critical points.

If the function is smooth, or, at least twice continuously differentiable, a critical point may be either a local maximum, a local minimum 
or a saddle point. The different cases may be distinguished by considering the eigenvalues of the Hessian matrix of second derivatives.

By Fermat's theorem, all local maxima and minima of a differentiable function occur at critical points. Therefore, to find the local maxima and minima, it suffices, theoretically, to compute the zeros of the gradient and the eigenvalues of the Hessian matrix at these zeros. 
