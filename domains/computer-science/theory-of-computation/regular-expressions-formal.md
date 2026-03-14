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
