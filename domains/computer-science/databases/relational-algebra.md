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
- id: set-operations-and-notation
  type: soft
- id: set-fundamentals
  type: soft
- id: relations-properties-and-types
  type: soft
- id: set-operations-union-intersection-complement
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

## Explainer

From the relational model, you already know that a database stores data as relations — tables where each row is a tuple and each column is an attribute. Relational algebra gives you a formal language for asking questions of those relations. Every operator takes one or two relations as input and produces a new relation as output. This **closure property** is what makes the algebra compositional: you can chain operators together, feeding the output of one into the input of another, building arbitrarily complex queries from simple pieces.

The two most fundamental operators are **selection** (σ) and **projection** (π). Selection filters rows: σ_{age > 30}(Employees) returns a new relation containing only the employees older than 30. Projection filters columns: π_{name, salary}(Employees) returns a relation with just the name and salary attributes. If you know SQL, selection corresponds to WHERE and projection corresponds to the column list in SELECT. But there is a critical difference: in relational algebra, projection eliminates duplicate rows automatically because the result is a set, whereas SQL's SELECT preserves duplicates unless you write DISTINCT.

The remaining core operators handle combining relations. **Cartesian product** (×) pairs every row from one relation with every row from another — if you have 100 employees and 50 departments, the product has 5,000 rows. This is rarely useful on its own, but combined with selection it becomes a **join**: σ_{Employees.dept_id = Departments.id}(Employees × Departments) gives you employees matched to their departments. The **natural join** (⋈) is a shorthand that automatically matches on shared attribute names and removes the duplicate column. **Union** (∪) and **set difference** (−) combine or subtract relations with identical schemas, just as they do in set theory.

The real power of relational algebra lies not in writing queries — SQL is far more convenient for that — but in **query optimization**. Because the algebra defines precise equivalence rules, the database optimizer can transform your query into a more efficient form that produces identical results. The most important rule is **pushing selections down**: applying filters as early as possible to reduce the number of rows flowing through expensive operations like joins. For example, joining two million-row tables and then filtering is far slower than filtering each table first and then joining the smaller results. The optimizer proves these two expressions are equivalent using relational algebra, then chooses the cheaper execution path. Every time you write a SQL query, the database translates it into relational algebra, applies these rewrite rules, and executes the optimized version.
