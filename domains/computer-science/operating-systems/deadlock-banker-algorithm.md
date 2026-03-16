---
id: deadlock-banker-algorithm
title: 'Deadlock Avoidance: Banker''s Algorithm'
domain: computer-science
course: operating-systems
prerequisites:
- id: deadlock-prevention-and-avoidance
  type: hard
- id: deadlock-conditions-and-graphs
  type: hard
tags:
- deadlock
- avoidance
- banker
stage: formal-systems
status: draft
---

# Deadlock Avoidance: Banker's Algorithm

## Core Idea
Banker's algorithm grants resource requests only if the resulting state is safe (all processes can eventually finish). It uses maximum claims and simulates allocation; though expensive, it prevents deadlock without breaking any condition or blocking any progress.

## Explainer

From your study of deadlock conditions and prevention, you know the four necessary conditions for deadlock (mutual exclusion, hold-and-wait, no preemption, circular wait) and that prevention works by structurally eliminating one of them — for example, requiring processes to request all resources upfront eliminates hold-and-wait. Prevention is conservative: it restricts what processes can do even when no deadlock threat exists. **Deadlock avoidance** takes a different approach — it allows processes to request resources freely but refuses any request that would put the system into an unsafe state.

The **Banker's Algorithm**, named by analogy to a cautious banker who never lends out so much cash that remaining customers cannot be satisfied, requires one key piece of information upfront: the **maximum claim** of each process — the most of each resource type it will ever need simultaneously. At any moment, the system knows how many resources are allocated to each process, how many each process might still request (maximum claim minus current allocation), and how many resources remain available. A state is **safe** if there exists some ordering of processes such that each process can obtain its maximum remaining needs from the currently available resources plus the resources that will be released by processes that finish before it.

Here is a concrete example. Suppose there are 12 units of a single resource and three processes: P1 holds 5 (max 10), P2 holds 2 (max 4), P3 holds 2 (max 9). Available = 12 - 5 - 2 - 2 = 3. Is this safe? P2 needs at most 2 more, and 3 are available, so P2 can finish. After P2 finishes, available = 3 + 2 = 5. Now P1 needs at most 5 more, and 5 are available, so P1 can finish. After P1 finishes, available = 5 + 5 = 10. P3 needs at most 7 more, and 10 are available, so P3 can finish. The safe sequence is <P2, P1, P3>. If P1 now requests 1 more unit, the system would have available = 2. Can we still find a safe sequence? P2 can finish (needs 2, has 2), releasing to available = 4. P1 now holds 6, needs 4 more, and 4 are available — P1 can finish. Then P3 finishes. So the request is granted. If instead P3 requests 1 more, available drops to 2: P2 finishes (available = 4), but P1 needs 5 and P3 needs 7 — neither can finish with 4. No safe sequence exists, so the request is denied.

The algorithm runs this simulation on every resource request, which means its complexity is O(n² × m) where n is the number of processes and m the number of resource types. In practice this is too expensive for general-purpose operating systems with thousands of processes and resources, and the requirement that processes declare maximum claims upfront is often unrealistic. But the Banker's Algorithm is foundational as a conceptual model: it precisely defines what "safe state" means and demonstrates that deadlock can be avoided without restricting how processes use resources, as long as the system has enough information to reason about the future.
