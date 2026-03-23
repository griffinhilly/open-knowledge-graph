---
id: qos-quality-of-service
title: 'QoS: Quality of Service'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-flow-control-and-congestion-control
  type: soft
tags:
- qos
- traffic-shaping
- prioritization
- sla
- latency
- jitter
stage: advanced
status: validated
---

# QoS: Quality of Service

## Core Idea
QoS techniques prioritize and shape network traffic to meet application requirements (e.g., low latency for voice, high throughput for video). QoS mechanisms include traffic classification, queue scheduling (e.g., weighted fair queuing), and rate limiting, enabling service providers to offer differentiated services and meet service-level agreements.

## Questions

```yaml
- question: "A network uses strict priority queuing with voice traffic in the high-priority queue. During heavy congestion, file-download traffic experiences complete starvation — no packets are delivered for minutes at a time. What alternative scheduling mechanism addresses this problem?"
  type: multiple-choice
  options:
    - "Deep packet inspection, which reclassifies download traffic as high priority during starvation"
    - "Weighted fair queuing, which guarantees a minimum bandwidth share to every traffic class"
    - "RSVP signaling, which reserves bandwidth per-flow before transmission begins"
    - "DSCP remarking, which upgrades lower-priority packets when they have been waiting too long"
  answer: 1
  explanation: "Strict priority queuing always serves the highest-priority queue first, which can completely starve lower-priority traffic when the high-priority queue never empties. Weighted fair queuing (WFQ) allocates bandwidth proportionally — each class gets a guaranteed minimum share even during congestion, preventing starvation while still favoring high-priority traffic. RSVP (option C) is a signaling protocol for IntServ reservation, not a scheduling solution for starvation. DSCP remarking (option D) doesn't exist as described."

- question: "A service provider needs to offer guaranteed per-flow latency and bandwidth to 50,000 active video-conference sessions across a national backbone. Which QoS architecture is most appropriate?"
  type: multiple-choice
  options:
    - "DiffServ, because it provides stronger per-flow guarantees and scales to large networks"
    - "IntServ with RSVP, because it provides hard per-flow reservations — though scalability will be a concern"
    - "Best-effort forwarding with large buffers, because modern links are fast enough to absorb bursts"
    - "DiffServ, because per-hop behavior eliminates the need for any per-flow state across routers"
  answer: 1
  explanation: "IntServ with RSVP provides hard per-flow resource reservations — exactly what's needed for per-flow guarantees. The catch is that every router in the path must maintain state for every active flow, which scales poorly: 50,000 flows × hundreds of routers creates enormous state tables. DiffServ (option A, D) aggregates flows into classes and does NOT provide per-flow guarantees — its guarantees are statistical. This is the core scalability tradeoff between the two architectures."

- question: "In a QoS system using weighted fair queuing, each traffic class is guaranteed a minimum share of bandwidth even when the total offered load exceeds link capacity."
  type: true-false
  answer: true
  explanation: "This is the defining property of weighted fair queuing compared to strict priority queuing. WFQ distributes bandwidth according to configured weights — voice might get 40%, video 35%, best-effort 25% — and each class is served in proportion to its weight even during congestion. This prevents any class from being completely starved, which strict priority queuing does not guarantee."

- question: "DiffServ provides stronger per-flow guarantees than IntServ, which is why it is the preferred architecture for large backbone networks."
  type: true-false
  answer: false
  explanation: "This reverses the tradeoff. IntServ provides stronger per-flow guarantees via RSVP — resources are explicitly reserved for each flow end-to-end. DiffServ only marks packets into broad classes and applies per-hop behaviors; its guarantees are statistical and class-level, not per-flow. DiffServ is preferred in large backbone networks precisely because it scales well (no per-flow state), not because it provides better guarantees. The strength of guarantees and scalability trade off against each other."

- question: "Why is traffic classification the necessary first step in any QoS system, and what information can be used to classify packets?"
  type: short-answer
  answer: "Classification is necessary because QoS can only prioritize traffic if it knows which traffic belongs to which class. Without classification, all packets are indistinguishable and receive the same treatment — the default first-in-first-out behavior that QoS is designed to replace. Classification can use: port numbers (e.g., RTP ports for voice), DSCP bits in the IP header (6-bit field for marking traffic class), protocol type, or deep packet inspection examining payload content. Once classified, packets enter different queues that receive different scheduling treatment."
  explanation: "The scheduling and shaping mechanisms that follow — WFQ, policing, shaping — only work if packets have been sorted into classes. DSCP marking is particularly important because it allows classification to happen once at the network edge (by a trusted device close to the source) and persist hop-by-hop across the backbone without requiring each router to re-inspect every packet."
```

## Explainer

Networks carry many kinds of traffic simultaneously — video calls, file downloads, web browsing, database replication — and not all of it is equally sensitive to delay or loss. A video call becomes unusable with 200 ms of added latency, but a file download barely notices. Without intervention, routers treat every packet identically: first in, first out. **Quality of Service (QoS)** is the set of techniques that break this default equality, giving some traffic preferential treatment so that applications with strict requirements actually get what they need.

The first step in any QoS system is **traffic classification**: identifying which packets belong to which category. This can happen by inspecting port numbers (voice traffic often uses specific RTP ports), by reading DSCP markings in the IP header (a 6-bit field specifically designed for QoS labeling), or by deep packet inspection. Once classified, packets enter different **queues** inside the router. The simplest approach gives high-priority traffic its own queue that is always served first (strict priority queuing), but this risks starving lower-priority traffic entirely. More sophisticated schedulers like **weighted fair queuing (WFQ)** allocate bandwidth proportionally — voice might get 40% of link capacity guaranteed, video 35%, and best-effort traffic the remainder — ensuring every class gets some service while protecting sensitive traffic from congestion.

Beyond scheduling, QoS includes **traffic shaping** and **policing**. Shaping smooths bursty traffic by buffering excess packets and releasing them at a controlled rate, which prevents sudden bursts from overwhelming downstream links. Policing is harsher: packets exceeding the agreed rate are dropped or re-marked to a lower priority. Together, these mechanisms let service providers define **service-level agreements (SLAs)** — contractual guarantees about bandwidth, latency, jitter, and packet loss — and actually enforce them in the network. From your understanding of TCP congestion control, you know that endpoints already try to adapt to network conditions; QoS operates at the network layer to ensure that the conditions themselves are managed, not just reacted to.

The two dominant QoS architectures are **Integrated Services (IntServ)**, which reserves resources per-flow using RSVP signaling, and **Differentiated Services (DiffServ)**, which marks packets into broad classes and lets each router apply per-hop behavior without per-flow state. IntServ provides strong guarantees but scales poorly because every router must track every flow. DiffServ scales well because routers only need to recognize a handful of traffic classes, but its guarantees are statistical rather than absolute. In practice, most modern networks use DiffServ at scale, with IntServ-like reservation applied selectively for the most critical flows.
