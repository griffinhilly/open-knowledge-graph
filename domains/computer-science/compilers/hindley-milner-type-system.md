---
id: hindley-milner-type-system
title: Hindley-Milner Type System
domain: computer-science
course: compilers
prerequisites:
- id: type-inference-algorithms
  type: hard
- id: lambda-calculus-foundations
  type: hard
builds-toward:
- polymorphism-parametric
tags:
- type-inference
- polymorphism
- functional-languages
stage: advanced
status: draft
---

# Hindley-Milner Type System

## Core Idea
The Hindley-Milner (HM) type system is a polymorphic type system with implicit type inference. It assigns each expression a principal type (most general type satisfying constraints). Polymorphic functions are given rank-1 types: type variables are universally quantified at the top level. HM is used in languages like ML and Haskell; it balances expressiveness with decidable type inference.
