---
id: ground-instances-and-instantiation
title: Ground Instances and Variable Instantiation
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: most-general-unifier
  type: soft
- id: clausal-form-conversion
  type: soft
builds-toward:
- counterexample-and-refutation
tags:
- first-order-logic
- instances
- substitution
stage: formal-systems
status: draft
---

# Ground Instances and Variable Instantiation

## Core Idea
An instance of a first-order formula φ is obtained by uniformly substituting terms for variables in φ. A ground instance uses only ground terms (terms with no variables), resulting in a formula with no free variables. Working with instances allows us to reduce first-order reasoning to propositional reasoning on specific instantiations.
