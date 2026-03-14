---
id: multi-stage-programming
title: Multi-Stage Programming and Staged Compilation
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: code-generation
  type: hard
builds-toward:
- compiler-bootstrapping
tags:
- metaprogramming
- stages
- codegen
stage: advanced
status: draft
---

# Multi-Stage Programming and Staged Compilation

## Core Idea
Multi-stage programming separates computation into stages: stage 1 generates code as data structures, stage 2 executes the generated code. Used for compiler generators, template instantiation, and partial evaluation, it brings code-generation capabilities into the language itself.
