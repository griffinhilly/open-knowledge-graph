---
id: routing-convergence-flap-damping
title: Routing Convergence, Flapping, and Damping
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: bgp-border-gateway-protocol
  type: hard
builds-toward:
- network-standards-and-ietf
- network-management-and-monitoring
tags:
- routing
- bgp
- stability
- flap-damping
stage: advanced
status: draft
---

# Routing Convergence, Flapping, and Damping

## Core Idea
Routing flapping occurs when a route is advertised as up and down repeatedly due to link instability, causing routing churn and traffic loss. BGP flap damping penalizes unstable routes by suppressing them temporarily when they exceed a flap threshold. Proper configuration of dampening parameters balances stability (penalizing flaps) against availability (suppressing stable routes).

## How It's Best Learned
Simulate link flapping in a lab by rapidly toggling interfaces. Observe routing table updates and packet loss. Configure BGP dampening and observe suppression behavior. Monitor flap statistics using show ip bgp flap-statistics.

## Common Misconceptions
Flap damping does not prevent flaps; it hides them after a threshold. Over-aggressive dampening can suppress legitimate route changes. Flap damping should not be applied to eBGP routes learned from direct neighbors; it is most useful for route aggregates.

## Explainer

From your study of routing algorithms and BGP, you know that routers exchange reachability information and update their forwarding tables when the network topology changes. **Routing convergence** is the process by which all routers in the network agree on a consistent view of the topology after a change. During convergence, some routers have stale information while others have already updated, causing packets to be dropped, looped, or black-holed. The faster a network converges, the shorter this window of instability — but convergence speed depends on how quickly change notifications propagate and how many routers must recalculate their tables.

**Route flapping** is what happens when a route alternates rapidly between available and unavailable — typically because a physical link is unstable (a damaged cable, an overheating interface, or an intermittent connection). Each time the route goes down, the router withdraws it from its BGP neighbors. Each time it comes back, the router re-advertises it. These updates ripple outward through the internet's BGP mesh. A single flapping link in one autonomous system can generate thousands of update messages across hundreds of routers worldwide, each one triggering a table recalculation. This is called **routing churn**, and at scale it can consume so much CPU on core routers that it destabilizes routes that have nothing to do with the flapping link.

**Flap damping** is BGP's defense mechanism. Each route is assigned a penalty score that increases every time the route flaps. When the penalty exceeds a **suppress threshold**, the route is suppressed — the router stops advertising it to its neighbors, effectively hiding the instability. The penalty decays exponentially over time with a configurable **half-life** (typically 15 minutes). Once the penalty drops below a **reuse threshold**, the route is unsuppressed and advertised again. The key insight is that a route that flaps once or twice will never accumulate enough penalty to be suppressed, but a route that flaps repeatedly will be quickly silenced until it stabilizes.

The art of configuring flap damping lies in balancing stability against reachability. If thresholds are too aggressive, even legitimate route changes (like a planned maintenance event) can trigger suppression, making destinations unreachable for minutes longer than necessary. If thresholds are too lenient, flapping routes continue to generate churn. Modern best practice, informed by RFC 7196, recommends using flap damping conservatively — primarily on aggregate routes rather than specific prefixes, and with half-lives and thresholds tuned to the network's tolerance for convergence delay. Many operators have disabled flap damping entirely for directly connected eBGP peers, preferring fast convergence over churn reduction at the edge.
