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
status: draft
---

# EIGRP: Enhanced Interior Gateway Routing Protocol

## Core Idea
EIGRP (Enhanced Interior Gateway Routing Protocol) is a Cisco proprietary distance-vector protocol that uses a composite metric of bandwidth, delay, reliability, and load. It converges faster than RIP using the Diffusing Update Algorithm (DUAL) and maintains backup routes (feasible successors). EIGRP sends incremental updates only when topology changes, reducing overhead significantly.

## How It's Best Learned
Deploy EIGRP on Cisco equipment or GNS3 with IOS images. Observe DUAL calculations and feasible successor selection. Cause link failures and measure convergence compared to RIP. Configure EIGRP for IPv6 (EIGRPv6) and compare protocol behavior.

## Common Misconceptions
EIGRP is not proprietary in modern versions; Cisco submitted it as an IETF draft but does not enforce patents. EIGRP does not send periodic updates like RIP; it sends triggered updates only. Feasible distance is not the same as advertised distance from the neighbor.

## Explainer

From your study of distance-vector routing protocols and RIP, you know the basic model: each router maintains a table of distances to every destination, shares that table with its neighbors, and updates its routes when it learns of a shorter path. RIP works, but it has serious limitations — it converges slowly after topology changes, is vulnerable to routing loops during convergence, and uses hop count as its only metric, ignoring link speed entirely. **EIGRP** was designed to keep the simplicity of distance-vector routing while solving all of these problems.

The most important innovation in EIGRP is the **Diffusing Update Algorithm (DUAL)**, which guarantees loop-free routing at every instant — not just after convergence, but during topology changes as well. DUAL achieves this by tracking two key values for every route: the **feasible distance (FD)**, which is the best known metric from this router to the destination, and the **advertised distance (AD)**, which is the metric a neighbor reports from itself to the destination. A neighbor qualifies as a **feasible successor** — a guaranteed loop-free backup — only if its advertised distance is strictly less than the current feasible distance. This condition ensures that the backup neighbor is genuinely closer to the destination and cannot be routing through you, which would create a loop. When the primary route fails, EIGRP can instantly switch to a feasible successor without querying other routers, enabling sub-second failover.

Unlike RIP, which broadcasts its entire routing table every 30 seconds regardless of whether anything changed, EIGRP sends **incremental, triggered updates** — only when the network topology actually changes. Routers maintain neighbor relationships through lightweight hello packets (sent every 5 seconds on most links) and use reliable transport to ensure updates are received. This dramatically reduces bandwidth consumption. EIGRP also uses a **composite metric** that considers bandwidth, delay, reliability, and load on each link, allowing it to make intelligent path selections that RIP's simple hop count cannot. A path through two high-speed links is correctly preferred over a path through one slow link, even though the latter has fewer hops.

When no feasible successor exists for a failed route, EIGRP enters an **active state** for that destination and sends queries to its neighbors, asking if they have an alternative path. Those neighbors may query their own neighbors, diffusing the computation outward through the network — hence the name "diffusing update algorithm." Once all queries are answered, the router either installs a new route or declares the destination unreachable. This query process is the main risk in large EIGRP networks: if queries propagate widely (a condition called **stuck in active**), convergence can be slow. Proper network design with route summarization at boundaries limits query scope and keeps EIGRP's convergence fast even in large deployments.
