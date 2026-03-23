---
id: nc-class-parallel-circuits
title: NC Class and Parallel Circuit Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: circuit-complexity
  type: hard
- id: time-complexity-classes-formal
  type: soft
tags:
- parallel-computation
- circuits
- depth-bounds
stage: advanced
status: validated
---

# NC Class and Parallel Circuit Complexity

## Core Idea
NC (Nick's Class) contains languages computable by circuits of polynomial size and logarithmic depth. These circuits model highly parallel computation: depth corresponds to parallel time while size represents total operations. NC ⊆ P, and whether NC = P remains open. NC-hierarchy captures degrees of parallelizability, with NC^1 (linear size, log depth) being particularly fundamental for understanding parallelism.

## Questions

```yaml
- question: "An algorithm computes a result using O(n³) total operations (size), but is structured so that the computation can be completed in O(log² n) stages with unlimited processors. Which complexity class best describes this problem?"
  type: multiple-choice
  options:
    - "P but not NC, because O(n³) operations exceeds the NC size bound"
    - "NC^2, because the circuit has polylogarithmic depth (O(log² n)) and polynomial size (O(n³))"
    - "NC^1, because the depth is polylogarithmic and that is the only criterion for NC^1"
    - "Outside P, because having unlimited processors changes the model of computation entirely"
  answer: 1
  explanation: "NC^i consists of problems computable by polynomial-size, O(log^i n)-depth circuits. This algorithm uses O(n³) ≤ polynomial size and O(log² n) = O(log^2 n) depth — so it falls in NC^2 (the NC class indexed by log-squared depth). NC^1 requires O(log n) depth (not log² n), so option C is wrong. Option A incorrectly asserts O(n³) exceeds NC size bounds — NC requires polynomial size, and n³ is polynomial. Option D is wrong; the circuit model with unlimited parallelism is a standard computational model, and its relationship to P is the central question of the NC vs. P problem."

- question: "Why does NC ⊆ P follow directly from the definitions of NC and P, without requiring any sophisticated proof?"
  type: multiple-choice
  options:
    - "Because every NC algorithm can be converted to a polynomial-time Turing machine by evaluating the circuit gate by gate in topological order"
    - "Because NC = P is currently believed to be true, and NC ⊆ P follows from the equality"
    - "Because all polynomial-size circuits can be evaluated in logarithmic time on a sequential machine"
    - "Because NC problems have low depth, and low depth implies low sequential time on any machine"
  answer: 0
  explanation: "A circuit of polynomial size S has at most S gates. Evaluating gates in topological order (inputs first, then gates whose inputs are already computed) takes at most S steps sequentially — one step per gate. Since S is polynomial, this sequential evaluation is polynomial-time. Therefore any NC circuit can be evaluated in polynomial time by a Turing machine. NC ⊆ P. Option B incorrectly states NC = P is believed true — in fact NC = P is open and likely false. Option C reverses the relationship: low depth allows fast *parallel* evaluation, not fast sequential evaluation. Option D is imprecise; depth alone doesn't bound sequential time — it's the size that matters for sequential simulation."

- question: "In circuit complexity, a circuit's depth measures the total number of gates — the more gates, the deeper the circuit."
  type: true-false
  answer: false
  explanation: "Depth and size are distinct resources. *Size* is the total number of gates in the circuit. *Depth* is the length of the longest path from any input to the output — it measures how many sequential computation steps are needed if all gates on the same level can compute in parallel. A circuit can have enormous size (millions of gates) but shallow depth if those gates can all operate in parallel. Conversely, a small circuit can have large depth if computations are chained sequentially. NC exploits this distinction: it demands polylogarithmic depth (fast parallel time) but allows polynomial size (large total work)."

- question: "The circuit value problem (CVP) — evaluating a Boolean circuit on a given input — is in NC, making it a natural benchmark for efficient parallelism."
  type: true-false
  answer: false
  explanation: "CVP is P-complete, not in NC (under standard assumptions). This is the central irony noted in the topic: the very computational model used to define NC turns out to characterize what is believed to be outside NC. P-completeness means CVP is as hard as any problem in P under NC reductions — if CVP were in NC, then NC = P. CVP is P-complete because evaluating a circuit inherently requires following the computation gate by gate, and each gate's output may depend on the previous gate's output in ways that cannot be parallelized. This makes CVP the canonical example of a problem that appears inherently sequential."

- question: "Explain why NC ⊆ P but the question of whether P ⊆ NC (equivalently, NC = P) remains open, using the relationship between circuit depth and sequential computation."
  type: short-answer
  answer: "NC ⊆ P because any NC circuit (polynomial size, polylogarithmic depth) can be evaluated sequentially in polynomial time by processing gates in topological order — polynomial size bounds the number of steps. The reverse direction P ⊆ NC would require showing that every polynomial-time algorithm can be restructured to use only polylogarithmic depth. The obstacle is that some P algorithms appear to be inherently sequential: each step depends on the result of the previous step in a chain that cannot be parallelized. P-complete problems like circuit value problem are believed to capture this sequential dependency — if any P-complete problem were in NC, all of P would be. The question remains open because we lack the tools to prove circuit lower bounds that would separate NC from P."
  explanation: "The NC = P question is the parallel analog of P vs. NP: it asks whether efficient sequential computation can always be efficiently parallelized. The intuition that the answer is 'no' (NC ≠ P) is strong — sequential algorithms with step-by-step dependency seem genuinely not parallelizable — but proving lower bounds on circuit depth remains technically elusive, just as proving P ≠ NP remains beyond current mathematics."
```

## Explainer

From your study of circuit complexity, you know that Boolean circuits measure two distinct resources: **size** (total gates, corresponding to work) and **depth** (longest path from input to output, corresponding to time if gates can compute in parallel). NC exploits this separation: it defines the class of problems solvable with polynomial total work but only logarithmic parallel time.

The key intuition is that depth measures how many sequential steps you need if you have unlimited processors. Consider adding two n-bit numbers: naively done left to right, you have n sequential carries — depth Θ(n). But with a carry-lookahead tree, you can compute carries in O(log n) depth using O(n) gates. This is why integer addition is in NC^1 (circuits of O(n) size and O(log n) depth). More generally, NC^i consists of problems solvable by polynomial-size circuits of depth O(log^i n). The full class NC = ∪_i NC^i is what you can solve in polylogarithmic parallel time.

NC ⊆ P follows directly: a polynomial-size, polylogarithmic-depth circuit can be evaluated in polynomial time sequentially (just evaluate gate by gate in topological order). The reverse containment NC = P is open — it asks whether every polynomial-time algorithm can be efficiently parallelized down to polylogarithmic depth. The intuition for why P ≠ NC is plausible: some problems seem inherently sequential, where each step depends critically on the previous result.

The NC hierarchy refines parallelizability: NC^1 captures the most aggressively parallelizable problems (formula evaluation, regular languages), while NC^2 captures linear algebra over finite fields (matrix multiplication). Between NC and P lies an important class called **P-complete**: problems that are in P but believed not to be in NC because they capture sequential computation. The canonical P-complete problem is circuit value problem (CVP) — evaluating a given circuit on a given input — with all the irony that the very model used to define NC turns out to characterize its complement.
