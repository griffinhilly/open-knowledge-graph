---
id: model-interpretation-and-satisfaction
title: Model Interpretation and Satisfaction
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: structures-and-formal-languages
  type: hard
- id: first-order-semantics
  type: hard
builds-toward:
- elementary-equivalence-indistinguishability
- complete-first-order-theories
tags:
- semantics
- satisfaction
- truth
- Tarski
- valuation
stage: advanced
status: draft
---

# Model Interpretation and Satisfaction

## Core Idea
Satisfaction formalizes what it means for a formula to be true in a structure through recursive definition: atomic formulas are satisfied by checking the actual interpretation; logical connectives and quantifiers are evaluated inductively. A model of a set of sentences is a structure in which all sentences are satisfied. This Tarskian framework unifies logic and mathematics under a single unified notion of truth.
