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

## Questions

```yaml
- question: "Router R receives an IPv4 datagram of 3000 bytes on an incoming link. The outgoing link has an MTU of 1500 bytes. The DF bit is not set. What does Router R do?"
  type: multiple-choice
  options:
    - "Router R drops the datagram and sends an ICMP Fragmentation Needed message to the source"
    - "Router R queues the datagram until the outgoing link's MTU increases"
    - "Router R splits the datagram into fragments that each fit within 1500 bytes, giving each fragment the same Identification value but different Fragment Offset values"
    - "Router R forwards the oversized datagram anyway, trusting the next router to handle it"
  answer: 2
  explanation: "When the DF bit is clear, IPv4 routers are permitted to fragment. Each fragment gets a copy of the original IP header with the same Identification field (so the destination can group them), different Fragment Offset fields (indicating position in 8-byte units), and the More Fragments flag set on all but the last. Option A describes behavior when DF is SET. Options B and D are not valid IP behavior."

- question: "Fragment 2 of a 4-fragment IPv4 datagram is dropped by a congested router midway to the destination. What happens at the destination?"
  type: multiple-choice
  options:
    - "The destination requests retransmission of the missing fragment from the last router that held it"
    - "The destination reassembles the remaining three fragments and delivers the partial data to the application"
    - "The destination waits for a reassembly timeout, then discards all received fragments — the entire original datagram is lost"
    - "The destination uses the Fragment Offset fields to reconstruct the data, filling the gap with zeros"
  answer: 2
  explanation: "IP reassembly is all-or-nothing. The destination collects fragments and waits for the complete set. If any fragment is missing when the reassembly timer expires (typically 60 seconds), it discards all received fragments. There is no fragment-level retransmission at the IP layer — that responsibility belongs to higher-layer protocols like TCP. This is precisely why fragmentation is expensive: losing one small fragment wastes all the bandwidth consumed by the others."

- question: "In IPv4 networks, intermediate routers are responsible for both fragmenting oversized packets and reassembling them before forwarding."
  type: true-false
  answer: false
  explanation: "Routers in IPv4 can fragment packets but they never reassemble them. Reassembly happens only at the final destination host. This design keeps routers stateless and fast — they do not need to buffer and track fragments across multiple flows. The cost is that any lost fragment must be handled end-to-end. If reassembly happened at routers, every router on the path would need to buffer potentially many incomplete datagrams, adding memory pressure and latency."

- question: "IPv6 routers can fragment packets if needed, but the source host must set a special flag to enable this behavior."
  type: true-false
  answer: false
  explanation: "IPv6 routers cannot fragment packets at all. If an IPv6 packet is too large for the outgoing link, the router drops it and sends an ICMPv6 Packet Too Big message to the source. Only the source host can fragment IPv6 packets, using an extension header. This is a deliberate architectural choice that pushes complexity to the endpoints and keeps the network core fast and simple — a principle sometimes called the end-to-end argument."

- question: "Why does losing a single IP fragment cause the entire original datagram to be discarded, rather than delivering the successfully received portions?"
  type: short-answer
  answer: "IP delivers complete datagrams or nothing — partial datagrams are meaningless to higher-layer protocols. Without the missing fragment, the destination cannot reconstruct the original byte stream; the data would have a gap of unknown content. IP also has no mechanism to request retransmission of individual fragments at the network layer. The all-or-nothing design keeps IP simple and stateless; reliability is the responsibility of transport-layer protocols like TCP, which can detect the loss (via timeout or missing ACK) and retransmit the entire segment."
  explanation: "This also explains why fragmentation is avoided in modern networks: one dropped fragment invalidates all the bandwidth spent delivering the other fragments, making fragmentation disproportionately expensive under packet loss."
```

## Explainer

From your study of IPv4 addressing and the OSI model, you know that IP datagrams carry data across networks by hopping from router to router, and that each link in the path has its own data-link technology (Ethernet, Wi-Fi, PPP, etc.). Each link technology imposes a **Maximum Transmission Unit (MTU)** — the largest frame payload it can carry. Ethernet's MTU is typically 1500 bytes. If a router receives an IP datagram that is larger than the outgoing link's MTU, it cannot forward the datagram as-is. In IPv4, the router's solution is **fragmentation**: splitting the oversized datagram into smaller pieces that each fit within the MTU.

Each fragment is a valid IP datagram in its own right, carrying a copy of the original IP header with a few critical fields adjusted. The **Identification** field stays the same across all fragments of the original datagram, so the receiver knows they belong together. The **Fragment Offset** field tells the receiver where this fragment's data fits within the original datagram, measured in 8-byte units. The **More Fragments (MF)** flag is set to 1 on every fragment except the last one, signaling that more pieces are coming. Using these three fields, the destination host can collect all fragments, arrange them by offset, and reconstruct the original datagram.

Reassembly happens only at the **final destination**, never at intermediate routers. This design keeps routers simple — they only need to fragment, not track and reassemble — but it creates a vulnerability. If any single fragment is lost in transit, the destination cannot reconstruct the original datagram and must discard all received fragments after a reassembly timeout (typically 60 seconds). There is no mechanism to retransmit individual fragments at the IP layer; that responsibility falls to higher layers like TCP. This all-or-nothing property makes fragmentation costly: losing one small fragment wastes the bandwidth consumed by all the others.

Because of these inefficiencies and security concerns (fragmentation has been exploited in various attacks like the "teardrop" attack using overlapping offsets), modern networks actively avoid fragmentation. The **Don't Fragment (DF)** bit in the IP header tells routers to drop the datagram rather than fragment it, returning an ICMP "Fragmentation Needed" message to the sender. The sender then reduces its packet size and retries — a process called **Path MTU Discovery (PMTUD)**. IPv6 took this further by eliminating router-based fragmentation entirely: if a packet is too large, the router drops it and sends an ICMPv6 Packet Too Big message, and only the source host can fragment using an extension header. This pushes the complexity to the endpoints, keeping the network core fast and simple.
