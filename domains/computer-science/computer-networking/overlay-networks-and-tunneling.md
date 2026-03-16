---
id: overlay-networks-and-tunneling
title: Overlay Networks and Tunneling
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
builds-toward:
- software-defined-networking
- vpn-virtual-private-networks
tags:
- overlay
- tunneling
- encapsulation
- virtual-networks
stage: advanced
status: draft
---

# Overlay Networks and Tunneling

## Core Idea
Overlay networks layer logical topologies on top of physical networks by tunneling packets from one endpoint to another through intermediate routers. A tunnel encapsulates packets from the overlay network inside packets destined to the tunnel endpoint, where they are decapsulated. Overlays enable VPNs, multicast on unicast-only networks, and experimental protocol deployments.

## Explainer

From your understanding of IP routing, you know that routers forward packets hop by hop based on destination IP addresses, and that the physical topology of the network determines the paths packets can take. An **overlay network** breaks free from this constraint by building a virtual topology on top of the existing one. Two overlay nodes that are separated by dozens of physical routers can appear to be directly connected neighbors in the overlay, because the overlay hides the underlying hops inside a tunnel. Think of it like a private courier service that operates on top of the public highway system — the courier has its own routes and addresses, but every package still physically travels on the same roads as everyone else.

The mechanism that makes overlays work is **tunneling**. When an overlay node wants to send a packet to another overlay node, it wraps (encapsulates) the original packet inside a new outer packet addressed to the tunnel endpoint's real IP address. Intermediate routers along the path see only the outer header and forward the packet normally — they have no idea there is an inner packet riding along. When the packet arrives at the tunnel endpoint, the outer header is stripped off (decapsulated) and the original inner packet is delivered as if it had traveled directly. Common tunneling protocols include GRE, IP-in-IP, and VXLAN, each adding different amounts of overhead and supporting different features.

This architecture is remarkably powerful because it **decouples logical connectivity from physical topology**. A company with offices in New York, London, and Tokyo can create an overlay where all three sites appear to be on the same local network, even though their traffic crosses dozens of ISP routers. VPNs use exactly this approach — encrypting the inner packet before encapsulation so that intermediate routers cannot read the payload. Cloud providers use VXLAN overlays to give each tenant their own isolated virtual network on shared physical infrastructure, with millions of virtual network segments running on top of the same switches.

The tradeoff is overhead and complexity. Every tunneled packet carries extra headers, reducing the effective payload size (the **MTU** shrinks). If the inner packet plus outer headers exceed the link MTU, fragmentation occurs, which hurts performance. Overlay networks also add debugging difficulty — when something goes wrong, you must reason about both the overlay and underlay topologies. Despite these costs, overlays are now ubiquitous: the internet itself was bootstrapped as an overlay on telephone networks, and modern data centers are essentially overlays all the way down.
