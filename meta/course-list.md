# Mathematics Course List

Courses are organizational groupings that correspond roughly to how mathematics is taught in the US K-12 and early university system. They define the subdirectory structure within `domains/mathematics/`.

A topic belongs to the course where it is **first formally introduced**. Topics may be reviewed or extended in later courses, but each topic has exactly one home course.

## Courses

| Course | Directory | Stage | Description |
|--------|-----------|-------|-------------|
| 4th Grade Math | `4th-grade/` | concrete-operations | Multi-digit arithmetic, fractions intro, basic geometry, measurement |
| 5th Grade Math | `5th-grade/` | concrete-operations | Fraction arithmetic, decimals, volume, coordinate plane intro |
| Prealgebra | `prealgebra/` | abstract-reasoning | Integers, ratios, proportions, percents, basic equations, data |
| Algebra 1 | `algebra-1/` | abstract-reasoning | Linear equations, inequalities, systems, exponents, polynomials intro |
| Geometry | `geometry/` | abstract-reasoning | Euclidean geometry, congruence, similarity, area, volume, basic proof |
| Algebra 2 | `algebra-2/` | abstract-reasoning | Quadratics, complex numbers, logarithms, sequences, rational expressions |
| Precalculus | `precalculus/` | formal-systems | Trigonometry, advanced functions, limits intuition, polar coordinates |
| Calculus 1 | `calculus-1/` | formal-systems | Limits, derivatives, applications of differentiation |
| Calculus 2 | `calculus-2/` | formal-systems | Integration techniques, series, parametric/polar calculus |
| Linear Algebra | `linear-algebra/` | formal-systems | Vectors, matrices, transformations, eigenvalues, vector spaces |
| Multivariable Calculus | `multivariable-calculus/` | formal-systems | Partial derivatives, multiple integrals, vector calculus |
| Methods of Proof | `methods-of-proof/` | formal-systems | Logic, direct proof, contradiction, induction, set theory |
| Probability & Statistics | `probability-and-statistics/` | formal-systems | Combinatorics, probability distributions, inference, regression |
| Discrete Math | `discrete-math/` | formal-systems | Graph theory, combinatorics, number theory, recursion, algorithms |

## Notes

- Courses earlier than 4th grade (K-3) are omitted for now. These can be added as `kindergarten/`, `1st-grade/`, `2nd-grade/`, `3rd-grade/` when contributors are ready.
- The traditional vs. integrated math track distinction (Algebra 1/Geometry/Algebra 2 vs. Integrated Math I/II/III) is handled by the prerequisite graph, not by course directories. Topics are filed under the traditional course names. An integrated pathway is a different *traversal* of the same graph.
- AP Calculus AB is a subset of `calculus-1/`. AP Calculus BC spans `calculus-1/` and `calculus-2/`.
