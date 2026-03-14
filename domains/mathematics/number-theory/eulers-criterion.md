---
id: eulers-criterion
title: Euler's Criterion
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-legendre-symbol
  type: hard
- id: fermats-little-theorem
  type: hard
builds-toward:
- law-quadratic-reciprocity
tags:
- eulers-criterion
- quadratic-residues
- legendre-symbol
stage: advanced
status: draft
---

# Euler's Criterion

## Core Idea
(a/p) ≡ a^((p-1)/2) (mod p). This criterion computes the Legendre symbol via modular exponentiation and reveals that quadratic residuosity is determined by the group structure of (Z/pZ)*.
