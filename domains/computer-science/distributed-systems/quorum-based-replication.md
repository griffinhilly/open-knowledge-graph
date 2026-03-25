---
id: quorum-based-replication
title: Quorum-Based Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: replication-strategies-analysis
  type: soft
- id: state-machine-replication
  type: soft
- id: multi-master-replication
  type: soft
builds-toward:
- distributed-hash-tables
tags:
- quorum
- replication
- majority
stage: advanced
status: validated
---
# Quorum-Based Replication

## Core Idea
Quorum-based replication requires writes to be acknowledged by a quorum (majority) of replicas and reads to contact a quorum, ensuring read and write quorums always overlap. This decentralizes replication without a single primary and tolerates minority failures. Trade-off: reads and writes are slower since they must contact multiple replicas.

## Questions

```yaml
- question: "A system has N=5 replicas with write quorum W=3 and read quorum R=3. A client reads from 3 replicas. Can it be guaranteed that at least one of those replicas has the most recently written value?"
  type: multiple-choice
  options:
    - "No — it depends on which 3 replicas are contacted; if none of the 3 that acknowledged the write are in the read set, the latest value is missed"
    - "Yes — because W+R=6 > N=5, any set of 3 read replicas must overlap with any set of 3 write replicas by the pigeonhole principle"
    - "Only if the system uses a leader that tracks which replicas are up to date"
    - "Only if all 5 replicas are available; if any replica is down the guarantee fails"
  answer: 1
  explanation: "This is the mathematical core of quorum systems. If W+R > N, then the write set (W replicas) and any read set (R replicas) together account for more than N total slots. Since there are only N replicas, the two sets must share at least one member. That shared member has seen the latest write. With W=3, R=3, N=5: 3+3=6 > 5, so at least one replica in any read quorum of 3 also received the latest write quorum of 3. This is a guarantee for *any* choice of 3 read replicas — not just a lucky one."

- question: "A designer sets W=1 and R=N for an N-replica system. What is the effect on read and write performance, and is this less reliable than a majority quorum?"
  type: multiple-choice
  options:
    - "Writes become faster, reads become slower, and the system is less reliable because only one copy holds the latest data"
    - "Writes are very fast (only one acknowledgment needed), reads are slow (must contact all replicas), but consistency is still guaranteed as long as W+R > N"
    - "This configuration violates W+R > N, so it is invalid and provides no consistency guarantee"
    - "Both reads and writes are slower because contacting all replicas for reads adds latency that offsets write gains"
  answer: 1
  explanation: "W=1, R=N: 1+N = N+1 > N, so W+R > N is satisfied. Every write is acknowledged by just one replica (fast writes), but every read must contact all N replicas (slow reads) — and the highest-version response is the latest write. This is a legitimate configuration with its own tradeoff profile. It is not less reliable in terms of correctness, but it is less available for reads during failures: if any replica is down, R=N cannot be satisfied. Reliability and performance tradeoffs come from where you set W and R, not from violating the quorum invariant."

- question: "Meeting the quorum invariant W+R > N guarantees that a read will always return the most recently written value without any additional protocol mechanisms."
  type: true-false
  answer: false
  explanation: "The quorum invariant guarantees that at least one replica in the read set *has* the latest value — but it does not automatically return it to the client. If the client simply takes the first response, a slow replica might reply with stale data first. Version numbers, timestamps, or vector clocks must be attached to each response so the client can identify which is freshest. Some systems also use read repair: on discovering stale replicas in the quorum, the latest value is pushed back to them. The quorum overlap is the mathematical prerequisite; the protocol on top determines whether that freshness guarantee is actually realized."

- question: "In quorum-based replication, increasing the write quorum W always improves read performance."
  type: true-false
  answer: false
  explanation: "Increasing W means more replicas hold the latest write, which allows R to decrease while still satisfying W+R > N — so yes, it can enable faster reads. But increasing W directly *slows writes*, since more replicas must acknowledge each write. There is no free lunch: the sum W+R must exceed N, so making writes heavier (higher W) creates room to make reads lighter (lower R), and vice versa. If W is increased while R is held constant, there is no improvement in read performance — just slower writes with more replicas storing the latest data."

- question: "Explain in your own words why the invariant W+R > N guarantees that any read quorum must contain at least one replica that has seen the most recent write."
  type: short-answer
  answer: "If W replicas must acknowledge every write, those W replicas form the 'write set.' If R replicas must respond to every read, those R replicas form the 'read set.' Since there are only N replicas total, and W+R > N, the write set and read set together claim more than N slots among N replicas — so they must share at least one replica by the pigeonhole principle. That shared replica received the latest write and is in the read set, so the reader can always find the latest version by taking the highest-version response across the R replies."
  explanation: "This is the only theorem needed to understand quorum systems. Everything else — version numbers, read repair, tunable W and R — is engineering built on top of this guarantee. A common misconception is that quorums require luck or that freshness depends on which nodes happen to respond. The invariant eliminates that luck: *any* R nodes will include at least one write-quorum member, regardless of which ones respond first."
```

## Explainer

In primary-backup replication, a single leader handles all writes and forwards them to followers. This is simple but creates a bottleneck and a single point of failure — if the primary crashes before replicating, writes can be lost, and electing a new primary takes time. **Quorum-based replication** removes the need for a designated leader by requiring that every write reach enough replicas, and every read contact enough replicas, that at least one replica in any read set has seen the most recent write.

The math behind quorums is straightforward. Suppose you have N replicas. You choose a write quorum W (the number of replicas that must acknowledge a write) and a read quorum R (the number of replicas you must contact on a read). The key invariant is **W + R > N**. This guarantees that the write set and read set always overlap — at least one replica contacted during a read has the latest written value. For example, with 5 replicas, you might set W = 3 and R = 3. Any 3 replicas you read from must include at least one of the 3 that acknowledged the last write. When reading, you take the response with the highest version number or timestamp, which is the most recent value.

This gives you a tunable knob between read and write performance. Setting W = N and R = 1 means writes are slow (all replicas must respond) but reads are fast (any single replica has the latest data). Setting W = 1 and R = N reverses the tradeoff. The classic balanced choice is W = R = (N/2) + 1 — a simple majority. The system tolerates up to N - W write failures and N - R read failures while remaining available. With the majority quorum on 5 nodes, any 2 nodes can fail and the system continues operating.

Quorum replication does not automatically give you strong consistency. If you simply take the first R responses, a slow replica might return stale data. Systems must attach version numbers or vector clocks to values so that the reader can identify which response is freshest. Some systems also use **read repair** — when a quorum read discovers that some replicas have stale data, it pushes the latest value back to them. The quorum mechanism provides the mathematical guarantee that freshness information is always reachable; the protocol layered on top determines how that guarantee translates into the consistency the application actually sees.
