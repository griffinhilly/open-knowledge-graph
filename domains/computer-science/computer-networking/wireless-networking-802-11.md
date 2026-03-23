---
id: wireless-networking-802-11
title: Wireless Networking (802.11 WiFi)
domain: computer-science
course: computer-networking
prerequisites:
- id: network-topologies
  type: hard
- id: mac-addressing
  type: hard
builds-toward:
- mobile-ip-and-handover
tags:
- wifi
- '802.11'
- wireless
- csma-ca
stage: advanced
status: validated
---

# Wireless Networking (802.11 WiFi)

## Core Idea
802.11 (WiFi) is a wireless LAN standard that uses CSMA/CA for medium access and frequency bands like 2.4 GHz and 5 GHz shared with many other devices. Modern standards (802.11ax) achieve multi-gigabit throughput but face challenges from interference and fading. WiFi's simplicity and low cost make it ubiquitous despite its susceptibility to interference.

## Questions

```yaml
- question: "Two laptops at opposite ends of a large office can each communicate with the central access point but cannot hear each other's transmissions. Both transmit simultaneously. What problem does this illustrate, and how does WiFi address it?"
  type: multiple-choice
  options:
    - "Multipath fading — resolved by MIMO antennas combining multiple signal paths"
    - "The hidden node problem — addressed by CSMA/CA with optional RTS/CTS handshaking to reserve the channel"
    - "Channel saturation — resolved by switching to the 5 GHz band's wider channels"
    - "MAC address collision — resolved by ARP to ensure unique addressing before transmission"
  answer: 1
  explanation: "This is the classic hidden node problem: two devices are hidden from each other but both visible to the access point, so a collision at the AP goes undetected by either sender. CSMA/CA's RTS/CTS mechanism addresses it — a device sends a short RTS frame; the AP replies with a CTS that all nearby devices hear, causing them to defer transmission. The two hidden laptops both hear the CTS and back off."

- question: "Why does 802.11 WiFi use CSMA/CA (Collision Avoidance) rather than CSMA/CD (Collision Detection), which is used in wired Ethernet?"
  type: multiple-choice
  options:
    - "Collision avoidance is faster because it eliminates the need for backoff timers"
    - "Wireless devices transmit and receive on different frequency bands, making CD unnecessary"
    - "A wireless transmitter cannot detect collisions because its own outgoing signal overwhelms any incoming signal during transmission"
    - "The 802.11 standard was designed before collision detection was invented, so avoidance was used for historical reasons"
  answer: 2
  explanation: "In wired Ethernet, a device can compare what it is sending to what it hears on the wire, detecting a mismatch that signals a collision. Wireless devices cannot do this because their own transmitted signal is orders of magnitude stronger than any received signal — the transmitter effectively deafens its own receiver. Since detection is impossible, avoidance through random backoff and optional RTS/CTS is the only viable strategy, even though it wastes time on precaution."

- question: "The 5 GHz WiFi band provides longer wireless range than the 2.4 GHz band because higher frequency signals propagate further."
  type: true-false
  answer: false
  explanation: "False. Higher frequency signals attenuate more rapidly as they pass through walls and obstacles. The 5 GHz band actually has shorter range than 2.4 GHz for this reason. Its advantages are more non-overlapping channels, less interference from Bluetooth and microwaves, and higher throughput — not range. 2.4 GHz penetrates walls better and reaches further, which is why it remains preferred for large or obstacle-heavy environments despite its congestion."

- question: "A WiFi frame in infrastructure mode can carry up to four MAC addresses, whereas an Ethernet frame carries only two."
  type: true-false
  answer: true
  explanation: "True. Ethernet frames identify source and destination. WiFi adds transmitter and receiver fields because the access point acts as a relay in infrastructure mode: a frame from your laptop to an internet server has your laptop's MAC as the source, the server's MAC as the destination, the AP's MAC as the receiver (for the first hop), and your laptop's MAC as the transmitter. The source/transmitter and destination/receiver distinctions only matter because packets must hop through the AP. This extended addressing supports the management frames that handle association, authentication, and beaconing."

- question: "Why is CSMA/CA less efficient than CSMA/CD, and what fundamental property of wireless transmission makes avoidance the only viable option?"
  type: short-answer
  answer: "CSMA/CA wastes channel time on random backoff periods and optional RTS/CTS handshakes even when no collision actually occurs — precautionary delays are built into every transmission. CSMA/CD wastes time only on actual collisions, reacting immediately when they happen. Wireless avoidance is necessary because a transmitting device's own signal is far stronger than any incoming signal, so it cannot hear a collision while transmitting. Without the ability to detect collisions in progress, the device must avoid them before they happen."
  explanation: "The efficiency gap matters especially in high-density WiFi environments where many devices share a channel. Every random backoff represents wasted airtime. 802.11ax (WiFi 6) addresses this with OFDMA, which divides the channel into sub-carriers assigned to different clients simultaneously, reducing the contention problem rather than relying purely on CSMA/CA's collision avoidance for medium access."
```

## Explainer

You already understand network topologies and MAC addressing from your prerequisite work — WiFi builds directly on both. In a wired Ethernet network, devices share a physical medium (the cable) and use MAC addresses to identify each other. **802.11 (WiFi)** does the same thing, but the shared medium is radio spectrum instead of copper. This single change — replacing a wire with radio waves — introduces a cascade of engineering challenges that define how WiFi works.

The most fundamental challenge is **medium access**. On a wired network, a device can listen for traffic before transmitting and detect collisions as they happen (CSMA/CD). Wireless devices cannot reliably detect collisions because a transmitter's own signal drowns out incoming signals — this is called the **hidden node problem**, where two devices out of range of each other can both transmit simultaneously to the same access point, causing a collision neither detects. WiFi solves this with **CSMA/CA (Collision Avoidance)** instead of collision detection. Before transmitting, a device listens to the channel, waits for a random backoff period if the channel is busy, and optionally uses RTS/CTS (Request to Send / Clear to Send) handshakes to reserve the channel. This avoidance strategy is less efficient than detection — it wastes time on waiting and coordination — but it is the best option when you cannot hear collisions.

WiFi operates in unlicensed frequency bands, primarily **2.4 GHz** and **5 GHz** (with 6 GHz added in WiFi 6E). The 2.4 GHz band has only three non-overlapping channels, is shared with Bluetooth, microwave ovens, and countless other devices, and offers longer range but lower throughput. The 5 GHz band provides many more non-overlapping channels and higher throughput but shorter range due to greater signal attenuation through walls. Each successive WiFi generation — from 802.11b (11 Mbps) through 802.11n, 802.11ac, to **802.11ax (WiFi 6)** — has introduced techniques to push more data through this shared spectrum: wider channels, MIMO (multiple antennas transmitting simultaneously), higher-order modulation, and OFDMA (dividing a channel into sub-carriers assigned to different clients).

The WiFi frame format extends Ethernet's MAC addressing with additional fields needed for wireless operation. Where an Ethernet frame has two MAC addresses (source and destination), a WiFi frame carries up to four: source, destination, transmitter (the device that put the signal on the air), and receiver (the device that should process it off the air). This distinction matters because in infrastructure mode, the access point acts as a relay — a frame from your laptop to a server passes through the AP, so the transmitter and source are different devices. Understanding this framing, along with the management frames that handle association, authentication, and beaconing, is essential for diagnosing wireless network issues and understanding WiFi security mechanisms like WPA3.
