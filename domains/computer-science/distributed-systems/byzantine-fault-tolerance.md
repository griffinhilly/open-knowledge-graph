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
stage: expert
status: validated
---

# Byzantine Fault Tolerance and Practical BFT

## Core Idea
Byzantine fault tolerance (BFT) handles nodes that fail arbitrarily, including lying to different nodes. Consensus among n nodes tolerating f Byzantine failures requires n > 3f. Practical BFT (PBFT) uses a primary and backups, with request phases (pre-prepare, prepare, commit) coordinated by the primary; backups ensure agreement before committing.

## Questions

```yaml
- question: "A distributed system has 10 nodes. What is the maximum number of Byzantine failures it can tolerate while still achieving consensus?"
  type: multiple-choice
  options:
    - "4 — because 10 > 3×4 = 12 is false, but 10 > 3×3 = 9 is true"
    - "5 — a simple majority of 10 nodes means half can be faulty"
    - "3 — because n > 3f requires f < 10/3 ≈ 3.33, so f ≤ 3"
    - "2 — because safety requires at least 3× the faults to be honest nodes"
  answer: 2
  explanation: "The bound n > 3f means f < n/3. With n = 10, f < 3.33, so the maximum is f = 3. With f = 3, n = 10 > 3×3 = 9. Option B reflects the crash fault tolerance threshold (n > 2f), not BFT. Option A confuses the direction of the inequality. The one-third bound is a proven lower bound — it is not a design choice but a mathematical consequence of the Byzantine Generals Problem."

- question: "An engineering team is building an internal distributed database for a company's own servers. Some nodes occasionally crash. Which fault tolerance model is most appropriate, and why?"
  type: multiple-choice
  options:
    - "Byzantine fault tolerance — because any production system should use the strongest possible guarantees"
    - "Crash fault tolerance (e.g., Raft or Paxos) — because the nodes are trusted and only crash failures are expected"
    - "Byzantine fault tolerance — because crashed nodes can send conflicting messages before stopping"
    - "No fault tolerance is needed — internal servers can be considered reliable"
  answer: 1
  explanation: "BFT is necessary when nodes may be actively malicious or send different messages to different peers — scenarios that arise when nodes are controlled by different, potentially adversarial parties (e.g., blockchain networks). In an internal corporate system, nodes are trusted and only crash failures (stop-and-stay-down) are expected. Crash fault tolerance (Raft, Paxos) handles this at O(n) message complexity, whereas BFT costs O(n²) per round. Choosing BFT for an internal system would impose massive overhead without providing real benefit."

- question: "A node that crashes and stops responding is an example of a Byzantine failure."
  type: true-false
  answer: false
  explanation: "A node that crashes and stops responding is a crash failure — the simplest and most benign failure mode. Byzantine failures are qualitatively different: a Byzantine node can continue operating but behave arbitrarily, sending different messages to different peers, lying about its state, or actively trying to undermine consensus. The key distinction is that crash failures simply remove a node from participation, while Byzantine failures add a potentially deceptive participant. This is why BFT requires a stricter threshold (n > 3f) than crash fault tolerance (n > 2f)."

- question: "A system with 4 nodes using PBFT can tolerate 1 Byzantine failure, because 4 > 3×1."
  type: true-false
  answer: true
  explanation: "With n = 4 and f = 1, n > 3f gives 4 > 3, which is satisfied. This is the smallest possible BFT system — one Byzantine failure tolerated with the minimum viable node count. In PBFT, consensus requires 2f + 1 = 3 matching prepare and commit messages, and the client waits for f + 1 = 2 matching replies. With 4 nodes, 1 can be Byzantine without preventing the 3 honest nodes from reaching agreement."

- question: "Why does tolerating Byzantine failures require more than two-thirds of nodes to be honest, while crash fault tolerance only requires a simple majority?"
  type: short-answer
  answer: "A Byzantine node can actively deceive by sending 'attack' to some nodes and 'retreat' to others, creating confusion rather than simply disappearing. To outvote conflicting messages, honest nodes need enough of a majority that even after removing the f potentially faulty nodes' votes AND accounting for f conflicting messages injected by Byzantine nodes, a clear honest majority still remains. With n = 3f, the math doesn't work — honest nodes cannot distinguish a Byzantine node from an honest node that received different information. At n = 3f + 1, the honest supermajority is just sufficient to unmask the deception. Crash failures, in contrast, simply remove nodes, so only a simple majority of remaining nodes is needed."
  explanation: "The intuition is that Byzantine failures add noise rather than subtract participants. The 2/3 honest threshold is a proven impossibility result — no BFT protocol can tolerate f Byzantine failures with fewer than 3f + 1 total nodes, regardless of how clever the protocol design is."
```

## Explainer

From your study of failure models, you know that crash failures are relatively benign — a node either works correctly or stops responding. **Byzantine failures** are far worse: a faulty node can behave arbitrarily, sending different messages to different peers, lying about its state, or even actively trying to sabotage the system. The name comes from the **Byzantine Generals Problem**, a thought experiment: imagine several generals surrounding a city, communicating by messenger, who must agree on whether to attack or retreat. Some generals are traitors who may send contradictory messages. The question is: can the loyal generals still reach agreement? The answer is yes, but only if fewer than one-third of the generals are traitors.

This one-third bound is a proven mathematical result, not a design choice. With **n** total nodes and **f** Byzantine-faulty nodes, consensus requires **n > 3f**. The intuition: a Byzantine node can send "attack" to some peers and "retreat" to others. To outvote these conflicting messages, the honest nodes need enough of a majority that even after removing f potentially faulty votes and accounting for f conflicting messages, a clear majority remains. With n = 3f, the system deadlocks — honest nodes can't distinguish between a faulty node and an honest node that received different information from another faulty node. At n = 3f + 1 (e.g., 4 nodes tolerating 1 Byzantine failure), the protocol has just enough redundancy to unmask the liar.

**Practical Byzantine Fault Tolerance (PBFT)** made BFT usable in real systems. The protocol works in three phases. A designated **primary** node receives the client request and broadcasts a **pre-prepare** message proposing an ordering. Each backup node validates this proposal and broadcasts a **prepare** message to all other nodes. Once a node collects 2f + 1 matching prepare messages (including its own), it knows that enough honest nodes agree, so it broadcasts a **commit** message. After collecting 2f + 1 commit messages, the node executes the request and replies to the client. The client waits for f + 1 matching replies to be confident at least one came from an honest node. If the primary is faulty (refusing to send pre-prepares or sending conflicting ones), a **view change** protocol replaces it with the next backup.

The cost of Byzantine tolerance is significant: PBFT requires O(n²) messages per consensus round because every node communicates with every other node in the prepare and commit phases. This limits practical deployments to relatively small clusters — typically tens of nodes, not thousands. For most internal distributed systems where you trust your own hardware and software, crash fault tolerance (like Raft or Paxos, requiring only n > 2f) is sufficient and far cheaper. BFT becomes essential in environments where nodes are controlled by different, potentially adversarial parties — the most prominent example being blockchain networks, where any participant might try to cheat. Understanding when Byzantine tolerance is actually needed versus when crash tolerance suffices is a key architectural judgment in distributed system design.
