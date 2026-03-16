---
id: parse-trees-ambiguity-and-derivation
title: Parse Trees, Derivations, and Ambiguity in CFGs
domain: computer-science
course: theory-of-computation
prerequisites:
- id: context-free-grammars-and-languages
  type: hard
builds-toward:
- normal-forms-for-context-free-grammars
- cyk-parsing-algorithm
tags:
- cfg
- parse-trees
- ambiguity
stage: abstract-reasoning
status: draft
---

# Parse Trees, Derivations, and Ambiguity in CFGs

## Core Idea
A derivation is a sequence of rule applications producing a string from the start symbol. A parse tree is a hierarchical representation of this derivation. A grammar is ambiguous if some string has multiple distinct parse trees (or leftmost derivations), which complicates parsing and semantics.

## Explainer

From your work with context-free grammars, you know that a CFG generates strings by repeatedly replacing nonterminals with the right-hand side of production rules. A **derivation** is the full sequence of these replacements, starting from the start symbol S and ending with a string of terminals. For example, if you have S → AB, A → a, B → b, then S ⇒ AB ⇒ aB ⇒ ab is a derivation. A **leftmost derivation** always expands the leftmost nonterminal first; a **rightmost derivation** always expands the rightmost. Both produce the same string, but the order of rule applications differs.

A **parse tree** captures the *structure* of a derivation without caring about the order. The root is the start symbol, internal nodes are nonterminals, leaves are terminals, and each parent-children relationship corresponds to one production rule. The key insight is that many different derivation orders can produce the same parse tree — a leftmost and rightmost derivation of the same string often correspond to the same tree, just read in different orders. The parse tree is therefore a more fundamental object than the derivation sequence: it shows *how* the string is structured, not merely *that* it can be generated.

**Ambiguity** arises when a single string has two or more *distinct* parse trees under the same grammar. Consider the classic arithmetic expression grammar: E → E + E | E × E | a. The string "a + a × a" can be parsed as either (a + a) × a or a + (a × a), corresponding to two different parse trees. These trees assign different meanings to the same string — one adds first, the other multiplies first. This is not an abstract concern; in a compiler, ambiguous grammars mean a program could have multiple interpretations, which is unacceptable.

Ambiguity is a property of the *grammar*, not the *language*. Often you can rewrite an ambiguous grammar into an unambiguous one that generates the same language — for arithmetic, you introduce separate nonterminals for terms and factors to enforce precedence. However, some context-free languages are **inherently ambiguous**, meaning every grammar for them is ambiguous. Recognizing and resolving ambiguity is a central skill in both theoretical computer science and practical compiler design, because the parse tree is exactly the data structure that determines what a program means.
