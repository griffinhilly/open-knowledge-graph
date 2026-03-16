---
id: cyk-algorithm-membership-testing
title: CYK Algorithm and Membership Testing
domain: computer-science
course: theory-of-computation
prerequisites:
- id: grammar-normal-forms-analysis
  type: hard
- id: dynamic-programming-intro
  type: soft
builds-toward:
- pushdown-automata
tags:
- cyk
- parsing
- membership
- dynamic-programming
- cubic-time
stage: advanced
status: draft
---

# CYK Algorithm and Membership Testing

## Core Idea
The Cocke-Younger-Kasami algorithm tests whether a string belongs to a CFL in O(n³) time, assuming grammar in CNF. It builds a table: entry [i,j] lists non-terminals deriving substring i..j. CYK is polynomial—optimal for arbitrary CFGs without compilation overhead—making it crucial for parsing without grammar restrictions.

## How It's Best Learned
Trace CYK on a small example (e.g., balanced parentheses grammar). Fill the table bottom-up, checking which rules produce needed sub-derives.

## Explainer

The fundamental question in parsing is: given a grammar G and a string w, does G generate w? For context-free grammars, the **CYK algorithm** (Cocke-Younger-Kasami) answers this question in O(n³) time using **dynamic programming** — a technique you have seen in other contexts, where you solve small subproblems first and combine their solutions to tackle larger ones. CYK requires the grammar to be in **Chomsky Normal Form** (CNF), where every production is either A → BC (two nonterminals) or A → a (a single terminal). Your prerequisite on grammar normal forms showed that any CFG can be converted to CNF, so this is not a real restriction.

The algorithm builds a triangular table where each cell **T[i,j]** stores the set of nonterminals that can derive the substring of w from position i to position j. The base case fills the bottom row: for each single character w[i], T[i,i] contains every nonterminal A such that A → w[i] is a production rule. This is straightforward — you are just asking which rules directly produce each individual symbol.

The recursive case is where the dynamic programming logic appears. To fill T[i,j] for a substring of length greater than 1, you try every way to split the substring into two non-empty parts: positions i to k and k+1 to j, for every valid k. For each split, you check whether there is a production A → BC where B ∈ T[i,k] and C ∈ T[k+1,j]. If so, A goes into T[i,j]. You are asking: "Can I split this substring into two pieces, each derivable from nonterminals that combine via some rule?" By working bottom-up from substrings of length 1 to length n, every cell you need has already been computed by the time you need it.

The string w belongs to L(G) if and only if the start symbol S appears in T[1,n] — the cell representing the entire string. The cubic time complexity comes from three nested loops: O(n) choices for substring length, O(n) choices for starting position, and O(n) choices for the split point. While O(n³) is not fast enough for production parsers that process millions of lines (specialized parsers for restricted grammar subclasses run in linear time), CYK is theoretically important because it works for *any* CFG without requiring the grammar to have special structure beyond CNF. It is also the foundation for probabilistic parsing, where you attach probabilities to grammar rules and use the CYK table to find the most likely parse.
