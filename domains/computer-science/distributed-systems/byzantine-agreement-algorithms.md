---
id: byzantine-agreement-algorithms
title: Byzantine Agreement Algorithms
domain: computer-science
course: distributed-systems
prerequisites:
- id: byzantine-fault-tolerance
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- view-change-protocols
tags:
- byzantine
- consensus
- fault-tolerance
- malicious
stage: advanced
status: draft
---

# Byzantine Agreement Algorithms

## Core Idea
Byzantine agreement handles both crash failures and arbitrary (malicious) failures where replicas may lie. Algorithms like PBFT (Practical Byzantine Fault Tolerance) require f < N/3 honest replicas and use rounds of voting to ensure all honest replicas agree, even if up to f replicas are corrupted.

## Explainer

You already know what Byzantine faults are — nodes that can behave arbitrarily, sending contradictory messages to different peers or lying about their state — and you understand the consensus problem: getting a group of nodes to agree on a single value despite failures. **Byzantine agreement algorithms** solve consensus under the hardest failure model, where you cannot trust that a faulty node will simply crash and go silent. It might actively try to sabotage the protocol.

The foundational result, proved by Lamport, Shostak, and Pease, is that Byzantine agreement requires **N ≥ 3f + 1** nodes to tolerate f Byzantine failures. The intuition behind the bound comes from a voting argument: if a third or more of the nodes can lie, the honest nodes cannot distinguish between a scenario where the faulty nodes are echoing the truth and one where they are fabricating a false consensus. With fewer than 2f + 1 honest nodes, the honest majority is too slim to outvote a coordinated group of liars who send different messages to different peers.

**PBFT** (Practical Byzantine Fault Tolerance) is the landmark algorithm that made Byzantine consensus viable for real systems. It works in three phases. In the **pre-prepare** phase, a designated leader proposes an ordering of requests. In the **prepare** phase, each replica broadcasts its agreement with the proposal — once a replica collects 2f + 1 matching prepare messages, it knows that a quorum of honest nodes have seen the same proposal. In the **commit** phase, replicas broadcast commit messages, and upon collecting 2f + 1 commits, each replica executes the request. The two rounds of 2f + 1 voting ensure that even if the leader is Byzantine (proposing different values to different replicas), the honest replicas will detect the inconsistency and refuse to proceed.

The cost of Byzantine tolerance is significant. PBFT has **O(N²)** message complexity per consensus round — every node communicates with every other node in both the prepare and commit phases. This makes it impractical for large networks (hundreds or thousands of nodes), which is why most Byzantine agreement deployments use small replica groups (typically 4 to 7 nodes). When the leader itself is faulty, PBFT triggers a **view change** — a protocol to elect a new leader — which adds further rounds of communication. Modern variants like HotStuff reduce message complexity by using a tree-based communication pattern and threshold signatures, making them more suitable for blockchain and large-scale systems where the original PBFT approach would be prohibitively expensive.
