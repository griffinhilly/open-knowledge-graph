---
id: clique-problem-np-complete
title: Clique Problem and Its Variants
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: three-sat-np-complete
  type: hard
- id: np-completeness-formal
  type: hard
- id: graph-theory-fundamentals
  type: soft
builds-toward:
- vertex-cover-problem
tags:
- graph-problems
- np-complete
- optimization
stage: formal-systems
status: draft
---

# Clique Problem and Its Variants

## Core Idea
The clique problem asks whether a graph contains a subset of k vertices all pairwise adjacent (a complete subgraph). NP-completeness of the clique problem follows from reduction from 3-SAT. Its complement, the independent set problem, is also NP-complete, illustrating how graph optimization problems naturally exhibit computational hardness.

## Questions

```yaml
- question: "The clique problem is in NP. What does this mean precisely?"
  type: multiple-choice
  options:
    - "It can be solved in polynomial time by a deterministic algorithm"
    - "Given a proposed solution — a set of k vertices — a verifier can check in polynomial time whether all pairs are connected"
    - "It is no harder than any problem solvable in polynomial time"
    - "It can only be solved by a nondeterministic Turing machine, never a deterministic one"
  answer: 1
  explanation: "NP (nondeterministic polynomial time) is defined as the class of decision problems where a proposed solution can be VERIFIED in polynomial time by a deterministic algorithm. For CLIQUE, the certificate is simply a list of k vertices. Verification requires checking all k(k−1)/2 pairs to confirm each has an edge — this is O(k²) time, hence polynomial. Note that NP says nothing about how hard it is to FIND a solution, only to check one. Option A describes P (polynomial-time solvability), not NP. Whether CLIQUE (or any NP-complete problem) can be solved in polynomial time is the unresolved P vs. NP question."

- question: "In the 3-SAT to CLIQUE reduction, a graph is constructed where vertices represent literals in clauses, edges connect non-contradictory literals from different clauses, and k equals the number of clauses. Why does a k-clique correspond exactly to a satisfying assignment?"
  type: multiple-choice
  options:
    - "Each clique member represents a clause that evaluates to true under the assignment, so k members cover all k clauses"
    - "A k-clique must include exactly one vertex per clause (vertices from the same clause are not connected) and no two clique members can be contradictory (contradictory literals have no edge), giving a consistent assignment that satisfies every clause"
    - "The clique size k forces all variables to be set to true, which satisfies any CNF formula"
    - "k-cliques in this graph always correspond to valid logical assignments by construction of the clique definition"
  answer: 1
  explanation: "The reduction is elegant because every constraint of the clique structure maps exactly to a constraint of satisfiability. Vertices from the same clause share no edges, so a k-clique must pick exactly one vertex per clause (otherwise two same-clause vertices would share an edge, which they don't). No edge connects contradictory literals (x and ¬x), so a k-clique can never include both — this means the k chosen literals define a consistent (non-contradictory) partial assignment. Since one literal per clause is chosen and it must be satisfiable, the assignment satisfies every clause. The forward direction is symmetric: a satisfying assignment picks one true literal per clause; those literals form a k-clique because they are from different clauses and cannot be contradictory."

- question: "The fact that checking whether a given set of k vertices forms a clique can be done in polynomial time implies that finding a maximum clique in a graph can also be done efficiently."
  type: true-false
  answer: false
  explanation: "This is a classic confusion between verification and search. NP is defined by efficient verification, not efficient search. Checking a proposed clique is O(k²) — polynomial and easy. But finding the maximum clique requires searching through exponentially many subsets of vertices in the worst case. The clique problem is NP-complete, meaning no polynomial-time algorithm is known for finding it, and the P ≠ NP conjecture asserts no such algorithm exists. Easy verification is a necessary condition for NP, not a sufficient condition for efficient solution. The entire difficulty of the P vs. NP question stems from this gap between verification and search."

- question: "A set S of vertices is a clique in graph G if and only if S is an independent set in the complement graph Ḡ (which has edges exactly where G does not), proving that CLIQUE and INDEPENDENT SET are polynomial-time equivalent."
  type: true-false
  answer: true
  explanation: "The complement relationship is exact: Ḡ has an edge between u and v whenever G does not. So 'all pairs in S are adjacent in G' is logically equivalent to 'no pairs in S are adjacent in Ḡ' — which is the definition of an independent set. Since this graph complement can be computed in polynomial time, CLIQUE ≤_P INDEPENDENT SET and INDEPENDENT SET ≤_P CLIQUE. Because CLIQUE is NP-complete, INDEPENDENT SET is also NP-complete. The same complement technique shows INDEPENDENT SET and VERTEX COVER are polynomial-time equivalent via S independent ⟺ V\S is a vertex cover."

- question: "What is the structural insight of the 3-SAT to CLIQUE reduction? Why does the construction ensure that a k-clique exists if and only if the formula is satisfiable?"
  type: short-answer
  answer: "The reduction encodes the constraints of satisfiability as constraints of clique membership. The graph has one vertex per (literal, clause) pair. Two vertices are connected if and only if (1) they come from different clauses and (2) they are not contradictory. Setting k equal to the number of clauses forces a k-clique to select exactly one vertex per clause (since same-clause vertices have no edges, a clique cannot contain two) and to avoid contradictory literals (since x and ¬x have no edge). This means each k-clique defines a consistent partial assignment that makes at least one literal true in every clause — exactly a satisfying assignment. Conversely, any satisfying assignment picks one true literal per clause, and those literals form a k-clique because satisfying assignments are by definition non-contradictory. The construction works because the two hard constraints of satisfiability (one true literal per clause, no variable assigned both values) map perfectly onto the two structural constraints of a clique (one vertex per clause group, no complementary literals)."
  explanation: "The key skill is seeing the correspondence between the logical structure of satisfiability and the graph structure of cliques. This is the art of NP-completeness reductions: finding the exact combinatorial matching between two problem structures."
```

