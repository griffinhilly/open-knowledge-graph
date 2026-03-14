---
id: overload-resolution-typing
title: Overload Resolution in Type Systems
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: ad-hoc-polymorphism-overloading
  type: hard
tags:
- type-systems
- polymorphism
- overloading
stage: advanced
status: draft
---

# Overload Resolution in Type Systems

## Core Idea
Overload resolution selects the best-matching function among multiple declarations with the same name. It uses specificity rules (int matches int better than Object), type compatibility (subtype matches supertype), and tie-breaking by definition order, enabling elegant APIs where operations feel unified despite different implementations.
