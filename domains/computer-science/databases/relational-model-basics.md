---
id: relational-model-basics
title: The Relational Model
domain: computer-science
course: databases
prerequisites:
- id: boolean-logic-programming
  type: soft
- id: set-theory-basics
  type: soft
builds-toward:
- primary-and-foreign-keys
- relational-algebra
- sql-select-basics
tags:
- relational model
- tables
- tuples
- schema
- Codd
stage: formal-systems
status: validated
---

# The Relational Model

## Core Idea
The relational model organizes data into tables (relations), where each row is a tuple and each column is an attribute with a defined domain. Data is accessed declaratively through queries rather than by navigating pointers or paths. This model, introduced by E.F. Codd in 1970, provides a mathematical foundation for structured data storage based on set theory and predicate logic. Relationships between entities are expressed through shared attribute values rather than explicit links.

## How It's Best Learned
Start by manually designing a small table (e.g., a contacts list) and identifying what makes each row unique. Compare the relational model to spreadsheets and file-based storage to understand what it adds. Read about Codd's 12 rules for historical context.

## Common Misconceptions
- A relation is not an ordered list — rows have no inherent order in the relational model.
- NULL is not zero or empty string; it means 'unknown or missing.'
- Tables represent sets of tuples, so duplicates are theoretically forbidden (though SQL relaxes this with multisets/bags by default).

## Questions

```yaml
- question: "In the relational model, how are relationships between different entities expressed?"
  type: multiple-choice
  options: ["Through explicit pointer links between rows", "Through shared attribute values", "Through the physical order of rows in the table", "Through named relationship objects stored separately"]
  answer: 1
  explanation: "The relational model expresses relationships declaratively through shared values — a foreign key in one table matches a primary key in another. There are no stored pointers or navigation paths. This is a deliberate design choice that gives the query optimizer freedom to choose access paths."

- question: "In the relational model, the rows of a table have a defined order that is part of the table's structure."
  type: true-false
  answer: false
  explanation: "A relation is a mathematical set, and sets have no ordering. Rows in a table have no inherent order — any apparent order in query results is incidental unless you explicitly specify ORDER BY. This is one of the most practically important properties to internalize before writing SQL."

- question: "What does NULL mean in the relational model, and why does it differ from zero or an empty string?"
  type: short-answer
  answer: "NULL means 'unknown or missing' — the value either does not exist or is not recorded. Zero and empty string are actual known values. NULL participates in three-valued logic (true/false/unknown), which affects how comparisons and aggregations behave."
  explanation: "NULL = NULL evaluates to UNKNOWN in SQL, not TRUE, which catches many developers off guard. Aggregates like COUNT and SUM ignore NULLs. Understanding NULL as a sentinel for missing information (not a value) is essential for writing correct SQL queries."
```

## Explainer

Before the relational model, databases stored data in hierarchical or network structures where applications navigated explicit pointers to retrieve records — you had to know the physical path to the data. E.F. Codd's 1970 paper proposed a radically different idea: organize data into **relations** (tables of rows and columns) and let users describe *what* they want with logical predicates, leaving the database to figure out *how* to retrieve it. This declarative separation of logic from access paths is the relational model's core insight.

A **relation** is a set of **tuples** (rows), where each tuple has the same set of **attributes** (columns), and each attribute has a defined **domain** (the set of allowed values). Because a relation is a mathematical set, two fundamental properties follow: there are no duplicate tuples, and there is no inherent ordering of rows. Both of these feel counterintuitive coming from spreadsheets or arrays, but they are load-bearing. The no-order property means that SQL queries without ORDER BY can return rows in any sequence — the database is free to retrieve them however is most efficient.

Relationships between entities are expressed through **shared attribute values**, not pointers. A table of orders might contain a `customer_id` column whose values match the `id` column of a customers table. This shared value is a foreign key. The database does not store a literal pointer from an order row to its customer row — it stores a value, and the query engine figures out the join at query time. This is what gives the relational model its flexibility: you can query relationships in any direction without designing access paths in advance.

**NULL** deserves special attention. In the relational model, NULL is not a value — it is a marker meaning "unknown or missing." This produces three-valued logic: a comparison like `salary > 50000` where salary is NULL yields UNKNOWN (not FALSE), which in turn means the row is excluded from WHERE clause results. Aggregations like SUM and COUNT skip NULLs entirely. Many SQL bugs trace back to treating NULL as zero or empty string when it is actually the absence of information. Codd himself considered NULL one of the model's more controversial design choices.

The relational model provides the mathematical foundation for everything you will learn next: primary and foreign keys formalize entity identity and relationships, relational algebra gives the theoretical basis for SQL's query operations, and SQL itself is a practical language for expressing the predicates and joins that Codd's model makes possible. The model's power comes from what it *doesn't* require: no schema-baked access paths, no navigational code, just data and the logic to query it.

