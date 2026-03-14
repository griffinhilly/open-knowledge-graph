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
