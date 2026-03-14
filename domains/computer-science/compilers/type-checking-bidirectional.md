---
id: type-checking-bidirectional
title: Bidirectional Type Checking
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: hindley-milner-type-system
  type: soft
builds-toward:
- polymorphism-and-type-variables
tags:
- type-checking
- type-inference
stage: advanced
status: draft
---

# Bidirectional Type Checking

## Core Idea
Bidirectional type checking works in two modes: checking (verifying an expression has an expected type) and inference (discovering a term's type). This approach is more efficient than pure inference and handles more complex type systems. Many modern languages use bidirectional checking.

## How It's Best Learned
Implement a bidirectional type checker for a language with polymorphism. Compare performance and error messages with unidirectional approaches.

## Common Misconceptions
Type checking and inference are opposite processes (they are complementary modes). Bidirectional checking is only for functional languages (many imperative and systems languages use it).
