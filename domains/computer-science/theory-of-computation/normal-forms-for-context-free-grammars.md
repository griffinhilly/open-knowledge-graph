---
id: normal-forms-for-context-free-grammars
title: Normal Forms for Context-Free Grammars
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cfg-pda-equivalence
  type: hard
builds-toward:
- cyk-parsing-algorithm
- closure-properties-context-free
tags:
- cfg
- normal-forms
- cnf
- gnf
stage: advanced
status: validated
---

# Normal Forms for Context-Free Grammars

## Core Idea
Chomsky Normal Form (CNF) restricts productions to A → BC or A → a, eliminating ε-productions and unit productions. Greibach Normal Form (GNF) requires A → aα where a is a terminal. Both normal forms simplify parsing and proofs while maintaining expressiveness; any CFG can be converted to CNF or GNF.

## Questions

```yaml
- question: "A theorem about context-free languages begins: 'Without loss of generality, assume the grammar is in Chomsky Normal Form.' What justifies this assumption?"
  type: multiple-choice
  options:
    - "CNF grammars are more common in practice, so assuming CNF is a reasonable approximation"
    - "Any CFG can be mechanically converted to CNF while generating exactly the same language, so results proved for CNF hold for all CFLs"
    - "CNF is assumed because it simplifies notation, but the result would not necessarily apply to non-CNF grammars"
    - "The assumption only holds for grammars that do not generate the empty string"
  answer: 1
  explanation: "The 'without loss of generality' claim rests on the fact that CNF conversion is both universal (any CFG can be converted) and language-preserving (the converted grammar generates the same strings, possibly minus ε). This means any property proved about CNF grammars applies to the entire class of context-free languages — not just to grammars that happen to be in CNF. Normal forms are tools for enabling proofs and algorithms by standardizing structure, not by restricting what can be expressed."

- question: "Why is Chomsky Normal Form particularly useful as the foundation for the CYK parsing algorithm?"
  type: multiple-choice
  options:
    - "CNF eliminates all ambiguity in the grammar, making parsing deterministic"
    - "CNF's binary branching structure (A → BC) means every derivation of a string of length n takes exactly 2n−1 steps, enabling systematic dynamic programming over parse subtrees"
    - "CNF reduces the number of nonterminals, which makes the grammar smaller and faster to process"
    - "CYK requires GNF, not CNF — CNF is used for PDA construction instead"
  answer: 1
  explanation: "The A → BC rule in CNF means every non-terminal production splits into exactly two parts. This binary structure means a derivation of any string of length n takes exactly 2n−1 steps (since each step introduces one new terminal or one binary split). CYK exploits this by filling a triangular table of substrings bottom-up: for each substring, it checks whether any pair of adjacent substrings can combine via a CNF rule. The fixed 2n−1 step count makes the substring-combination approach exhaustive and efficient. Without binary branching, this dynamic programming structure would not work cleanly."

- question: "Converting a CFG to Chomsky Normal Form changes the language the grammar generates."
  type: true-false
  answer: false
  explanation: "CNF conversion is language-preserving: the resulting grammar generates exactly the same set of strings as the original (up to the empty string, which may be handled separately). The conversion process eliminates ε-productions, unit productions, and long right-hand sides through systematic substitution steps that preserve derivability. This equivalence is what makes CNF useful for theoretical arguments — you can assume CNF without restricting generality, because any result about CNF grammars applies to all context-free languages."

- question: "In a grammar in Greibach Normal Form, every derivation step consumes exactly one symbol from the input string."
  type: true-false
  answer: true
  explanation: "GNF requires every production to take the form A → aα, where a is a terminal and α is a (possibly empty) string of nonterminals. This means every time you expand a nonterminal, you immediately consume one terminal from the input. There is no way to perform a derivation step without reading a symbol. This property directly mirrors how a pushdown automaton reads input one symbol at a time, which is why GNF conversion makes the grammar-to-PDA translation transparent and eliminates infinite loops that can occur in top-down parsing of left-recursive grammars."

- question: "Explain the key insight behind normal forms: why are they useful if they don't change what a grammar can express?"
  type: short-answer
  answer: "Normal forms are useful precisely because they standardize structure without restricting expressive power. Algorithms and proofs often require specific structural properties of grammars to work correctly. CNF's binary branching (A → BC) enables the CYK algorithm's dynamic programming over binary subtrees. GNF's terminal-first structure (A → aα) makes each derivation step correspond to one input symbol read, enabling clean PDA construction. Without these constraints, a grammar might have productions of arbitrary length, left recursion, or epsilon productions that complicate algorithmic treatment. Normal forms let algorithm designers assume a fixed, well-behaved structure without losing any generative power."
  explanation: "This is the central point that students miss when they focus only on the mechanics of conversion. Normal forms are not restrictions — they are standardizations. Every CFG that matters can be put into CNF or GNF, so assuming normal form loses nothing. What is gained is the ability to build algorithms that rely on structural regularity. Understanding this motivates why the conversion process matters: not as an end in itself, but as the prerequisite for using grammars as input to algorithms."
```

## Explainer

You already know that context-free grammars and pushdown automata recognize exactly the same class of languages. But context-free grammars in their general form are messy — productions can have arbitrary mixes of terminals and nonterminals on the right side, chains of unit productions like A → B → C → D, and ε-productions that generate the empty string. This freedom makes grammars flexible for language designers but nightmarish for algorithm designers. Normal forms solve this by constraining production rules into a disciplined shape while preserving the grammar's generative power.

**Chomsky Normal Form** (CNF) is the most widely used normal form. Every production must be either A → BC (two nonterminals) or A → a (a single terminal). That's it — no mixed right-hand sides, no long chains, no epsilon. The conversion process works in stages: first eliminate ε-productions by propagating their effect into other rules, then eliminate unit productions by short-circuiting chains, then break long right-hand sides into binary pairs by introducing fresh nonterminals, and finally replace terminals that appear alongside nonterminals with dedicated "terminal nonterminals." Each step preserves the language (possibly minus ε). The result is a grammar where every derivation of a string of length n takes exactly 2n − 1 steps, which makes CNF the foundation for the CYK parsing algorithm — a dynamic programming approach that relies on this binary branching structure.

**Greibach Normal Form** (GNF) takes a different approach: every production starts with a terminal followed by zero or more nonterminals, as in A → aBC. This means every derivation step consumes exactly one input symbol, which directly corresponds to one move of a pushdown automaton. GNF conversion is more involved — it requires eliminating left recursion and rewriting productions using substitution — but the result makes the grammar-to-PDA construction transparent and eliminates the possibility of infinite loops in top-down parsing.

The key insight is that normal forms are not about changing what a grammar can express — they are about standardizing structure to enable algorithms and proofs. CNF gives you binary parse trees and polynomial-time parsing. GNF gives you deterministic single-symbol consumption and clean PDA construction. When you encounter a proof that says "without loss of generality, assume the grammar is in CNF," the claim rests on the fact that any CFG can be mechanically transformed into CNF while generating the same language, so anything proved about CNF grammars holds for all context-free languages.