## Explainer

A **clique** in a graph is a set of vertices that are all mutually connected — every pair has an edge between them. The clique decision problem CLIQUE asks: given a graph G and integer k, does G contain a clique of size k? This seems like a search problem over vertex subsets, and while checking a candidate clique is easy (inspect all k(k−1)/2 pairs), finding one requires searching exponentially many subsets in the worst case. Your prerequisite work with NP-completeness gives you the tools to explain why no polynomial algorithm is known.

To prove CLIQUE is NP-complete, you reduce from 3-SAT — the problem you already know is NP-complete. Given a 3-CNF formula with m clauses C₁, C₂, …, Cₘ, construct a graph as follows: create one vertex for each literal in each clause (so up to 3m vertices total, labeled by their (literal, clause) pair), then connect two vertices with an edge if and only if they come from *different* clauses and are *not* contradictory (i.e., not a literal and its negation). Now set k = m. The key insight is that a satisfying assignment to the formula corresponds exactly to choosing one true literal per clause, and those m chosen literals form a clique — they're all from different clauses and no two are contradictory (a satisfying assignment never makes both x and ¬x true). Conversely, any k-clique must pick exactly one vertex per clause and can never pick complementary literals, so it defines a consistent partial assignment that satisfies every clause. The reduction runs in polynomial time, so CLIQUE is NP-hard; it's also in NP (a clique certificate can be verified in polynomial time), hence NP-complete.

The **independent set** problem — does G contain a set of k vertices with *no* edges between them? — is the complement in a precise sense: a set S is a clique in G if and only if S is an independent set in the complement graph Ḡ (which has an edge where G doesn't). This means CLIQUE and INDEPENDENT SET are polynomial-time equivalent, and since CLIQUE is NP-complete, so is INDEPENDENT SET. Similarly, **VERTEX COVER** (find a set of k vertices touching every edge) is NP-complete and connects to independent set via the complement: S is an independent set if and only if V \ S is a vertex cover. These three problems form a tightly linked family, all capturing the same underlying computational hardness from different angles.

The pattern generalizes: many natural graph optimization problems — maximum clique, maximum independent set, minimum vertex cover — are NP-hard even to approximate within constant factors. This is not merely about exact computation; it reflects deep structure in how combinatorial optimization interacts with constraint satisfaction. The polynomial reduction framework you learned with 3-SAT is the workhorse that connects all these problems into a single web of hardness, where solving any one efficiently would collapse the entire NP-complete class to P.
