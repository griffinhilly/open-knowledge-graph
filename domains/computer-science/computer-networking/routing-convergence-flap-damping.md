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
status: validated
---

# Routing Convergence, Flapping, and Damping

## Core Idea
Routing flapping occurs when a route is advertised as up and down repeatedly due to link instability, causing routing churn and traffic loss. BGP flap damping penalizes unstable routes by suppressing them temporarily when they exceed a flap threshold. Proper configuration of dampening parameters balances stability (penalizing flaps) against availability (suppressing stable routes).

## How It's Best Learned
Simulate link flapping in a lab by rapidly toggling interfaces. Observe routing table updates and packet loss. Configure BGP dampening and observe suppression behavior. Monitor flap statistics using show ip bgp flap-statistics.

## Common Misconceptions
Flap damping does not prevent flaps; it hides them after a threshold. Over-aggressive dampening can suppress legitimate route changes. Flap damping should not be applied to eBGP routes learned from direct neighbors; it is most useful for route aggregates.

## Questions

```yaml
- question: "A BGP route flaps 10 times in 20 minutes, accumulating a penalty of 3000. The suppress threshold is 2000. What does the router do with this route?"
  type: multiple-choice
  options:
    - "It withdraws the route from the routing table permanently until manually reset"
    - "It continues advertising the route but doubles the update interval to reduce churn"
    - "It suppresses the route — stops advertising it to BGP neighbors — until the penalty decays below the reuse threshold"
    - "It reroutes traffic over the secondary path and waits for the primary path to stabilize on its own"
  answer: 2
  explanation: "When a route's accumulated penalty exceeds the suppress threshold, BGP flap damping suppresses the route: the router stops advertising it to neighbors. The penalty continues to decay exponentially with the configured half-life. Only when the penalty drops below the reuse threshold is the route advertised again. Crucially, the route is NOT permanently withdrawn — it returns automatically once the penalty decays. Option A is wrong because suppression is temporary. Option B is not how damping works."

- question: "An operator observes that a destination prefix has been unreachable for 45 minutes despite the underlying link being stable for the last 40 minutes. What is the most likely cause?"
  type: multiple-choice
  options:
    - "BGP convergence is inherently slow and 45 minutes is within the normal convergence window"
    - "The route was suppressed by flap damping due to earlier instability, and the penalty has not yet decayed below the reuse threshold"
    - "The router's routing table is full and has dropped the prefix entry"
    - "BGP hold timers have expired and the session is being re-established"
  answer: 1
  explanation: "This is the classic failure mode of over-aggressive flap damping. After the link stabilized, the penalty was still above the suppress threshold, so the route remained hidden from neighbors even though the underlying link was healthy. The half-life determines how long suppression lasts — with a 15-minute half-life and a high penalty, suppression can persist for 30–60 minutes after the link stabilizes. This illustrates why damping parameters must be carefully tuned: overly aggressive thresholds trade availability for stability."

- question: "A route that flaps exactly once will never be suppressed by BGP flap damping, even with very aggressive penalty parameters."
  type: true-false
  answer: true
  explanation: "Flap damping is designed to suppress repeatedly unstable routes while leaving occasionally-flapping routes unaffected. A single flap adds a fixed penalty increment (typically 1000) that begins decaying immediately. For suppression to occur, the penalty must exceed the suppress threshold (typically 2000). A single flap can only reach that threshold if the penalty increment itself exceeds the threshold, which standard configurations do not allow. The mechanism is specifically designed this way — planned maintenance events that cause a one-time route withdrawal should not trigger suppression."

- question: "BGP flap damping prevents route flapping by stabilizing the underlying link before advertising the route to neighbors."
  type: true-false
  answer: false
  explanation: "Flap damping does not prevent flaps — it hides them. The link continues to go up and down; the local router's routing table still reflects these changes. What damping does is suppress the route advertisements sent to BGP neighbors, so those neighbors do not receive the repeated withdraw/re-announce updates. The instability itself is not fixed — it is merely concealed from the rest of the network. This distinction matters: operators must still fix the underlying link issue; damping is only a tool to prevent the instability from propagating churn across the internet."

- question: "Explain the difference between routing convergence and routing churn, and why route flapping makes routing churn a global internet problem rather than a local one."
  type: short-answer
  answer: "Routing convergence is the process by which all routers agree on a consistent topology after a change — it is a transition from one stable state to another. Routing churn is the ongoing processing load on routers from a stream of update messages, particularly when those updates do not lead to a new stable state. Route flapping generates churn because each flap causes a withdraw message followed by a re-announce message that propagates outward through the BGP mesh. Every router that receives these updates must recalculate its forwarding table. A single flapping link in one autonomous system can generate thousands of update messages across hundreds of global routers, consuming CPU on core infrastructure that has nothing to do with the flapping link. The problem is global because BGP's update propagation is internet-wide."
  explanation: "The distinction between convergence (finite, goal-directed) and churn (ongoing, resource-consuming) is key to understanding why flap damping exists. Convergence is acceptable and necessary; churn is pathological. Damping is justified because it trades a delay in convergence (routes take longer to re-stabilize) for elimination of churn. The tradeoff only makes sense when the instability is genuine — which is why damping should be conservative and targeted at aggregate routes rather than specific prefixes."
```

## Explainer

From your study of routing algorithms and BGP, you know that routers exchange reachability information and update their forwarding tables when the network topology changes. **Routing convergence** is the process by which all routers in the network agree on a consistent view of the topology after a change. During convergence, some routers have stale information while others have already updated, causing packets to be dropped, looped, or black-holed. The faster a network converges, the shorter this window of instability — but convergence speed depends on how quickly change notifications propagate and how many routers must recalculate their tables.

**Route flapping** is what happens when a route alternates rapidly between available and unavailable — typically because a physical link is unstable (a damaged cable, an overheating interface, or an intermittent connection). Each time the route goes down, the router withdraws it from its BGP neighbors. Each time it comes back, the router re-advertises it. These updates ripple outward through the internet's BGP mesh. A single flapping link in one autonomous system can generate thousands of update messages across hundreds of routers worldwide, each one triggering a table recalculation. This is called **routing churn**, and at scale it can consume so much CPU on core routers that it destabilizes routes that have nothing to do with the flapping link.

**Flap damping** is BGP's defense mechanism. Each route is assigned a penalty score that increases every time the route flaps. When the penalty exceeds a **suppress threshold**, the route is suppressed — the router stops advertising it to its neighbors, effectively hiding the instability. The penalty decays exponentially over time with a configurable **half-life** (typically 15 minutes). Once the penalty drops below a **reuse threshold**, the route is unsuppressed and advertised again. The key insight is that a route that flaps once or twice will never accumulate enough penalty to be suppressed, but a route that flaps repeatedly will be quickly silenced until it stabilizes.

The art of configuring flap damping lies in balancing stability against reachability. If thresholds are too aggressive, even legitimate route changes (like a planned maintenance event) can trigger suppression, making destinations unreachable for minutes longer than necessary. If thresholds are too lenient, flapping routes continue to generate churn. Modern best practice, informed by RFC 7196, recommends using flap damping conservatively — primarily on aggregate routes rather than specific prefixes, and with half-lives and thresholds tuned to the network's tolerance for convergence delay. Many operators have disabled flap damping entirely for directly connected eBGP peers, preferring fast convergence over churn reduction at the edge.
