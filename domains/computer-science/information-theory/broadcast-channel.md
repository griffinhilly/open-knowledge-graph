---
id: broadcast-channel
title: Broadcast Channel
domain: computer-science
course: information-theory
prerequisites:
- id: channel-capacity
  type: hard
- id: network-information-theory
  type: hard
- id: mutual-information
  type: hard
tags:
- broadcast channel
- superposition coding
- degraded
- multi-user
- downlink
stage: expert
status: validated
---

# Broadcast Channel

## Core Idea
The broadcast channel (BC) models one sender transmitting independent messages to multiple receivers through a shared medium. Unlike the MAC (many-to-one), the BC is one-to-many. For the degraded BC (where receiver 2's signal is a noisier version of receiver 1's), superposition coding achieves capacity: the sender layers messages at different power levels, and stronger receivers decode all layers while weaker receivers decode only their own. The Gaussian BC capacity region is fully characterized and equals the MAC capacity region by duality. The general (non-degraded) BC capacity region remains incompletely characterized, though Marton's inner bound is known to be tight in many cases.

## Questions

```yaml
- question: "In a degraded Gaussian broadcast channel, user 1 has better SNR than user 2. The sender uses superposition coding, allocating power alpha*P to user 2's message and (1-alpha)*P to user 1's message (0 < alpha < 1). Why does user 2 get more power?"
  type: multiple-choice
  options:
    - "User 2 needs more power because they have a weaker channel — their message must be robust enough to decode despite higher noise"
    - "User 2 always has higher priority in broadcast systems"
    - "The power allocation is arbitrary and does not affect capacity"
    - "User 1 gets more power because they have the better channel"
  answer: 0
  explanation: "In superposition coding, user 2's message is encoded at higher power so that BOTH receivers can decode it — user 2 (weak receiver) decodes only this high-power layer. User 1 (strong receiver) first decodes user 2's message (treating user 1's message as noise), subtracts it (like SIC), then decodes their own lower-power message from the residual. The stronger receiver can afford to decode the weaker receiver's message because it has better channel quality. The power split alpha controls the rate tradeoff between users."

- question: "The broadcast channel is simply the multiple access channel with the communication direction reversed, so their capacity regions are identical."
  type: true-false
  answer: false
  explanation: "The BC and MAC are duals in a specific mathematical sense — the Gaussian BC and MAC capacity regions are related by a duality transformation (the sum-power constraint maps between them). But they are NOT 'the same channel reversed.' The MAC has independent senders with no coordination; the BC has a single sender with full control. The MAC uses SIC at the receiver; the BC uses superposition coding at the transmitter. The achievability techniques, converse proofs, and information-theoretic challenges are different. The MAC capacity region is completely known for general channels; the general BC is not."

- question: "Explain superposition coding and why it outperforms time-division (TDMA) on the degraded broadcast channel."
  type: short-answer
  answer: "In superposition coding, the sender transmits both messages simultaneously: X = X_1 + X_2, where X_2 (for the weaker user) has higher power alpha*P and X_1 (for the stronger user) has power (1-alpha)*P. The weak user decodes X_2 while treating X_1 as noise. The strong user first decodes X_2 (because they have a better channel), subtracts it, then decodes X_1. Both users receive data simultaneously without dividing time or bandwidth. TDMA gives user 1 a fraction t of the time at full power and user 2 the remaining (1-t), so each user's rate is scaled by their time fraction. Superposition coding beats TDMA because the strong user can 'see through' the weak user's message, extracting their own message from the residual — this concurrent transmission utilizes the channel more efficiently than orthogonal sharing."
  explanation: "The intuition is that the channel quality difference between users is an asset, not a liability. The strong user's ability to decode the weak user's message first creates a natural layering that TDMA cannot exploit. This is the information-theoretic basis for NOMA (non-orthogonal multiple access) in 5G downlink."
```

## Explainer

The broadcast channel is the canonical downlink model: a base station sending different messages to multiple users, a satellite broadcasting different programs, or a server transmitting to multiple clients with different connection qualities. One transmitter, multiple receivers, each wanting their own message.

The simplest and best-understood case is the **degraded broadcast channel**, where the receivers can be ordered by quality — receiver 1 gets a strictly better version of the signal than receiver 2. For the Gaussian case, Y_1 = X + Z_1 and Y_2 = X + Z_2 with N_1 < N_2 (user 1 has less noise). The capacity-achieving strategy is **superposition coding**: encode user 2's message as a "cloud center" at high power, and encode user 1's message as a "cloud point" at lower power around this center. User 2 (weak) treats user 1's signal as noise and decodes the cloud center. User 1 (strong) first decodes user 2's message (the cloud center), subtracts it, then decodes their own message from the residual.

The capacity region for the two-user degraded Gaussian BC is: R_2 <= (1/2) log(1 + alpha*P/(( 1-alpha)*P + N_2)) and R_1 <= (1/2) log(1 + (1-alpha)*P/N_1), for alpha in [0,1]. As alpha varies, the tradeoff between user rates traces the capacity region boundary. Setting alpha = 1 gives all power to user 2 (R_1 = 0); setting alpha = 0 gives all power to user 1 (R_2 = 0). No TDMA or FDMA scheme can match the superposition coding boundary — orthogonal schemes are strictly suboptimal.

The general (non-degraded) broadcast channel is far harder. When receivers are not ordered by quality (e.g., one receiver is better at low frequencies, the other at high frequencies), superposition coding alone is insufficient. Marton's coding scheme, which uses correlated auxiliary random variables, provides the best known inner bound and is tight for several important classes. The general BC capacity region remains one of the major open problems in information theory, highlighting how multi-user problems can be vastly more complex than their single-user counterparts.
