---
id: clausal-form-conversion
title: Conversion to Clausal Form
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: normal-forms-cnf-dnf
  type: hard
- id: prenex-normal-form
  type: hard
- id: skolemization-and-witnesses
  type: hard
builds-toward:
- ground-instances-and-instantiation
tags:
- first-order-logic
- normal-forms
- automated-reasoning
stage: formal-systems
status: draft
---

# Conversion to Clausal Form

## Core Idea
Any first-order formula can be converted to clausal form (a conjunction of disjunctions of literals), which is the canonical input format for resolution-based theorem provers. The conversion process involves converting to prenex normal form, Skolemization, and distribution of conjunction over disjunction—understanding this process is essential for using automated reasoning tools.
