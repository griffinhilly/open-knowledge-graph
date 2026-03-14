---
id: generics-and-specialization
title: Generics and Template Specialization
domain: computer-science
course: compilers
prerequisites:
- id: polymorphism-parametric
  type: hard
tags:
- generics
- templates
- code-generation
stage: advanced
status: draft
---

# Generics and Template Specialization

## Core Idea
Generic types and functions are parameterized by type variables and must be monomorphized (specialized) to concrete types for execution. Template instantiation generates type-specific code for each use; monomorphization creates multiple copies, increasing code size but enabling optimization. Languages like C++ use templates; languages like Java use erasure (runtime type information is discarded).
