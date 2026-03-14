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
