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
- id: graph-theory-intro
  type: soft
builds-toward:
- vertex-cover-problem
tags:
- graph-problems
- np-complete
- optimization
stage: formal-systems
status: validated
---

# Clique Problem and Its Variants

## Core Idea
The clique problem asks whether a graph contains a subset of k vertices all pairwise adjacent (a complete subgraph). NP-completeness of the clique problem follows from reduction from 3-SAT. Its complement, the independent set problem, is also NP-complete, illustrating how graph optimization problems naturally exhibit computational hardness.

## Explainer

A **clique** in a graph is a set of vertices that are all mutually connected — every pair has an edge between them. The clique decision problem CLIQUE asks: given a graph G and integer k, does G contain a clique of size k? This seems like a search problem over vertex subsets, and while checking a candidate clique is easy (inspect all k(k−1)/2 pairs), finding one requires searching exponentially many subsets in the worst case. Your prerequisite work with NP-completeness gives you the tools to explain why no polynomial algorithm is known.

To prove CLIQUE is NP-complete, you reduce from 3-SAT — the problem you already know is NP-complete. Given a 3-CNF formula with m clauses C₁, C₂, …, Cₘ, construct a graph as follows: create one vertex for each literal in each clause (so up to 3m vertices total, labeled by their (literal, clause) pair), then connect two vertices with an edge if and only if they come from *different* clauses and are *not* contradictory (i.e., not a literal and its negation). Now set k = m. The key insight is that a satisfying assignment to the formula corresponds exactly to choosing one true literal per clause, and those m chosen literals form a clique — they're all from different clauses and no two are contradictory (a satisfying assignment never makes both x and ¬x true). Conversely, any k-clique must pick exactly one vertex per clause and can never pick complementary literals, so it defines a consistent partial assignment that satisfies every clause. The reduction runs in polynomial time, so CLIQUE is NP-hard; it's also in NP (a clique certificate can be verified in polynomial time), hence NP-complete.

The **independent set** problem — does G contain a set of k vertices with *no* edges between them? — is the complement in a precise sense: a set S is a clique in G if and only if S is an independent set in the complement graph Ḡ (which has an edge where G doesn't). This means CLIQUE and INDEPENDENT SET are polynomial-time equivalent, and since CLIQUE is NP-complete, so is INDEPENDENT SET. Similarly, **VERTEX COVER** (find a set of k vertices touching every edge) is NP-complete and connects to independent set via the complement: S is an independent set if and only if V \ S is a vertex cover. These three problems form a tightly linked family, all capturing the same underlying computational hardness from different angles.

The pattern generalizes: many natural graph optimization problems — maximum clique, maximum independent set, minimum vertex cover — are NP-hard even to approximate within constant factors. This is not merely about exact computation; it reflects deep structure in how combinatorial optimization interacts with constraint satisfaction. The polynomial reduction framework you learned with 3-SAT is the workhorse that connects all these problems into a single web of hardness, where solving any one efficiently would collapse the entire NP-complete class to P.

## Questions

- id: clique-problem-np-complete-q1
  type: mc
  question: "In the reduction from 3-SAT to CLIQUE, how is the graph constructed from a 3-CNF formula with m clauses?"
  options:
    - "One vertex per variable, edges between variables in the same clause"
    - "One vertex per literal occurrence in each clause, edges between non-contradictory literals from different clauses"
    - "One vertex per clause, edges between clauses that share a variable"
    - "One vertex per literal occurrence in each clause, edges between all literals in the same clause"
  correct: 1
  explanation: "The reduction creates one vertex per literal in each clause and connects two vertices with an edge if and only if they come from different clauses and are not contradictory (not a literal and its negation)."

- id: clique-problem-np-complete-q2
  type: mc
  question: "What is the relationship between the clique problem and the independent set problem?"
  options:
    - "They are the same problem with different names"
    - "A set S is a clique in G if and only if S is an independent set in the complement graph of G"
    - "Independent set is solvable in polynomial time while clique is not"
    - "A clique in G corresponds to a vertex cover in the complement graph of G"
  correct: 1
  explanation: "A set S is a clique in G if and only if S is an independent set in the complement graph (the graph with edges exactly where G has none). This makes the two problems polynomial-time equivalent."

- id: clique-problem-np-complete-q3
  type: tf
  question: "Verifying that a given set of k vertices forms a clique can be done in polynomial time."
  correct: true
  explanation: "Verification requires checking all k(k-1)/2 pairs of vertices for edges, which is polynomial in k and thus polynomial in the size of the input. This is why CLIQUE is in NP."

- id: clique-problem-np-complete-q4
  type: tf
  question: "In the 3-SAT to CLIQUE reduction, a clique of size m in the constructed graph may include two vertices from the same clause."
  correct: false
  explanation: "Edges only connect vertices from different clauses, so no two vertices from the same clause are adjacent. A clique of size m must therefore pick exactly one vertex per clause."

- id: clique-problem-np-complete-q5
  type: sa
  question: "What is the name of the property relating a vertex cover to an independent set in the same graph?"
  correct: "S is an independent set if and only if V \\ S is a vertex cover"
  explanation: "The complement relationship means that removing an independent set from the vertex set yields a vertex cover, and vice versa. This links the two NP-complete problems directly."
