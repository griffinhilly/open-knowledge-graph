---
id: pessimistic-concurrency-control
title: 'Pessimistic Concurrency Control: Locking'
domain: computer-science
course: databases
prerequisites:
- id: lost-update-problem
  type: hard
- id: optimistic-concurrency-control
  type: soft
tags:
- concurrency
- locking
- locks
stage: formal-systems
status: validated
---
# Pessimistic Concurrency Control: Locking

## Core Idea
Pessimistic concurrency control acquires locks on rows before reading or modifying them. Locks are held until commit, ensuring no other transaction can interfere.

## How It's Best Learned
Use SELECT...FOR UPDATE to lock rows, observe how other sessions block, and commit to release locks.

## Common Misconceptions
Locks are held until COMMIT, not after the UPDATE statement finishes. Deadlocks can occur if two transactions lock resources in different orders.

## Questions

```yaml
- question: "Transaction A executes UPDATE orders SET status='shipped' WHERE id=1, then continues running other operations. Transaction B tries to read row id=1. Which statement is correct?"
  type: multiple-choice
  options:
    - "Transaction B can read the row because Transaction A's UPDATE statement has already completed"
    - "Transaction B must wait because Transaction A still holds the exclusive lock on that row until it commits or rolls back"
    - "Transaction B can proceed using a shared lock since it is only reading, not modifying"
    - "Transaction B's wait will automatically time out when the UPDATE statement finishes"
  answer: 1
  explanation: "Under pessimistic concurrency control and two-phase locking, a lock acquired during a transaction is held until COMMIT or ROLLBACK — not released when the individual statement finishes. Transaction A's UPDATE acquired an exclusive lock on row id=1; that lock persists for the entire duration of Transaction A, regardless of how many more operations follow. Transaction B must wait for Transaction A to commit or abort. This is the most common misconception: conflating 'statement complete' with 'lock released.'"

- question: "Transaction A locks row X then waits for row Y. Transaction B locks row Y then waits for row X. What will the database do?"
  type: multiple-choice
  options:
    - "Both transactions will eventually proceed once the database serializes their lock requests"
    - "A deadlock will be detected; the database will abort one transaction to break the cycle so the other can proceed"
    - "Both transactions will wait indefinitely until an administrator manually kills one"
    - "The second lock request in each transaction will immediately fail with a lock-not-available error"
  answer: 1
  explanation: "This is a classic deadlock: each transaction holds a resource the other needs, and neither can proceed. Databases handle deadlocks through automatic detection — periodically checking for cycles in the wait-for graph — and resolution by aborting one transaction (typically the one with the least work or lowest cost to retry). The aborted transaction receives an error and can be retried. This is not an administrator task; the database engine handles it automatically. Preventing deadlocks in application code requires acquiring locks in a consistent order."

- question: "Pessimistic concurrency control is called 'pessimistic' because it acquires locks upfront, assuming conflicts are likely, rather than checking for conflicts at commit time."
  type: true-false
  answer: true
  explanation: "Correct. The 'pessimistic' label reflects the assumption that another transaction might interfere — so you prevent interference by locking before you read or write. The contrasting approach, optimistic concurrency control, assumes conflicts are rare: it allows transactions to proceed without locks and only checks at commit time whether any conflict actually occurred. Pessimistic is safer for high-contention workloads; optimistic is better when conflicts are infrequent."

- question: "A shared (read) lock prevents other transactions from reading the same row simultaneously."
  type: true-false
  answer: false
  explanation: "Shared locks allow concurrent reads — multiple transactions can hold shared locks on the same row at the same time without blocking each other. Reads do not conflict with reads. A shared lock only blocks *exclusive locks* (writes): a transaction trying to modify a row that others are reading must wait for the readers to release their shared locks. This is why read-heavy workloads can achieve significant concurrency even under pessimistic locking."

- question: "Why can a long-running transaction significantly reduce database throughput even if it never actually conflicts with other transactions?"
  type: short-answer
  answer: "Under two-phase locking, any lock acquired during a transaction is held until commit or abort — even if the locked row is never touched again. A transaction that acquires a lock early and runs for minutes holds that lock the entire time, blocking every other transaction that needs the same row, whether or not an actual conflict would occur."
  explanation: "This is the fundamental cost of pessimistic concurrency control: locking is conservative. The system doesn't know whether a conflict will occur, so it prevents all potential conflicts. The result is that long transactions act as bottlenecks, serializing access to locked resources even during periods when no concurrent modification is happening. Keeping transactions short is the standard mitigation."
```

## Explainer

When multiple transactions access the same data concurrently, things can go wrong — you already saw this with the **lost update problem**, where two transactions read and write the same row and one silently overwrites the other's changes. Pessimistic concurrency control is the straightforward solution: before you touch a row, you lock it. While you hold the lock, nobody else can modify that row. It is called "pessimistic" because it assumes conflicts are likely and prevents them upfront, rather than detecting them after the fact.

In practice, most relational databases implement this through **shared locks** and **exclusive locks**. A shared lock (read lock) allows multiple transactions to read the same row simultaneously — reads do not conflict with each other. An exclusive lock (write lock) gives one transaction sole access to a row for modification, blocking both readers and writers. When you execute `SELECT ... FOR UPDATE`, you are explicitly requesting an exclusive lock on the returned rows. Other transactions that try to read or modify those same rows will block — they wait, paused, until you commit or roll back and release your locks.

The critical detail is *when* locks are released. Under the standard **two-phase locking** protocol, a transaction acquires all the locks it needs (the growing phase) and releases them only at commit or abort (the shrinking phase). This means a lock acquired early in a long transaction is held for the entire duration, even if the row is not touched again. This guarantees serializability — the result is equivalent to running transactions one at a time — but it also means long transactions can block other work for extended periods.

The main danger of pessimistic locking is **deadlock**: transaction A locks row 1 and waits for row 2, while transaction B locks row 2 and waits for row 1. Neither can proceed. Databases handle this with deadlock detection — periodically checking for cycles in the wait graph and aborting one transaction to break the cycle. You can minimize deadlocks by always acquiring locks in a consistent order (e.g., by primary key) and keeping transactions as short as possible. The tradeoff is clear: pessimistic control gives you strong correctness guarantees at the cost of reduced concurrency and the risk of blocking. For workloads where conflicts are frequent and correctness is paramount — such as financial transfers or inventory updates — that tradeoff is well worth it.
