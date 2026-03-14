---
id: scope-shadowing-and-lifetime
title: Scope, Shadowing, and Variable Lifetime
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: scope-binding-resolution
  type: hard
- id: variable-names-and-conventions
  type: soft
builds-toward:
- parameter-passing-value-vs-reference
tags:
- scope
- variables
- lifetime
stage: abstract-reasoning
status: draft
---

# Scope, Shadowing, and Variable Lifetime

## Core Idea
Scope determines where a variable is accessible: local (inside a function), block (inside {…}), or global (everywhere). Shadowing occurs when a variable in inner scope hides one in outer scope. Variables exist from declaration to end of scope (lifetime).

## How It's Best Learned
Trace variable scope in code with multiple levels; deliberately shadow variables to see which one is used; print variable values to verify scope.

## Common Misconceptions
That global variables are accessible everywhere (scope rules apply); that local and global variables with the same name are the same (they're not—shadowing); that variables persist after their scope ends (they don't).
