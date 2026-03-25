---
id: relational-algebra
title: Relational Algebra
domain: computer-science
course: databases
prerequisites:
- id: relational-data-model
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
- sql-data-retrieval-select
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

## Questions

```yaml
- question: "A query first joins a 1,000,000-row Employees table with a 500,000-row Transactions table, then filters for employees in department 'Engineering'. A database optimizer rewrites this to filter Employees first (returning ~5,000 rows) before performing the join. What principle justifies this rewrite?"
  type: multiple-choice
  options:
    - "Projection elimination — removing unused columns reduces data size"
    - "Pushing selection down — applying filters early reduces rows flowing into expensive operations"
    - "Natural join substitution — replacing Cartesian product with natural join avoids duplicates"
    - "Closure property — operators always return relations, enabling any reorder"
  answer: 1
  explanation: "Pushing selections (filters) as early as possible is the single most impactful query optimization rule. Joining 1,000,000 rows × 500,000 rows before filtering produces a 500-billion-row intermediate result; filtering first reduces one input to ~5,000 rows before the join. Relational algebra proves these two expressions are equivalent, so the optimizer can safely substitute the cheaper plan. The closure property (option D) enables composition but does not itself justify reordering."

- question: "A student writes π_{name}(Employees) and gets back 950 rows from a 1,000-row table. In SQL, SELECT name FROM Employees returns 1,000 rows. What explains the difference?"
  type: multiple-choice
  options:
    - "SQL projection and relational algebra projection are computed differently — SQL is slower"
    - "Relational algebra projection returns a set (no duplicates), while SQL SELECT returns a bag by default"
    - "The SQL query is incorrect; it should use DISTINCT to match relational algebra"
    - "Relational algebra projection automatically joins with a key column to count rows"
  answer: 1
  explanation: "In relational algebra, the result of any operation is a relation, which by definition is a set — duplicate rows are eliminated. SQL's SELECT preserves duplicates (it operates on bags/multisets) unless you explicitly add DISTINCT. So π_{name}(Employees) and SELECT name FROM Employees are not equivalent unless the SQL uses SELECT DISTINCT name. This is a foundational difference between the formal algebra and its SQL implementation."

- question: "The closure property of relational algebra means that operators can be arbitrarily nested and composed, feeding one operator's output into another's input."
  type: true-false
  answer: true
  explanation: "Closure is the defining feature: every operator takes relations as input and produces a relation as output. This means the result of any expression is itself a valid input to any other operator, enabling arbitrary nesting. For example, σ_{salary > 100000}(π_{name,salary,dept}(Employees)) first projects columns, then filters rows — the intermediate relation produced by π feeds directly into σ."

- question: "The natural join (⋈) between two relations produces the same result as a Cartesian product (×) when the relations share no attribute names."
  type: true-false
  answer: true
  explanation: "When two relations share no column names, there are no shared attributes to join on, so the natural join condition is vacuously satisfied for all pairs — every row from one relation matches every row from the other. The result is identical to the Cartesian product. This is a precise and often surprising consequence of the definition. The natural join's useful behavior — automatic matching and duplicate column elimination — only kicks in when shared attribute names exist."

- question: "Why does the real power of relational algebra lie in query optimization rather than query writing, and what makes 'pushing selections before joins' a valid optimization?"
  type: short-answer
  answer: "Relational algebra defines precise equivalence rules proving that different orderings of operators produce identical results. Optimizers use these rules to substitute cheaper execution plans for the user's original query. Pushing selections before joins is valid because σ_{condition}(A ⋈ B) ≡ σ_{condition}(A) ⋈ B when the condition only involves attributes from A — both expressions produce the same final relation, but the right side joins smaller intermediate tables. The equivalence is algebraically provable, making the substitution safe regardless of data values."
  explanation: "SQL is for expressing what data you want; relational algebra is the substrate for proving that different ways of getting it are equivalent. Without a formal algebra, an optimizer would have to either enumerate all possible orderings (infeasible) or trust heuristics (unreliable). The algebra provides guaranteed-correct rewrite rules, which is why it is not merely an academic formalism but an active component of every serious database system."
```

## Explainer

From the relational model, you already know that a database stores data as relations — tables where each row is a tuple and each column is an attribute. Relational algebra gives you a formal language for asking questions of those relations. Every operator takes one or two relations as input and produces a new relation as output. This **closure property** is what makes the algebra compositional: you can chain operators together, feeding the output of one into the input of another, building arbitrarily complex queries from simple pieces.

The two most fundamental operators are **selection** (σ) and **projection** (π). Selection filters rows: σ_{age > 30}(Employees) returns a new relation containing only the employees older than 30. Projection filters columns: π_{name, salary}(Employees) returns a relation with just the name and salary attributes. If you know SQL, selection corresponds to WHERE and projection corresponds to the column list in SELECT. But there is a critical difference: in relational algebra, projection eliminates duplicate rows automatically because the result is a set, whereas SQL's SELECT preserves duplicates unless you write DISTINCT.

The remaining core operators handle combining relations. **Cartesian product** (×) pairs every row from one relation with every row from another — if you have 100 employees and 50 departments, the product has 5,000 rows. This is rarely useful on its own, but combined with selection it becomes a **join**: σ_{Employees.dept_id = Departments.id}(Employees × Departments) gives you employees matched to their departments. The **natural join** (⋈) is a shorthand that automatically matches on shared attribute names and removes the duplicate column. **Union** (∪) and **set difference** (−) combine or subtract relations with identical schemas, just as they do in set theory.

The real power of relational algebra lies not in writing queries — SQL is far more convenient for that — but in **query optimization**. Because the algebra defines precise equivalence rules, the database optimizer can transform your query into a more efficient form that produces identical results. The most important rule is **pushing selections down**: applying filters as early as possible to reduce the number of rows flowing through expensive operations like joins. For example, joining two million-row tables and then filtering is far slower than filtering each table first and then joining the smaller results. The optimizer proves these two expressions are equivalent using relational algebra, then chooses the cheaper execution path. Every time you write a SQL query, the database translates it into relational algebra, applies these rewrite rules, and executes the optimized version.
