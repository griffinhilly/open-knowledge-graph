---
id: subtyping-and-bounds
title: Subtyping and Type Bounds
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: hindley-milner-type-system
  type: soft
builds-toward:
- gradual-typing-systems
tags:
- type-systems
- subtyping
- generics
stage: advanced
status: draft
---

# Subtyping and Type Bounds

## Core Idea
Subtyping introduces a type ordering where subtypes are usable wherever supertypes are expected (Liskov substitution). Type bounds on generics (e.g., 'T extends Comparable') restrict which types can instantiate parameters, enabling safe polymorphic operations while maintaining type safety.
