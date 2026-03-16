---
id: ipv4-ipv6-comparison
title: IPv4 vs. IPv6 Comparison
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: ipv6-addressing
  type: hard
builds-toward:
- network-virtualization-network-slicing
tags:
- ipv4
- ipv6
- address-space
- protocol-upgrade
stage: advanced
status: draft
---

# IPv4 vs. IPv6 Comparison

## Core Idea
IPv6 expands address space from 32 bits to 128 bits, eliminating the need for NAT and enabling direct end-to-end communication. IPv6 also simplifies headers, improves security through mandatory IPsec support, and provides better multicast and anycast support. The transition from IPv4 to IPv6 has been gradual because of the installed base of IPv4 infrastructure.

## Explainer

From your study of IPv4 and IPv6 addressing individually, you understand how each protocol assigns addresses and structures its headers. Comparing them side by side reveals not just incremental improvements but a fundamental rethinking of how the Internet's network layer should work. The most visible difference — **32-bit addresses (IPv4) versus 128-bit addresses (IPv6)** — gets the most attention, but the header redesign and the elimination of NAT dependency are equally significant for how networks actually operate.

IPv4's 32-bit address space provides roughly 4.3 billion addresses. That seemed inexhaustible in 1981, but the explosion of connected devices exhausted the free pool by 2011. The Internet has survived on **Network Address Translation (NAT)**, which lets many devices share one public address. NAT works, but it breaks the end-to-end principle: a device behind NAT cannot be directly reached from outside without port forwarding or hole-punching techniques. IPv6's 128-bit space provides 3.4 × 10³⁸ addresses — enough to assign a unique address to every atom on the surface of the Earth, with room to spare. This restores true end-to-end connectivity: every device gets a globally routable address, and protocols that depend on direct reachability (peer-to-peer, VoIP, IoT) work without NAT workarounds.

Beyond address size, IPv6 **simplifies the packet header**. The IPv4 header has 12 fields, a variable-length options section, and requires a header checksum that every router must recompute at each hop (because TTL changes). The IPv6 header has just 8 fixed fields, no checksum (upper-layer protocols like TCP handle integrity), and no in-header options. Optional features use **extension headers** — a chain of next-header pointers that routers can skip unless the header is specifically addressed to them. This means routers can forward most IPv6 packets by examining only the fixed 40-byte base header, improving forwarding speed. IPv6 also eliminates fragmentation by routers — the source must perform **Path MTU Discovery** and fragment at the source if needed, simplifying router processing.

The transition from IPv4 to IPv6 has been the slowest protocol migration in Internet history, spanning decades. The core problem is that IPv4 and IPv6 are **not directly compatible** — an IPv4-only host cannot communicate with an IPv6-only host without translation. Three main transition mechanisms exist: **dual-stack** (running both protocols simultaneously), **tunneling** (encapsulating IPv6 packets inside IPv4 for transit across IPv4-only segments), and **translation** (NAT64/DNS64, which converts between protocols at network boundaries). Most major networks today run dual-stack, with IPv6 adoption above 40% globally. The practical lesson is that protocol transitions in deployed networks are constrained not by technical superiority but by the cost of upgrading every device, router, and application in an installed base of billions.
