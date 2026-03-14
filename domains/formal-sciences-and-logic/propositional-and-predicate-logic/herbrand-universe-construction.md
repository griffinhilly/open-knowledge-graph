---
id: herbrand-universe-construction
title: Herbrand Universe and Herbrand Models
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: ground-terms-and-formulas
  type: hard
- id: model-interpretation-and-satisfaction
  type: hard
builds-toward:
- skolemization-and-equisatisfiability
- resolution-fol
tags:
- first-order-logic
- model-theory
- herbrand
- decidability
stage: formal-systems
status: draft
---

# Herbrand Universe and Herbrand Models

## Core Idea
The Herbrand universe of a language is the set of all ground terms constructible from the language's constants and function symbols. A Herbrand model is an interpretation where the domain is the Herbrand universe and function symbols are interpreted as themselves. Herbrand's key insight is that for checking satisfiability of a formula in first-order logic, it suffices to consider only Herbrand models. This enables mechanization: instead of quantifying over all possible interpretations, we work with the concrete, effectively computable Herbrand universe.

## How It's Best Learned
Build the Herbrand universe step-by-step for a language with constants and function symbols. Show how interpretations map predicates to sets of ground atoms. Verify a formula in a Herbrand model by checking its ground instances. Connect to resolution methods, which work implicitly with Herbrand models.

## Common Misconceptions
- Thinking the Herbrand universe is always finite (it's infinite if there are function symbols of arity > 0).
- Confusing the domain (ground terms) with the interpretation of predicates (which are sets of tuples of ground terms).
- Assuming every formula has a Herbrand model (unsatisfiable formulas have no models, Herbrand or otherwise).
