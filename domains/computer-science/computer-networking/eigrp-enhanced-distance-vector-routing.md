---
id: eigrp-enhanced-distance-vector-routing
title: 'EIGRP: Enhanced Interior Gateway Routing Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: distance-vector-routing-protocols
  type: hard
- id: routing-algorithms-overview
  type: hard
- id: rip-routing-information-protocol
  type: soft
builds-toward:
- routing-convergence-flap-damping
- bgp-border-gateway-protocol
tags:
- routing
- eigrp
- igp
- dynamic-routing
- cisco
stage: advanced
status: validated
---

# EIGRP: Enhanced Interior Gateway Routing Protocol

## Core Idea
EIGRP (Enhanced Interior Gateway Routing Protocol) is a Cisco proprietary distance-vector protocol that uses a composite metric of bandwidth, delay, reliability, and load. It converges faster than RIP using the Diffusing Update Algorithm (DUAL) and maintains backup routes (feasible successors). EIGRP sends incremental updates only when topology changes, reducing overhead significantly.

## How It's Best Learned
Deploy EIGRP on Cisco equipment or GNS3 with IOS images. Observe DUAL calculations and feasible successor selection. Cause link failures and measure convergence compared to RIP. Configure EIGRP for IPv6 (EIGRPv6) and compare protocol behavior.

## Common Misconceptions
EIGRP is not proprietary in modern versions; Cisco submitted it as an IETF draft but does not enforce patents. EIGRP does not send periodic updates like RIP; it sends triggered updates only. Feasible distance is not the same as advertised distance from the neighbor.

## Questions

```yaml
- question: "Router A currently reaches destination X via neighbor B with a feasible distance (FD) of 100. Neighbor B reports an advertised distance (AD) of 70. Neighbor C reports an AD of 110. Which neighbor can serve as a feasible successor (loop-free backup)?"
  type: multiple-choice
  options:
    - "Only C — it has a higher AD, meaning it has a longer path that could not be routing back through A"
    - "Only B — its AD (70) is strictly less than the current FD (100), satisfying the feasibility condition and guaranteeing a loop-free alternate path"
    - "Both B and C — any alternate path qualifies as a feasible successor"
    - "Neither — a feasible successor can only be selected after B's route fails and DUAL queries are sent"
  answer: 1
  explanation: "DUAL's feasibility condition requires that the neighbor's advertised distance (AD) be strictly less than the current feasible distance (FD). If neighbor B's AD < FD, it is provably not routing through A to reach X — it has a genuinely shorter independent path. Neighbor C's AD (110) exceeds the FD (100), meaning C might be routing through A, which could create a loop. The feasibility condition is EIGRP's guarantee of loop-free routing at every instant: B can be used as an instant failover; C cannot without re-querying."

- question: "A network engineer needs to minimize routing protocol bandwidth overhead on a WAN link. Why would she prefer EIGRP over RIP?"
  type: multiple-choice
  options:
    - "EIGRP uses a simpler hop-count metric that requires less computation to advertise"
    - "EIGRP sends only incremental, triggered updates when topology changes occur — not periodic full routing-table broadcasts like RIP's 30-second updates"
    - "EIGRP compresses its routing table before transmission, reducing packet size"
    - "EIGRP automatically reduces update frequency when bandwidth is congested"
  answer: 1
  explanation: "RIP broadcasts its entire routing table to all neighbors every 30 seconds, regardless of whether anything changed. On a slow WAN link, this constant churn wastes precious bandwidth. EIGRP establishes neighbor relationships with lightweight hello packets (sent every 5 seconds by default) and only sends updates for specific routes that changed — triggered by actual topology changes. An EIGRP network with a stable topology may go hours or days with virtually no update traffic. This is one of EIGRP's most important operational advantages over RIP in real deployments."

- question: "EIGRP's feasibility condition guarantees that a feasible successor cannot be routing traffic back through the querying router, making loop-free instant failover possible."
  type: true-false
  answer: true
  explanation: "This is the mathematical insight behind DUAL. If neighbor B's advertised distance (the metric B reports from itself to destination X) is less than router A's current feasible distance to X, then B cannot possibly be routing through A to reach X — if it were, B's distance would have to include A's distance, making it at least as large as A's FD. The strict inequality (AD < FD) is the invariant that proves no loop exists. When the primary route fails, the feasible successor can be used immediately without any query-response cycle, enabling sub-second convergence."

- question: "In EIGRP, the feasible distance (FD) for a route and the advertised distance (AD) reported by the successor router refer to the same metric value."
  type: true-false
  answer: false
  explanation: "FD and AD are distinct values. The advertised distance (AD) is what the neighbor router reports — the metric from that neighbor to the destination. The feasible distance (FD) is the full metric from the local router to the destination, which equals the metric of the link to the neighbor plus the neighbor's AD. FD ≥ AD always (since FD includes additional path cost). This distinction is critical to the feasibility condition: a backup route is safe if its AD is less than the current FD, not less than the current AD."

- question: "Explain how EIGRP's feasibility condition prevents routing loops during a topology change, and contrast this with how RIP handles the same situation."
  type: short-answer
  answer: "EIGRP pre-qualifies backup routes (feasible successors) before any failure occurs, using the feasibility condition (neighbor's AD < current FD). When a primary route fails, the router instantly switches to the feasible successor without querying other routers — no temporary loop can form because the backup was mathematically proven loop-free in advance. RIP has no such pre-qualification: when a route fails, neighboring routers may still advertise the old route to each other, causing count-to-infinity loops where routers increment the metric through each other indefinitely. RIP's slow-convergence fixes (split horizon, route poisoning, holddown timers) reduce but do not eliminate this risk, and they introduce delays. EIGRP trades computational complexity (maintaining FD/AD state) for guaranteed loop-freedom and fast convergence."
  explanation: "This is the fundamental difference between basic distance-vector routing and DUAL. RIP's simplicity comes at the cost of loop vulnerability during convergence. EIGRP's DUAL algorithm maintains enough state to guarantee loop-freedom at every moment — not just after convergence stabilizes. The 'stuck in active' problem is EIGRP's remaining weakness: when no feasible successor exists, the router must query neighbors, and in large flat networks this query diffusion can be slow."
```

