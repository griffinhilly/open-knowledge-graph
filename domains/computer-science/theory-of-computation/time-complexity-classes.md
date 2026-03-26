---
id: time-complexity-classes
title: 'Time Complexity Classes: P and EXPTIME'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: time-space-complexity
  type: soft
- id: big-o-complexity-analysis
  type: soft
- id: asymptotic-notation-big-o-omega-theta
  type: soft
builds-toward:
- nondeterministic-complexity
- space-complexity-classes
tags:
- P
- EXPTIME
- complexity
- polynomial-time
- time-complexity
stage: advanced
status: validated
---

# Time Complexity Classes: P and EXPTIME

## Core Idea
The class P consists of all decision problems solvable by a deterministic TM in polynomial time O(nᵏ) for some constant k. P captures problems that are 'efficiently solvable' and includes sorting, shortest paths, primality testing, and linear programming. EXPTIME contains problems solvable in exponential time 2^poly(n); it strictly contains P. Basing complexity on TM running time formalizes the intuitive notion of tractability. The polynomial-time model is robust across reasonable machine models — polynomial in one is polynomial in another.

## How It's Best Learned
Classify known algorithms into P: sorting is O(n log n) ⊆ P, BFS/DFS is O(V+E) ⊆ P. Then encounter problems (chess, exponential-search problems) known to require exponential time. This calibrates the P boundary.

## Common Misconceptions
- Thinking P means 'fast' in practice — O(n¹⁰⁰) is in P but completely impractical.
- Confusing EXPTIME with 'undecidable' — EXPTIME problems are decidable, just slow.

## Questions

```yaml
- question: "An engineer proposes an algorithm that solves a scheduling problem in O(n^50) time and argues it is efficient because it is in P. What is the most precise criticism of this reasoning?"
  type: multiple-choice
  options:
    - "O(n^50) is not in P — P only contains algorithms with exponents up to around O(n^3)"
    - "P captures theoretical tractability and robustness across machine models, not practical efficiency — O(n^50) is in P but completely impractical for any realistic input"
    - "O(n^50) is actually in EXPTIME, since 50 is too large to be called a polynomial exponent"
    - "The criticism is invalid — P algorithms are by definition efficient and this one must be practical"
  answer: 1
  explanation: "P is defined as solvable in O(nᵏ) for some fixed constant k, with no upper bound on k. O(n^50) is legitimately in P. But P's significance is not practical speed — it is the robustness of the polynomial-time boundary across different reasonable computational models. An algorithm in P on a Turing machine is also polynomial on a RAM machine or multi-tape machine. O(n^50) is theoretically tractable but completely useless in practice. The engineer is correct about membership in P but wrong about what that implies for efficiency."

- question: "What does the time hierarchy theorem establish about the relationship between P and EXPTIME?"
  type: multiple-choice
  options:
    - "P = EXPTIME — both classes solve the same problems, just with different machine models"
    - "P ⊊ EXPTIME — P is strictly contained in EXPTIME, and there exist problems that are decidable but provably require exponential time"
    - "EXPTIME contains all decidable problems, so P ⊊ EXPTIME follows trivially from the definition"
    - "P and EXPTIME are incomparable — some P problems are outside EXPTIME and vice versa"
  answer: 1
  explanation: "The time hierarchy theorem proves that giving a Turing machine substantially more time allows it to solve strictly more problems. Applied to the gap between polynomial and exponential time, it establishes that P ⊊ EXPTIME — the containment is strict, not equality. This is one of the few known strict separations in complexity theory and is established rigorously by diagonalization, unlike the P vs. NP question which remains open."

- question: "EXPTIME-complete problems such as determining the winner of generalized chess on an n×n board are decidable — they have correct yes/no answers that can in principle be computed."
  type: true-false
  answer: true
  explanation: "Correct. EXPTIME problems require exponential time but are decidable: there exists an algorithm that terminates and gives the correct answer for every input. Generalized chess (on an n×n board) is EXPTIME-complete — a Turing machine can solve it given exponential time, even if no polynomial-time algorithm exists. This distinguishes EXPTIME from undecidable problems like the halting problem, for which no algorithm exists at all regardless of time allowed."

- question: "Any problem outside P is unsolvable in practice, because computers can seldom realistically run algorithms that are not polynomial-time."
  type: true-false
  answer: false
  explanation: "Problems outside P range widely in difficulty: NP problems (efficiently verifiable, unknown if efficiently solvable), PSPACE problems, EXPTIME problems (exponential but decidable), and finally undecidable problems (no algorithm exists). Many practically important problems — cryptographic attacks, game-tree search, constraint satisfaction — sit outside P but are solved in practice using heuristics, approximations, or for small instances. 'Outside P' means no polynomial-time general algorithm is known (or provably exists), not that the problem is impossible to approach."

- question: "What makes P a theoretically meaningful complexity class, and why is the polynomial-time boundary considered robust across different machine models?"
  type: short-answer
  answer: "P is meaningful not because polynomial algorithms are always fast, but because the polynomial-time boundary is preserved across all reasonable deterministic computational models. A problem solvable in polynomial time on a single-tape Turing machine is also polynomial on a multi-tape machine, a RAM machine, or any standard deterministic model — the exponent and constant may change, but polynomial remains polynomial. This robustness means P is a property of the problem itself, not an artifact of a particular machine definition. It gives complexity theory a stable foundation: membership in P is a machine-independent characterization of tractability."
  explanation: "The robustness property is what allows computer scientists to reason about problem difficulty abstractly, without worrying about implementation details. Without it, 'efficient' would be a hardware-specific concept rather than a mathematical one."
```

## Explainer

From your study of Turing machines and algorithm analysis, you know that some problems are computable and some are not. **Time complexity classes** refine the computable problems by asking: how much time does the fastest algorithm need? The class **P** (polynomial time) contains every decision problem — every yes-or-no question — that a deterministic Turing machine can solve in time O(nᵏ) for some fixed constant k, where n is the input size. Sorting an array, finding shortest paths in a graph, testing whether a number is prime, and solving linear programs are all in P.

The significance of P is not that polynomial algorithms are always fast in practice — O(n¹⁰⁰) is technically polynomial but useless. Rather, P captures a robust notion of **tractability** that is independent of the specific computational model. A problem solvable in polynomial time on a single-tape Turing machine is also polynomial on a multi-tape machine, a RAM machine, or any other reasonable deterministic model. The exponent and constants may change, but the polynomial boundary holds. This **robustness** is what makes P a meaningful theoretical class rather than an artifact of one particular machine definition.

**EXPTIME** contains problems solvable in time 2^p(n) for some polynomial p(n). Unlike the relationship between many complexity classes, we can prove that P ⊊ EXPTIME — P is strictly contained in EXPTIME. This is established by diagonalization and the time hierarchy theorem, which shows that giving a Turing machine substantially more time allows it to solve strictly more problems. Concrete EXPTIME-complete problems include determining the winner of generalized chess, checkers, or Go on an n×n board — games where the enormous branching factor and game length provably require exponential exploration.

Between P and EXPTIME lies the landscape where the most famous open questions in computer science reside. The class NP (which you will study next as nondeterministic polynomial time) sits between P and EXPTIME, and the P vs. NP question asks whether efficient verification of solutions implies efficient discovery of solutions. For now, the key conceptual takeaway is the hierarchy: some decidable problems are efficiently solvable (P), some require exponential time (EXPTIME-complete), and the time hierarchy theorem guarantees that more time genuinely means more computational power. Undecidable problems like the halting problem sit entirely outside this framework — they cannot be solved in any amount of time, no matter how generous.
