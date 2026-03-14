---
id: quadratic-congruences
title: Quadratic Congruences
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-legendre-symbol
  type: hard
- id: chinese-remainder-theorem
  type: soft
builds-toward:
- pells-equation
tags:
- quadratic-congruences
- quadratic-equations
stage: advanced
status: draft
---

# Quadratic Congruences

## Core Idea
Quadratic congruences ax^2 + bx + c ≡ 0 (mod n) reduce to a = 1 and a = prime power cases. Solutions exist iff the discriminant is a quadratic residue modulo relevant prime factors, determined via Legendre symbols and Hensel lifting.
