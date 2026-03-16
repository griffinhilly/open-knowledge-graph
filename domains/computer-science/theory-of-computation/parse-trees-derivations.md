---
id: parse-trees-derivations
title: Parse Trees and Derivations
domain: computer-science
course: theory-of-computation
prerequisites:
- id: context-free-grammars
  type: hard
- id: binary-trees
  type: soft
builds-toward:
- chomsky-normal-form
- cfg-pda-equivalence
tags:
- parse-trees
- derivations
- ambiguity
- CFG
stage: advanced
status: validated
---

# Parse Trees and Derivations

## Core Idea
A parse tree for a CFG derivation is a rooted tree where the root is labeled by the start variable, internal nodes are labeled by variables, leaves are terminals (or ε), and each internal node's children match the right-hand side of some production rule. The yield (left-to-right reading of the leaves) is the derived string. A grammar is ambiguous if some string has two distinct parse trees. Ambiguity matters for parsing: an ambiguous grammar for arithmetic expressions would give different operator precedence for the same input.

## How It's Best Learned
Write parse trees for arithmetic expressions under different grammars (ambiguous vs. unambiguous) and observe how tree structure encodes operator precedence. Distinguish leftmost derivation (always expand leftmost variable first) from rightmost derivation and show both correspond to unique parse trees.

## Common Misconceptions
- Conflating ambiguity in a grammar with ambiguity of a language — some languages are *inherently* ambiguous (no unambiguous grammar exists), but this is distinct from a particular grammar being ambiguous.
- Thinking leftmost and rightmost derivations are the same — they yield the same string but may produce different parse trees for ambiguous grammars.

## Explainer

A context-free grammar gives you production rules for generating strings, but a derivation — the sequence of rule applications that produces a string — can feel like a flat, linear process. A **parse tree** reveals the hidden structure: it shows *how* a string was built, not just *that* it was built. The root is the start variable, each internal node is a variable that was expanded using some production, and the leaves (read left to right) spell out the derived string. If you know binary trees from your prerequisites, a parse tree is simply a labeled tree where branching is determined by grammar rules rather than by comparison operations.

Consider the arithmetic expression 3 + 4 × 5. An ambiguous grammar might let you build two different parse trees: one where + is applied first (grouping as (3 + 4) × 5 = 35) and another where × is applied first (grouping as 3 + (4 × 5) = 23). The tree structure encodes **operator precedence and associativity** — deeper subtrees are evaluated first. This is why compilers care about parse trees: the tree determines the meaning of the program, not just its text. An unambiguous grammar forces a single parse tree per string, eliminating this kind of semantic confusion.

A **derivation** is the step-by-step sequence of variable expansions that builds a string. A **leftmost derivation** always expands the leftmost remaining variable; a **rightmost derivation** always expands the rightmost. For an unambiguous grammar, both derivation orders produce the same parse tree — they just visit nodes in different orders, like pre-order vs. post-order traversals of the same tree. For an ambiguous grammar, different derivation orders can correspond to genuinely different parse trees, each encoding a different structural interpretation of the string.

The distinction between an ambiguous *grammar* and an ambiguous *language* is subtle but important. A grammar is ambiguous if some string has two distinct parse trees under that grammar. But you might be able to rewrite the grammar — adding new variables and restructuring productions — to eliminate the ambiguity while generating the same language. An **inherently ambiguous language** is one where *no* unambiguous grammar exists, a much stronger and rarer condition. Most practical languages (programming languages, arithmetic) are not inherently ambiguous; their grammars can be carefully designed to enforce a unique parse for every valid input.
