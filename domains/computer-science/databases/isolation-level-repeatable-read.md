---
id: isolation-level-repeatable-read
title: 'Isolation Level: REPEATABLE READ'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
- id: isolation-level-serializable
  type: soft
builds-toward:
- phantom-read-anomaly
tags:
- isolation
- concurrency
- anomalies
stage: formal-systems
status: validated
---
# Isolation Level: REPEATABLE READ

## Core Idea
REPEATABLE READ prevents dirty reads and non-repeatable reads by holding read locks for the duration of the transaction, but allows phantom reads (new rows matching a WHERE clause).

## How It's Best Learned
Demonstrate that the same query in a transaction returns the same rows, even if another session inserts new matching rows.

## Questions

```yaml
- question: "Transaction A starts and reads all orders for customer 42, finding 3 rows. Transaction B then inserts a 4th order for customer 42 and commits. Transaction A re-runs the same SELECT query. Under REPEATABLE READ, what does Transaction A see?"
  type: multiple-choice
  options:
    - "3 rows — REPEATABLE READ prevents all changes from other transactions from being visible"
    - "4 rows — the newly inserted row can appear as a phantom read"
    - "Transaction A is blocked until Transaction B commits before it can re-query"
    - "An error — REPEATABLE READ detects the conflict and aborts Transaction A"
  answer: 1
  explanation: "This is the phantom read anomaly, which REPEATABLE READ does NOT prevent. REPEATABLE READ guarantees that rows you have already read cannot be modified or deleted by other transactions — those existing rows will look the same if you re-read them. But it does not prevent other transactions from inserting *new* rows that match your WHERE clause. Transaction A's second query may return 4 rows, with the newly inserted row appearing as a 'phantom.' To prevent phantom reads, you need SERIALIZABLE isolation, which adds range locks or serialization conflict detection. Option A describes what SERIALIZABLE provides."

- question: "REPEATABLE READ isolation prevents which of the following anomalies?"
  type: multiple-choice
  options:
    - "Dirty reads and phantom reads"
    - "Non-repeatable reads and phantom reads"
    - "Dirty reads and non-repeatable reads"
    - "Only dirty reads"
  answer: 2
  explanation: "REPEATABLE READ prevents dirty reads (reading uncommitted data from other transactions) and non-repeatable reads (re-reading the same row and getting different values because another transaction modified it). It does NOT prevent phantom reads (new rows matching your WHERE clause appearing in a subsequent query). This puts REPEATABLE READ above READ COMMITTED (which prevents dirty reads but allows non-repeatable reads) but below SERIALIZABLE (which prevents all three anomalies). Remembering the spectrum — READ UNCOMMITTED → READ COMMITTED → REPEATABLE READ → SERIALIZABLE — helps place each level's guarantees."

- question: "Under REPEATABLE READ, if Transaction A reads a row, then Transaction B modifies and commits that row, Transaction A will see the updated value on its next read of that row."
  type: true-false
  answer: false
  explanation: "This is precisely what REPEATABLE READ prevents — the non-repeatable read anomaly. Once Transaction A has read a row, REPEATABLE READ guarantees that row will look the same for the duration of Transaction A's lifetime. Other transactions cannot modify or delete that row while A is in progress (in lock-based implementations), or A simply reads from a consistent snapshot taken at its start (in snapshot-based implementations like PostgreSQL). The updated value from Transaction B is invisible to Transaction A. This predictability is the key benefit of REPEATABLE READ over READ COMMITTED."

- question: "REPEATABLE READ is sufficient to prevent phantom reads in most SQL database systems."
  type: true-false
  answer: false
  explanation: "REPEATABLE READ prevents phantom reads in some implementations (notably MySQL/InnoDB, which uses gap locks to block inserts into ranges you've queried), but this is implementation-specific, not guaranteed by the SQL standard. The SQL standard defines REPEATABLE READ as allowing phantom reads — they are only prevented at the SERIALIZABLE level. PostgreSQL's REPEATABLE READ implementation uses snapshot isolation, which happens to prevent some but not all phantom scenarios. You should not rely on phantom protection from REPEATABLE READ if your application requires it; use SERIALIZABLE to guarantee that the set of matching rows is stable across re-queries."

- question: "Explain the difference between a non-repeatable read and a phantom read, and why REPEATABLE READ prevents one but not the other."
  type: short-answer
  answer: "A non-repeatable read occurs when a transaction re-reads the same row and gets different values because another transaction modified or deleted that row in between. REPEATABLE READ prevents this by locking (or snapshotting) already-read rows. A phantom read occurs when a transaction re-runs the same query and gets additional rows that didn't exist before, because another transaction inserted new matching rows. REPEATABLE READ does not prevent phantoms because its protection covers only rows that were already read — it has no mechanism to block insertions that would match a future query."
  explanation: "The distinction matters for application design. If your transaction re-reads individual rows (e.g., checking a user's balance twice to verify consistency), REPEATABLE READ is sufficient. If your transaction re-runs a range query and needs the count or set of matching rows to be stable (e.g., verifying that no new inventory has been created before completing a purchase), you need SERIALIZABLE. The practical question is: do you care about the *values within rows* staying stable, or about the *set of rows* matching a condition staying stable? REPEATABLE READ handles the first; SERIALIZABLE handles both."
```

## Explainer

You already understand that concurrency control allows multiple transactions to run simultaneously while maintaining the illusion that each runs in isolation. Different **isolation levels** make different tradeoffs between how much isolation you get and how much concurrency the system can support. **REPEATABLE READ** sits in the middle of this spectrum — it provides stronger guarantees than READ COMMITTED but weaker ones than SERIALIZABLE.

The guarantee of REPEATABLE READ is this: if your transaction reads a row, and you read that same row again later in the same transaction, you will see the same data both times. No other transaction can modify or delete that row while yours is in progress. Under READ COMMITTED, by contrast, a second read could return different values if another transaction committed a change in between — this is the **non-repeatable read** anomaly, and REPEATABLE READ eliminates it. The mechanism varies by database: some use **read locks** held for the entire transaction duration (so no one else can modify the rows you've read), while others like PostgreSQL use **snapshot isolation** (your transaction sees a consistent snapshot of the database as of when it began, so other transactions' changes are simply invisible to you).

The important limitation of REPEATABLE READ is that it does not prevent **phantom reads**. While no existing row you've read can change, a different transaction can *insert new rows* that would match your query's WHERE clause. If you run `SELECT * FROM orders WHERE customer_id = 42` twice in the same transaction, both queries return the same values for the rows they find, but the second query might return additional rows that didn't exist when the first query ran. This matters in scenarios like reporting or inventory checks where you need the set of matching rows to be stable, not just the values within individual rows. To prevent phantoms, you need SERIALIZABLE isolation, which typically adds range locks or serialization conflict detection.

In practice, REPEATABLE READ is the default isolation level in MySQL/InnoDB and a commonly chosen level in other systems. It provides a good balance: your transaction sees a consistent view of any data it has touched, which prevents most concurrency anomalies that trip up application logic, while still allowing enough concurrent access that throughput remains high. The key design question for your application is whether phantom reads matter for your use case — if you are updating individual rows based on their values, REPEATABLE READ is usually sufficient; if you are making decisions based on the entire *set* of rows matching a condition, you may need SERIALIZABLE.
