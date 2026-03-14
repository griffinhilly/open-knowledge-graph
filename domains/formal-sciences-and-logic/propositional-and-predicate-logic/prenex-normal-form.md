---
id: prenex-normal-form
title: Prenex Normal Form
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: quantifier-scope-ambiguity
  type: soft
builds-toward:
- skolemization-and-witnesses
tags:
- first-order-logic
- normal-forms
- quantifiers
stage: formal-systems
status: draft
---

# Prenex Normal Form

## Core Idea
A first-order formula is in prenex normal form (PNF) if all quantifiers are pulled to the front, followed by a quantifier-free body. Every first-order formula can be converted to an equivalent one in PNF, making PNF a canonical form that simplifies reasoning about quantified formulas and is essential for automated reasoning techniques.
