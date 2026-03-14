---
id: unification-algorithm
title: Unification Algorithm
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: dynamic-programming-intro
  type: soft
builds-toward:
- type-inference-algorithms
tags:
- unification
- constraint-solving
- algorithm
stage: advanced
status: draft
---

# Unification Algorithm

## Core Idea
Unification finds a substitution that makes two terms syntactically identical. In type inference, it solves type constraints by finding variable substitutions. The algorithm recursively decomposes terms and detects occurs-check violations (a variable cannot appear in a term it must equal). Unification is fundamental to type systems and logic programming.
