---
id: context-free-grammars
title: Context-Free Grammars (CFGs)
domain: computer-science
course: theory-of-computation
prerequisites:
- id: regular-language-properties
  type: soft
- id: set-theory-basics
  type: soft
- id: recursion-basics
  type: soft
- id: formal-languages-and-strings
  type: soft
builds-toward:
- parse-trees-derivations
- chomsky-normal-form
- pushdown-automata
- closure-properties-cfl
tags:
- CFG
- context-free
- grammars
- productions
- derivation
stage: advanced
status: validated
---

# Context-Free Grammars (CFGs)

## Core Idea
A context-free grammar (CFG) is a 4-tuple (V, Σ, R, S) of variables, terminals, production rules, and a start variable. Each rule replaces a single variable with any string of variables and terminals. The language of a CFG is the set of terminal strings derivable from the start variable. CFGs are strictly more powerful than regular expressions — they can describe languages like {aⁿbⁿ} that no DFA can recognize. CFGs are the foundation of programming language syntax, used in parser generators and compilers.

## How It's Best Learned
Begin by writing grammars for arithmetic expressions (which naturally requires recursion) and palindromes. Trace leftmost and rightmost derivations step-by-step. Then attempt to characterize which languages require CFGs versus which are regular.

## Common Misconceptions
- Thinking 'context-free' means the grammar is simple — the term refers specifically to the rule form (single variable on the left side), not the complexity of the language.
- Confusing a grammar with its language: many grammars can generate the same language.
- Assuming every grammar is unambiguous — ambiguity (multiple parse trees for one string) is common and often problematic.

## Questions

```yaml
- question: "Which of the following languages requires a context-free grammar and cannot be described by any regular expression?"
  type: multiple-choice
  options: ["{ aⁿ | n ≥ 0 }", "{ aⁿbⁿ | n ≥ 0 }", "{ strings over {a,b} containing at least one a }", "{ ab, ba }"]
  answer: 1
  explanation: "{ aⁿbⁿ } requires counting equal numbers of a's and b's — a form of memory that finite automata cannot provide. The pumping lemma for regular languages proves no DFA can recognize it. The other options are all regular: any finite language or simple pattern is describable by a regex. CFGs handle { aⁿbⁿ } via the rule S → aSb | ε."

- question: "If two different context-free grammars both generate the same string w, then w is ambiguous."
  type: true-false
  answer: false
  explanation: "Ambiguity is a property of a single grammar with respect to a single string: a string is ambiguous in grammar G if G produces more than one distinct parse tree for it. Having two different grammars that each generate the same string says nothing about ambiguity. In fact, many different grammars generate the same language — and a language is only inherently ambiguous if every grammar for it is ambiguous."

- question: "What is the difference between a context-free grammar and the context-free language it defines?"
  type: short-answer
  answer: "A grammar is a finite set of production rules; the language is the (potentially infinite) set of all terminal strings derivable from the start symbol by applying those rules. Multiple different grammars can define the same language."
  explanation: "This distinction is crucial for understanding equivalence and ambiguity. Algorithms like CYK parse strings relative to a grammar, not a language. When we say a language is context-free, we mean there exists at least one CFG that generates exactly that set of strings."
```

## Explainer

You have already seen that regular languages — described by regular expressions and recognized by finite automata — have a fundamental limitation: they cannot count. A DFA has no memory beyond its current state, which means it cannot verify that a string has exactly as many a's as b's. Context-free grammars (CFGs) overcome this by introducing recursive structure, and recursion is the key insight.

A CFG is a 4-tuple (V, Σ, R, S): a set of variables (non-terminals), a terminal alphabet, a set of production rules, and a start variable. Each rule has the form A → α, where A is a single variable and α is any string of variables and terminals. A derivation begins at S, repeatedly replaces a variable using some rule, and terminates when no variables remain. The language of the grammar is the set of all terminal strings reachable this way. Notice that derivations can be arbitrarily long — this is where the expressive power comes from.

The name "context-free" refers to the rule form: the left side is always a single variable, with no surrounding context constraining when the rule can fire. This is in contrast to context-sensitive grammars, where a rule A → B might only apply when A appears between specific symbols. Context-free rules are simple but powerful enough to capture nested structure, which is exactly what programming languages require — parentheses must balance, if-else blocks must be properly nested, function calls must close with matching arguments.

A crucial concept is ambiguity. A string w is ambiguous in grammar G if G admits two or more distinct parse trees for w. This is not just a theoretical curiosity: an ambiguous grammar for a programming language means a statement like 1 + 2 * 3 could be parsed as (1 + 2) * 3 or 1 + (2 * 3), giving different results. Grammar designers go to considerable effort to eliminate ambiguity, often by introducing operator precedence rules directly into the grammar structure.

CFGs sit in the middle of the Chomsky hierarchy: strictly more powerful than regular languages (they can express { aⁿbⁿ }), but strictly less powerful than context-sensitive and Turing-complete grammars (they cannot express { aⁿbⁿcⁿ }). The decision problem for CFLs — membership testing — is solvable in polynomial time (CYK algorithm runs in O(n³)), which makes CFGs practical for real compilers. Every time a compiler parses your source code, it is essentially running a CFL recognition algorithm on a carefully designed CFG.
