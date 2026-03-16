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
status: draft
---

# UPDATE with JOINs: Conditional Updates

## Core Idea
UPDATE statements can reference other tables via JOINs to conditionally modify rows based on data in related tables, enabling complex data synchronization and audit logic.

## Explainer

You already know how to UPDATE rows using a WHERE clause and how JOINs combine data from multiple tables. **UPDATE with JOINs** merges these two ideas: instead of filtering rows to update based only on the target table's own columns, you can bring in data from other tables to decide which rows to change and what values to set. This is essential whenever a modification depends on a relationship — "update all orders whose customer is in California" or "set the discount column based on the product's category."

The syntax varies by database, which is a practical detail worth knowing. In MySQL and SQL Server, you write it directly: `UPDATE orders JOIN customers ON orders.customer_id = customers.id SET orders.tax_rate = 0.0725 WHERE customers.state = 'CA'`. In PostgreSQL, the syntax uses a `FROM` clause: `UPDATE orders SET tax_rate = 0.0725 FROM customers WHERE orders.customer_id = customers.id AND customers.state = 'CA'`. The logic is identical — you are joining to filter and compute — but the syntax difference catches people who switch between databases.

A powerful pattern is using a joined table not just to filter but to **supply values**. For example, suppose you have a `price_updates` staging table with new prices loaded from a vendor feed. You can write `UPDATE products SET price = price_updates.new_price FROM price_updates WHERE products.sku = price_updates.sku` — a single statement that synchronizes thousands of rows. This is far more efficient than looping through rows one at a time and is the standard pattern for bulk data synchronization.

The biggest risk with UPDATE-JOIN is accidentally updating more rows than intended. If the join produces multiple matching rows for a single target row, the behavior is database-dependent — some will apply one arbitrary match, others will error. Always test your join as a SELECT first: replace the UPDATE/SET with a SELECT that shows which rows would be affected and what values they would receive. If the SELECT returns duplicates in the target table's primary key, your join conditions need tightening before you run the actual UPDATE.
