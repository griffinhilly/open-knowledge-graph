---
id: saga-pattern-distributed-transactions
title: Saga Pattern for Long-Running Distributed Transactions
domain: computer-science
course: distributed-systems
prerequisites:
- id: two-phase-commit-protocol
  type: hard
builds-toward:
- distributed-lock-management
tags:
- transactions
- saga
- long-running
- consistency
stage: concrete-techniques
status: draft
---

# Saga Pattern for Long-Running Distributed Transactions

## Core Idea
Sagas are long-running transactions split into a sequence of local transactions, each with a compensating transaction for rollback. If any step fails, compensations run in reverse order. Sagas avoid blocking (unlike 2PC) but must handle partial failures and idempotence carefully.

## How It's Best Learned
Model a travel booking saga: reserve hotel, reserve flight, reserve car. Write compensations: cancel hotel, cancel flight, cancel car. Then trace through a failure (flight reservation fails) and verify the rollback is correct and can be retried safely.

## Common Misconceptions
- Sagas provide ACID guarantees like 2PC; they provide eventual consistency and require application logic to handle compensations.
- Saga compensations are always available; a failing compensation can leave the system in an inconsistent state requiring manual intervention.
