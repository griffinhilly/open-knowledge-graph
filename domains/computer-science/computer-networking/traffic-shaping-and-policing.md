---
id: traffic-shaping-and-policing
title: Traffic Shaping and Policing
domain: computer-science
course: computer-networking
prerequisites:
- id: qos-quality-of-service
  type: hard
tags:
- traffic-shaping
- policing
- rate-limiting
- qos
stage: advanced
status: draft
---

# Traffic Shaping and Policing

## Core Idea
Traffic shaping smooths bursty traffic to match a specified rate, buffering excess packets for later transmission without discarding them. Policing enforces a rate limit by discarding excess traffic, providing hard guarantees but risking packet loss. Both techniques use token bucket algorithms and are essential for implementing service-level agreements and preventing congestion.

## Explainer

From your study of Quality of Service, you know that network links have finite capacity and that different types of traffic compete for bandwidth. QoS mechanisms classify and prioritize traffic, but classification alone doesn't prevent a single flow from overwhelming a link. **Traffic shaping** and **policing** are the enforcement mechanisms — they control *how much* traffic enters or crosses a network boundary, ensuring that agreed-upon rate limits are respected.

The easiest way to distinguish the two is by analogy. Traffic shaping is like a dam with a spillway: when water flows in faster than the spillway can handle, the excess is held in a reservoir and released gradually. Packets arriving above the configured rate are buffered in a queue and transmitted later, smoothing the flow into a steady stream. The sender experiences added **delay** (latency and jitter increase), but no packets are lost. Policing, by contrast, is like a bouncer at a door: if more people arrive than the venue can hold, the excess are turned away immediately. Packets exceeding the rate limit are **dropped** (or re-marked to a lower priority), with no buffering. The sender must detect the loss and retransmit.

Both mechanisms commonly use the **token bucket algorithm**. Imagine a bucket that fills with tokens at a constant rate — say, one token per microsecond for a 1 Mbps rate limit. Each packet that arrives needs to "spend" tokens equal to its size. If enough tokens are in the bucket, the packet passes immediately. If not, the shaper holds the packet until tokens accumulate, while a policer drops it outright. The bucket has a maximum depth (the **burst size**), which determines how much traffic can pass in a sudden burst before rate limiting kicks in. A larger burst size tolerates short spikes; a smaller one enforces a stricter, more uniform rate.

The choice between shaping and policing depends on where you sit in the network and what you're trying to achieve. **Shapers** are typically deployed on the sender's side — an enterprise router shaping outbound traffic to match the bandwidth purchased from an ISP, for example. The added delay is acceptable because TCP adapts smoothly to a steady rate. **Policers** are typically deployed at network boundaries — an ISP policing incoming traffic from a customer to enforce a service-level agreement. Here, the ISP has no buffer obligation; excess traffic is the customer's problem. In practice, the two are often used together: a customer shapes its outbound traffic to stay within limits, and the ISP polices inbound traffic as a backstop, dropping anything that still exceeds the contracted rate.
