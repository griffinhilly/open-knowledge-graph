---
id: ethernet-protocol
title: Ethernet and Frame Structure
domain: computer-science
course: computer-networking
prerequisites:
- id: bandwidth-latency-throughput
  type: soft
builds-toward:
- mac-addressing
- switching-basics
tags:
- ethernet
- link-layer
- frame-format
- lan
stage: advanced
status: draft
---

# Ethernet and Frame Structure

## Core Idea
Ethernet is the dominant Link Layer (Layer 2) technology for local area networks, defining how frames are structured, addressed via MAC addresses, and transmitted over shared or switched media. Modern Ethernet supports speeds from 10 Mbps to 400 Gbps and can work over twisted-pair copper or fiber-optic cable.

## How It's Best Learned
Use packet capture tools (tcpdump, Wireshark) to examine real Ethernet frames, identifying header fields (source/destination MAC, EtherType, CRC) in captured data.

## Common Misconceptions
- Ethernet is only for wired networks; Ethernet frames also travel over wireless via WiFi.
- Ethernet inherently broadcasts; modern switched Ethernet is point-to-point except for broadcast/multicast frames.

## Explainer

From your understanding of bandwidth, latency, and throughput, you know that data transmission involves real physical constraints. **Ethernet** is the technology that defines how devices on a local area network actually package and deliver data across those physical links. It operates at **Layer 2** (the Data Link Layer) of the network stack, sitting between the raw physical transmission of bits (Layer 1) and the logical addressing of IP (Layer 3). Ethernet's job is to move data reliably between two devices that share the same physical network segment.

The fundamental unit of Ethernet communication is the **frame**. Every Ethernet frame has a fixed structure: a **preamble** (8 bytes of alternating bits that help the receiver synchronize its clock), a **destination MAC address** (6 bytes identifying the intended recipient), a **source MAC address** (6 bytes identifying the sender), an **EtherType** field (2 bytes indicating which upper-layer protocol the payload contains — 0x0800 for IPv4, 0x86DD for IPv6), the **payload** (46 to 1,500 bytes of actual data), and a **frame check sequence** (FCS, a 4-byte CRC checksum for error detection). If the receiver computes the CRC and it does not match the FCS, the frame is silently discarded — Ethernet detects errors but does not attempt retransmission; that responsibility falls to higher layers like TCP.

**MAC addresses** (Media Access Control) are the addressing system that Ethernet uses. Each network interface card (NIC) is manufactured with a globally unique 48-bit MAC address, typically written as six hexadecimal pairs like `00:1A:2B:3C:4D:5E`. Unlike IP addresses, which are assigned logically and can change, MAC addresses are tied to the physical hardware. When a device wants to send a frame to another device on the same local network, it must know the destination's MAC address — this is where ARP (Address Resolution Protocol) comes in, translating IP addresses to MAC addresses. The special broadcast address `FF:FF:FF:FF:FF:FF` delivers a frame to every device on the network segment.

Early Ethernet used a shared medium (coaxial cable) where all devices competed for access using **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection) — devices listened before transmitting and backed off if two transmitted simultaneously. Modern Ethernet has largely eliminated this problem by replacing shared cables with **switches** that create dedicated point-to-point links between each device and the switch. Each port on a switch gets the full bandwidth, and the switch forwards frames only to the port where the destination MAC address resides, learning these associations by observing source addresses. This evolution from shared to switched Ethernet is why the technology has scaled from its original 10 Mbps to 400 Gbps and beyond while keeping the same frame format — the framing and addressing are timeless, even as the physical layer underneath has been reinvented repeatedly.
