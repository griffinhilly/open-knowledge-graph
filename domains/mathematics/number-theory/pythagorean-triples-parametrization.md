---
id: pythagorean-triples-parametrization
title: Pythagorean Triples and Their Parametrization
domain: mathematics
course: number-theory
prerequisites:
- id: sum-of-two-squares-theorem
  type: soft
builds-toward:
- fermat-last-theorem-overview
tags:
- pythagorean-triples
- parametrization
- diophantine
stage: advanced
status: draft
---

# Pythagorean Triples and Their Parametrization

## Core Idea
A Pythagorean triple (a, b, c) satisfies a² + b² = c². All primitive Pythagorean triples are parametrized by a = m² − n², b = 2mn, c = m² + n² for coprime m > n > 0 of opposite parity. This parametrization connects geometry to number-theoretic structure and is completely constructive.

## How It's Best Learned
Derive the parametrization geometrically by intersecting lines through (−1, 0) with the unit circle x² + y² = 1. Verify that it generates all primitive triples and understand how multiples produce non-primitive ones.

## Common Misconceptions
The parametrization generates primitive triples, not all Pythagorean triples; multiples of primitives give others. The conditions on m and n (coprime, opposite parity) are essential; without them, the parametrization either misses triples or generates non-primitives.
