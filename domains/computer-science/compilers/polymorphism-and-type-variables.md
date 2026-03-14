---
id: polymorphism-and-type-variables
title: Polymorphism and Type Variables
domain: computer-science
course: compilers
prerequisites:
- id: type-checking-bidirectional
  type: hard
- id: hindley-milner-type-system
  type: soft
builds-toward:
- three-address-intermediate-code
tags:
- type-systems
- generics
- polymorphism
stage: advanced
status: draft
---

# Polymorphism and Type Variables

## Core Idea
Parametric polymorphism allows functions and data structures to work with multiple types. This is more general than ad-hoc polymorphism (overloading). Implementing polymorphism requires careful handling of type variables, instantiation, and specialization.

## How It's Best Learned
Implement parametric polymorphism using type variables and instantiation. Study how Java generics and C++ templates compile differently.

## Common Misconceptions
Type variables are just placeholders (they are constraints on valid operations). Polymorphism requires runtime type checking (parametric polymorphism can be fully static).
