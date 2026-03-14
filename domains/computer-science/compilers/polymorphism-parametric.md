---
id: polymorphism-parametric
title: Parametric Polymorphism
domain: computer-science
course: compilers
prerequisites:
- id: hindley-milner-type-system
  type: hard
builds-toward:
- generics-and-specialization
tags:
- polymorphism
- generics
- type-parameters
stage: advanced
status: draft
---

# Parametric Polymorphism

## Core Idea
Parametric polymorphism allows functions and data types to be generic over type variables. A polymorphic function like `length: ∀α. [α] → int` works on lists of any element type, and a single compiled function serves all instantiations (via code generation or runtime dispatch). This contrasts with ad-hoc polymorphism (overloading), where different code handles different types.
