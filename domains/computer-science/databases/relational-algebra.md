---
id: relational-algebra
title: Relational Algebra
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
- id: set-theory-basics
  type: soft
- id: set-operations
  type: soft
builds-toward:
- sql-select-basics
- query-execution-plans
- query-optimization
tags:
- relational algebra
- projection
- selection
- join
- formal query language
stage: formal-systems
status: validated
---

# Relational Algebra

## Core Idea
Relational algebra is the formal mathematical language underlying relational databases, defining a closed set of operators that take relations as input and produce new relations as output. Core operators include selection (σ, filtering rows by condition), projection (π, choosing columns), union (∪), set difference (−), Cartesian product (×), and natural join (⋈). Every SQL query can be expressed as a relational algebra expression, making it the formal basis for query equivalence proofs and optimizer rewrites. The algebra is compositional — operators can be nested arbitrarily.

## How It's Best Learned
Map SQL queries you already know to their relational algebra equivalents. Work through equivalence rules (e.g., pushing selections before joins to reduce intermediate sizes) to understand why optimizers rewrite queries.

## Common Misconceptions
- The natural join eliminates duplicate columns and only joins on identically named attributes, unlike Cartesian product which creates all combinations.
- Projection in relational algebra returns a set (no duplicates), whereas SQL's SELECT returns a bag by default unless DISTINCT is specified.
