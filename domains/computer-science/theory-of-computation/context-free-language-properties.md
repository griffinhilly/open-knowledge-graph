---
id: context-free-language-properties
title: Context-Free Language Properties and Closure
domain: computer-science
course: theory-of-computation
prerequisites:
- id: closure-properties-cfl
  type: hard
- id: context-free-grammar-properties-and-ambiguity
  type: soft
builds-toward:
- pushdown-automata
tags:
- cfl
- closure-properties
- union
- concatenation
- kleene-star
stage: advanced
status: draft
---

# Context-Free Language Properties and Closure

## Core Idea
CFLs are closed under union, concatenation, and Kleene star (proven by grammar transformation). However, they are NOT closed under intersection or complementation, a key distinction from regular languages. These closure properties constrain what languages can be context-free, and non-closure is used to prove languages non-CF (e.g., {a^nb^nc^n}).
