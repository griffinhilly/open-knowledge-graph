---
id: dirty-read-anomaly
title: 'Dirty Read Anomaly: Reading Uncommitted Changes'
domain: computer-science
course: databases
prerequisites:
- id: isolation-level-read-uncommitted
  type: hard
tags:
- concurrency
- anomalies
- isolation-problems
stage: formal-systems
status: validated
---

# Dirty Read Anomaly: Reading Uncommitted Changes

## Core Idea
A dirty read occurs when a transaction reads data written by another uncommitted transaction. If the writing transaction rolls back, the reading transaction has consumed invalid data.

## Questions

```yaml
- question: "Transaction A debits $200 from an account (balance drops from $500 to $300) but has not yet committed. Transaction B reads the balance, sees $300, and approves a $250 withdrawal. Transaction A then rolls back. What is the core problem?"
  type: multiple-choice
  options:
    - "Transaction B has acted on data that never existed in any committed state — the 'true' balance was always $500, and B's decision was based on a phantom value"
    - "Transaction A's rollback is invalid because Transaction B already observed its changes"
    - "There is no real problem — rollbacks always restore committed state correctly regardless of what other transactions observed"
    - "The issue is that B should have used SELECT FOR UPDATE to lock the row first"
  answer: 0
  explanation: "The dirty read problem is that B consumed uncommitted, provisional data. From the database's committed perspective, the balance was $500 the entire time A was running — A's debit was tentative. When A rolled back, committed state was restored correctly, but B has already made a decision (approving a $250 withdrawal) based on a value ($300) that never validly existed. Option C misses the point: the database state is fine, but B's external action or further writes cannot be undone."

- question: "Why does the Read Uncommitted isolation level exist in databases, despite allowing dirty reads?"
  type: multiple-choice
  options:
    - "It is a historical artifact that modern databases have deprecated in favor of safer alternatives"
    - "It prevents phantom reads while permitting dirty reads, making it appropriate for financial applications"
    - "It offers better performance by skipping locking and versioning overhead, making it acceptable for approximate queries where exact correctness is not required"
    - "It is required by distributed databases that cannot coordinate transaction commits across nodes"
  answer: 2
  explanation: "Read Uncommitted exists for performance-sensitive scenarios where approximate results are acceptable — dashboards showing rough row counts, analytics that can tolerate slightly stale or provisional data, or debugging queries. By skipping shared read locks or MVCC versioning, reads complete faster. The isolation level is not deprecated; it's simply dangerous for any logic that requires correctness. Option B is wrong — phantom reads are a different anomaly prevented by higher isolation levels."

- question: "A dirty read can only cause problems if the reading transaction itself also writes data based on what it read."
  type: true-false
  answer: false
  explanation: "Even a purely read-only transaction is harmed by dirty reads. If Transaction B generates a bank statement based on an uncommitted balance, the statement is wrong regardless of whether B writes anything. The problem is that B's *output* (report, decision, response to a user) was based on data that never entered committed state. Dirty reads corrupt any downstream artifact, not just further database writes."

- question: "If Transaction A rolls back after Transaction B has read its uncommitted changes, the database's committed state is correctly restored, but Transaction B may have made decisions or produced output based on data that never existed in any committed form."
  type: true-false
  answer: true
  explanation: "This precisely captures the dirty read problem. The database recovers correctly — committed state is intact. But Transaction B has consumed a 'dirty' (uncommitted, provisional) value. Any logic, output, or further actions B took based on that value are based on a phantom. The rollback fixes the database; it cannot fix what B already did with the data it read."

- question: "Why is the term 'dirty' used for dirty reads? What specific characteristic of the read makes it dangerous?"
  type: short-answer
  answer: "A 'dirty' write is one that is uncommitted and provisional — it may or may not survive. Reading dirty data means reading changes that have not passed the point of no return. The danger is that the writing transaction might roll back, erasing the data the reading transaction observed. The reader then has acted on a value that never validly existed in the committed state of the database. Unlike a committed read (which reflects a stable, permanent fact), a dirty read reflects a tentative fact that may vanish."
  explanation: "The 'dirty' metaphor contrasts with 'clean' (committed) writes. Committed data is clean because it has been durably validated; uncommitted data is dirty because it is still in flux. The specific danger is the possibility of rollback: the writer may undo everything, leaving the reader having consumed a ghost value. This cannot happen with committed reads because committed writes, by definition, are permanent."
```

## Explainer

You understand from studying the Read Uncommitted isolation level that it allows a transaction to see changes made by other transactions before those transactions commit. A **dirty read** is the specific anomaly this creates — and understanding why it's dangerous requires tracing through what happens when things go wrong.

Consider a banking scenario. Transaction A transfers $500 from Account X (balance: $1000) to Account Y, first debiting X to $500. Before A commits, Transaction B reads Account X's balance and sees $500. Now suppose Transaction A encounters an error and rolls back — Account X returns to $1000. But Transaction B has already acted on the $500 figure. If B was generating a bank statement, it shows the wrong balance. If B was checking whether to approve a loan, it made its decision on data that never actually existed in any committed state of the database. This is the core problem: B read **uncommitted, tentative data** that the database later erased.

The term "dirty" comes from the idea that uncommitted writes are "dirty" — they are provisional changes that may or may not become permanent. A committed write is "clean" because it has passed the point of no return. When you allow dirty reads, you're letting transactions base their logic on data that might vanish. The danger isn't just seeing a wrong number once; it's that the reading transaction might make further writes or decisions based on that phantom value, propagating the error outward in ways that are hard to trace.

Dirty reads are prevented by requiring transactions to only see **committed** data — which is exactly what the Read Committed isolation level guarantees, typically by using shared locks on reads or maintaining separate committed and uncommitted versions of each row. The reason Read Uncommitted exists at all, despite this risk, is performance: skipping the locking or versioning overhead makes reads faster. In practice, it's only safe for approximate queries where exact correctness doesn't matter — things like rough row counts or dashboard estimates where being slightly wrong is acceptable. For anything involving business logic, financial calculations, or data integrity, dirty reads are unacceptable.
