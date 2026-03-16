---
id: ip-fragmentation-reassembly
title: IP Fragmentation and Reassembly
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: osi-model-layers
  type: hard
builds-toward:
- path-mtu-discovery-pmtud
- icmp-internet-control-message-protocol
tags:
- network-layer
- ip
- fragmentation
- mtu
stage: advanced
status: draft
---

# IP Fragmentation and Reassembly

## Core Idea
IP fragmentation occurs when a datagram exceeds the Maximum Transmission Unit (MTU) of a network link, splitting it into smaller fragments. Each fragment carries the original IP header plus an offset and a flag indicating more fragments. The destination host reassembles fragments, and loss of any fragment causes the entire datagram to be discarded.

## How It's Best Learned
Use ping with large packet sizes (-s flag) to trigger fragmentation across different network links. Observe fragment reassembly timeouts by dropping fragments in a controlled lab. Compare IPv4 fragmentation with IPv6's approach (no fragmentation at routers).

## Common Misconceptions
Routers fragment packets in IPv4, not TCP; TCP must use MSS negotiation to avoid fragmentation. IPv6 does not fragment at routers; the source must discover MTU via ICMPv6. Fragmentation is not efficient; modern networks prefer to avoid it via MTU discovery.

## Explainer

From your study of IPv4 addressing and the OSI model, you know that IP datagrams carry data across networks by hopping from router to router, and that each link in the path has its own data-link technology (Ethernet, Wi-Fi, PPP, etc.). Each link technology imposes a **Maximum Transmission Unit (MTU)** — the largest frame payload it can carry. Ethernet's MTU is typically 1500 bytes. If a router receives an IP datagram that is larger than the outgoing link's MTU, it cannot forward the datagram as-is. In IPv4, the router's solution is **fragmentation**: splitting the oversized datagram into smaller pieces that each fit within the MTU.

Each fragment is a valid IP datagram in its own right, carrying a copy of the original IP header with a few critical fields adjusted. The **Identification** field stays the same across all fragments of the original datagram, so the receiver knows they belong together. The **Fragment Offset** field tells the receiver where this fragment's data fits within the original datagram, measured in 8-byte units. The **More Fragments (MF)** flag is set to 1 on every fragment except the last one, signaling that more pieces are coming. Using these three fields, the destination host can collect all fragments, arrange them by offset, and reconstruct the original datagram.

Reassembly happens only at the **final destination**, never at intermediate routers. This design keeps routers simple — they only need to fragment, not track and reassemble — but it creates a vulnerability. If any single fragment is lost in transit, the destination cannot reconstruct the original datagram and must discard all received fragments after a reassembly timeout (typically 60 seconds). There is no mechanism to retransmit individual fragments at the IP layer; that responsibility falls to higher layers like TCP. This all-or-nothing property makes fragmentation costly: losing one small fragment wastes the bandwidth consumed by all the others.

Because of these inefficiencies and security concerns (fragmentation has been exploited in various attacks like the "teardrop" attack using overlapping offsets), modern networks actively avoid fragmentation. The **Don't Fragment (DF)** bit in the IP header tells routers to drop the datagram rather than fragment it, returning an ICMP "Fragmentation Needed" message to the sender. The sender then reduces its packet size and retries — a process called **Path MTU Discovery (PMTUD)**. IPv6 took this further by eliminating router-based fragmentation entirely: if a packet is too large, the router drops it and sends an ICMPv6 Packet Too Big message, and only the source host can fragment using an extension header. This pushes the complexity to the endpoints, keeping the network core fast and simple.
