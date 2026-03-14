---
id: scope-binding-resolution
title: Scope and Binding Resolution
domain: computer-science
course: compilers
prerequisites:
- id: semantic-analysis
  type: hard
- id: symbol-tables-and-scope
  type: hard
builds-toward:
- name-binding-strategies
tags:
- scoping
- name-resolution
- binding
stage: advanced
status: draft
---

# Scope and Binding Resolution

## Core Idea
Scope determines which declarations are visible at each program point. Scope resolution maps uses to declarations by walking scope hierarchies, handling shadowing, and checking access rules. Different languages have different scoping rules (static vs dynamic, lexical vs block scope).

## How It's Best Learned
Implement scope resolution for nested scopes with shadowing. Trace name lookups manually through complex scope structures.

## Common Misconceptions
Scope can always be resolved in a single pass (some languages require multiple passes or context from type inference). Symbol tables must be flat (hierarchical or chained tables handle nesting more naturally).
