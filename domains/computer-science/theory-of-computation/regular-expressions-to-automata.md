---
id: regular-expressions-to-automata
title: Regular Expressions and Conversion to Automata
domain: computer-science
course: theory-of-computation
prerequisites:
- id: nondeterministic-finite-automata-nfa
  type: hard
builds-toward:
- regular-languages-fundamentals
- kleene-closure-and-regular-expressions
tags:
- regular-expressions
- automata
- conversion
stage: abstract-reasoning
status: draft
---

# Regular Expressions and Conversion to Automata

## Core Idea
Regular expressions are a compact notation for specifying regular languages using operators: concatenation, alternation (union), and Kleene star. Thompson's construction converts any regular expression into an equivalent NFA, providing a systematic way to build automata from high-level descriptions.

## Explainer

You already know that a **nondeterministic finite automaton** can recognize patterns by exploring multiple possible paths through its states simultaneously. Regular expressions give you a completely different way to describe the exact same set of strings — not as a state machine, but as a concise algebraic formula. The expression `(a|b)*c` says "any number of a's or b's, followed by a c." That single line captures the same language that an NFA with multiple states and epsilon transitions would recognize. The power of regular expressions comes from three operators: **concatenation** (placing symbols in sequence), **alternation** (the `|` operator, meaning "or"), and **Kleene star** (the `*` operator, meaning "zero or more repetitions").

The deep result here is that regular expressions and NFAs are equivalent in power — every regular expression has a corresponding NFA, and vice versa. **Thompson's construction** is the algorithm that makes one direction of this equivalence concrete. It works recursively: for each basic element of the expression, you build a tiny NFA fragment, then combine fragments using rules that mirror the three operators. For concatenation, you chain two fragments end-to-end. For alternation, you add a new start state with epsilon transitions branching to both sub-NFAs. For Kleene star, you add epsilon transitions that allow looping back to the start of the fragment or skipping it entirely.

Consider the expression `a(b|c)*`. Thompson's construction would first build a single-transition NFA for `a`, then build separate NFAs for `b` and `c`, combine them with an alternation construction (a new start state branching to both via epsilon transitions), wrap that combined NFA with the Kleene star construction (adding a loop-back epsilon transition and a skip path), and finally concatenate the `a` fragment with the starred fragment. The resulting NFA may have many epsilon transitions and look more complex than one you might design by hand, but it is guaranteed to be correct — and that guarantee is what matters.

This conversion is not just a theoretical curiosity. It is the engine behind every regex library in practical programming. When you type a regular expression into a search tool or programming language, the system internally converts it into an automaton (or something equivalent) to actually match strings. Understanding Thompson's construction also sets up the reverse direction — converting NFAs back to regular expressions — which together prove that the class of **regular languages** can be characterized equivalently by machines or by algebraic expressions. This duality between operational descriptions (automata) and declarative descriptions (expressions) is a recurring theme throughout the theory of computation.
