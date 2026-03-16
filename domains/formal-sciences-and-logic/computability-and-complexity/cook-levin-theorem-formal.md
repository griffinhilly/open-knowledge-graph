---
id: cook-levin-theorem-formal
title: The Cook-Levin Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: polynomial-time-reductions
  type: hard
- id: nondeterministic-turing-machines
  type: hard
- id: boolean-algebra
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-analysis-big-o
  type: soft
tags:
- NP-complete
- SAT
- satisfiability
- Cook-Levin
stage: advanced
status: validated
---

# The Cook-Levin Theorem

## Core Idea
The Cook-Levin theorem proves that Boolean satisfiability (SAT) is NP-complete — the first problem proven NP-complete (Cook 1971, independently Levin 1973). The proof encodes the computation of an arbitrary NTM as a propositional formula: variables represent tape cells, head positions, and states at each time step, while clauses enforce the transition rules. Since every NP problem reduces to SAT, SAT is the 'universal' hard problem in NP and the historical starting point for the entire theory of NP-completeness.

## How It's Best Learned
Work through the tableau construction carefully: understand how an NTM's accepting computation of length t is encoded as a formula of size O(t²). Appreciate that the reduction itself runs in polynomial time even though the formula can be large relative to the original instance.

## Common Misconceptions
- The theorem proves SAT is NP-complete, not that SAT is unsolvable — SAT is in NP, so it can be solved, just not known to be solvable in polynomial time.
- The historical significance is not merely proving SAT hard, but establishing the concept of NP-completeness itself and identifying the first complete problem from which all others reduce.

## Explainer

You already know that NP is the class of problems solvable by a **nondeterministic Turing machine (NTM)** in polynomial time, and that a polynomial-time reduction from problem A to problem B means "if we could solve B quickly, we could solve A quickly." The Cook-Levin theorem asks a sharper question: is there a single problem in NP so hard that *every* NP problem reduces to it? The answer is yes, and that problem is **Boolean satisfiability (SAT)** — the question of whether a propositional formula over variables x₁, …, xₙ has a truth assignment making it true.

The proof works by encoding computation as logic. Any NP problem has a polynomial-time NTM M that witnesses its solutions. Given an input w of length n, M runs in at most t(n) = nᶜ steps. The trick is to build a propositional formula φ_{M,w} — the **tableau formula** — whose satisfying assignments correspond exactly to accepting computation histories of M on w. The formula uses three families of variables: cell variables encoding what symbol occupies each tape cell at each time step, head variables encoding where the read/write head is, and state variables encoding M's current state. Together, they describe a t × t grid of "snapshots" of the machine's tape. Clauses then enforce: (1) the initial configuration matches w, (2) each transition follows the NTM's rules, and (3) M reaches an accepting state by step t.

The formula φ_{M,w} has size O(t²) — polynomial in n — and can be constructed in polynomial time. Here is the key insight: φ_{M,w} is satisfiable if and only if M accepts w. An accepting computation history is exactly a satisfying assignment. So the polynomial-time reduction from any NP problem to SAT is: "given an instance w, output the formula φ_{M,w}." This works for *any* NTM M, which means *every* NP problem reduces to SAT. Combined with the fact that SAT is itself in NP (guess an assignment, verify in polynomial time), SAT is NP-complete.

The theorem's historical weight goes beyond the single result. Before Cook and Levin, there was no vocabulary for saying "these hard-looking problems are all equally hard." By identifying SAT as a universal NP problem, the theorem gave complexity theory its organizing principle: to classify a new problem as NP-complete, you only need to show it's in NP and reduce a single known NP-complete problem to it. Every subsequent NP-completeness proof stands on this foundation — SAT is the ancestor of all known NP-complete problems.

One subtlety worth internalizing: the theorem does not say SAT is unsolvable, or that it requires exponential time. It says SAT is as hard as any problem in NP. Whether NP contains problems that *genuinely* require superpolynomial time — whether P ≠ NP — remains open. Cook-Levin identifies SAT as the right problem to study if you want to resolve P vs. NP; it does not resolve the question itself.
