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

## Questions

```yaml
- question: "A switch receives an Ethernet frame destined for a MAC address it has learned. What does the switch do with the frame?"
  type: multiple-choice
  options:
    - "Broadcasts it out all ports so every device can receive it"
    - "Forwards it only to the port associated with the destination MAC address"
    - "Returns an acknowledgment to the sender and buffers the frame"
    - "Floods it out all ports except the source port, then learns the destination"
  answer: 1
  explanation: "Modern switches learn MAC-to-port associations by observing source addresses. When the destination MAC is known, the switch forwards the frame only to that specific port — creating a point-to-point link. This is a critical difference from early shared-medium Ethernet, where every device saw every frame. Broadcasting (option A) only occurs for the all-ones destination address FF:FF:FF:FF:FF:FF or for unknown destinations."

- question: "An Ethernet frame arrives at a NIC and the computed CRC does not match the Frame Check Sequence in the frame. What happens next?"
  type: multiple-choice
  options:
    - "The NIC requests retransmission by sending a NACK to the source"
    - "The frame is corrected using the FCS as an error-correcting code"
    - "The frame is silently discarded; error recovery is handled by higher-layer protocols"
    - "The frame is forwarded anyway with an error flag set in the header"
  answer: 2
  explanation: "Ethernet performs error *detection* only, not correction or retransmission. A mismatched CRC causes the frame to be silently dropped at Layer 2. Recovery — if needed — is the responsibility of higher layers, primarily TCP, which detects missing data through sequence numbers and retransmits. This division of responsibility keeps Ethernet simple and fast while delegating reliability to layers that need it."

- question: "Modern switched Ethernet gives each connected device its own dedicated full-bandwidth link to the switch, unlike early shared-medium Ethernet."
  type: true-false
  answer: true
  explanation: "Early Ethernet used a shared coaxial cable where all devices competed for the medium using CSMA/CD. Modern switches replace this with separate point-to-point links: each port gets the full rated bandwidth, and frames are forwarded selectively rather than broadcast to everyone. This is why CSMA/CD collision handling is essentially irrelevant in modern networks, and why Ethernet has scaled from 10 Mbps to 400 Gbps while keeping the same frame format."

- question: "Ethernet's Frame Check Sequence (FCS) both detects corrupted frames and triggers automatic retransmission to recover the lost data."
  type: true-false
  answer: false
  explanation: "The FCS uses a CRC checksum to *detect* bit errors, but Ethernet does not retransmit. A frame with a bad FCS is silently dropped. Retransmission is left entirely to higher-layer protocols — TCP handles this at the transport layer through acknowledgments and timeouts. Ethernet's design philosophy is to be a fast, simple delivery mechanism; reliability and recovery belong elsewhere in the stack."

- question: "Why does Ethernet detect errors but not correct or retransmit them? Which layer of the network stack takes responsibility for reliable delivery, and how?"
  type: short-answer
  answer: "Ethernet detects errors (via the CRC/FCS) to allow corrupted frames to be discarded quickly, keeping the link layer fast and simple. Retransmission is handled by TCP at the transport layer (Layer 4), which numbers segments, expects acknowledgments, and resends anything not confirmed within a timeout window. This separation follows the end-to-end principle: reliability logic belongs at the endpoints, not in every intermediate link."
  explanation: "The division of responsibility is fundamental to layered network design. If Ethernet retransmitted frames, every link would have to implement complex reliability logic — even on links where data is already reliable (e.g., fiber). By delegating retransmission to TCP, the network stays efficient: UDP applications that don't need reliability avoid the overhead entirely, and TCP applications get reliability at the layer where it's actually needed."
```

## Explainer

From your understanding of bandwidth, latency, and throughput, you know that data transmission involves real physical constraints. **Ethernet** is the technology that defines how devices on a local area network actually package and deliver data across those physical links. It operates at **Layer 2** (the Data Link Layer) of the network stack, sitting between the raw physical transmission of bits (Layer 1) and the logical addressing of IP (Layer 3). Ethernet's job is to move data reliably between two devices that share the same physical network segment.

The fundamental unit of Ethernet communication is the **frame**. Every Ethernet frame has a fixed structure: a **preamble** (8 bytes of alternating bits that help the receiver synchronize its clock), a **destination MAC address** (6 bytes identifying the intended recipient), a **source MAC address** (6 bytes identifying the sender), an **EtherType** field (2 bytes indicating which upper-layer protocol the payload contains — 0x0800 for IPv4, 0x86DD for IPv6), the **payload** (46 to 1,500 bytes of actual data), and a **frame check sequence** (FCS, a 4-byte CRC checksum for error detection). If the receiver computes the CRC and it does not match the FCS, the frame is silently discarded — Ethernet detects errors but does not attempt retransmission; that responsibility falls to higher layers like TCP.

**MAC addresses** (Media Access Control) are the addressing system that Ethernet uses. Each network interface card (NIC) is manufactured with a globally unique 48-bit MAC address, typically written as six hexadecimal pairs like `00:1A:2B:3C:4D:5E`. Unlike IP addresses, which are assigned logically and can change, MAC addresses are tied to the physical hardware. When a device wants to send a frame to another device on the same local network, it must know the destination's MAC address — this is where ARP (Address Resolution Protocol) comes in, translating IP addresses to MAC addresses. The special broadcast address `FF:FF:FF:FF:FF:FF` delivers a frame to every device on the network segment.

Early Ethernet used a shared medium (coaxial cable) where all devices competed for access using **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection) — devices listened before transmitting and backed off if two transmitted simultaneously. Modern Ethernet has largely eliminated this problem by replacing shared cables with **switches** that create dedicated point-to-point links between each device and the switch. Each port on a switch gets the full bandwidth, and the switch forwards frames only to the port where the destination MAC address resides, learning these associations by observing source addresses. This evolution from shared to switched Ethernet is why the technology has scaled from its original 10 Mbps to 400 Gbps and beyond while keeping the same frame format — the framing and addressing are timeless, even as the physical layer underneath has been reinvented repeatedly.
