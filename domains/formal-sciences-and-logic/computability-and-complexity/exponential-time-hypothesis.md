---
id: exponential-time-hypothesis
title: Exponential Time Hypothesis (ETH)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: time-complexity-classes-formal
  type: soft
tags:
- conjecture
- lower-bounds
- hardness
stage: advanced
status: validated
---

# Exponential Time Hypothesis (ETH)

## Core Idea
The Exponential Time Hypothesis (ETH) conjectures that 3-SAT requires time 2^(c·n) for some constant c > 0, implying SAT cannot be solved in 2^(o(n)) time. ETH is a refined hardness assumption stronger than P ≠ NP but potentially weaker than assuming exponential lower bounds hold universally. It has become influential for proving conditional lower bounds: many problems' hardness is established assuming ETH holds.

## Questions

```yaml
- question: "ETH conjectures that 3-SAT requires time 2^(cn) for some constant c > 0. This is a strictly stronger claim than P ≠ NP because:"
  type: multiple-choice
  options:
    - "ETH applies to all NP-complete problems, while P ≠ NP only establishes hardness for 3-SAT specifically"
    - "ETH rules out subexponential algorithms like 2^(√n) or n^(log n), which P ≠ NP says nothing about"
    - "ETH implies that no approximation algorithm can efficiently solve 3-SAT, extending beyond exact solving"
    - "ETH establishes that all NP-hard problems require exponential time, closing the gap between NP and EXP"
  answer: 1
  explanation: "P ≠ NP only draws a line between polynomial and superpolynomial time — it says NP-hard problems cannot be solved in n^k time for any fixed k, but says nothing about the specific exponent within superpolynomial time. An algorithm running in 2^(√n) or 2^(n/log n) would be superpolynomial (satisfying P ≠ NP) but vastly faster than 2^n. ETH forbids exactly these 'subexponential' algorithms, making it a much stronger hardness assumption that enables precise algorithmic lower bounds. ETH concerns the exponent; P ≠ NP concerns only the dividing line between polynomial and beyond."

- question: "A researcher proves that, assuming ETH holds, k-Clique cannot be solved in time f(k)·n^(o(k)) for any computable function f. This result is best described as:"
  type: multiple-choice
  options:
    - "A polynomial-time reduction showing k-Clique is NP-complete under standard assumptions"
    - "A fine-grained conditional lower bound establishing the asymptotic optimality of existing algorithms under ETH"
    - "A derandomization showing k-Clique is in P when k is fixed as a constant"
    - "An upper bound showing k-Clique is fixed-parameter tractable with running time f(k)·n^(O(k))"
  answer: 1
  explanation: "Fine-grained complexity uses ETH (or related hypotheses like SETH) to prove that known algorithms are not just 'good' but *optimal up to lower-order terms*. This result says: if ETH holds, no algorithm can solve k-Clique faster than the n^(Θ(k)) algorithms we already have — the exponent in n cannot be o(k). This is not an upper bound or an NP-completeness proof; it is a conditional lower bound that proves algorithmic optimality, which classical complexity theory (even assuming P ≠ NP) cannot achieve."

- question: "ETH implies that no algorithm can solve 3-SAT in subexponential time — ruling out running times like 2^(√n) and n^(log n) — even though P ≠ NP alone does not rule out such algorithms."
  type: true-false
  answer: true
  explanation: "P ≠ NP says 3-SAT cannot be solved in polynomial time (n^k for any fixed k), but permits algorithms like 2^(√n) which grow faster than any polynomial yet slower than any 2^(cn). ETH's claim that 3-SAT requires 2^(cn) for some constant c > 0 specifically forbids these subexponential algorithms. An algorithm in 2^(o(n)) time (subexponential) would refute ETH. This is why ETH is the foundation for fine-grained complexity: it provides a benchmark that P ≠ NP cannot."

- question: "An algorithm that solves 3-SAT in time 2^(0.001n) would refute the Exponential Time Hypothesis, because it is asymptotically faster than 2^n."
  type: true-false
  answer: false
  explanation: "ETH asserts that 3-SAT requires time 2^(cn) for *some* constant c > 0. An algorithm running in 2^(0.001n) has c = 0.001 > 0 — it is still exponential, just with a small constant. ETH is not refuted by having a small constant in the exponent; it is only refuted by a *subexponential* algorithm, one running in 2^(o(n)) time (e.g., 2^(√n) or 2^(n/log n)). Being 'asymptotically faster than 2^n' in the sense of having a smaller constant does not violate ETH — the hypothesis only specifies that *some* positive constant must exist in the exponent."

- question: "Why does ETH enable 'fine-grained' complexity results — pinning down exact running-time exponents — that P ≠ NP alone cannot provide?"
  type: short-answer
  answer: "P ≠ NP only establishes a polynomial-vs-superpolynomial dividing line: NP-hard problems are not in P, but this says nothing about whether the best algorithm runs in 2^n, 2^(n/2), or n^100. ETH makes a specific quantitative claim about the *exponent* of the best algorithm for 3-SAT. Through reductions that preserve instance sizes tightly (unlike classical polynomial reductions that may expand inputs), ETH lower bounds propagate to show that specific known algorithms are optimal — not just that no polynomial algorithm exists, but that no algorithm with a better exponent can exist."
  explanation: "The technical key is the Sparsification Lemma plus tight reductions. Classical NP-completeness reductions are size-blowing: reducing problem A to SAT might turn an n-variable instance into an n^3-clause formula. Fine-grained reductions preserve linear instance size, so an ETH lower bound on 3-SAT (size n) propagates to a lower bound on the other problem in the same quantitative form. This is the machinery that transforms 'hard in some superpolynomial sense' into 'requires at least 2^(cn) for this specific c.'"
```

