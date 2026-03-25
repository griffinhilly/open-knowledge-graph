---
id: nl-completeness
title: NL-Completeness and Space-Bounded Reductions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: logarithmic-space-classes
  type: hard
- id: computability-reductions
  type: soft
- id: np-completeness-reduction-proof-techniques
  type: soft
tags:
- space-complexity
- completeness
- reductions
stage: advanced
status: validated
---
# NL-Completeness and Space-Bounded Reductions

## Core Idea
A problem is NL-complete if it lies in NL and every language in NL reduces to it via a log-space reduction. The most canonical NL-complete problem is REACHABILITY: given a directed graph and two vertices, does a path exist between them? NL-completeness demonstrates that even space-constrained computation has meaningful completeness notions and hardness hierarchy.

## Questions

```yaml
- question: "Why are NL-completeness reductions required to be computable in log space rather than polynomial time?"
  type: multiple-choice
  options:
    - "Because polynomial-time reductions are too powerful — they could solve NL problems directly, making every problem in NL trivially 'hard'"
    - "Because log-space reductions are faster to compute and NL problems require fast reductions for efficiency"
    - "Because polynomial-time reductions cannot be defined for graph problems, which is where NL-completeness arises"
    - "Because the Church-Turing thesis requires all reductions to match the space bound of the target class"
  answer: 0
  explanation: "The reductions used to define hardness must be strictly weaker than the class being studied; otherwise the reduction itself solves the problem. If we allowed polynomial-time reductions for NL-hardness, any NL-complete problem would be solvable in polynomial time using the reduction plus the NL algorithm, trivializing the notion. Log-space reductions are strictly weaker than NL (since L ⊆ NL and log-space machines are within L), making them the right tool."

- question: "Why is REACHABILITY (directed graph path problem: does a path exist from s to t?) a natural NL-complete problem?"
  type: multiple-choice
  options:
    - "Any NL computation can be encoded as a configuration graph where edges represent one-step transitions, so acceptance becomes reachability from start to accept configuration"
    - "REACHABILITY requires O(log n) space to solve, which exactly matches the NL space bound"
    - "Directed graphs are the only combinatorial structure expressible in log space, so all NL problems must reduce to graph problems"
    - "REACHABILITY is complete because it requires nondeterminism — no deterministic log-space algorithm can solve it"
  answer: 0
  explanation: "The configuration graph of an NL machine has vertices representing (state, work-tape content, head positions) — each configuration fits in log space. Edges connect configurations reachable in one step. The NL machine accepts iff the accept configuration is reachable from the start, which is exactly REACHABILITY on the configuration graph. Every NL language reduces to REACHABILITY via this encoding, establishing its NL-hardness."

- question: "NL = co-NL: nondeterministic log space is closed under complement, just as NP is known to be closed under complement."
  type: true-false
  answer: false
  explanation: "NL = co-NL is true (Immerman-Szelepcsényi theorem, 1988), but NP is NOT known to be closed under complement — NP = co-NP remains an open question. The space-bounded analogue was resolved, while the time-bounded analogue has not been. This asymmetry is a striking result: certificate-counting techniques that work in log space do not appear to transfer to polynomial time."

- question: "Using a polynomial-time reduction to show that a language L reduces to REACHABILITY would not be sufficient to prove L is NL-hard."
  type: true-false
  answer: true
  explanation: "NL-hardness requires a log-space reduction, not merely a polynomial-time reduction. If only a polynomial-time reduction exists, the reduction itself might be solving the hard part of the problem, and we learn nothing meaningful about L's membership in NL. Log-space reductions ensure the reduction uses resources strictly within the NL bound, so the hardness conclusion is meaningful."

- question: "The Immerman-Szelepcsényi theorem proves NL = co-NL using an inductive counting argument. Why can this counting be done in log space?"
  type: short-answer
  answer: "The key insight is that you do not need to store the full list of reachable vertices — only the count. At each inductive stage, you maintain a single counter (log space) tracking how many vertices are reachable from s in at most k steps, then verify whether each candidate vertex is reachable by simulating nondeterministic paths. The counter fits in O(log n) bits since there are at most n vertices, and the verification at each stage reuses the same workspace rather than accumulating a growing list."
  explanation: "The proof certifies non-reachability by counting: first compute the number of vertices reachable from s (call it c_k for k steps), then show t is not among them by iterating over all vertices, nondeterministically guessing a path to each, and verifying the count matches. Maintaining one counter of size O(log n) and reusing workspace keeps the entire computation in log space, showing that non-reachability is in NL — and therefore NL = co-NL."
```

## Explainer

From your study of logarithmic-space classes, you know that NL (nondeterministic logarithmic space) captures computation that uses only O(log n) workspace but can branch nondeterministically — accepting if any branch accepts. The space bound is severe: you cannot even write down a full path through a graph in log space. What you *can* do is maintain a current vertex pointer and a step counter, then nondeterministically guess the next step. This is precisely why graph reachability — "is there a path from s to t?" — sits at the heart of NL.

**NL-completeness** follows the same template as NP-completeness: a problem is NL-complete if (1) it is in NL, and (2) every language in NL **log-space reduces** to it. Log-space reductions are the right notion here because we are studying log-space computation — using polynomial-time reductions would trivially allow solving the problem yourself. A log-space reduction from L to REACHABILITY maps instances of L to directed graphs such that x ∈ L iff a designated target vertex is reachable from a source. REACHABILITY is NL-complete because any NL computation can be viewed as a graph of configurations, with edges between configurations reachable in one step, and the question "does the machine accept?" becomes "is the accept configuration reachable from the start configuration?"

The striking result in this area is the **Immerman-Szelepcsényi theorem**: NL = co-NL. Unlike the NP vs. co-NP question (which remains open), the space-bounded analogue was resolved in 1988. The proof uses **inductive counting**: to certify that no path exists from s to t, you can count the number of vertices reachable from s using only log space, then certify that t is not among them. This certificate-counting technique works in log space, showing that non-reachability is itself in NL. The theorem implies that NL is closed under complement, a nontrivial structural property that time-bounded classes like NP are not known to share.

NL-completeness illustrates a broader principle in complexity theory: each resource-bounded class has its own completeness notion under appropriately weak reductions. The reductions must be strictly weaker than the class itself, or the notion collapses. For NL, log-space reductions are the natural choice. For P, log-space reductions are again used (since AC¹ reductions would let you solve P problems directly). Understanding NL-completeness prepares you for the general pattern: pick a class, pick reductions weaker than the class, identify a natural combinatorial problem that is complete, and use it as the canonical hard instance for the class.
