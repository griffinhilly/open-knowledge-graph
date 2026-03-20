---
id: regular-expressions-and-languages
title: Regular Expressions and Languages
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: nondeterministic-finite-automata-formal
  type: hard
builds-toward:
- context-free-grammars-formal
tags:
- regular-languages
- automata
- formal-languages
stage: advanced
status: draft
---

# Regular Expressions and Languages

## Core Idea
Regular expressions are a compact algebraic notation for describing regular languages using concatenation, union, and Kleene star. Kleene's theorem establishes that the languages described by regular expressions are exactly those recognized by finite automata — every regex can be converted to an NFA, and every DFA can be converted to a regex. The pumping lemma for regular languages provides a tool for proving that certain languages (e.g., {a^n b^n}) are not regular, by showing that sufficiently long strings in the language must contain a pumpable substring.

## How It's Best Learned
Practice converting between the three representations: regex to NFA (Thompson's construction), NFA to DFA (subset construction), and DFA to regex (state elimination). Then use the pumping lemma to prove specific languages are not regular — this sharpens understanding of what finite memory cannot achieve.

## Common Misconceptions
- The "regular expressions" in programming languages (Perl, Python, etc.) include backreferences and lookaheads that go beyond the formal definition and can match some non-regular languages.
- The pumping lemma is a necessary condition for regularity, not sufficient — satisfying it does not prove a language is regular.

## Explainer

You have studied nondeterministic finite automata (NFAs), so you know what a regular language is: a language accepted by some finite automaton, deterministic or nondeterministic. **Regular expressions** give you a completely different notation for exactly the same class of languages — an algebraic description rather than a machine description. Kleene's theorem, the central result here, says these two descriptions are interchangeable.

The syntax of regular expressions builds languages from three operations. **Concatenation** (AB) means "a string from A followed by a string from B." **Union** (A|B) means "a string from A or from B." **Kleene star** (A*) means "zero or more strings from A concatenated together." Starting from single-character base cases (and ∅ and ε), these three operations generate exactly the regular languages. So the expression `a(b|c)*` describes strings starting with 'a' followed by any sequence of 'b's and 'c's — a language you could also describe with a small NFA.

**Kleene's theorem** formalizes the equivalence. Every regular expression can be converted to an NFA (Thompson's construction builds the NFA inductively over the expression's structure, introducing ε-transitions to combine pieces), and every DFA can be converted back to a regular expression (state elimination removes states one by one, accumulating transitions into regular expression labels). This triangle of conversions — regex ↔ NFA ↔ DFA — means you can choose whichever representation is most convenient: regex for compact human-readable descriptions, NFA for theoretical reasoning about closure properties, DFA for efficient simulation.

The **pumping lemma** gives you a way to prove that certain languages are *not* regular. The key insight is that any finite automaton has a fixed number of states. If a string is long enough to exceed that count, the automaton must repeat a state while reading it — creating a "loop" in the computation. This loop can be pumped (iterated any number of times) while keeping the result in the same language, because the automaton follows the same path each time around the loop. If a language lacks this pumpable-substring property for sufficiently long strings, no finite automaton can recognize it. The classic example is {a^n b^n : n ≥ 0} — matching that n a's are followed by n b's requires memory that grows with n, which no finite automaton provides. The pumping lemma is a *necessary* condition for regularity, not sufficient: it proves languages are non-regular, but satisfying it doesn't make a language regular.
