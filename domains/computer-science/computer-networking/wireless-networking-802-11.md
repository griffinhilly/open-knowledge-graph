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
status: draft
---

# Wireless Networking (802.11 WiFi)

## Core Idea
802.11 (WiFi) is a wireless LAN standard that uses CSMA/CA for medium access and frequency bands like 2.4 GHz and 5 GHz shared with many other devices. Modern standards (802.11ax) achieve multi-gigabit throughput but face challenges from interference and fading. WiFi's simplicity and low cost make it ubiquitous despite its susceptibility to interference.

## Explainer

You already understand network topologies and MAC addressing from your prerequisite work — WiFi builds directly on both. In a wired Ethernet network, devices share a physical medium (the cable) and use MAC addresses to identify each other. **802.11 (WiFi)** does the same thing, but the shared medium is radio spectrum instead of copper. This single change — replacing a wire with radio waves — introduces a cascade of engineering challenges that define how WiFi works.

The most fundamental challenge is **medium access**. On a wired network, a device can listen for traffic before transmitting and detect collisions as they happen (CSMA/CD). Wireless devices cannot reliably detect collisions because a transmitter's own signal drowns out incoming signals — this is called the **hidden node problem**, where two devices out of range of each other can both transmit simultaneously to the same access point, causing a collision neither detects. WiFi solves this with **CSMA/CA (Collision Avoidance)** instead of collision detection. Before transmitting, a device listens to the channel, waits for a random backoff period if the channel is busy, and optionally uses RTS/CTS (Request to Send / Clear to Send) handshakes to reserve the channel. This avoidance strategy is less efficient than detection — it wastes time on waiting and coordination — but it is the best option when you cannot hear collisions.

WiFi operates in unlicensed frequency bands, primarily **2.4 GHz** and **5 GHz** (with 6 GHz added in WiFi 6E). The 2.4 GHz band has only three non-overlapping channels, is shared with Bluetooth, microwave ovens, and countless other devices, and offers longer range but lower throughput. The 5 GHz band provides many more non-overlapping channels and higher throughput but shorter range due to greater signal attenuation through walls. Each successive WiFi generation — from 802.11b (11 Mbps) through 802.11n, 802.11ac, to **802.11ax (WiFi 6)** — has introduced techniques to push more data through this shared spectrum: wider channels, MIMO (multiple antennas transmitting simultaneously), higher-order modulation, and OFDMA (dividing a channel into sub-carriers assigned to different clients).

The WiFi frame format extends Ethernet's MAC addressing with additional fields needed for wireless operation. Where an Ethernet frame has two MAC addresses (source and destination), a WiFi frame carries up to four: source, destination, transmitter (the device that put the signal on the air), and receiver (the device that should process it off the air). This distinction matters because in infrastructure mode, the access point acts as a relay — a frame from your laptop to a server passes through the AP, so the transmitter and source are different devices. Understanding this framing, along with the management frames that handle association, authentication, and beaconing, is essential for diagnosing wireless network issues and understanding WiFi security mechanisms like WPA3.
