---
id: ackermann-function
title: Ackermann Function
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: primitive-recursive-functions
  type: hard
builds-toward:
- mu-recursive-functions
tags:
- computability
- recursive-functions
- fast-growing-hierarchy
stage: advanced
status: validated
---

# Ackermann Function

## Core Idea
The Ackermann function is a total computable function that grows faster than any primitive recursive function, proving that the primitive recursive functions do not exhaust all total computable functions. It is defined by double recursion: A(0, n) = n+1, A(m+1, 0) = A(m, 1), and A(m+1, n+1) = A(m, A(m+1, n)). Even small inputs produce astronomically large outputs — A(4, 2) exceeds 10^19,000. The function demonstrates that the primitive recursive hierarchy, despite containing all common arithmetic operations and bounded loops, is strictly contained within the total computable functions.

## How It's Best Learned
Compute A(m, n) by hand for small values (m = 0, 1, 2, 3 and small n) and recognize the pattern: A(1, n) = n+2, A(2, n) = 2n+3, A(3, n) = 2^(n+3) - 3. Then understand why A(4, n) involves towers of exponents. This concretely demonstrates growth beyond any fixed level of the primitive recursive hierarchy.

## Common Misconceptions
- The Ackermann function IS computable (a Turing machine can compute it) — it is just not primitive recursive. Being non-primitive-recursive does not mean uncomputable.
- There are multiple variants of the Ackermann function in the literature (Ackermann's original three-argument version, the two-argument Robinson/Peter version); the two-argument version is standard in computability courses.

## Questions

```yaml
- question: "A(4, 2) — the Ackermann function evaluated at (4, 2) — produces an output larger than 10^19,000. Which of the following best characterizes this function?"
  type: multiple-choice
  options:
    - "A(4, 2) is not computable because no physical device could store or process a number that large"
    - "A(4, 2) is computable by a Turing machine, but the function A is not primitive recursive"
    - "A(4, 2) is computable and the Ackermann function is primitive recursive — it just requires many nested recursions"
    - "A(4, 2) is undecidable in the same sense that the halting problem is undecidable"
  answer: 1
  explanation: "The Ackermann function is total and computable — a Turing machine can evaluate A(m, n) for any inputs using a stack to manage recursive calls. Astronomically large outputs do not make a function uncomputable; computability is about the existence of a terminating procedure, not whether the output fits in physical memory. What Ackermann IS NOT is primitive recursive. Primitive recursive functions are defined by recursion schemes that bound the recursion depth in advance; the Ackermann function's double recursion escapes this, growing faster than any primitive recursive function. The distinction is between 'can be computed' and 'can be computed using only bounded-loop recursion.'"

- question: "The Ackermann function A(m, n) can be informally understood as selecting the m-th level of an arithmetic hierarchy. What is A(3, n) equivalent to, and what does this reveal about the growth rate of A(4, n)?"
  type: multiple-choice
  options:
    - "A(3, n) = 3n, a linear function; A(4, n) is therefore polynomial"
    - "A(3, n) = n^3, a cubic function; A(4, n) involves iterated cubing"
    - "A(3, n) = 2^(n+3) − 3, an exponential function; A(4, n) involves iterated exponentiation (tetration), growing as towers of 2s"
    - "A(3, n) = n! (factorial); A(4, n) involves iterated factorial composition"
  answer: 2
  explanation: "A(0,n)=n+1 (successor), A(1,n)=n+2 (addition), A(2,n)=2n+3 (multiplication-like), A(3,n)=2^(n+3)−3 (exponentiation-like). Each level is not just faster than the previous — it is a categorically new kind of growth. A(4, n) corresponds to tetration: 2^(2^(2^...)) — towers of 2s of height proportional to n. A(4,2) requires evaluating A(3, A(4,1)) = A(3, A(3, A(4,0))) = A(3, A(3, A(3,1))). Each A(3,k) is exponential in k, so this cascades to a tower of 65,536 twos in the exponent — far beyond any fixed level of the primitive recursive hierarchy."

- question: "The Ackermann function is not computable by a Turing machine because its outputs grow too fast for any finite computation to terminate."
  type: true-false
  answer: false
  explanation: "False — this is the most important misconception about the Ackermann function. It IS computable by a Turing machine. The machine evaluates A(m, n) by simulating the recursion using an explicit stack: at each step, it records the current (m, n) pair, applies the recursive definition, and works through the stack until reaching a base case. The computation terminates for all finite inputs because A is a total function — every input has a defined output. The computation may require astronomical time and space for large inputs, but that is a complexity question, not a computability one. 'Too large to compute in practice' is not the same as 'uncomputable in principle.'"

- question: "For every primitive recursive function f, there exists an N such that A(n, n) > f(n) for all n > N."
  type: true-false
  answer: true
  explanation: "True, and this is the precise theorem that proves A is not primitive recursive. A(n,n) eventually dominates every primitive recursive function f. Since every primitive recursive function is bounded by some level of the Ackermann hierarchy (there exists a k such that f(n) < A(k, n) for all large n), and A(n,n) grows faster than any fixed A(k, n) as n increases, no primitive recursive function can keep pace with A(n,n). This makes A a 'proof' that the primitive recursive class is strictly smaller than the total computable functions — the gap between them is nonempty and contains Ackermann."

- question: "What property of the Ackermann function's definition allows it to escape the primitive recursive hierarchy, and why does this matter for computability theory?"
  type: short-answer
  answer: "The Ackermann function uses *double recursion*: both arguments m and n decrease toward base cases simultaneously, with recursive calls to A(m, A(m+1, n)) — an inner call whose argument is itself the result of another call to A at a higher m. Primitive recursive functions may only recurse on a single argument (n), with the depth of recursion bounded by the initial value of n. This is the 'bounded loop' property: at most n iterations. Double recursion allows A to recurse on m a number of times determined by the output of A itself, which is unbounded by any fixed function of the inputs. This matters for computability theory because it proves the primitive recursive functions do not exhaust all total computable functions — the class of 'nicely structured' computations is strictly narrower than full Turing computability."
  explanation: "The Ackermann function lives in the gap between two important classes: primitive recursive functions (which have bounded recursion depth and capture all 'obviously terminating' procedures) and total computable functions (which terminate for all inputs but may require reasoning about termination that cannot be bounded in advance). Ackermann showed this gap is nonempty in 1928, predating Turing's formalization of computability. The double recursion scheme is the mechanism — it requires the computer to track an unbounded stack of recursive calls rather than a fixed number."
```

## Explainer

From your study of primitive recursive functions, you know that every primitive recursive function is built up from zero, successor, and projection using composition and primitive recursion — a scheme where the recursion on n is bounded in advance by a fixed number of steps. Addition is defined by recursing on the second argument for n steps; multiplication by recursing on addition n times; exponentiation by recursing on multiplication n times. Each new operation uses the previous one as a primitive, forming a layered hierarchy. The key limitation: each primitive recursive definition only reaches one level higher than what it builds on.

The **Ackermann function** A(m, n) escapes this hierarchy by using *double recursion* — recursing simultaneously on both m and n. The base cases are simple: A(0, n) = n+1 is just the successor function. A(1, n) = n+2 is essentially repeated successor (addition). A(2, n) = 2n+3 corresponds to multiplication. A(3, n) = 2^(n+3) − 3 corresponds to exponentiation. So the first argument m selects a "level" of the arithmetic hierarchy: successor, addition, multiplication, exponentiation, tetration (tower of exponents), and beyond. Each new level is not just faster than the previous — it is a qualitatively new kind of growth.

Here is why A(4, 2) becomes incomprehensibly large: A(4, 2) = A(3, A(4, 1)) = A(3, A(3, A(4, 0))) = A(3, A(3, A(3, 1))). Each A(3, k) produces a tower of 2s of height k+3. So A(3, 1) = 2^4 − 3 = 13, A(3, 13) = 2^16 − 3 = 65533, A(3, 65533) is a tower of 65536 twos — and we are not done yet. The final result exceeds 10^19,000. The double recursion means that even computing A(m, 0) for large m requires unwinding a cascade of recursive calls that span all previous levels.

The significance for computability theory is precise: for every primitive recursive function f, there exists an N such that A(n, n) > f(n) for all n > N. This means A is not bounded by any fixed level of the primitive recursive hierarchy. No matter how many times you nest the primitive recursion scheme, Ackermann's growth escapes it. Yet A is still computable — a Turing machine can evaluate it using a stack to track the recursive calls. This separates two concepts you might have conflated: "having a nice closed-form recursion scheme" and "being computable at all." The Ackermann function lives in the gap between primitive recursive and the full class of total computable functions, proving that gap is nonempty.
