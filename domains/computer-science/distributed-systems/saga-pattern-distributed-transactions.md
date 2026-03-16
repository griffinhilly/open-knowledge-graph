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
stage: advanced
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

## Explainer

From your study of the two-phase commit protocol, you know that 2PC provides strong atomicity guarantees — all participants commit or all abort — but at a steep cost: resources are locked for the entire duration of the transaction, and a coordinator crash can leave participants blocked indefinitely. For short-lived transactions within a single database, this tradeoff is often acceptable. But consider a travel booking that reserves a hotel, a flight, and a rental car across three independent services. If the entire workflow takes thirty seconds and any service can fail, holding locks across all three services for that duration is impractical and fragile. The **saga pattern** offers an alternative.

A saga breaks a distributed transaction into a sequence of **local transactions**, each of which commits independently against its own service. The hotel service commits the reservation locally, then the flight service commits its reservation locally, then the car service commits its reservation. There is no global coordinator holding locks across all three. Each local transaction is fully committed — its changes are visible to other users — before the next step begins. This eliminates the blocking problem that plagues 2PC.

The price of this freedom is that you lose automatic rollback. If the flight reservation fails after the hotel reservation has already committed, you cannot simply abort — the hotel reservation is already durable. Instead, each step in a saga has a corresponding **compensating transaction** that semantically undoes its effect. The hotel compensation cancels the reservation, the flight compensation cancels the flight, and so on. When a step fails, the saga executes compensations in **reverse order** for all previously completed steps. This is not a true rollback — it is a new set of forward actions that happen to reverse the business effect.

Two coordination styles exist for sagas. In **choreography**, each service publishes events when it completes its local transaction, and the next service listens for those events and begins its work. This is decentralized and loosely coupled but can become hard to trace and debug as the number of steps grows. In **orchestration**, a central saga coordinator tells each service what to do and tracks the overall progress, making the workflow explicit and easier to monitor. The orchestrator does not hold locks like a 2PC coordinator — it simply sequences the local transactions and triggers compensations on failure.

The critical design challenge in sagas is **idempotence**. Network failures can cause a compensation or a local transaction to be delivered more than once, so every step must produce the same result whether executed once or multiple times. A "cancel hotel reservation" compensation that runs twice should not fail or double-refund. Sagas also require careful thought about **isolation** — since intermediate states are visible (the hotel is reserved before the flight is confirmed), other transactions can see and act on partially completed sagas. Designing compensations that are safe, idempotent, and available under failure is the core engineering challenge, and it is why sagas provide **eventual consistency** rather than the strict atomicity of 2PC.
