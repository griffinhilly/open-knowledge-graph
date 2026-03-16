---
id: distributed-systems-overview
title: 'Distributed Systems: Overview and Challenges'
domain: computer-science
course: distributed-systems
prerequisites:
- id: threads-and-concurrency
  type: hard
- id: socket-programming-basics
  type: soft
builds-toward:
- distributed-system-models
- failure-models-distributed
tags:
- distributed-systems
- concurrency
- scalability
stage: advanced
status: draft
---

# Distributed Systems: Overview and Challenges

## Core Idea
Distributed systems are collections of independent computers communicating via message passing to coordinate and solve problems. Key challenges include managing concurrency, handling failures, ensuring consistency, and tolerating latency and network partitions that are impossible in single-machine systems.

## Questions

```yaml
- question: "A distributed database stops accepting writes whenever it cannot confirm that all replicas are synchronized, even if some replicas are unreachable. Which property is this system prioritizing over the others?"
  type: multiple-choice
  options: ["Availability", "Partition tolerance", "Consistency", "Scalability"]
  answer: 2
  explanation: "This system refuses to serve requests that might return stale data — it chooses consistency over availability. The CAP theorem states that during a network partition, a distributed system must choose between consistency (every read gets the most recent write) and availability (every request gets a response, even if it might be stale). Refusing writes when replicas are unreachable is the consistency choice."

- question: "A distributed system is essentially the same as a multi-threaded program running on a single machine — the same concurrency techniques apply in both cases."
  type: true-false
  answer: false
  explanation: "Distributed systems face challenges that simply do not exist on a single machine: network messages can be lost, delayed, or duplicated; individual nodes can fail while others continue running (partial failures); there is no shared memory or shared clock; and network partitions can split the system in ways that have no analogue in multi-threaded programs. These differences require fundamentally different techniques for coordination, consistency, and fault tolerance."

- question: "Why is it impossible for a distributed system to simultaneously guarantee consistency, availability, and partition tolerance at all times?"
  type: short-answer
  answer: "The CAP theorem proves that when a network partition occurs (nodes cannot communicate), the system must choose: either refuse requests to stay consistent, or respond with potentially stale data to stay available. No system can do both during a partition."
  explanation: "Partition tolerance cannot be avoided in real networks — messages do get lost and nodes do get isolated. When a partition happens, a system serving reads from an isolated replica either returns possibly-stale data (available but inconsistent) or refuses to respond until it can verify consistency (consistent but unavailable). This is not a design flaw but a fundamental theorem about distributed systems."
```

## Explainer

From your work with threads and concurrency, you know that coordinating multiple tasks on a single machine is already challenging — you need locks, semaphores, and careful sequencing to avoid race conditions. Distributed systems take these challenges and add an entirely new set of problems that don't exist when everything runs on one machine: nodes can fail independently, messages can be lost or arrive out of order, and there is no shared memory or global clock.

A distributed system is a collection of independent computers (nodes) that communicate only through message passing over a network — typically to provide a service that appears unified to users. The goal is to make multiple machines look and act like one. Examples include web services that spread load across hundreds of servers, databases that replicate data across data centers, and blockchain networks where thousands of nodes maintain a shared ledger. The common thread is that no single node has the full picture, yet the system must behave coherently.

The central challenge is that networks are unreliable. A message sent from node A to node B might arrive instantly, arrive after a long delay, arrive twice, or never arrive at all. Worse, node A has no reliable way to distinguish "B is slow to respond" from "B has crashed." This ambiguity — fundamental to distributed systems — forces designers to build for partial failures: states where some nodes are working correctly while others are not, and the working nodes don't know which scenario they're in.

The CAP theorem (Consistency, Availability, Partition tolerance) formalizes a key tradeoff. When a network partition splits a distributed system into isolated groups, the system must choose: serve requests with data that might be stale (available but inconsistent), or refuse to serve requests until it can verify the data is current (consistent but unavailable). Partition tolerance isn't really optional in real networks — partitions happen — so the real tradeoff is between consistency and availability during those failures. Different systems make different choices depending on their use case: a banking system prioritizes consistency, while a social media feed might prefer availability.

Understanding distributed systems starts with internalizing that the assumptions you take for granted on a single machine — a reliable clock, instant function calls, guaranteed memory visibility — simply don't hold across a network. This shift in mental model is the foundation for everything that follows: consensus protocols, replication strategies, eventual consistency, and failure detection all exist to manage the gap between the distributed ideal and the messy reality of unreliable networks and independently failing machines.
