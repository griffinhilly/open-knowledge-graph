---
id: cardinal-comparison-and-schroeder-bernstein
title: 'Comparing Cardinalities: The Schröder-Bernstein Theorem'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: injections-surjections-and-inverse-functions
  type: hard
- id: uncountable-sets-and-the-reals
  type: soft
builds-toward:
- aleph-and-beth-hierarchy-introduction
- cardinal-arithmetic
tags:
- comparison
- order
- bijection
stage: formal-systems
status: draft
---

# Comparing Cardinalities: The Schröder-Bernstein Theorem

## Core Idea
The Schröder-Bernstein theorem states: if there exist injections f: A → B and g: B → A, then there exists a bijection between A and B. This makes cardinality a total order: for any two sets A and B, either |A| < |B|, |A| = |B|, or |A| > |B|. It avoids needing explicit bijections.
