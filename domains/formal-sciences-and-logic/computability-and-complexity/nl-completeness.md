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
tags:
- space-complexity
- completeness
- reductions
stage: advanced
status: draft
---

# NL-Completeness and Space-Bounded Reductions

## Core Idea
A problem is NL-complete if it lies in NL and every language in NL reduces to it via a log-space reduction. The most canonical NL-complete problem is REACHABILITY: given a directed graph and two vertices, does a path exist between them? NL-completeness demonstrates that even space-constrained computation has meaningful completeness notions and hardness hierarchy.

## Explainer

From your study of logarithmic-space classes, you know that NL (nondeterministic logarithmic space) captures computation that uses only O(log n) workspace but can branch nondeterministically — accepting if any branch accepts. The space bound is severe: you cannot even write down a full path through a graph in log space. What you *can* do is maintain a current vertex pointer and a step counter, then nondeterministically guess the next step. This is precisely why graph reachability — "is there a path from s to t?" — sits at the heart of NL.

**NL-completeness** follows the same template as NP-completeness: a problem is NL-complete if (1) it is in NL, and (2) every language in NL **log-space reduces** to it. Log-space reductions are the right notion here because we are studying log-space computation — using polynomial-time reductions would trivially allow solving the problem yourself. A log-space reduction from L to REACHABILITY maps instances of L to directed graphs such that x ∈ L iff a designated target vertex is reachable from a source. REACHABILITY is NL-complete because any NL computation can be viewed as a graph of configurations, with edges between configurations reachable in one step, and the question "does the machine accept?" becomes "is the accept configuration reachable from the start configuration?"

The striking result in this area is the **Immerman-Szelepcsényi theorem**: NL = co-NL. Unlike the NP vs. co-NP question (which remains open), the space-bounded analogue was resolved in 1988. The proof uses **inductive counting**: to certify that no path exists from s to t, you can count the number of vertices reachable from s using only log space, then certify that t is not among them. This certificate-counting technique works in log space, showing that non-reachability is itself in NL. The theorem implies that NL is closed under complement, a nontrivial structural property that time-bounded classes like NP are not known to share.

NL-completeness illustrates a broader principle in complexity theory: each resource-bounded class has its own completeness notion under appropriately weak reductions. The reductions must be strictly weaker than the class itself, or the notion collapses. For NL, log-space reductions are the natural choice. For P, log-space reductions are again used (since AC¹ reductions would let you solve P problems directly). Understanding NL-completeness prepares you for the general pattern: pick a class, pick reductions weaker than the class, identify a natural combinatorial problem that is complete, and use it as the canonical hard instance for the class.
