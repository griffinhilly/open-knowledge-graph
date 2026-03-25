---
id: distributed-system-models
title: Models of Distributed Computation
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
builds-toward:
- synchronous-asynchronous-systems
- failure-models-distributed
tags:
- models
- computation
- theory
stage: advanced
status: validated
---

# Models of Distributed Computation

## Core Idea
Distributed computation models formalize assumptions about timing, communication, and failures. Synchronous models assume bounded message delays and clock synchronization; asynchronous models make no timing guarantees. The choice of model fundamentally affects which problems are solvable and determines which algorithms can guarantee correctness.

## Questions

```yaml
- question: "In a fully asynchronous distributed system, Process A sends a message to Process B and receives no response after 10 seconds. What can Process A conclude?"
  type: multiple-choice
  options:
    - "Process B has crashed — 10 seconds is too long for any functioning process"
    - "The network has partitioned between A and B"
    - "Nothing definitive — B may be slow, the message may be in transit, or B may have crashed"
    - "Process B received the message but chose not to respond"
  answer: 2
  explanation: "This is the fundamental problem of the asynchronous model: without timing bounds, a slow process and a crashed process are indistinguishable from the outside. There is no timeout threshold you can set that definitively means 'crashed' rather than 'slow' — because asynchrony allows arbitrarily long delays. This indistinguishability is why many problems (including consensus) are provably impossible in the pure asynchronous model. It is also why real distributed systems must either accept uncertainty or impose additional assumptions about timing."

- question: "Why do practical consensus algorithms like Raft guarantee safety (no incorrect decisions) at all times but only guarantee liveness (making progress) when the system is behaving well?"
  type: multiple-choice
  options:
    - "They are designed for the synchronous model, where safety and liveness are both always guaranteed"
    - "They are designed for partial synchrony — safety holds under any timing, but liveness requires eventual synchrony for timeouts to function correctly"
    - "They trade safety for liveness during high-load periods to improve throughput"
    - "Liveness is impossible in any distributed system, so algorithms don't guarantee it"
  answer: 1
  explanation: "Raft and Paxos are designed for the partially synchronous model, which captures real-world systems that are usually well-behaved but occasionally suffer bursts of delay. Safety (e.g., never electing two leaders simultaneously) is maintained under any timing conditions through quorum requirements and term numbers. Liveness (electing a leader and making progress) requires that the system eventually becomes synchronous enough for election timeouts to work reliably. During prolonged asynchrony (severe network partition, cascading delays), the system may halt rather than risk an incorrect decision."

- question: "In the synchronous distributed model, failure detection is reliable because you can use timeouts to definitively conclude that a non-responding process has crashed."
  type: true-false
  answer: true
  explanation: "This is the key advantage of the synchronous model. Because there is a known upper bound on message delivery time and process step time, if no response arrives within that bound, the process must have failed — there is no other explanation. This makes failure detection clean and consensus algorithms straightforward. Contrast with the asynchronous model, where any delay could be arbitrarily long, making timeout-based failure detection unreliable: a 'suspected' process might simply be slow."

- question: "The partially synchronous model is merely a theoretical curiosity with no relevance to real distributed systems."
  type: true-false
  answer: false
  explanation: "Partial synchrony is the most practically relevant model. It captures the reality of systems like the internet, cloud infrastructure, and data center networks: most of the time, messages arrive within milliseconds (behaving synchronously), but occasionally there are spikes of delay from network congestion, garbage collection pauses, or load spikes. The most widely deployed consensus protocols — Paxos, Raft, Zab (used in ZooKeeper) — are all designed for this model. Understanding partial synchrony is essential for understanding why these systems sometimes stall during network disruptions but recover once conditions improve."

- question: "Why does the choice of computational model (synchronous vs. asynchronous vs. partially synchronous) matter for distributed algorithm design?"
  type: short-answer
  answer: "The model defines what assumptions you can rely on — specifically, whether you can set reliable timeouts, whether you can distinguish slow processes from crashed ones, and whether clocks are synchronized. These assumptions determine what problems are solvable and which correctness guarantees are achievable. A problem that is easily solved in the synchronous model (like failure detection) may be provably impossible in the asynchronous model. Every algorithm and impossibility theorem comes with a model attached — claiming a result without specifying the model is incomplete."
  explanation: "The classic example is the FLP impossibility result: consensus is impossible in a fully asynchronous system even with just one crash fault. This sounds alarming but is a consequence of the asynchronous model's strongest assumption — that no timing bounds exist. In the synchronous model, consensus is straightforward. In partial synchrony, it is achievable when the system stabilizes. Without understanding these models, you cannot interpret impossibility results correctly, and you cannot reason about whether a real system's behavior violates or is consistent with theoretical guarantees."
```

## Explainer

From your distributed systems overview, you understand the basic challenge: multiple computers communicating over a network, with no shared memory and no guarantee that messages arrive quickly or at all. A **model of distributed computation** is a set of formal assumptions about this environment — how fast messages travel, how reliable processes are, and what kinds of failures can occur. These assumptions are not descriptions of any particular real system; they are simplifications that let you prove what is and is not possible.

The **synchronous model** makes the strongest assumptions. It says there exists a known upper bound on message delivery time, a known upper bound on the time each process takes to execute a step, and clocks that are synchronized within a known drift. Under these assumptions, many problems become straightforward. For instance, a process can detect that another process has crashed simply by waiting for the maximum message delay — if no response arrives within that bound, the other process must be down. Consensus algorithms in the synchronous model are relatively simple because timeout-based failure detection is reliable.

The **asynchronous model** makes no timing assumptions at all. Messages can take arbitrarily long to arrive. Processes can pause for arbitrary periods before executing the next step. There is no upper bound you can rely on. This is a much harder world to design for because you cannot distinguish a slow process from a crashed one — a message that has not arrived might still be in transit. The asynchronous model is closer to the reality of the internet, where network congestion, garbage collection pauses, and load spikes can cause unpredictable delays.

Between these extremes lies the **partially synchronous model**, which assumes that timing bounds exist but are unknown, or that the system behaves asynchronously for some period but eventually becomes synchronous. This model captures the practical reality of most distributed systems: most of the time, messages arrive within a few milliseconds, but occasionally there are bursts of delay. Most practical consensus algorithms (like Paxos and Raft) are designed for partial synchrony — they guarantee safety always, but only guarantee progress (liveness) when the system is behaving synchronously enough for timeouts to work.

The choice of model is not a matter of preference — it determines what you can prove. The same problem that is solvable in the synchronous model may be provably impossible in the asynchronous model. Understanding these models is essential before studying impossibility results and consensus algorithms, because every theorem and every algorithm comes with a model attached. When someone says "consensus is impossible," the first question is always: in which model?
