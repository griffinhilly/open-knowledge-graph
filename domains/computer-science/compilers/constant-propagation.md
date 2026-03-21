---
id: constant-propagation
title: Constant Propagation and Folding
domain: computer-science
course: compilers
prerequisites:
- id: reaching-definitions-analysis
  type: hard
tags:
- optimization
- constant-propagation
- algebraic-simplification
stage: advanced
status: draft
---

# Constant Propagation and Folding

## Core Idea
Constant propagation identifies variables assigned constant values and replaces their uses with the constant. Constant folding evaluates constant expressions at compile-time. For example, `x = 5; y = x + 3` becomes `y = 8`. This simple optimization enables further simplifications and can expose dead code.

## Questions

```yaml
- question: "In a control flow graph, one branch of an if-statement assigns x = 5 and the other assigns x = 7. At the merge point after both branches, what does constant propagation's lattice assign to x?"
  type: multiple-choice
  options:
    - "x = 5 (the first assignment wins)"
    - "x = 6 (the average of the two values)"
    - "x = 'not a constant' (multiple different values may reach this point)"
    - "x = 'undefined' (the assignment is considered ambiguous)"
  answer: 2
  explanation: "At a merge point, constant propagation must account for all paths that could have been taken. If one path sets x = 5 and another sets x = 7, the value at runtime depends on which branch executed — information unavailable at compile time. The lattice rule is: if both paths agree on the same constant, x stays that constant; if they disagree, x becomes 'not a constant.' This is the correct conservative choice — propagating a value the compiler isn't certain about risks generating incorrect code."

- question: "After constant propagation and folding replace a variable with a known constant in a branch condition, what further optimization typically becomes possible?"
  type: multiple-choice
  options:
    - "Loop unrolling, because the loop bound is now statically known"
    - "Dead code elimination, because the branch condition is now statically true or false"
    - "Register allocation, because constants do not need to occupy registers"
    - "Function inlining, because constant arguments can be substituted at call sites"
  answer: 1
  explanation: "If constant propagation determines that x = 7, the condition `if (x > 5)` becomes statically true. The else-branch can never execute — it is dead code. Dead code elimination then removes it entirely, shrinking the program and potentially exposing more constants by removing conflicting assignments. This chain — propagation enables folding, folding enables dead code elimination — is why constant propagation is often run early in the optimization pipeline."

- question: "Constant folding and constant propagation are the same operation: both replace program values with known constants."
  type: true-false
  answer: false
  explanation: "They are complementary but distinct. Constant propagation replaces variable *uses* with known constant values: if x is known to be 5, every use of x is replaced with the literal 5. Constant folding evaluates constant *expressions* at compile time: if the code contains `5 + 3`, folding replaces it with `8`. They work together — propagation creates constant-only expressions that folding can then evaluate — and the result of folding may itself be propagated further."

- question: "If every reaching definition of a variable assigns the same constant value, the compiler can safely replace all uses of that variable with that constant."
  type: true-false
  answer: true
  explanation: "This is exactly what constant propagation does: it uses reaching definitions analysis to determine, for each variable at each program point, whether all possible prior assignments agree on one constant value. If they do, the variable's value is known at compile time and every use can be replaced with the literal constant. The runtime load instruction becomes unnecessary, and the compiler may eliminate storage for that variable entirely."

- question: "Why do constant propagation and constant folding typically create cascading opportunities for further compiler optimizations, rather than being a self-contained pass with limited effect?"
  type: short-answer
  answer: "When propagation replaces variables with literals, and folding evaluates the resulting constant expressions, the simplified code often reveals conditions or values that other optimizations can act on. A constant in a branch condition makes the condition statically evaluable, enabling dead code elimination of the unreachable branch. Removing dead code may expose more reaching definitions with constant values, enabling another round of propagation and folding. Each pass creates the conditions that the next pass needs."
  explanation: "This chaining behavior is why compilers often run optimization passes in multiple rounds. Constant propagation and folding are usually applied early because their simplifications are foundational — they reduce the program to a simpler form that reveals more opportunities for subsequent passes like dead code elimination, strength reduction, and loop optimization."
```

## Explainer

From reaching definitions analysis, you know how to determine, for each point in a program, which assignments could have produced the current value of a variable. Constant propagation builds directly on this: if every reaching definition of a variable assigns it the same constant value, then every use of that variable can be replaced with that constant. The compiler does not need to wait until runtime to look up the variable — it already knows the answer.

Consider a straightforward example. If the program says `x = 7` on line 3 and no other assignment to x reaches line 10, then at line 10 the compiler knows x is 7 and can substitute the literal value directly. **Constant propagation** performs this substitution throughout the program. **Constant folding** is the companion step: once propagation has replaced variables with constants, expressions like `7 + 3` can be evaluated at compile time to produce `10`. Together, these two transformations often chain — propagating a constant enables folding an expression, which produces a new constant that can be propagated further.

The analysis works on the control flow graph using a **lattice** of values for each variable. Each variable starts as "undefined" (no assignment has been seen), can become a specific constant (exactly one constant value reaches this point), or can become "not a constant" (multiple different values reach this point, or the value depends on runtime input). At merge points in the control flow — where two branches of an if-statement rejoin — the values from both paths are combined: if both paths agree on the same constant, the variable remains that constant; if they disagree, the variable becomes "not a constant." This is a forward dataflow analysis that iterates until the lattice values stabilize at a fixed point.

The power of constant propagation lies in what it enables downstream. Replacing a variable with a constant can make a branch condition statically evaluable — if `x` is known to be 7, then `if (x > 5)` is always true, and the compiler can eliminate the branch and its dead else-block entirely. This **dead code elimination** shrinks the program, which in turn may expose more constants by removing conflicting assignments. Many compiler optimizations work this way: each pass creates opportunities for the next, and constant propagation is often one of the first and most impactful passes in the sequence because its simplifications cascade broadly.
