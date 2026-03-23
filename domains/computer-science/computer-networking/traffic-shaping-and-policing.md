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
status: validated
---

# Traffic Shaping and Policing

## Core Idea
Traffic shaping smooths bursty traffic to match a specified rate, buffering excess packets for later transmission without discarding them. Policing enforces a rate limit by discarding excess traffic, providing hard guarantees but risking packet loss. Both techniques use token bucket algorithms and are essential for implementing service-level agreements and preventing congestion.

## Questions

```yaml
- question: "A TCP sender transmits a burst of data at twice its contracted rate for 500ms, then returns to normal. Under traffic shaping, what does the receiver observe?"
  type: multiple-choice
  options:
    - "Packets are delayed but eventually all arrive; TCP sees increased latency but no loss"
    - "All packets exceeding the rate limit are immediately dropped; TCP retransmits them"
    - "The burst passes through unaffected because TCP handles rate control end-to-end"
    - "The sender is disconnected from the network for violating the rate limit"
  answer: 0
  explanation: "Traffic shaping buffers excess packets rather than discarding them. The burst is absorbed into the shaper's queue and released at the configured rate, so all packets arrive — but later than they would have without shaping. TCP sees higher latency and possible jitter, but not packet loss. Under policing, the excess packets would instead be dropped, forcing TCP retransmission."

- question: "In the token bucket algorithm, what does a larger bucket (burst size) allow compared to a smaller one?"
  type: multiple-choice
  options:
    - "Larger bursts of traffic to pass at full rate before rate limiting kicks in"
    - "A higher sustained average rate over time"
    - "Faster token generation, effectively increasing the configured rate"
    - "More packets to be dropped before alerting the network operator"
  answer: 0
  explanation: "The token bucket's burst size determines how many tokens can accumulate. A larger bucket lets more packets pass in a sudden burst (while tokens are plentiful) before the rate limit is enforced. The average sustained rate is still determined by the token generation rate, not the bucket size. A smaller bucket enforces a stricter, more uniform flow."

- question: "Traffic shaping adds latency to excess packets but does not discard them."
  type: true-false
  answer: true
  explanation: "Shaping holds excess packets in a queue until enough tokens are available for transmission — packets are delayed, not dropped. This is its defining characteristic and the key difference from policing. The tradeoff is that buffers add latency and jitter, which matters for real-time applications but is generally acceptable for bulk transfers like file downloads or TCP streams."

- question: "Policing is always preferable to shaping because it never adds latency to network traffic."
  type: true-false
  answer: false
  explanation: "While policing avoids adding latency (excess packets are dropped immediately, not queued), it causes packet loss, which is often worse. Lost packets force TCP retransmission, wasting bandwidth and adding overall delay. For applications where packet loss is costly (file transfers, video streaming), shaping's added latency is usually preferable. Policing is appropriate at network boundaries where the operator has no buffer obligation — not as a universal improvement."

- question: "Why would an ISP deploy policing at its network edge rather than shaping, even though policing causes packet loss for customers who exceed their contracted rate?"
  type: short-answer
  answer: "The ISP's role at its edge is enforcement, not accommodation. The ISP has no obligation to buffer a customer's excess traffic — doing so would consume ISP resources (memory, latency) on behalf of a customer who has exceeded their service agreement. Policing places the cost of rate violation on the offending party: excess packets are dropped, TCP detects loss, and the sender must retransmit. The customer's own edge router should shape outbound traffic to stay within limits; the ISP polices as a backstop to ensure contracted rates are respected regardless."
  explanation: "The placement of shaping vs. policing reflects who owns the buffer. Shapers are deployed where the sender accepts responsibility for smooth delivery; policers are deployed where the network operator enforces a hard contractual limit and bears no obligation for non-conforming traffic."
```

## Explainer

From your study of Quality of Service, you know that network links have finite capacity and that different types of traffic compete for bandwidth. QoS mechanisms classify and prioritize traffic, but classification alone doesn't prevent a single flow from overwhelming a link. **Traffic shaping** and **policing** are the enforcement mechanisms — they control *how much* traffic enters or crosses a network boundary, ensuring that agreed-upon rate limits are respected.

The easiest way to distinguish the two is by analogy. Traffic shaping is like a dam with a spillway: when water flows in faster than the spillway can handle, the excess is held in a reservoir and released gradually. Packets arriving above the configured rate are buffered in a queue and transmitted later, smoothing the flow into a steady stream. The sender experiences added **delay** (latency and jitter increase), but no packets are lost. Policing, by contrast, is like a bouncer at a door: if more people arrive than the venue can hold, the excess are turned away immediately. Packets exceeding the rate limit are **dropped** (or re-marked to a lower priority), with no buffering. The sender must detect the loss and retransmit.

Both mechanisms commonly use the **token bucket algorithm**. Imagine a bucket that fills with tokens at a constant rate — say, one token per microsecond for a 1 Mbps rate limit. Each packet that arrives needs to "spend" tokens equal to its size. If enough tokens are in the bucket, the packet passes immediately. If not, the shaper holds the packet until tokens accumulate, while a policer drops it outright. The bucket has a maximum depth (the **burst size**), which determines how much traffic can pass in a sudden burst before rate limiting kicks in. A larger burst size tolerates short spikes; a smaller one enforces a stricter, more uniform rate.

The choice between shaping and policing depends on where you sit in the network and what you're trying to achieve. **Shapers** are typically deployed on the sender's side — an enterprise router shaping outbound traffic to match the bandwidth purchased from an ISP, for example. The added delay is acceptable because TCP adapts smoothly to a steady rate. **Policers** are typically deployed at network boundaries — an ISP policing incoming traffic from a customer to enforce a service-level agreement. Here, the ISP has no buffer obligation; excess traffic is the customer's problem. In practice, the two are often used together: a customer shapes its outbound traffic to stay within limits, and the ISP polices inbound traffic as a backstop, dropping anything that still exceeds the contracted rate.