## Explainer

The Exponential Time Hypothesis sits at the boundary between what we believe and what we can prove about computational hardness. You already know from NP-completeness that 3-SAT is among the hardest problems in NP — but knowing a problem is NP-complete only tells you no polynomial-time algorithm exists (assuming P ≠ NP). ETH makes a sharper claim: 3-SAT doesn't just require superpolynomial time, it requires genuinely exponential time, at minimum 2^(cn) for some constant c > 0, where n is the number of variables.

To appreciate why this matters, consider what "no 2^(o(n)) algorithm" rules out concretely. It says no algorithm can solve 3-SAT in, say, 2^(√n) time or 2^(n/log n) time — both of which are vastly faster than 2^n but still not polynomial. Such **subexponential** algorithms, while impractical for large n, would represent genuine structural breakthroughs. ETH says they don't exist. This is why ETH is called a "refined" hardness assumption: it is strictly stronger than P ≠ NP (which says nothing about the exponent) but potentially weaker than claiming all exponential hardness results we care about hold simultaneously.

The real power of ETH emerges in **conditional lower bounds** — proofs of the form "if ETH holds, then problem X cannot be solved faster than T(n)." For example, under ETH, k-Clique cannot be solved in time f(k) · n^(o(k)), and many parameterized problems have tight running-time bounds. This lets researchers prove *optimality*: not just "we don't know a faster algorithm" but "no faster algorithm exists unless ETH fails." This transforms complexity theory from a study of hardness classes into a study of precise running times, and makes ETH central to the field of **fine-grained complexity**.

The **Sparsification Lemma** is the key technical tool for applying ETH: it shows that, without loss of generality when analyzing ETH lower bounds, 3-SAT instances can be assumed to have O(n) clauses rather than O(n^3). This means the hardest 3-SAT instances are *sparse* — a counterintuitive but important fact. Together with reductions that preserve instance size tightly (unlike classical polynomial reductions, which may blow up sizes), ETH lets researchers pin down the exact exponent of the best algorithm for each problem. The goal is no longer merely "polynomial or exponential?" but "2^n or 2^(n/2) or n^k for which k?" — a far more precise account of algorithmic difficulty.
