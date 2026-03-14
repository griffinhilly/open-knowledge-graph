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
stage: formal-systems
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
