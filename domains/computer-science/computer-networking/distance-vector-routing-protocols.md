---
id: distance-vector-routing-protocols
title: Distance-Vector Routing Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: bellman-ford-distance-vector-routing
  type: hard
builds-toward:
- bgp-border-gateway-protocol
tags:
- distance-vector
- dv-routing
- bellman-ford
- rip
stage: advanced
status: draft
---

# Distance-Vector Routing Protocols

## Core Idea
Distance-vector routing protocols compute shortest paths based on a simple metric by having each router advertise its distances to all destinations and update based on neighbors' advertisements. RIP is a classic distance-vector protocol that uses hop count as its metric. Distance-vector protocols converge slowly and suffer from count-to-infinity problems, but remain simple to implement.

## Questions

```yaml
- question: "Router A reaches network X with cost 3 via Router B. B's direct link to X then fails. Before B can propagate the failure, A sends its periodic update saying 'I reach X with cost 3.' B concludes it can now reach X via A with cost 4, and begins advertising cost 4. A then updates to cost 5, B to 6, and so on. This scenario illustrates:"
  type: multiple-choice
  options:
    - "The Bellman-Ford algorithm failing to converge due to incorrect initialization"
    - "The count-to-infinity problem, where stale routing information creates a self-reinforcing feedback loop of increasing costs"
    - "Split horizon successfully preventing the loop from forming"
    - "Poison reverse correctly marking the route as unreachable"
  answer: 1
  explanation: "This is the textbook count-to-infinity scenario. After the failure, B no longer has a valid route to X, but before it can propagate that information, it receives A's stale advertisement and mistakenly believes it can reach X through A. A in turn updates based on B's updated cost. The two routers bounce the route back and forth with increasing costs until the metric hits the maximum (16 in RIP). Options C and D describe mitigations that would have prevented this, not the problem itself."

- question: "RIP uses a maximum hop count of 15 and treats 16 as 'infinity' (unreachable). The primary reason for this hard cap is:"
  type: multiple-choice
  options:
    - "To ensure RIP converges faster than OSPF on small networks"
    - "To bound the count-to-infinity problem, preventing counting from running indefinitely when a destination becomes unreachable"
    - "To limit the size of routing tables that routers must maintain"
    - "To enforce a maximum network diameter for administrative reasons"
  answer: 1
  explanation: "Without a maximum metric, the count-to-infinity problem would cause routers to increment a failed route's cost forever. The max-15 cap means the loop terminates after at most 15 increment cycles, at which point both routers agree the destination is unreachable. The cap makes the protocol eventually correct, though it still converges slowly. Options A and C are not the primary motivation; option D is a side effect, not the design purpose."

- question: "Split horizon completely solves the count-to-infinity problem by preventing routers from ever advertising stale routes back to the neighbor from which they learned them."
  type: true-false
  answer: false
  explanation: "Split horizon reduces the problem but does not fully solve it. It prevents a two-router loop (A learned from B, so A won't advertise back to B), but multi-router loops involving three or more routers can still cause count-to-infinity. For example, if A and C both have routes through B, and B's link fails, A might hear C advertising a stale route and update, then C hears A's update, etc. This is why larger networks prefer link-state protocols with a complete topology view rather than relying on split horizon."

- question: "In distance-vector routing, each router periodically sends its entire routing table — its distances to all known destinations — to its directly connected neighbors."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of distance-vector protocols and the source of both their simplicity and their problems. Each router shares its complete distance vector (not just directly connected links), which allows knowledge to propagate through the network in successive rounds. It also means that stale information can spread — if a router's routing table contains an outdated entry, it will share that bad information with neighbors, who may then rely on it. This is contrast to link-state protocols, where routers share only the state of their directly connected links."

- question: "Explain why distance-vector protocols are susceptible to the count-to-infinity problem and describe one mitigation technique along with its limitation."
  type: short-answer
  answer: "Distance-vector routers only know their distances to destinations, not the full topology. When a link fails, neighbors may have already cached the failed router's distance advertisement and believe they have an alternate route through it — creating a routing loop. Each router increments the cost based on what its neighbor advertises, which was itself based on the original router's stale distance. Split horizon partially fixes this by refusing to advertise a route back to the neighbor from which it was learned, breaking two-node loops. But split horizon fails for loops involving three or more routers, which can still count up to the maximum metric before convergence."
  explanation: "The fundamental problem is that distance vectors carry no path information — a router can't tell whether the route it's hearing about loops back through itself. Link-state protocols solve this by flooding the complete topology to every router, so loops are immediately detectable. The price of distance-vector simplicity is slow convergence and vulnerability to these feedback loops."
```

## Explainer

From your study of routing algorithms and Bellman-Ford, you know the mathematical foundation: the shortest distance from node X to destination D equals the minimum over all neighbors N of (cost to N + N's distance to D). **Distance-vector routing protocols** are the direct implementation of this equation in real networks. Each router maintains a **routing table** (the "distance vector") that lists, for every known destination, the best distance and the next-hop router to use. Periodically, each router sends its entire distance vector to its directly connected neighbors.

Here is how convergence works in practice. Initially, each router only knows about its directly connected networks (distance = 0 or the link cost). Router A tells neighbor B: "I can reach network 10.0.1.0 with cost 1." Router B, which has cost 1 to reach A, now knows it can reach 10.0.1.0 with cost 2 via A. B adds this to its table and shares its updated vector with its own neighbors. Through repeated exchanges, knowledge of all destinations propagates outward like ripples in a pond. After enough rounds of updates (bounded by the network diameter), every router has a consistent shortest-path entry for every destination. This is the Bellman-Ford algorithm running in a distributed, asynchronous fashion.

**RIP (Routing Information Protocol)** is the textbook distance-vector protocol. It uses **hop count** as its metric (each link costs 1), sends updates every 30 seconds, and caps the maximum distance at 15 hops (16 = infinity/unreachable). RIP's simplicity makes it easy to configure but limits it to small networks. Larger or more complex networks use protocols with richer metrics.

The critical weakness of distance-vector routing is slow convergence after failures — the **count-to-infinity problem**. Suppose router A reaches network X through B with cost 2, and the link from B to X fails. B removes its route, but then receives A's next update saying "I can reach X with cost 2." B mistakenly concludes it can reach X through A with cost 3. A then updates to cost 4 via B, B updates to 5, and so on — the distance "counts to infinity" (15 in RIP) before the routers agree the network is unreachable. Mitigations include **split horizon** (don't advertise a route back to the neighbor you learned it from), **poison reverse** (advertise it back with infinite cost), and **triggered updates** (send changes immediately instead of waiting for the periodic timer). These techniques reduce but do not fully eliminate slow convergence, which is why larger networks often prefer link-state protocols that have a complete topology view.
