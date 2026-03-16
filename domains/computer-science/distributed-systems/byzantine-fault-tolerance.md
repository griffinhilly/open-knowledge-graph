---
id: byzantine-fault-tolerance
title: Byzantine Fault Tolerance and Practical BFT
domain: computer-science
course: distributed-systems
prerequisites:
- id: failure-models-distributed
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- flp-impossibility
tags:
- byzantine
- byzantine-faults
- fault-tolerance
- pbft
stage: advanced
status: draft
---

# Byzantine Fault Tolerance and Practical BFT

## Core Idea
Byzantine fault tolerance (BFT) handles nodes that fail arbitrarily, including lying to different nodes. Consensus among n nodes tolerating f Byzantine failures requires n > 3f. Practical BFT (PBFT) uses a primary and backups, with request phases (pre-prepare, prepare, commit) coordinated by the primary; backups ensure agreement before committing.

## Explainer

From your study of failure models, you know that crash failures are relatively benign — a node either works correctly or stops responding. **Byzantine failures** are far worse: a faulty node can behave arbitrarily, sending different messages to different peers, lying about its state, or even actively trying to sabotage the system. The name comes from the **Byzantine Generals Problem**, a thought experiment: imagine several generals surrounding a city, communicating by messenger, who must agree on whether to attack or retreat. Some generals are traitors who may send contradictory messages. The question is: can the loyal generals still reach agreement? The answer is yes, but only if fewer than one-third of the generals are traitors.

This one-third bound is a proven mathematical result, not a design choice. With **n** total nodes and **f** Byzantine-faulty nodes, consensus requires **n > 3f**. The intuition: a Byzantine node can send "attack" to some peers and "retreat" to others. To outvote these conflicting messages, the honest nodes need enough of a majority that even after removing f potentially faulty votes and accounting for f conflicting messages, a clear majority remains. With n = 3f, the system deadlocks — honest nodes can't distinguish between a faulty node and an honest node that received different information from another faulty node. At n = 3f + 1 (e.g., 4 nodes tolerating 1 Byzantine failure), the protocol has just enough redundancy to unmask the liar.

**Practical Byzantine Fault Tolerance (PBFT)** made BFT usable in real systems. The protocol works in three phases. A designated **primary** node receives the client request and broadcasts a **pre-prepare** message proposing an ordering. Each backup node validates this proposal and broadcasts a **prepare** message to all other nodes. Once a node collects 2f + 1 matching prepare messages (including its own), it knows that enough honest nodes agree, so it broadcasts a **commit** message. After collecting 2f + 1 commit messages, the node executes the request and replies to the client. The client waits for f + 1 matching replies to be confident at least one came from an honest node. If the primary is faulty (refusing to send pre-prepares or sending conflicting ones), a **view change** protocol replaces it with the next backup.

The cost of Byzantine tolerance is significant: PBFT requires O(n²) messages per consensus round because every node communicates with every other node in the prepare and commit phases. This limits practical deployments to relatively small clusters — typically tens of nodes, not thousands. For most internal distributed systems where you trust your own hardware and software, crash fault tolerance (like Raft or Paxos, requiring only n > 2f) is sufficient and far cheaper. BFT becomes essential in environments where nodes are controlled by different, potentially adversarial parties — the most prominent example being blockchain networks, where any participant might try to cheat. Understanding when Byzantine tolerance is actually needed versus when crash tolerance suffices is a key architectural judgment in distributed system design.
