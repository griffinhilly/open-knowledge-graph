---
id: regular-expressions-formal
title: Regular Expressions (Formal Language Theory)
domain: computer-science
course: theory-of-computation
prerequisites:
- id: finite-state-machines
  type: hard
- id: boolean-algebra
  type: soft
builds-toward:
- kleene-theorem
- regular-language-properties
- closure-properties-regular
tags:
- regular-expressions
- formal-languages
- regular
- kleene-star
stage: advanced
status: validated
---

# Regular Expressions (Formal Language Theory)

## Core Idea
In formal language theory, a regular expression is built from atomic expressions (∅, ε, and single symbols) using three operations: union (R₁ ∪ R₂), concatenation (R₁R₂), and Kleene star (R*). The language denoted by a regular expression is the set of strings it describes. Formal regular expressions differ from the regex syntax used in programming (which adds many shorthand features) but describe the same class of languages. Every regular expression can be converted to an NFA (Thompson's construction), and vice versa.

## How It's Best Learned
Practice writing regular expressions for specific languages, then convert them to NFAs using Thompson's construction. Distinguish carefully between union, concatenation, and star — most errors stem from operator precedence (star > concatenation > union).

## Common Misconceptions
- Conflating formal regular expressions with PCRE/regex syntax in programming languages — they are related but not identical.
- Misapplying operator precedence: R₁R₂* means R₁ followed by any number of R₂, not (R₁R₂)*.
- Assuming regular expressions can describe any pattern — languages like {aⁿbⁿ} are not regular.

## Explainer

You already understand finite state machines — devices with a fixed number of states that read input one symbol at a time and either accept or reject. **Regular expressions** are a completely different notation for describing the same class of languages, using algebraic syntax instead of state diagrams. The connection is deep: every pattern you can describe with a regular expression corresponds to some finite automaton, and every language a finite automaton accepts can be written as a regular expression.

A regular expression is built from just three atomic pieces and three operations. The atoms are: ∅ (the empty language — no strings at all), ε (the language containing only the empty string), and individual symbols from the alphabet (like *a* or *b*, each denoting the language containing just that one-character string). The operations combine these atoms into larger expressions. **Union** (R₁ ∪ R₂) means "strings matching R₁ or R₂." **Concatenation** (R₁R₂) means "a string from R₁ followed by a string from R₂." **Kleene star** (R*) means "zero or more strings from R concatenated together." From these primitives, you can build up descriptions of surprisingly complex languages — for instance, (0 ∪ 1)*0 describes all binary strings ending in 0.

Operator precedence matters and is a common source of errors. Star binds tightest, then concatenation, then union — just as exponentiation binds tighter than multiplication, which binds tighter than addition. So *ab** means *a* followed by zero or more *b*'s, not zero or more repetitions of *ab*. For the latter, you need parentheses: (ab)*. Getting this wrong is the regular expression equivalent of misreading 2 + 3 × 4 as (2 + 3) × 4.

The formal regular expressions you study in theory of computation are deliberately minimal — just union, concatenation, and star. The regex engines in programming languages (grep, Python's `re`, PCRE) add many conveniences: character classes like `[a-z]`, quantifiers like `+` and `?`, backreferences, lookahead, and more. Some of these additions (like backreferences) actually go beyond regular languages, allowing the engine to match patterns that no finite automaton can recognize. The formal definition matters precisely because it draws a clean boundary: these three operations, and nothing more, characterize the regular languages. This boundary is what the Kleene theorem makes precise, connecting regular expressions, NFAs, and DFAs into a single equivalence.
