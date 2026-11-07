# New topics report: mathematics

Status: COMPLETE. 26 new topic files written; 29 proposed edges into existing topics. No existing file was edited.

Method: for each course I grepped the `title:` lines (and, for each candidate gap, the bodies of all files under `domains/`) and compared them against a named syllabus. A candidate counted as a gap only if no topic anywhere in `domains/` covers it as its subject. A passing mention inside another topic's explainer was not counted as coverage. All new ids were checked unique with Glob. All prerequisite and builds-toward ids were checked to exist with Glob. Each new edge was checked by hand for cycles against the prerequisite lists of the targets.

## 1. Syllabi compared against

| course | syllabus used |
|---|---|
| kindergarten to 5th-grade | Common Core State Standards for Mathematics (CCSS-M), grade-level clusters. Spot-checked only, because coverage is dense, with many near-duplicate topics. |
| prealgebra | CCSS-M Grades 6 to 8 (The Number System, Expressions and Equations, Functions, Geometry, Statistics and Probability) |
| algebra-1 | CCSS-M High School Algebra I course (A-SSE, A-CED, A-REI, F-IF, F-BF, F-LE, S-ID) |
| geometry | CCSS-M High School Geometry (G-CO, G-SRT, G-C, G-GPE, G-GMD), checked against the chapter order of a standard high-school geometry text (Larson) |
| algebra-2 | CCSS-M Algebra II course |
| precalculus | Stewart, Redlin and Watson, *Precalculus*; College Board AP Precalculus CED |
| calculus-1, calculus-2 | College Board AP Calculus AB/BC CED; Stewart, *Calculus*, chapters 1 to 11 |
| multivariable-calculus | Stewart, *Calculus*, chapters 12 to 16 |
| linear-algebra | Lay, *Linear Algebra and Its Applications* |
| methods-of-proof | Velleman, *How to Prove It*; Hammack, *Book of Proof* |
| probability-and-statistics | College Board AP Statistics CED; standard intro probability and statistics texts |
| discrete-math | Rosen, *Discrete Mathematics and Its Applications* |
| differential-equations | Boyce and DiPrima, *Elementary Differential Equations and Boundary Value Problems*; Zill |
| real-analysis | Rudin, *Principles of Mathematical Analysis*; Abbott, *Understanding Analysis* |
| abstract-algebra | Gallian, *Contemporary Abstract Algebra*; Dummit and Foote, *Abstract Algebra* |
| topology | Munkres, *Topology* |
| complex-analysis | Brown and Churchill; Stein and Shakarchi, *Complex Analysis*; Ahlfors |
| number-theory | Burton, *Elementary Number Theory*; Niven, Zuckerman and Montgomery |
| probability-and-mathematical-statistics | Casella and Berger, *Statistical Inference*; Hogg, McKean and Craig |
| numerical-analysis | Burden and Faires, *Numerical Analysis* |
| graph-theory-and-combinatorics | West, *Introduction to Graph Theory*; Brualdi, *Introductory Combinatorics* |
| measure-theory-and-functional-analysis | Folland, *Real Analysis*; Royden, *Real Analysis* |
| algebraic-topology | Hatcher, *Algebraic Topology* |
| partial-differential-equations | Evans, *Partial Differential Equations*; Strauss |
| differential-geometry | do Carmo, *Differential Geometry of Curves and Surfaces*; Lee, *Introduction to Smooth Manifolds* |
| commutative-algebra | Atiyah and Macdonald; Eisenbud |
| stochastic-processes | Ross, *Introduction to Probability Models*; Durrett |
| representation-theory | Fulton and Harris, *Representation Theory*; Serre, *Linear Representations of Finite Groups* |

Courses with no gaps found: kindergarten to 5th-grade (spot-checked), precalculus, linear-algebra, methods-of-proof, discrete-math, topology, number-theory (see deferred list), numerical-analysis (see deferred list), graph-theory-and-combinatorics, algebraic-topology, partial-differential-equations.

## 2. New topics

