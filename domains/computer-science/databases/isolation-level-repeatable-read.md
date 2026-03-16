---
id: isolation-level-repeatable-read
title: 'Isolation Level: REPEATABLE READ'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- phantom-read-anomaly
tags:
- isolation
- concurrency
- anomalies
stage: formal-systems
status: draft
---

# Isolation Level: REPEATABLE READ

## Core Idea
REPEATABLE READ prevents dirty reads and non-repeatable reads by holding read locks for the duration of the transaction, but allows phantom reads (new rows matching a WHERE clause).

## How It's Best Learned
Demonstrate that the same query in a transaction returns the same rows, even if another session inserts new matching rows.

## Explainer

You already understand that concurrency control allows multiple transactions to run simultaneously while maintaining the illusion that each runs in isolation. Different **isolation levels** make different tradeoffs between how much isolation you get and how much concurrency the system can support. **REPEATABLE READ** sits in the middle of this spectrum — it provides stronger guarantees than READ COMMITTED but weaker ones than SERIALIZABLE.

The guarantee of REPEATABLE READ is this: if your transaction reads a row, and you read that same row again later in the same transaction, you will see the same data both times. No other transaction can modify or delete that row while yours is in progress. Under READ COMMITTED, by contrast, a second read could return different values if another transaction committed a change in between — this is the **non-repeatable read** anomaly, and REPEATABLE READ eliminates it. The mechanism varies by database: some use **read locks** held for the entire transaction duration (so no one else can modify the rows you've read), while others like PostgreSQL use **snapshot isolation** (your transaction sees a consistent snapshot of the database as of when it began, so other transactions' changes are simply invisible to you).

The important limitation of REPEATABLE READ is that it does not prevent **phantom reads**. While no existing row you've read can change, a different transaction can *insert new rows* that would match your query's WHERE clause. If you run `SELECT * FROM orders WHERE customer_id = 42` twice in the same transaction, both queries return the same values for the rows they find, but the second query might return additional rows that didn't exist when the first query ran. This matters in scenarios like reporting or inventory checks where you need the set of matching rows to be stable, not just the values within individual rows. To prevent phantoms, you need SERIALIZABLE isolation, which typically adds range locks or serialization conflict detection.

In practice, REPEATABLE READ is the default isolation level in MySQL/InnoDB and a commonly chosen level in other systems. It provides a good balance: your transaction sees a consistent view of any data it has touched, which prevents most concurrency anomalies that trip up application logic, while still allowing enough concurrent access that throughput remains high. The key design question for your application is whether phantom reads matter for your use case — if you are updating individual rows based on their values, REPEATABLE READ is usually sufficient; if you are making decisions based on the entire *set* of rows matching a condition, you may need SERIALIZABLE.
