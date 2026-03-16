---
id: distributed-lock-management
title: Distributed Lock Management
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: leader-election-algorithms
  type: soft
builds-toward:
- paxos-made-practical
- raft-leader-election
tags:
- locks
- mutual-exclusion
- consensus
- deadlock
stage: advanced
status: draft
---

# Distributed Lock Management

## Core Idea
Distributed locks coordinate access to shared resources across processes that cannot share memory. Lock managers must handle failures (a process crashes while holding a lock), enforce mutual exclusion, and avoid deadlock. Solutions range from simple (lease-based locks) to robust (consensus-based or quorum-based).

## How It's Best Learned
Implement a simple lease-based lock manager: clients request locks with an expiration time and renew before expiration. Then add failure handling: what happens if a client crashes and never renews? Understand why leases eliminate indefinite blocking.

## Explainer

From your study of the consensus problem, you know that getting multiple distributed processes to agree on a single value is fundamentally difficult in the presence of failures and network partitions. **Distributed lock management** is a direct application of this problem: multiple processes need to agree on *who currently holds a lock* so that only one process accesses a shared resource at a time. Unlike locks in a single-machine program where a shared memory mutex suffices, distributed locks must work across machines that communicate only via unreliable networks and can crash independently.

The simplest and most widely used approach is the **lease-based lock**. Instead of granting a lock indefinitely, the lock manager grants a **lease** — a lock that expires after a specified duration. The client must periodically renew the lease before it expires. If the client crashes or becomes unreachable, the lease simply times out and the lock becomes available to other processes. This elegantly solves the "holder crashes while holding the lock" problem that plagues indefinite locks: no manual intervention or failure detection is needed. The tradeoff is that clients must finish their work before the lease expires, or risk another process acquiring the lock while they are still operating — a subtle source of bugs if lease duration is set too short.

For stronger guarantees, systems use **consensus-based locks** built on algorithms like Paxos or Raft. A majority quorum of lock servers must agree on each lock grant, ensuring that even if some servers fail, the lock state is consistent. This is how systems like Apache ZooKeeper and etcd provide distributed locking — they use consensus internally so that clients see a single consistent view of which locks are held. The cost is higher latency per lock operation (multiple round trips to achieve consensus) and the operational complexity of running a consensus cluster.

**Deadlock** remains a concern in distributed locking, just as in single-machine concurrency, but is harder to detect because no single node has a complete view of all lock dependencies. Strategies include lock ordering (always acquire locks in a globally agreed order), timeouts (if you cannot acquire a lock within a deadline, release all held locks and retry), and deadlock detection through distributed wait-for graphs. In practice, most systems use timeouts and leases together — they prevent both indefinite blocking from holder failures and deadlock from circular dependencies. The fundamental design question is always the same: how much latency and complexity are you willing to pay for how strong a mutual-exclusion guarantee?
