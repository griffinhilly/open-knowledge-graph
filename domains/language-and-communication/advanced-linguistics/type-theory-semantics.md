---
id: type-theory-semantics
title: Type Theory and Semantic Types
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: lambda-calculus-for-linguistics
  type: hard
- id: montague-semantics
  type: hard
tags:
- semantics
- type-theory
- formal
stage: advanced
status: draft
---

# Type Theory and Semantic Types

## Core Idea
Type theory organizes semantic values hierarchically: basic types (individuals e, truth values t) combine into complex types such as (e,t) for properties and (e,(e,t)) for two-place relations. This typing system constrains semantic composition and ensures well-formedness.

## How It's Best Learned
Build up complex types systematically from basic types for increasingly complex expressions; use type-driven parsing to resolve ambiguities and verify compositionality.

## Common Misconceptions
Types are not inherent to words but assigned relative to syntactic position and context; type-shifting operations allow flexibility when strict typing would fail.