## Explainer

From your study of distance-vector routing protocols and RIP, you know the basic model: each router maintains a table of distances to every destination, shares that table with its neighbors, and updates its routes when it learns of a shorter path. RIP works, but it has serious limitations — it converges slowly after topology changes, is vulnerable to routing loops during convergence, and uses hop count as its only metric, ignoring link speed entirely. **EIGRP** was designed to keep the simplicity of distance-vector routing while solving all of these problems.

The most important innovation in EIGRP is the **Diffusing Update Algorithm (DUAL)**, which guarantees loop-free routing at every instant — not just after convergence, but during topology changes as well. DUAL achieves this by tracking two key values for every route: the **feasible distance (FD)**, which is the best known metric from this router to the destination, and the **advertised distance (AD)**, which is the metric a neighbor reports from itself to the destination. A neighbor qualifies as a **feasible successor** — a guaranteed loop-free backup — only if its advertised distance is strictly less than the current feasible distance. This condition ensures that the backup neighbor is genuinely closer to the destination and cannot be routing through you, which would create a loop. When the primary route fails, EIGRP can instantly switch to a feasible successor without querying other routers, enabling sub-second failover.

Unlike RIP, which broadcasts its entire routing table every 30 seconds regardless of whether anything changed, EIGRP sends **incremental, triggered updates** — only when the network topology actually changes. Routers maintain neighbor relationships through lightweight hello packets (sent every 5 seconds on most links) and use reliable transport to ensure updates are received. This dramatically reduces bandwidth consumption. EIGRP also uses a **composite metric** that considers bandwidth, delay, reliability, and load on each link, allowing it to make intelligent path selections that RIP's simple hop count cannot. A path through two high-speed links is correctly preferred over a path through one slow link, even though the latter has fewer hops.

When no feasible successor exists for a failed route, EIGRP enters an **active state** for that destination and sends queries to its neighbors, asking if they have an alternative path. Those neighbors may query their own neighbors, diffusing the computation outward through the network — hence the name "diffusing update algorithm." Once all queries are answered, the router either installs a new route or declares the destination unreachable. This query process is the main risk in large EIGRP networks: if queries propagate widely (a condition called **stuck in active**), convergence can be slow. Proper network design with route summarization at boundaries limits query scope and keeps EIGRP's convergence fast even in large deployments.
