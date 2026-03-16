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
status: draft
---

# QoS: Quality of Service

## Core Idea
QoS techniques prioritize and shape network traffic to meet application requirements (e.g., low latency for voice, high throughput for video). QoS mechanisms include traffic classification, queue scheduling (e.g., weighted fair queuing), and rate limiting, enabling service providers to offer differentiated services and meet service-level agreements.

## Explainer

Networks carry many kinds of traffic simultaneously — video calls, file downloads, web browsing, database replication — and not all of it is equally sensitive to delay or loss. A video call becomes unusable with 200 ms of added latency, but a file download barely notices. Without intervention, routers treat every packet identically: first in, first out. **Quality of Service (QoS)** is the set of techniques that break this default equality, giving some traffic preferential treatment so that applications with strict requirements actually get what they need.

The first step in any QoS system is **traffic classification**: identifying which packets belong to which category. This can happen by inspecting port numbers (voice traffic often uses specific RTP ports), by reading DSCP markings in the IP header (a 6-bit field specifically designed for QoS labeling), or by deep packet inspection. Once classified, packets enter different **queues** inside the router. The simplest approach gives high-priority traffic its own queue that is always served first (strict priority queuing), but this risks starving lower-priority traffic entirely. More sophisticated schedulers like **weighted fair queuing (WFQ)** allocate bandwidth proportionally — voice might get 40% of link capacity guaranteed, video 35%, and best-effort traffic the remainder — ensuring every class gets some service while protecting sensitive traffic from congestion.

Beyond scheduling, QoS includes **traffic shaping** and **policing**. Shaping smooths bursty traffic by buffering excess packets and releasing them at a controlled rate, which prevents sudden bursts from overwhelming downstream links. Policing is harsher: packets exceeding the agreed rate are dropped or re-marked to a lower priority. Together, these mechanisms let service providers define **service-level agreements (SLAs)** — contractual guarantees about bandwidth, latency, jitter, and packet loss — and actually enforce them in the network. From your understanding of TCP congestion control, you know that endpoints already try to adapt to network conditions; QoS operates at the network layer to ensure that the conditions themselves are managed, not just reacted to.

The two dominant QoS architectures are **Integrated Services (IntServ)**, which reserves resources per-flow using RSVP signaling, and **Differentiated Services (DiffServ)**, which marks packets into broad classes and lets each router apply per-hop behavior without per-flow state. IntServ provides strong guarantees but scales poorly because every router must track every flow. DiffServ scales well because routers only need to recognize a handful of traffic classes, but its guarantees are statistical rather than absolute. In practice, most modern networks use DiffServ at scale, with IntServ-like reservation applied selectively for the most critical flows.
