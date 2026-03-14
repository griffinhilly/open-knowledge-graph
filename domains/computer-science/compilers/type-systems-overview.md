---
id: type-systems-overview
title: Type Systems Overview
domain: computer-science
course: compilers
prerequisites:
- id: semantic-analysis
  type: hard
- id: primitive-data-types
  type: soft
builds-toward:
- type-inference-algorithms
- hindley-milner-type-system
- polymorphism-parametric
tags:
- type-systems
- type-checking
- language-design
stage: advanced
status: draft
---

# Type Systems Overview

## Core Idea
A type system assigns types to expressions and enforces type compatibility. Static type systems check types at compile-time, preventing type errors before runtime. Strongly-typed languages reject invalid operations; weakly-typed languages attempt coercions. Type systems vary in expressiveness: simple (int, float, bool), composite (structs, classes), and advanced (generics, dependent types).
