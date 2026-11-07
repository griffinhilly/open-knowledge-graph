---
id: multiple-access-protocols
title: "Multiple Access Protocols: ALOHA, CSMA, and Taking Turns"
domain: computer-science
course: computer-networking
prerequisites:
- id: network-fundamentals
  type: hard
- id: error-detection-and-correction
  type: soft
- id: simple-probability
  type: soft
builds-toward:
- ethernet-protocol
- wireless-networking-802-11
tags:
- link-layer
- medium-access-control
- MAC
- ALOHA
- CSMA-CD
- CSMA-CA
- collisions
stage: advanced
status: validated
---
# Multiple Access Protocols: ALOHA, CSMA, and Taking Turns

## Core Idea
When many nodes share one broadcast channel, such as a radio frequency or an old shared Ethernet cable, two frames sent at once collide and are both lost. A multiple access protocol is the set of rules that decides who may transmit when. These protocols fall into three families: channel partitioning (divide the channel by time, frequency or code), random access (transmit freely and recover from collisions, as in ALOHA and CSMA), and taking turns (polling or passing a token). Each family trades efficiency under heavy load against delay and fairness under light load.

## How It's Best Learned
Simulate the channel in class: students "send" by raising a hand in time slots, and two raised hands mean a collision. Run the same activity under fixed time-slot rules, then random rules, then a passed token, and record throughput. Follow with the Kurose and Ross derivation of slotted ALOHA's maximum efficiency, and finish by explaining why Wi-Fi avoids collisions instead of detecting them.

## Common Misconceptions
- Collisions happen only if two nodes start at exactly the same instant. (Because signals take time to travel, a node can sense an idle channel and start sending while another node's frame is already on its way.)
- Wi-Fi uses the same collision detection as classic Ethernet. (802.11 uses collision avoidance, CSMA/CA, with acknowledgments, because a radio cannot easily hear a collision while it is transmitting.)
- Modern Ethernet networks still depend on CSMA/CD. (Switched, full-duplex Ethernet gives each link its own pair of directions, so collisions do not occur and CSMA/CD is not used in practice.)

## Questions

```yaml
- question: "Under the standard model with many active nodes, what is the maximum fraction of time slots that carry a successful frame in slotted ALOHA?"
  type: multiple-choice
  options:
    - "About 18%"
    - "About 37%"
    - "About 50%"
    - "100%"
  answer: 1
  explanation: "The maximum efficiency of slotted ALOHA is 1/e, about 0.37. Unslotted (pure) ALOHA reaches only 1/(2e), about 0.18, because a frame can collide with frames that began during a window twice as long."

- question: "Classic Ethernet's binary exponential backoff has a node, after its n-th collision on a frame, choose K at random from {0, 1, ..., 2^n - 1} and wait K x 512 bit times. After the third collision, what is the range of K?"
  type: multiple-choice
  options:
    - "{0, 1, 2}"
    - "{0, 1, 2, 3}"
    - "{0, 1, ..., 7}"
    - "{0, 1, ..., 15}"
  answer: 2
  explanation: "With n = 3, 2^3 - 1 = 7, so K is chosen from 0 to 7. Doubling the range after each collision spreads retries out more widely as the channel gets busier. Ethernet caps n at 10 for this choice."

- question: "IEEE 802.11 Wi-Fi uses CSMA/CD, aborting a transmission as soon as it detects a collision."
  type: true-false
  answer: false
  explanation: "802.11 uses CSMA/CA (collision avoidance). A wireless sender cannot reliably detect a collision while transmitting, and some collisions are caused by hidden terminals it cannot hear. So it waits random backoff times before sending and relies on acknowledgments to learn whether a frame got through."

- question: "Ten nodes share a channel using TDMA, each owning one fixed time slot out of every ten. Why does this perform poorly when only one node has data to send?"
  type: short-answer
  answer: "The active node may use only its own slot, so it gets just one tenth of the channel's capacity while the other nine slots go unused. Channel partitioning wastes capacity when traffic is bursty or few nodes are active."
  explanation: "Random access protocols avoid that waste because a lone active node can use the full channel. They lose efficiency instead when many nodes are active and collisions become frequent."
```

## Explainer

On a point-to-point link, one sender talks to one receiver and there is nothing to coordinate. Many links are different: a Wi-Fi channel, a cellular frequency or a classic shared Ethernet cable is a **broadcast channel** that every attached node hears. If two nodes transmit at once, their signals interfere, a **collision**, and both frames are lost. A **multiple access protocol** decides who may send when, using only the channel itself to coordinate.

The first family is **channel partitioning**. Time division (TDMA) gives each node a fixed, repeating time slot. Frequency division (FDMA) gives each node its own frequency band. Code division (CDMA) lets all nodes send at once using different codes. Partitioning is fair and collision-free, but a node may use only its share, even when everyone else is idle.

The second family is **random access**: send when you have data, and recover from collisions. It began with ALOHAnet, a packet radio network built at the University of Hawaii around 1970 under Norman Abramson. In **slotted ALOHA**, time is divided into slots. A node sends at the start of a slot, and after a collision it retries in each later slot with some probability p. With many active nodes, the best possible efficiency is 1/e, about 37% of slots.

**CSMA** (carrier sense multiple access) adds a simple rule: listen before talking, and wait if the channel is busy. Collisions still occur, because a signal takes time to travel and a distant node may sense an idle channel after another node has already started. **CSMA/CD** (collision detection), used by classic shared Ethernet, also listens while sending and stops at once when it hears a collision. It then waits a random time chosen by **binary exponential backoff**, doubling the range of possible waits after each collision. Wireless networks use **CSMA/CA** (collision avoidance) instead, because a radio cannot easily hear others while transmitting. An 802.11 node waits a random backoff before sending, and the receiver confirms each frame with an acknowledgment.

The third family is **taking turns**. In **polling**, a controller invites each node to send in order. In **token passing**, a special frame circulates and only its holder may transmit. These schemes avoid collisions and use the channel well under load, but the controller or token is a single point of failure.

Today's switched, full-duplex Ethernet has no shared medium, so CSMA/CD is mostly history there. The same ideas remain central in Wi-Fi, cellular systems and other shared radio links.
