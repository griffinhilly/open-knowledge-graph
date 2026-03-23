---
id: nondeterministic-polynomial-time
title: NP Class and Nondeterministic Polynomial Time
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-p-class
  type: hard
builds-toward:
- np-completeness
tags:
- np-class
- nondeterminism
- verification
stage: advanced
status: validated
---

# NP Class and Nondeterministic Polynomial Time

## Core Idea
The complexity class NP consists of languages decidable by a nondeterministic Turing machine in polynomial time. Equivalently, NP consists of languages where membership can be verified in polynomial time given a certificate. P ⊆ NP, and the question P = NP is the most important open problem in computer science.

## Questions

```yaml
- question: "A researcher discovers that given a proposed solution to a certain problem, she can verify its correctness in polynomial time. However, she has no algorithm that finds solutions in polynomial time. Which complexity class does this problem belong to?"
  type: multiple-choice
  options:
    - "P only, since the verification step is efficient"
    - "NP — problems with polynomial-time verifiers are in NP, regardless of how hard finding a solution appears to be"
    - "A class outside NP, since NP requires polynomial-time solving"
    - "EXPTIME, because exponential search time is what defines the class"
  answer: 1
  explanation: "NP is defined precisely by the existence of a polynomial-time verifier: a procedure that can confirm a 'yes' answer in polynomial time given a certificate (proposed solution). The question of how hard it is to *find* a solution is separate. This problem is in NP because checking is easy. Whether it is also in P — whether efficient solvers exist — is unknown and is exactly the P vs. NP question. Every problem in P is automatically in NP, but the converse is unproven."

- question: "The Boolean satisfiability problem (SAT) asks: does a variable assignment exist that makes a given Boolean formula true? Why is SAT in NP?"
  type: multiple-choice
  options:
    - "Because there is a known polynomial-time algorithm for finding satisfying assignments"
    - "Because given a specific variable assignment, you can verify in polynomial time whether it satisfies the formula"
    - "Because all Boolean formulas can be solved by exhaustive search in polynomial time"
    - "Because SAT can be reduced to a problem already known to be in P"
  answer: 1
  explanation: "SAT is in NP because of its polynomial-time verifier: given a proposed assignment of True/False to all variables, you evaluate the formula by substituting values and checking each clause. This takes time proportional to the formula size — polynomial. No one knows how to *find* a satisfying assignment efficiently; what places SAT in NP is that *checking* a candidate assignment is easy. SAT was the first problem proven to be NP-complete, establishing that it is at least as hard as any other problem in NP."

- question: "NP stands for 'Not Polynomial,' meaning that problems in NP cannot be solved in polynomial time."
  type: true-false
  answer: false
  explanation: "NP stands for 'Nondeterministic Polynomial time' — the class of problems solvable by a nondeterministic Turing machine in polynomial time, or equivalently, the class of problems with polynomial-time verifiers. Every problem in P (solvable deterministically in polynomial time) is automatically in NP as well, because if you can solve a problem efficiently, you can certainly verify a solution efficiently (just solve it yourself and compare). Whether NP contains problems that are strictly not in P is the unsolved P vs. NP question."

- question: "If someone found a polynomial-time algorithm for the Hamiltonian path problem (does a graph contain a path visiting every vertex exactly once?), this would imply P = NP."
  type: true-false
  answer: true
  explanation: "Hamiltonian path is NP-complete, meaning every problem in NP can be reduced to it in polynomial time. If Hamiltonian path could be solved in polynomial time, then by those reductions, every problem in NP could also be solved in polynomial time — collapsing NP into P. NP-completeness is the key concept that links individual problems to the entire class: solving any one NP-complete problem efficiently would solve them all, resolving the central question in computational complexity theory."

- question: "Explain the difference between verifying a solution and finding a solution, using a concrete example to show why this distinction defines the NP complexity class."
  type: short-answer
  answer: "Verification means checking whether a proposed solution is correct; finding means constructing a solution from scratch. For Hamiltonian path: given a specific sequence of vertices as a certificate, checking that it visits each vertex once and uses only real edges takes linear time. But finding such a sequence — or proving none exists — appears to require exponential search through possibilities. NP captures exactly this asymmetry: problems where 'yes' answers have short, easily checkable proofs, even if producing those proofs is computationally hard."
  explanation: "The certificate model formalizes this: an NP problem has a polynomial-time verifier V(x, c) where x is the input and c is a proposed solution. If the answer is 'yes,' there exists a c that makes V accept in polynomial time; if 'no,' no such c exists. P is the special case where finding is also efficient — no certificate is needed because you can solve the problem directly. P vs. NP asks whether the existence of an efficient verifier always implies the existence of an efficient solver — a question that remains unanswered after 50 years."
```

## Explainer

You already know what it means for a problem to be in P: a deterministic Turing machine can solve it in polynomial time. NP extends this idea by changing what "solve" means. Instead of requiring a machine to *find* an answer efficiently, NP only requires that a machine can *check* a proposed answer efficiently. The class **NP** (nondeterministic polynomial time) contains every decision problem where, if the answer is "yes," there exists a short proof — called a **certificate** or **witness** — that a deterministic Turing machine can verify in polynomial time.

Consider a concrete example: the Hamiltonian path problem asks whether a graph contains a path that visits every vertex exactly once. Finding such a path appears to require exploring exponentially many possibilities. But if someone hands you a specific sequence of vertices and claims it is a Hamiltonian path, you can verify this easily — just check that every vertex appears exactly once and each consecutive pair is connected by an edge. That verification runs in polynomial time, so Hamiltonian path is in NP. Every problem in P is automatically in NP as well, because if you can *solve* a problem in polynomial time, you can certainly *verify* a solution in polynomial time (just solve it yourself and compare).

The formal definition uses **nondeterministic Turing machines** — machines that can branch into multiple computational paths simultaneously and accept if *any* branch accepts. A nondeterministic TM running in polynomial time can "guess" the right certificate on one of its branches and then verify it. This nondeterministic guessing is not physically realistic, which is why the verifier definition is more intuitive: NP is the set of problems where "yes" answers have efficiently checkable proofs.

The central open question in computer science — **P versus NP** — asks whether every problem whose solutions can be *verified* quickly can also be *solved* quickly. If P = NP, then the apparent difficulty of problems like Hamiltonian path, Boolean satisfiability, and integer factorization would be an illusion — efficient algorithms would exist even if we haven't found them yet. Most computer scientists believe P ≠ NP, meaning that verification is fundamentally easier than discovery, but no one has been able to prove this. The resolution of this question would reshape cryptography, optimization, artificial intelligence, and mathematics itself.
