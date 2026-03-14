---
id: kleene-recursion-theorem
title: Kleene's Recursion Theorem and Self-Reference
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: general-recursive-functions
  type: hard
- id: computability-reductions
  type: hard
tags:
- self-reference
- recursion
- fixed-points
stage: advanced
status: draft
---

# Kleene's Recursion Theorem and Self-Reference

## Core Idea
Kleene's recursion theorem states that for any computable function φ, there exists an index e such that φ_e = φ(e), where φ_e is the partial computable function with index e. This powerful result allows Turing machines to obtain their own descriptions, enabling paradox-free self-reference and fixed-point constructions. It underlies quines and demonstrates intrinsic limitations of formal systems.
