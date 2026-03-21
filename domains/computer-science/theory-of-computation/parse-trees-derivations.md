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

## Questions

```yaml
- question: "An arithmetic grammar allows E → E+E | E*E | int. A student argues this is fine because any valid arithmetic expression can still be parsed. What is the real problem?"
  type: multiple-choice
  options:
    - "The grammar is ambiguous — the string '2+3*4' has two distinct parse trees, one encoding (2+3)*4=35 and another encoding 2+(3*4)=23"
    - "The grammar is unusable because it does not handle parentheses"
    - "The grammar is inherently ambiguous, so no unambiguous grammar can generate arithmetic expressions"
    - "The grammar only allows leftmost derivations, not rightmost"
  answer: 0
  explanation: "The grammar is ambiguous — the same string has two parse trees encoding different operator precedences. Option C confuses an ambiguous grammar with an inherently ambiguous language. The language of arithmetic expressions is NOT inherently ambiguous; you can rewrite the grammar with additional variables (e.g., distinguishing Expr, Term, Factor) to enforce a unique parse tree per string."

- question: "A leftmost derivation and a rightmost derivation of the same string in an unambiguous grammar produce..."
  type: multiple-choice
  options:
    - "Different strings, since they expand different variables"
    - "Different parse trees, since nodes are visited in different orders"
    - "The same parse tree, since both derivations describe the same unique structural interpretation"
    - "Identical sequences of steps, since derivation order does not matter"
  answer: 2
  explanation: "For an unambiguous grammar, every string has exactly one parse tree, regardless of whether you expand variables leftmost-first or rightmost-first. The derivation order is like traversal order on a tree — pre-order vs. post-order visit nodes differently but describe the same tree. Only in an ambiguous grammar can different derivation strategies yield genuinely different trees."

- question: "An unambiguous grammar produces exactly one parse tree for every string in the language it generates."
  type: true-false
  answer: true
  explanation: "This is the definition of an unambiguous grammar. A grammar is ambiguous if and only if some string has two or more distinct parse trees. Unambiguity guarantees that every string in the language has a unique structural interpretation — exactly what compilers need to assign consistent semantics to programs."

- question: "If a particular grammar for a language is ambiguous, then that language is inherently ambiguous and no unambiguous grammar for it exists."
  type: true-false
  answer: false
  explanation: "Ambiguity is a property of a specific grammar, not necessarily of the language. An inherently ambiguous language is one where no unambiguous grammar exists — a much rarer and stronger condition. Most practical programming languages are not inherently ambiguous; their grammars can be carefully rewritten to eliminate ambiguity while generating the same language."

- question: "Why do compilers need unambiguous grammars, and what role does the parse tree play in determining program semantics?"
  type: short-answer
  answer: "The parse tree encodes the structural interpretation of a program — it determines operator precedence, associativity, and which subexpressions are evaluated first. An ambiguous grammar means a single program text could have two different parse trees and therefore two different meanings. Compilers rely on a unique parse tree to assign a single, consistent meaning to each program."
  explanation: "Consider '2+3*4': without a unique parse tree, a compiler might evaluate it as 35 or 23 depending on which tree it finds. Unambiguous grammars solve this by forcing a single tree — typically through stratification (separating expression, term, factor levels) that encodes precedence in the grammar structure itself."
```

## Explainer

A context-free grammar gives you production rules for generating strings, but a derivation — the sequence of rule applications that produces a string — can feel like a flat, linear process. A **parse tree** reveals the hidden structure: it shows *how* a string was built, not just *that* it was built. The root is the start variable, each internal node is a variable that was expanded using some production, and the leaves (read left to right) spell out the derived string. If you know binary trees from your prerequisites, a parse tree is simply a labeled tree where branching is determined by grammar rules rather than by comparison operations.

Consider the arithmetic expression 3 + 4 × 5. An ambiguous grammar might let you build two different parse trees: one where + is applied first (grouping as (3 + 4) × 5 = 35) and another where × is applied first (grouping as 3 + (4 × 5) = 23). The tree structure encodes **operator precedence and associativity** — deeper subtrees are evaluated first. This is why compilers care about parse trees: the tree determines the meaning of the program, not just its text. An unambiguous grammar forces a single parse tree per string, eliminating this kind of semantic confusion.

A **derivation** is the step-by-step sequence of variable expansions that builds a string. A **leftmost derivation** always expands the leftmost remaining variable; a **rightmost derivation** always expands the rightmost. For an unambiguous grammar, both derivation orders produce the same parse tree — they just visit nodes in different orders, like pre-order vs. post-order traversals of the same tree. For an ambiguous grammar, different derivation orders can correspond to genuinely different parse trees, each encoding a different structural interpretation of the string.

The distinction between an ambiguous *grammar* and an ambiguous *language* is subtle but important. A grammar is ambiguous if some string has two distinct parse trees under that grammar. But you might be able to rewrite the grammar — adding new variables and restructuring productions — to eliminate the ambiguity while generating the same language. An **inherently ambiguous language** is one where *no* unambiguous grammar exists, a much stronger and rarer condition. Most practical languages (programming languages, arithmetic) are not inherently ambiguous; their grammars can be carefully designed to enforce a unique parse for every valid input.
