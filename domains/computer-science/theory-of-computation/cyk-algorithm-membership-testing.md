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

## Questions

```yaml
- question: "Why does the CYK algorithm require the grammar to be in Chomsky Normal Form before it can be applied?"
  type: multiple-choice
  options:
    - "CNF grammars generate a strictly larger class of languages than arbitrary CFGs"
    - "CNF's restriction to productions A → BC means every substring can be split into exactly two non-empty parts to check — enabling the dynamic programming recurrence"
    - "CNF grammars are smaller and reduce the number of table entries needed"
    - "CYK only works correctly when the grammar has no epsilon productions"
  answer: 1
  explanation: "The CYK recurrence works because CNF productions are either A → BC (two nonterminals) or A → a (one terminal). The binary structure A → BC is essential: when checking what nonterminals can derive substring s[i..j], you try every split point k and check whether some rule A → BC exists where B derives s[i..k] and C derives s[k+1..j]. This binary decomposition maps cleanly onto the 'two sub-problems' structure of dynamic programming. If productions could have three or more nonterminals, the recurrence would not work in this simple form. Crucially, any CFG can be converted to CNF without changing the language."

- question: "You have run CYK on a string w of length n against a CNF grammar with start symbol S. What determines whether w is in the language?"
  type: multiple-choice
  options:
    - "Whether any cell in the table contains S"
    - "Whether the start symbol S appears in cell T[1,n]"
    - "Whether cell T[n,n] contains S after all productions are applied"
    - "Whether S appears in every cell along the main diagonal"
  answer: 1
  explanation: "T[1,n] represents the entire string — the set of nonterminals that can derive w[1..n]. The string belongs to the language if and only if the start symbol S can derive the entire string, which means S must appear in T[1,n]. Finding S in any other cell would mean S derives some proper substring of w, not w itself. The cell T[1,n] is the unique cell whose span covers the whole input."

- question: "CYK is a top-down parsing algorithm: it starts with the start symbol and expands production rules until it either matches the input or exhausts all possibilities."
  type: true-false
  answer: false
  explanation: "CYK is a bottom-up algorithm. It starts by filling the table for individual characters (substrings of length 1), then builds up to substrings of length 2, 3, and so on, until it reaches the full string. At each step, it combines previously computed results for shorter substrings. Top-down parsing (like recursive-descent) starts with the start symbol and tries to expand it to match the input — the opposite direction. CYK's bottom-up approach is what makes the dynamic programming recurrence well-founded: when computing T[i,j], all smaller subproblem cells T[i,k] and T[k+1,j] have already been computed."

- question: "Converting a CFG to CNF before applying CYK does not change which strings the grammar accepts — the language is preserved."
  type: true-false
  answer: true
  explanation: "CNF conversion uses a series of mechanical transformations (eliminating epsilon productions, unit productions, and rules with more than two nonterminals) that are all language-preserving. The resulting CNF grammar generates exactly the same strings as the original grammar, possibly with the exception of the empty string which requires separate handling. This is why CNF is not a real restriction on CYK's applicability — any CFG can be converted first, and the membership decision will be the same."

- question: "Where does CYK's O(n³) time complexity come from? Describe the three nested loops and what each iterates over."
  type: short-answer
  answer: "The three loops are: (1) substring length l, iterating from 1 to n — you must fill cells for every possible substring length before using them; (2) starting position i, iterating from 1 to n−l+1 — you must fill every substring of each length; (3) split point k, iterating from i to i+l−2 — for each cell T[i,j], you try every way to split the substring into two non-empty parts and check all applicable grammar rules. Each loop runs O(n) times, giving O(n³) total cell computations (multiplied by the constant grammar size)."
  explanation: "This cubic complexity is unavoidable for general CFGs without additional structure. It makes CYK unsuitable for production parsers handling large inputs, but it remains important as the theoretically optimal algorithm for arbitrary CFGs and as the foundation for probabilistic parsing (where you replace set membership with probability maximization in the same table structure)."
```

## Explainer

The fundamental question in parsing is: given a grammar G and a string w, does G generate w? For context-free grammars, the **CYK algorithm** (Cocke-Younger-Kasami) answers this question in O(n³) time using **dynamic programming** — a technique you have seen in other contexts, where you solve small subproblems first and combine their solutions to tackle larger ones. CYK requires the grammar to be in **Chomsky Normal Form** (CNF), where every production is either A → BC (two nonterminals) or A → a (a single terminal). Your prerequisite on grammar normal forms showed that any CFG can be converted to CNF, so this is not a real restriction.

The algorithm builds a triangular table where each cell **T[i,j]** stores the set of nonterminals that can derive the substring of w from position i to position j. The base case fills the bottom row: for each single character w[i], T[i,i] contains every nonterminal A such that A → w[i] is a production rule. This is straightforward — you are just asking which rules directly produce each individual symbol.

The recursive case is where the dynamic programming logic appears. To fill T[i,j] for a substring of length greater than 1, you try every way to split the substring into two non-empty parts: positions i to k and k+1 to j, for every valid k. For each split, you check whether there is a production A → BC where B ∈ T[i,k] and C ∈ T[k+1,j]. If so, A goes into T[i,j]. You are asking: "Can I split this substring into two pieces, each derivable from nonterminals that combine via some rule?" By working bottom-up from substrings of length 1 to length n, every cell you need has already been computed by the time you need it.

The string w belongs to L(G) if and only if the start symbol S appears in T[1,n] — the cell representing the entire string. The cubic time complexity comes from three nested loops: O(n) choices for substring length, O(n) choices for starting position, and O(n) choices for the split point. While O(n³) is not fast enough for production parsers that process millions of lines (specialized parsers for restricted grammar subclasses run in linear time), CYK is theoretically important because it works for *any* CFG without requiring the grammar to have special structure beyond CNF. It is also the foundation for probabilistic parsing, where you attach probabilities to grammar rules and use the CYK table to find the most likely parse.
