---
id: grammar-normal-forms-analysis
title: 'Grammar Normal Forms: CNF and GNF'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: chomsky-normal-form
  type: hard
- id: context-free-grammar-properties-and-ambiguity
  type: soft
builds-toward:
- cyk-algorithm-membership-testing
tags:
- cnf
- greibach-normal-form
- normal-forms
- transformation
- simplification
stage: advanced
status: validated
---

# Grammar Normal Forms: CNF and GNF

## Core Idea
Chomsky Normal Form (CNF) restricts productions to A → BC or A → a, enabling efficient algorithms and theoretical analysis. Greibach Normal Form ensures rightmost symbols are terminals, useful for top-down parsing. Transforming to normal form eliminates epsilon, unit, and useless productions—a preprocessing step that may increase grammar size but simplifies downstream algorithms.

## How It's Best Learned
Work through transformation steps (eliminate epsilon, unit productions, chain productions) on a concrete grammar. Verify the resulting grammar generates the same language.

## Questions

```yaml
- question: "Converting a grammar to CNF triples its number of rules and introduces many new non-terminals. A student objects that 'the grammar now generates different derivations than before.' Which response is correct?"
  type: multiple-choice
  options:
    - "The student is right — more rules means the grammar can derive additional strings"
    - "The student is right — eliminating epsilon productions removes the empty string from the language"
    - "The student is wrong — CNF changes the structure of derivations but the set of strings generated is identical to the original grammar"
    - "The student is wrong — CNF actually restricts the grammar to a proper subset of the original language to simplify algorithms"
  answer: 2
  explanation: "Normal form transformation is language-preserving: the grammar generates exactly the same strings before and after conversion. The derivations look different (more steps, different non-terminal names) and the parse trees may have different shapes, but every string derivable in the original grammar is still derivable in CNF, and vice versa. This is the foundational guarantee that makes normal forms useful — you can convert to a convenient form for algorithmic purposes without changing what the grammar accepts."

- question: "Why does Chomsky Normal Form specifically enable the CYK parsing algorithm to run in O(n³) time for an input of length n?"
  type: multiple-choice
  options:
    - "CNF eliminates ambiguity, ensuring each string has at most one parse tree to find"
    - "CNF's binary productions (A → BC) mean every string of length n has a derivation that can be split into two sub-problems, enabling a systematic bottom-up triangular table"
    - "CNF reduces the terminal alphabet size, cutting the number of comparisons by a constant factor"
    - "CNF removes left recursion, preventing infinite loops that would otherwise increase complexity"
  answer: 1
  explanation: "The key structural insight is that A → BC forces every non-trivial derivation to split into exactly two non-overlapping substrings. For a string of length n, you can systematically fill a triangular table: each cell (i, j) records which non-terminals can derive the substring from position i to j. Because every production splits into exactly two parts, each cell's computation depends only on previously computed cells — giving a clean O(n²) table with O(n) work per cell, totaling O(n³). Without the binary-production constraint of CNF, right-hand sides of varying lengths would make this systematic splitting impossible."

- question: "Transforming a grammar to CNF may result in more productions and non-terminals than the original grammar had."
  type: true-false
  answer: true
  explanation: "CNF transformation can significantly increase grammar size. Eliminating epsilon productions requires creating variants of rules with and without nullable non-terminals. Eliminating unit chains requires adding direct rules for each reachable non-terminal. Breaking long right-hand sides (A → BCD) into chains of binary rules (A → BX, X → CD) introduces fresh non-terminals. A grammar with long productions and many nullable symbols can expand substantially. This size increase is the cost of the algorithmic convenience CNF provides — it's an accepted tradeoff in compiler design."

- question: "Greibach Normal Form (GNF) is useful primarily because it eliminates ambiguity from context-free grammars."
  type: true-false
  answer: false
  explanation: "GNF does not eliminate ambiguity. A grammar in GNF can still be ambiguous — multiple leftmost derivations may still exist for some strings. GNF's actual advantage is structural: every production begins with a terminal (A → aα), which guarantees that every derivation step consumes exactly one input symbol. This prevents left-recursive loops in top-down parsers (since each step makes progress on the input) and aligns naturally with pushdown automaton operation. Ambiguity is a separate property that GNF transformation does not address."

- question: "A grammar has the unit production A → B. Explain why unit productions must be eliminated during CNF transformation and what the elimination process does."
  type: short-answer
  answer: "Unit productions (A → B where both sides are single non-terminals) violate CNF's requirement that every production be either A → BC or A → a. They also form chains — A → B → C → a — that add derivation steps without consuming input, complicating analysis. Elimination proceeds by finding all non-terminals reachable from A via chains of unit productions, then adding a direct production from A to whatever those non-terminals ultimately derive (their non-unit right-hand sides). The unit productions themselves are then removed. This may add rules but ensures every production has the correct CNF shape."
  explanation: "Unit production elimination is step two of the standard CNF pipeline (after epsilon elimination). The key is tracing the entire reachability closure: if A → B and B → C and C → aB, then A → aB must be added directly. Without this step, CNF's binary-production invariant would be violated by the unit chains."
```

## Explainer

From your study of Chomsky Normal Form, you know that any context-free grammar can be restructured so that every production has a specific shape. Normal forms are not about changing *what* a grammar generates — the language stays exactly the same — but about restricting *how* productions are written so that algorithms and proofs become simpler. Think of it like converting a fraction to lowest terms: the value does not change, but the simplified form is far easier to work with.

**Chomsky Normal Form (CNF)** requires every production to be either A → BC (two non-terminals) or A → a (a single terminal). No epsilon productions (except possibly S → ε for the start symbol), no unit productions (A → B), and no right-hand sides with more than two symbols. This rigid binary structure is what makes the **CYK parsing algorithm** possible: because every production splits into exactly two parts, you can fill in a triangular parsing table bottom-up in O(n³) time. Without CNF, the variable-length right-hand sides make systematic parsing much harder.

**Greibach Normal Form (GNF)** takes a different approach: every production must begin with a terminal followed by zero or more non-terminals (A → aα, where a is a terminal and α is a string of non-terminals). This form is useful for **top-down parsing** because reading one input symbol always consumes exactly one terminal from the front of a production, guaranteeing that the parser makes progress on every step without risk of infinite left-recursive loops. GNF also simplifies certain proofs about pushdown automata, since each derivation step corresponds naturally to one input read and one stack operation.

The transformation process follows a standard pipeline. First, **eliminate epsilon productions**: for every rule A → ε, find all places A appears on the right-hand side of other rules and create versions both with and without A. Second, **eliminate unit productions** (A → B): trace chains of unit productions and replace them with direct rules to the eventual terminal or multi-symbol result. Third, **remove useless symbols**: any non-terminal that cannot be reached from the start symbol or cannot derive a terminal string is dead weight. Finally, restructure the remaining productions into the target normal form — for CNF, break long right-hand sides into chains of binary rules using fresh non-terminals. The grammar may grow in size (more rules, more non-terminals), but it generates exactly the same language, and the standardized structure unlocks efficient algorithms downstream.
