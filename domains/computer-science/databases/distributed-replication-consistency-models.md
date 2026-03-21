---
id: distributed-replication-consistency-models
title: 'Distributed Databases: Replication Models and Consistency'
domain: computer-science
course: databases
prerequisites:
- id: distributed-systems-introduction
  type: hard
- id: cap-theorem
  type: hard
builds-toward:
- nosql-data-models-scalability
tags:
- replication
- consistency
- distributed
- sync
- async
stage: advanced
status: draft
---

# Distributed Databases: Replication Models and Consistency

## Core Idea
Distributed databases replicate data across sites for fault tolerance and scalability. Synchronous replication waits for replica acknowledgment before committing, ensuring strong consistency but reducing throughput. Asynchronous replication commits locally and updates replicas later, allowing higher throughput but risking inconsistency. Quorum replication requires acknowledgment from a majority, balancing consistency and availability. Understanding replication models is essential for choosing appropriate consistency levels.

## Questions

```yaml
- question: "A distributed database has N=3 replicas, configured with write quorum W=2 and read quorum R=2. Which of the following best explains why this guarantees that reads always see the most recent write?"
  type: multiple-choice
  options:
    - "Because W and R are both greater than 1, every replica is contacted for both reads and writes"
    - "Because W+R=4 > N=3, the write and read quorums must share at least one replica, and that replica has the latest write"
    - "Because reads outnumber writes (R=W=2, so they balance), consistency is maintained by majority voting"
    - "The W+R>N condition ensures that all 3 replicas confirm every write before it completes"
  answer: 1
  explanation: "The W+R>N condition is a pigeonhole argument. If 2 replicas confirmed the last write (W=2) and 2 replicas must respond to a read (R=2), and there are only 3 replicas total, then at least one replica must appear in both groups — it confirmed the write AND responded to the read. That overlapping replica has the latest data. If W+R were ≤ N, it would be possible for the write and read quorums to be completely disjoint, allowing stale data to be returned. Option D confuses quorum with synchronous full replication."

- question: "An e-commerce platform uses asynchronous replication for inventory updates. During a peak sale, the primary replica fails immediately after processing a purchase that reduced inventory from 1 to 0. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The transaction is rolled back because asynchronous replication detected the inconsistency"
    - "The inventory update is permanently lost if it had not yet been replicated; replicas may show inventory = 1, allowing another customer to purchase the last item"
    - "The system pauses all reads until the primary recovers, preventing any inconsistency"
    - "Asynchronous replication automatically falls back to synchronous mode during failures to prevent data loss"
  answer: 1
  explanation: "Asynchronous replication acknowledges writes to the client as soon as the primary stores them, before replicas have confirmed receipt. If the primary crashes in the window between the write and replication, that write is lost — replicas never received it. In this inventory scenario, replicas still show inventory = 1, and a new primary elected from a replica would allow another sale, causing overselling. This is the fundamental risk of asynchronous replication: data loss on primary failure. It is an acceptable tradeoff when consistency is less critical than availability, but not for inventory management."

- question: "Synchronous replication provides higher availability than asynchronous replication because it guarantees all replicas are always up to date."
  type: true-false
  answer: false
  explanation: "Synchronous replication provides *consistency*, not higher availability — in fact, it reduces availability. Because synchronous replication waits for every replica to confirm a write before acknowledging it to the client, any slow or unreachable replica causes writes to block or fail. If a network partition or replica failure occurs, the system may become unavailable for writes until the partition heals. Asynchronous replication commits locally and continues operating even if replicas are lagging or temporarily unreachable, providing higher availability at the cost of potential inconsistency."

- question: "In a quorum-based system, increasing the write quorum W (while keeping N and R fixed) improves write durability but reduces write availability."
  type: true-false
  answer: true
  explanation: "Higher W means more replicas must confirm a write before it is acknowledged. More confirmations means the data is stored on more nodes, reducing the risk of losing the write if some nodes fail (better durability). However, writes now require more replicas to be reachable and responsive, so fewer simultaneous failures can be tolerated before writes start failing (reduced availability). This tradeoff is why quorum systems like Cassandra expose W and R as configurable per-operation parameters — different operations have different durability vs. availability requirements."

- question: "Explain why the condition W + R > N guarantees that a read will always see the most recent write in a quorum-based replication system."
  type: short-answer
  answer: "If W replicas confirmed the latest write and R replicas must respond to a read, and W + R > N, then by the pigeonhole principle at least one replica must belong to both the write quorum and the read quorum — it both stored the latest write and responded to the read. Since this overlap node has the most recent data, and the system returns the freshest value among all read quorum responses, the read is guaranteed to see the latest write. If W + R ≤ N, the write and read quorums could be completely disjoint sets of replicas, allowing the read to return stale data from nodes that never received the latest write."
  explanation: "The overlap guarantee is the mathematical foundation of quorum consistency. Tuning W and R shifts where the overlap happens and how tolerant the system is to node failures, but as long as W + R > N, the overlap is guaranteed by counting alone."
```

## Explainer

From the CAP theorem, you know that a distributed system cannot simultaneously guarantee consistency, availability, and partition tolerance — it must sacrifice at least one during a network partition. **Replication** is the mechanism that forces this tradeoff into concrete engineering decisions. When you copy data across multiple nodes, you must decide: does a write need to reach all copies before it is considered complete, or can it succeed on one node and propagate to the others later? The answer determines where your system falls on the consistency-availability spectrum.

**Synchronous replication** takes the conservative approach: a write is not acknowledged to the client until every replica has confirmed it received and stored the data. This gives you **strong consistency** — any read from any replica returns the most recent write. The cost is latency and reduced availability. If any replica is slow or unreachable, the write blocks or fails. This model works well when correctness is paramount and replicas are geographically close (e.g., within a single data center), but it becomes impractical across continents where network round-trips add hundreds of milliseconds to every write.

**Asynchronous replication** is the opposite extreme: the write succeeds as soon as the primary node stores it, and replicas receive updates later in the background. This maximizes write throughput and availability — the system keeps working even if replicas lag behind. The tradeoff is **eventual consistency**: a read from a lagging replica might return stale data. If the primary fails before replicating a write, that write can be permanently lost. Many consumer-facing applications accept this tradeoff because a user seeing a slightly stale news feed or follower count is far less costly than the system being unavailable.

**Quorum replication** finds a middle ground by requiring acknowledgment from a **majority** of replicas rather than all of them. With N replicas, a write succeeds when W replicas acknowledge it, and a read succeeds when R replicas respond — as long as W + R > N, the read and write quorums must overlap, guaranteeing that at least one node in any read quorum has the latest write. For example, with 3 replicas, writing to 2 and reading from 2 ensures consistency without requiring all 3 to be available. Tuning W and R lets you shift the tradeoff: higher W strengthens write durability at the cost of availability; higher R strengthens read consistency. This flexibility is why quorum-based systems like Cassandra and DynamoDB expose these knobs to application developers — the right consistency level depends on the specific operation, not a one-size-fits-all system setting.
