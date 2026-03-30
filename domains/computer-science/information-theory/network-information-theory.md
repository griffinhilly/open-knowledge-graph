---
id: network-information-theory
title: Network Information Theory
domain: computer-science
course: information-theory
prerequisites:
- id: channel-coding-theorem
  type: hard
- id: channel-capacity
  type: hard
- id: mutual-information
  type: hard
builds-toward:
- slepian-wolf-coding
- multiple-access-channel
- broadcast-channel
tags:
- network
- multi-user
- distributed
- relay
- interference
stage: expert
status: validated
---

# Network Information Theory

## Core Idea
Network information theory extends Shannon's point-to-point results to multi-user communication networks. When multiple senders and/or receivers share a channel, new phenomena arise that have no single-user analog: cooperation, interference, distributed compression, and capacity regions (sets of achievable rate tuples rather than single numbers). The capacity of the multiple access channel, broadcast channel, and interference channel are central problems. While some multi-user capacity regions are fully characterized (multiple access channel, degraded broadcast channel), others remain open after 50+ years (general interference channel, relay channel), making network information theory one of the most active areas of information-theoretic research.

## Questions

```yaml
- question: "In point-to-point information theory, capacity is a single number. In multi-user information theory, it becomes a 'capacity region.' Why?"
  type: multiple-choice
  options:
    - "Multi-user channels have multiple noise sources, each contributing a capacity number"
    - "With multiple users, there is a tradeoff: increasing one user's rate generally decreases what is available for others, so the set of simultaneously achievable rate tuples (R1, R2, ...) forms a region rather than a single point"
    - "Multi-user capacity is undefined, so researchers use regions as approximations"
    - "Capacity regions are used because multi-user channels always have infinite capacity"
  answer: 1
  explanation: "Consider two users sharing a channel. If user 1 transmits at the full channel capacity, user 2 gets nothing. If user 1 is silent, user 2 can transmit at full capacity. Between these extremes lie rate pairs (R1, R2) where both users transmit at reduced rates. The set of all achievable (R1, R2) pairs is the capacity region — a two-dimensional set that captures all possible tradeoffs. The sum-rate (R1 + R2) boundary is analogous to single-user capacity, but the full region gives much richer information about the tradeoffs."

- question: "The capacity of a general multi-user network can always be determined by solving the capacity of each link independently."
  type: true-false
  answer: false
  explanation: "This is one of the deepest differences between single-user and multi-user information theory. In networks, interactions between links create phenomena that link-by-link analysis misses: interference (one user's signal degrades another's), cooperation (users can relay for each other), and distributed compression (correlated sources can be compressed more efficiently together). The capacity of the interference channel — just two sender-receiver pairs sharing a medium — remains an open problem in general, precisely because the coupling between users cannot be decomposed into independent single-user problems."

- question: "Describe the key difference between the multiple access channel (MAC) and the broadcast channel (BC), and explain why the MAC capacity region was characterized decades before the general BC."
  type: short-answer
  answer: "The MAC has multiple senders transmitting to one receiver; the BC has one sender transmitting to multiple receivers. The MAC capacity region is determined by successive decoding: the receiver decodes users one at a time, subtracting each decoded signal before decoding the next. The achievable rate region is a polymatroid characterized by I(X_S; Y | X_{S^c}) for all subsets S. The BC is harder because the sender must simultaneously serve receivers with different channel qualities. For degraded BCs (where one receiver's signal is a degraded version of another's), superposition coding achieves capacity (Cover, 1972). The general BC capacity region was not established until Marton's coding scheme and its converse were completed much later."
  explanation: "Network information theory is characterized by this asymmetry: many problems have elegant achievability schemes but the matching converse is extremely difficult. The general interference channel, relay channel, and non-degraded broadcast channel all illustrate this pattern."
```

## Explainer

Shannon's original theory considers one sender and one receiver. Real communication systems involve many users: cell phones sharing a base station, devices on a Wi-Fi network, satellites communicating with ground stations. Network information theory asks: what are the fundamental limits when multiple communication sessions share the same physical medium?

The simplest multi-user channels illustrate the key ideas. The **multiple access channel** (MAC) has K senders transmitting independent messages to one receiver. The capacity region is the set of rate tuples (R_1, ..., R_K) such that for every subset S of users, sum_{i in S} R_i <= I(X_S; Y | X_{S^c}). The receiver can decode all messages using successive interference cancellation: decode one user, subtract their signal, decode the next. The **broadcast channel** (BC) has one sender transmitting different messages to K receivers. The sender uses superposition coding: layering messages at different power levels so that stronger receivers can decode more layers. The **interference channel** has K sender-receiver pairs sharing the same medium, where each receiver wants only its own message but hears everyone's signal.

The mathematical challenge is that multi-user problems rarely decompose into independent single-user problems. Interference creates coupling between users. Cooperation (through relays or user coordination) can increase capacity beyond what independent links achieve. Distributed source coding (Slepian-Wolf) shows that correlated sources can be compressed to their joint entropy even when the encoders do not communicate. These phenomena — interference, cooperation, and correlation — are fundamentally multi-user and have no single-user analog.

The state of knowledge is uneven. The MAC capacity region is fully known. The degraded broadcast channel capacity is known (superposition coding). The Gaussian interference channel capacity is known in certain regimes (strong interference, very weak interference) but not in general. The relay channel capacity remains open despite being posed by van der Meulen in 1971. Each unsolved problem reveals gaps in our understanding of how information flows through networks — making network information theory one of the richest and most challenging areas of the field.
