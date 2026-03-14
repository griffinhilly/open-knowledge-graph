---
id: polynomial-hierarchy-levels
title: The Polynomial Hierarchy Beyond NP
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: pspace-and-complexity-hierarchy
  type: hard
- id: nondeterministic-polynomial-time
  type: hard
builds-toward:
- alternation-in-turing-machines
tags:
- polynomial-hierarchy
- complexity-classes
- quantifiers
stage: advanced
status: draft
---

# The Polynomial Hierarchy Beyond NP

## Core Idea
The polynomial hierarchy (PH) is a stratification of complexity classes: Σ₁P = NP, Π₁P = co-NP, Σ₂P = NP^NP, and so on. Each level corresponds to problems with an additional layer of quantified existential or universal conditions. Unless PH collapses (all levels coincide), the hierarchy is infinite and provides a fine-grained classification of hardness beyond NP.