| new id | course | why it is a gap (which syllabus unit) | prerequisites |
|---|---|---|---|
| gcf-and-lcm | prealgebra | CCSS 6.NS.4 (GCF and LCM). Only `factors-and-multiples` (4th grade) and `factoring-gcf` (algebra-1, monomials) exist. No topic teaches LCM. | factors-and-multiples (hard), prime-and-composite-numbers (hard), multiples-of-a-number (soft) |
| rational-and-irrational-numbers | prealgebra | CCSS 8.NS.1 to 2. No topic anywhere covers irrational numbers or the real number system. | square-roots-intro (hard), converting-fractions-decimals-percents (hard), rational-numbers-operations (soft) |
| mean-absolute-deviation | prealgebra | CCSS 6.SP.5c (measures of variability). The term "mean absolute deviation" appears nowhere in the graph. | mean-median-mode-with-data-sets (hard), absolute-value (hard), box-and-whisker-plots (soft) |
| functions-and-relations | algebra-1 | CCSS 8.F.1 / F-IF.1 (definition of a function, relations, vertical line test). Only function tables and a precalculus notation review exist. | function-tables (hard), coordinate-plane-all-four-quadrants (hard) |
| triangle-congruence-hl | geometry | HS Geometry right-triangle congruence (the HL theorem, a standard section). SSS, SAS, ASA and AAS exist; HL is only mentioned in `tangent-lines-to-circles`. | triangle-congruence-sss (hard), pythagorean-theorem (hard), triangle-congruence-sas (soft) |
| similar-right-triangles-geometric-mean | geometry | G-SRT.4 to 5; the "Similar Right Triangles" section (altitude to the hypotenuse, geometric mean). "Geometric mean" appears nowhere in geometry. | similar-triangles-aa (hard), proportions-in-similar-triangles (hard), pythagorean-theorem (soft) |
| angles-formed-by-chords-secants-tangents | geometry | G-C.2 (angles formed by chords, secants and tangents). Only inscribed and central angles exist. | inscribed-angles (hard), central-angles-and-arcs (hard), exterior-angle-theorem (hard), tangent-lines-to-circles (soft) |
| absolute-extrema-closed-interval | calculus-1 | AP Calculus 5.2 and 5.5; Stewart 4.1 (Extreme Value Theorem and the closed interval method). Calculus-1 has only the first and second derivative tests. | continuity-definition (hard), first-derivative-test (hard), intermediate-value-theorem (soft) |
| average-value-of-a-function | calculus-1 | AP Calculus 8.1; Stewart 6.5 (average value and the Mean Value Theorem for Integrals). No topic covers it. | definite-integral-definition (hard), fundamental-theorem-of-calculus-part-2 (hard), riemann-sums (soft), mean-value-theorem (soft) |
| hyperbolic-functions | calculus-1 | Stewart 3.11 (hyperbolic functions). "sinh" appears only in complex analysis and advanced files. | derivatives-of-exponential-functions (hard), trigonometric-identities-pythagorean (soft) |
| quadric-surfaces | multivariable-calculus | Stewart 12.6 (cylinders and quadric surfaces). Only passing mentions exist. | 3d-coordinate-systems (hard), conic-sections-overview (hard), equations-lines-planes-3d (soft) |
| bernoulli-differential-equations | differential-equations | Boyce and DiPrima 2.4 problems; Zill 2.5 (solutions by substitution: Bernoulli and homogeneous equations). No topic covers it. | integrating-factor-method (hard), separable-differential-equations (soft) |
| cauchy-euler-equations | differential-equations | Boyce and DiPrima 5.4 (Euler equations); Zill 4.7. Only one-line mentions exist. | characteristic-equation-method (hard), repeated-roots-reduction-of-order (soft), complex-roots-oscillatory-solutions (soft) |
| arzela-ascoli-theorem | real-analysis | Rudin ch. 7 (equicontinuous families of functions); Munkres ch. 7. Only a passing mention exists in `sequential-compactness-metric-spaces`. | uniform-convergence (hard), uniform-continuity (hard), compact-metric-spaces (hard), bolzano-weierstrass-theorem (soft), cantor-diagonalization (soft) |
| inverse-function-theorem | real-analysis | Rudin ch. 9; Spivak, *Calculus on Manifolds*, ch. 2. Only the manifold version of the implicit function theorem exists. The inverse function theorem is cited in three differential geometry topics with no topic of its own. | total-differential (hard), contraction-mapping-theorem (hard), matrix-inverses (hard), jacobian-change-of-variables (soft), mean-value-theorem-rigorous (soft) |
| schwarz-lemma | complex-analysis | Stein and Shakarchi 8.2; Ahlfors ch. 4 (Schwarz's lemma and automorphisms of the disk). Absent from the graph. | maximum-modulus-principle (hard), singularities-classification (soft), mobius-transformations (soft) |
| riemann-mapping-theorem | complex-analysis | Stein and Shakarchi 8.3; Ahlfors 6.1. Absent from the graph. | schwarz-lemma (hard), conformal-mappings (hard), connected-simply-connected-plane (hard), liouville-theorem (soft), arzela-ascoli-theorem (soft) |
| semidirect-products | abstract-algebra | Dummit and Foote 5.5. Mentioned once in `applications-sylow-theorems`, with no topic of its own. | normal-subgroups (hard), direct-products-groups (hard), group-homomorphisms (hard), group-isomorphisms (hard), dihedral-groups (soft) |
| transformations-of-random-variables | probability-and-mathematical-statistics | Casella and Berger 2.1 and 4.3; Hogg, McKean and Craig ch. 1 to 2 (distributions of functions of random variables). Only linear transformations exist. | probability-density-functions (hard), cumulative-distribution-function (hard), linear-transformations-of-random-variables (soft), jacobian-change-of-variables (soft) |
| order-statistics | probability-and-mathematical-statistics | Casella and Berger 5.4; Hogg 4.4. Mentioned in passing in three files, with no topic of its own. | cumulative-distribution-function (hard), probability-density-functions (hard), binomial-distribution (soft), transformations-of-random-variables (soft) |
| lebesgue-differentiation-theorem | measure-theory-and-functional-analysis | Folland 3.4 to 3.5; Royden ch. 6 (differentiation, absolute continuity, maximal function). Absent from the graph. | introduction-lebesgue-integral (hard), lebesgue-measure-euclidean-space (hard), dominated-convergence-theorem (soft), fundamental-theorem-calculus-rigorous (soft) |
| first-fundamental-form | differential-geometry | do Carmo 2.5. The course goes straight to manifolds; classical surface theory is absent. | parametric-surfaces (hard), surface-area-integrals (hard), dot-product (soft) |
| gaussian-and-mean-curvature | differential-geometry | do Carmo 3.2 to 3.3 (second fundamental form, shape operator, principal, Gaussian and mean curvature); also states Theorema Egregium (do Carmo 4.3). Absent from the graph. | first-fundamental-form (hard), curvature (hard), eigenvalues-and-eigenvectors (hard), hessian-matrix-second-derivative-test (soft) |
| ca-hilbert-nullstellensatz | commutative-algebra | Atiyah and Macdonald ch. 5 and 7 exercises; Eisenbud ch. 4. Cited in three files, with no topic of its own. | ca-noether-normalization (hard), ca-prime-and-maximal-ideals (hard), ca-ideal-operations (soft), ca-hilbert-basis-theorem (soft) |
| queueing-theory-mm1 | stochastic-processes | Ross, *Introduction to Probability Models*, ch. 8 (queueing theory, Little's law). Absent from the graph. | continuous-time-markov-chains (hard), poisson-processes (hard), exponential-distribution (hard), geometric-distribution (soft) |
| root-systems | representation-theory | Fulton and Harris, Part III (root systems, Dynkin diagrams, classification). Only sl₂ is covered; "root system" appears in no topic. | lie-groups-and-lie-algebras (hard), representations-of-sl2 (hard), inner-product-spaces (hard), eigenvalues-and-eigenvectors (soft) |

## Proposed edges into existing topics

ADD	gcf-and-lcm	factoring-gcf	soft	Factoring out a GCF assumes students can find the GCF of the numerical coefficients.
ADD	gcf-and-lcm	adding-fractions-unlike-denominators	soft	The least common denominator is the LCM of the denominators.
ADD	rational-and-irrational-numbers	radical-expressions-simplifying	soft	Simplifying radicals presumes knowing which roots are rational and which are irrational.
ADD	rational-and-irrational-numbers	completeness-axiom	soft	The completeness axiom distinguishes ℝ from ℚ; the informal rational/irrational picture motivates it.
ADD	mean-absolute-deviation	variance-standard-deviation	soft	MAD is the first measure of spread around the mean; standard deviation refines it with squared deviations.
ADD	functions-and-relations	linear-functions	hard	A linear function is a special case of the function concept defined here.
ADD	functions-and-relations	function-notation-review	hard	f(x) notation presupposes that each input has exactly one output.
ADD	functions-and-relations	domain-and-range	soft	Domain and range are introduced informally in the relations topic.
ADD	triangle-congruence-hl	tangent-lines-to-circles	soft	The two-tangent theorem in that topic is proved with HL (its own text says "hypotenuse-leg").
ADD	similar-right-triangles-geometric-mean	right-triangle-trigonometry-intro	soft	Similar right triangles explain why trigonometric ratios do not depend on triangle size.
ADD	absolute-extrema-closed-interval	optimization-problems	hard	Optimization on a closed interval uses the closed interval method.
ADD	absolute-extrema-closed-interval	extreme-value-theorem-rigorous	soft	The rigorous proof formalizes the Extreme Value Theorem first met here.
ADD	hyperbolic-functions	complex-trigonometric-functions	soft	cos(iz) = cosh z and sin(iz) = i sinh z link the two families.
ADD	hyperbolic-functions	trigonometric-substitution	soft	Hyperbolic substitutions are an alternative for integrals with √(x² + a²).
ADD	quadric-surfaces	functions-of-several-variables	soft	Graphs of functions of two variables are often quadric surfaces (paraboloids, saddles).
ADD	cauchy-euler-equations	frobenius-method	soft	The Frobenius indicial equation generalizes the Cauchy-Euler indicial equation at a regular singular point.
ADD	arzela-ascoli-theorem	compact-operators	soft	Compactness of integral operators is usually proved with Arzelà-Ascoli.
ADD	arzela-ascoli-theorem	existence-uniqueness-ode	soft	The Peano existence theorem (continuous f only) is proved with Arzelà-Ascoli.
ADD	inverse-function-theorem	implicit-function-theorem-on-manifolds	hard	The implicit function theorem is derived from the inverse function theorem.
ADD	inverse-function-theorem	exponential-map	soft	That topic invokes the inverse function theorem to show exp_p is a local diffeomorphism.
ADD	semidirect-products	applications-of-sylow-theorems	soft	Classifying groups of order pq and similar uses semidirect products.
ADD	first-fundamental-form	riemannian-metrics	soft	A Riemannian metric generalizes the first fundamental form from surfaces to manifolds.
ADD	first-fundamental-form	gauss-bonnet-theorem	soft	The classical Gauss-Bonnet theorem is stated for surfaces with metric E, F, G.
ADD	gaussian-and-mean-curvature	gauss-bonnet-theorem	soft	Gauss-Bonnet integrates the Gaussian curvature.
ADD	gaussian-and-mean-curvature	minimal-surfaces	soft	Minimal surfaces are defined by mean curvature H = 0.
ADD	gaussian-and-mean-curvature	sectional-curvature	soft	Sectional curvature generalizes the Gaussian curvature of a surface.
ADD	ca-hilbert-nullstellensatz	ca-spec-and-zariski-topology	soft	The Nullstellensatz motivates the ideal/variety correspondence behind Spec and the Zariski topology.
ADD	ca-hilbert-nullstellensatz	ca-krull-dimension	soft	It links Krull dimension of affine algebras to geometric dimension.
ADD	queueing-theory-mm1	reflected-brownian-motion	soft	Reflected Brownian motion arises as the heavy-traffic limit of queue lengths.

## 4. Gaps considered and rejected

Already covered by an existing topic:
- Rouché's theorem: covered by `argument-principle`, which states it as a corollary with its proof idea.
- Solvable groups and simplicity of Aₙ: covered by `insolvability-of-the-quintic` / `insolvability-quintic`.
- Field of fractions: covered by `ca-localization`.
- Quadratic forms (linear algebra): covered by `symmetric-matrices` and `positive-definite-matrices`.
- Logarithmic differentiation: covered by `derivatives-of-logarithmic-functions`.
- Derivatives of inverse functions: covered by `derivatives-of-logarithmic-functions` and `derivatives-of-inverse-trig-functions`.
- Rectilinear motion (position, velocity, acceleration): covered by `higher-order-derivatives`.
- Net change theorem: covered by `fundamental-theorem-of-calculus-part-2`.
- Newton's method: covered by `newton-method-convergence`.
- Trapezoidal and Simpson's rules: covered by `newton-cotes-formulas` and `composite-quadrature`.
- Logistic growth model: covered by `population-growth-models` (biology), `autonomous-equations` and `phase-line-analysis`.
- Euler's method and slope fields: covered by `eulers-method` and `direction-fields-and-solution-curves`.
- Taylor remainder / Lagrange error bound: covered by `taylors-theorem-remainder`.
- Compound and continuous interest: covered by `exponential-growth-and-decay` and `natural-logarithm-and-e`.
- De Moivre's theorem: covered by `polar-form-complex-numbers`.
- Rational expressions, radicals, variation, absolute-value inequalities: covered by existing algebra-1 topics of the same names.
- Compass-and-straightedge constructions: covered by `perpendicular-bisectors` and `angle-bisectors`.
- Cavalieri's principle: covered by `volume-of-prisms-and-cylinders`.
- Side-splitter theorem: covered by `proportions-in-similar-triangles`.
- Surface area of a sphere: covered by `volume-of-spheres`.
- Repeating decimals to fractions: covered by `converting-fractions-decimals-percents`.
- Cube roots: covered by `rational-exponents` and `radical-functions-and-graphs`.
- Experimental design: covered by `true-experimental-randomized-designs` (psychology) and `experimental-design-social` (social sciences).
- Conjugate gradient method: covered by `iterative-methods-linear-systems`.
- Lyapunov stability: covered by `nonlinear-control-lyapunov` (engineering).
- Optional stopping / gambler's ruin: covered by `martingales-introduction`.
- Markov chains (linear algebra application): covered by `markov-chains`.
- PCA: covered by `principal-component-analysis` (computer science).
- FFT: covered by `dft-and-fft-algorithms` (engineering) and `fft-polynomial-multiplication` (computer science).
- Stone-Weierstrass: covered within `weierstrass-approximation-theorem`.
- Elliptic curves: covered by `elliptic-curve-cryptography-basics` (computer science).
- Chinese remainder theorem, linear congruences, Euclidean algorithm: covered by discrete-math topics (`chinese-remainder-theorem`, `linear-congruences-discrete`, `euclidean-algorithm`).
- Kindergarten to grade 5 units (time, money, place value, graphs, shapes, fractions): covered, often by several near-duplicate topics.

Real gaps deferred to keep this set to the clearest cases (candidates for a later pass):
- Segment lengths in circles (power of a point; intersecting chords, secants, tangents). Larson ch. 10 / G-C.
- Theorema Egregium as a standalone topic. It is currently stated inside `gaussian-and-mean-curvature`.
- Delta method. It is mentioned only inside `asymptotic-normality-mle`.
- Finite difference methods for boundary value problems and PDEs (Burden and Faires ch. 11 to 12).
- Egorov's and Lusin's theorems (Royden 3.3).
- Hydrostatic force and centers of mass of plane regions (Stewart 8.3). Moments are partly covered by `applications-integrals-area-mass`.
- Perfect numbers and Mersenne primes (Burton ch. 11).
- Riemann-Stieltjes integral and functions of bounded variation (Rudin ch. 6).
- Geometry "reasoning and proof" unit (two-column proofs). It is partly covered by methods-of-proof topics and by proof practice in the congruence topics.

Observation outside scope: many lower-grade courses contain near-duplicate topics. For example, 1st grade has four files titled "Telling Time to the Hour" and duplicate pairs across several upper courses (e.g. `cosets-lagrange-theorem` / `cosets-and-lagrange-theorem`). These are a deduplication issue, not a gap issue.
