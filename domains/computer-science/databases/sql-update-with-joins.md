---
id: sql-update-with-joins
title: 'UPDATE with JOINs: Conditional Updates'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-insertion-modification
  type: hard
- id: sql-joins
  type: hard
tags:
- sql
- dml
- joins
stage: formal-systems
status: validated
---

# UPDATE with JOINs: Conditional Updates

## Core Idea
UPDATE statements can reference other tables via JOINs to conditionally modify rows based on data in related tables, enabling complex data synchronization and audit logic.

## Questions

```yaml
- question: "A developer wants to sync prices from a staging table: UPDATE products SET price = price_updates.new_price FROM price_updates WHERE products.sku = price_updates.sku. What should they do before running this UPDATE?"
  type: multiple-choice
  options:
    - "Run SELECT COUNT(*) FROM price_updates to ensure there are rows to update"
    - "Run the equivalent SELECT showing which rows would be affected, to verify matches and spot any duplicate SKUs in the staging table"
    - "Run EXPLAIN on the UPDATE to check query cost"
    - "Run SELECT * FROM products to see current prices"
  answer: 1
  explanation: "The key risk with UPDATE-JOIN is updating more rows than intended if the join produces duplicate matches for a target row. Running the equivalent SELECT first shows exactly which rows would be affected and what values they would receive. If the SELECT returns the same products.sku more than once, the join conditions need tightening before running the UPDATE. EXPLAIN shows cost but not which rows would change or whether duplicates exist."

- question: "A developer familiar with MySQL writes an UPDATE-JOIN query and then runs it on a PostgreSQL server. The query fails with a syntax error. What is the most likely cause?"
  type: multiple-choice
  options:
    - "PostgreSQL does not support updating rows based on data in other tables"
    - "PostgreSQL requires a FROM clause instead of writing the JOIN directly after UPDATE"
    - "UPDATE-JOIN only works in MySQL because PostgreSQL uses triggers for this pattern"
    - "The table aliases used in MySQL syntax are not valid in PostgreSQL"
  answer: 1
  explanation: "MySQL and SQL Server allow the joined table to appear directly after UPDATE: UPDATE t1 JOIN t2 ON ... SET t1.col = t2.col. PostgreSQL uses a different syntax: UPDATE t1 SET col = t2.col FROM t2 WHERE t1.id = t2.id. The logic is identical — joining to filter and supply values — but the syntax diverges. This is a practical portability trap when switching between database systems."

- question: "Using UPDATE with a JOIN to synchronize rows from a staging table is functionally equivalent to looping through rows one at a time and running individual UPDATE statements."
  type: true-false
  answer: false
  explanation: "While both produce the same result, a single UPDATE-JOIN is far more efficient. Individual row-by-row updates incur repeated round-trips to the database, transaction overhead for each update, and query parsing costs multiplied by row count. A set-based UPDATE-JOIN lets the database engine handle the full batch in one optimized operation, using its query planner, indexes, and bulk write mechanisms. For thousands of rows, the performance difference is typically orders of magnitude."

- question: "When a JOIN in an UPDATE statement matches multiple rows in the joined table to a single row in the target table, the behavior is consistent and predictable across all major relational databases."
  type: true-false
  answer: false
  explanation: "This is one of the most dangerous aspects of UPDATE-JOIN: when duplicates exist in the joined table, the behavior is database-dependent and often undefined. Some databases apply one arbitrary matching row; others raise an error. This is exactly why you should always test the join as a SELECT first — if duplicates appear in the target table's primary key, the update's behavior is unpredictable. The fix is to tighten join conditions or pre-deduplicate the staging table."

- question: "Why is it valuable to run an UPDATE-JOIN query as a SELECT statement first, before executing the actual update?"
  type: short-answer
  answer: "Running the equivalent SELECT reveals exactly which rows would be modified and what new values they would receive. Most importantly, it exposes the case where the join produces multiple matching rows for a single target row — which would result in undefined or unintended behavior in the actual UPDATE. If the SELECT shows duplicate primary keys in the target table's rows, the join conditions must be tightened. The SELECT is a dry run that makes the update's effects visible and auditable before any data is changed."
  explanation: "The risk unique to UPDATE-JOIN is not just performance but correctness — specifically, updating wrong rows or applying wrong values due to unexpected join cardinality. A SELECT costs nothing and can save a difficult rollback or data corruption scenario."
```

## Explainer

You already know how to UPDATE rows using a WHERE clause and how JOINs combine data from multiple tables. **UPDATE with JOINs** merges these two ideas: instead of filtering rows to update based only on the target table's own columns, you can bring in data from other tables to decide which rows to change and what values to set. This is essential whenever a modification depends on a relationship — "update all orders whose customer is in California" or "set the discount column based on the product's category."

The syntax varies by database, which is a practical detail worth knowing. In MySQL and SQL Server, you write it directly: `UPDATE orders JOIN customers ON orders.customer_id = customers.id SET orders.tax_rate = 0.0725 WHERE customers.state = 'CA'`. In PostgreSQL, the syntax uses a `FROM` clause: `UPDATE orders SET tax_rate = 0.0725 FROM customers WHERE orders.customer_id = customers.id AND customers.state = 'CA'`. The logic is identical — you are joining to filter and compute — but the syntax difference catches people who switch between databases.

A powerful pattern is using a joined table not just to filter but to **supply values**. For example, suppose you have a `price_updates` staging table with new prices loaded from a vendor feed. You can write `UPDATE products SET price = price_updates.new_price FROM price_updates WHERE products.sku = price_updates.sku` — a single statement that synchronizes thousands of rows. This is far more efficient than looping through rows one at a time and is the standard pattern for bulk data synchronization.

The biggest risk with UPDATE-JOIN is accidentally updating more rows than intended. If the join produces multiple matching rows for a single target row, the behavior is database-dependent — some will apply one arbitrary match, others will error. Always test your join as a SELECT first: replace the UPDATE/SET with a SELECT that shows which rows would be affected and what values they would receive. If the SELECT returns duplicates in the target table's primary key, your join conditions need tightening before you run the actual UPDATE.
