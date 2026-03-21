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

## Questions

```yaml
- question: "A packet is traveling through a GRE tunnel from a corporate office in New York to one in London. A router in Frankfurt (not an overlay node) handles the packet in transit. What does the Frankfurt router see when it examines the packet's headers?"
  type: multiple-choice
  options:
    - "The original inner packet's source and destination addresses — the corporate office IPs"
    - "Only the outer GRE header with the London tunnel endpoint's real IP as the destination"
    - "Both the inner and outer headers, which it must process to determine the correct route"
    - "An encrypted payload it cannot forward without tunnel decryption keys"
  answer: 1
  explanation: "Intermediate routers see ONLY the outer header. GRE encapsulates the original packet entirely inside a new outer IP packet addressed to the London tunnel endpoint. From Frankfurt's perspective, this is just a normal IP packet destined for a London address — it has no knowledge of the inner packet, the overlay topology, or the corporate network. This invisibility of the inner packet is the fundamental property of tunneling: the underlay routes the outer packet normally while the overlay structure rides invisibly inside."

- question: "Why does tunneling reduce the effective maximum transmission unit (MTU) available for application data compared to a non-tunneled connection?"
  type: multiple-choice
  options:
    - "Encryption adds computational overhead that reduces network throughput"
    - "The outer tunnel headers consume bytes within each packet, leaving less room for the original payload before hitting the physical link's size limit"
    - "Tunnel endpoints must fragment all packets to prevent routing loops in the overlay"
    - "Intermediate routers drop oversized packets because they cannot process two nested headers simultaneously"
  answer: 1
  explanation: "Every physical link has a maximum frame size (MTU, typically 1500 bytes for Ethernet). Tunnel headers — GRE adds ~24 bytes, VXLAN adds ~50 bytes — are part of the outer packet and count against this limit. If the inner packet fills the remaining space, the total outer packet exceeds the link MTU, forcing fragmentation, which hurts performance. Applications and inner protocols must therefore operate with a smaller effective MTU equal to the link MTU minus the tunnel overhead. This overhead is a real and unavoidable cost of overlay networks."

- question: "In an overlay network, the logical topology (which nodes appear to be direct neighbors) determines the physical routes that packets follow through the underlying network."
  type: true-false
  answer: false
  explanation: "The logical overlay topology is completely independent of physical routing. Two overlay nodes that appear as direct neighbors in the overlay may be physically separated by dozens of routers — the overlay link is a tunnel, not a wire. Physical routing is determined by the underlay's routing protocols (OSPF, BGP) applied to the outer packet's destination address. The entire point of overlay networks is this decoupling: any logical topology can be built on top of any physical topology, as long as tunnel endpoints are IP-reachable. The physical and logical layers are orthogonal."

- question: "VPNs typically encrypt the inner packet before encapsulating it in the outer tunnel packet, so intermediate routers cannot read the original payload."
  type: true-false
  answer: true
  explanation: "This is the standard VPN architecture: the inner packet is encrypted before being wrapped in the outer IP packet. Intermediate routers see only an encrypted blob inside a normal outer packet — they can forward it based on the outer destination address but cannot decode its contents. This provides confidentiality: even if an attacker captures packets in transit, they observe only ciphertext. The tunnel delivers the encrypted payload to the remote endpoint, which decrypts and delivers it. Security and connectivity are orthogonal overlay properties that can be combined independently."

- question: "Explain how tunneling 'decouples logical connectivity from physical topology' and give a concrete example where this property is essential."
  type: short-answer
  answer: "Tunneling encapsulates overlay packets inside physical packets routed by the underlay, making two overlay nodes appear directly connected even if physically separated by many routers — the physical routers only see and route the outer header. A concrete example: a company with offices in three cities can create an overlay where all three sites appear on the same local network, with the same IP subnet, even though their traffic crosses public internet routers. VPNs use this to give remote employees seamless access to corporate resources as if physically on the office LAN."
  explanation: "The decoupling is what makes overlays so powerful: any logical topology (star, mesh, full-mesh) can be created without reconfiguring physical hardware. Cloud providers use VXLAN overlays to give each tenant an isolated virtual network on shared physical infrastructure — millions of virtual networks on the same physical switches. The internet itself began as an overlay on telephone networks. The cost of this flexibility is tunnel overhead (extra headers, reduced MTU) and added debugging complexity when problems require reasoning about both the overlay and underlay simultaneously."
```

## Explainer

From your understanding of IP routing, you know that routers forward packets hop by hop based on destination IP addresses, and that the physical topology of the network determines the paths packets can take. An **overlay network** breaks free from this constraint by building a virtual topology on top of the existing one. Two overlay nodes that are separated by dozens of physical routers can appear to be directly connected neighbors in the overlay, because the overlay hides the underlying hops inside a tunnel. Think of it like a private courier service that operates on top of the public highway system — the courier has its own routes and addresses, but every package still physically travels on the same roads as everyone else.

The mechanism that makes overlays work is **tunneling**. When an overlay node wants to send a packet to another overlay node, it wraps (encapsulates) the original packet inside a new outer packet addressed to the tunnel endpoint's real IP address. Intermediate routers along the path see only the outer header and forward the packet normally — they have no idea there is an inner packet riding along. When the packet arrives at the tunnel endpoint, the outer header is stripped off (decapsulated) and the original inner packet is delivered as if it had traveled directly. Common tunneling protocols include GRE, IP-in-IP, and VXLAN, each adding different amounts of overhead and supporting different features.

This architecture is remarkably powerful because it **decouples logical connectivity from physical topology**. A company with offices in New York, London, and Tokyo can create an overlay where all three sites appear to be on the same local network, even though their traffic crosses dozens of ISP routers. VPNs use exactly this approach — encrypting the inner packet before encapsulation so that intermediate routers cannot read the payload. Cloud providers use VXLAN overlays to give each tenant their own isolated virtual network on shared physical infrastructure, with millions of virtual network segments running on top of the same switches.

The tradeoff is overhead and complexity. Every tunneled packet carries extra headers, reducing the effective payload size (the **MTU** shrinks). If the inner packet plus outer headers exceed the link MTU, fragmentation occurs, which hurts performance. Overlay networks also add debugging difficulty — when something goes wrong, you must reason about both the overlay and underlay topologies. Despite these costs, overlays are now ubiquitous: the internet itself was bootstrapped as an overlay on telephone networks, and modern data centers are essentially overlays all the way down.
