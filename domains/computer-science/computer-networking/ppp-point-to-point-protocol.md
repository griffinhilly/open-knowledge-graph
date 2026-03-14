---
id: ppp-point-to-point-protocol
title: 'PPP: Point-to-Point Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: osi-model-layers
  type: hard
- id: ethernet-protocol
  type: soft
builds-toward:
- pppoe-protocol-over-ethernet
- network-topologies
tags:
- link-layer
- dialup
- serial
- protocols
stage: advanced
status: draft
---

# PPP: Point-to-Point Protocol

## Core Idea
PPP (Point-to-Point Protocol) is a link-layer protocol for direct serial connections, widely used in dialup modems, leased lines, and wireless links. It provides framing, link negotiation (LCP), and network protocol negotiation (NCP) to support multiple network layers. PPP includes authentication (PAP, CHAP), compression, and error detection mechanisms.

## How It's Best Learned
Set up a PPP connection between two Linux systems using pppd. Monitor LCP and NCP negotiation in debug logs. Test authentication methods and compression to understand negotiation outcomes.

## Common Misconceptions
PPP is not just for dialup; it is used on modern serial and wireless links. LCP negotiates link parameters; NCP negotiates network protocols (IP, IPX, etc.). PPP frames use HDLC-like framing with flag bytes and escape sequences.
