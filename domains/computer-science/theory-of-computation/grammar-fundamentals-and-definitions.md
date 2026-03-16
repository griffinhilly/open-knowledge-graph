---
id: grammar-fundamentals-and-definitions
title: 'Grammar Fundamentals: Productions and Derivations'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: formal-languages-and-strings
  type: hard
builds-toward:
- context-free-grammars
- context-free-language-properties
tags:
- grammars
- productions
- derivation
- parse-trees
- chomsky-hierarchy
stage: advanced
status: draft
---

# Grammar Fundamentals: Productions and Derivations

## Core Idea
A formal grammar consists of production rules transforming symbols. A derivation is a sequence of rule applications from a start symbol to a string. The Chomsky hierarchy—regular, context-free, context-sensitive, recursively enumerable—classifies grammars by production restrictions, corresponding to automata of increasing computational power.

## Explainer

From your study of formal languages, you know that a language is a set of strings over some alphabet. But defining a language by listing its strings only works for finite sets. **Formal grammars** solve this by providing a finite set of rules that generate all (and only) the strings in a language — even an infinite one. A grammar is a compact, finite description of a potentially infinite language.

A grammar has four components: a set of **terminal symbols** (the actual characters that appear in output strings, like `a`, `b`, `0`, `1`), a set of **non-terminal symbols** (placeholders used during generation, like S, A, B), a **start symbol** (a distinguished non-terminal where generation begins), and a set of **production rules** (rewriting rules of the form α → β, meaning "replace α with β"). A **derivation** is the process of starting with the start symbol and repeatedly applying production rules until only terminal symbols remain. For example, with rules S → aB and B → b, the derivation S ⇒ aB ⇒ ab generates the string "ab". Each step replaces a non-terminal using one of its production rules.

The **Chomsky hierarchy** classifies grammars into four types based on the form of their production rules, and each type corresponds to a class of automata. **Type 3 (regular)** grammars restrict productions to A → aB or A → a — a single non-terminal producing a terminal optionally followed by one non-terminal. These generate exactly the regular languages recognized by finite automata. **Type 2 (context-free)** grammars allow A → γ for any string γ — a single non-terminal on the left can be replaced by any combination of terminals and non-terminals. These generate the context-free languages recognized by pushdown automata. **Type 1 (context-sensitive)** grammars allow αAβ → αγβ, where the replacement depends on surrounding context and cannot shrink the string. **Type 0 (unrestricted)** grammars place no restrictions on productions and generate exactly the recursively enumerable languages recognized by Turing machines.

This hierarchy is strictly nested: every regular language is context-free, every context-free language is context-sensitive, and every context-sensitive language is recursively enumerable — but not vice versa. The hierarchy reveals a fundamental tradeoff between the expressive power of a grammar and the computational resources needed to recognize its language. Regular grammars are the least expressive but can be recognized with no memory beyond the current state; context-free grammars can describe nested structures like balanced parentheses but require a stack; context-sensitive grammars can express length-dependent patterns but require linear memory; and unrestricted grammars can describe anything computable but may require unbounded resources. Understanding where a language falls in this hierarchy tells you what kind of machine you need to process it.
