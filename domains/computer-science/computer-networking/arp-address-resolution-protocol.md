---
id: arp-address-resolution-protocol
title: 'ARP: Address Resolution Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: mac-addressing
  type: hard
- id: ipv4-addressing
  type: hard
builds-toward:
- network-security-fundamentals
tags:
- arp
- protocol
- address-resolution
- mac-to-ip
stage: advanced
status: validated
---

# ARP: Address Resolution Protocol

## Core Idea
Address Resolution Protocol (ARP) is a Layer 2.5 protocol that maps IPv4 addresses to MAC addresses on a local network segment. When a host needs to send a packet to a destination IP address on the same link, it broadcasts an ARP request; the host with that IP responds with its MAC address, allowing the sender to frame the packet correctly.

## Questions

```yaml
- question: "Your computer (IP: 192.168.1.10) wants to send a packet to 8.8.8.8. What ARP request does your computer send?"
  type: multiple-choice
  options:
    - "An ARP broadcast asking 'Who has 8.8.8.8?' so it can address the Ethernet frame directly to Google's server"
    - "An ARP broadcast asking for the MAC address of the default gateway (e.g., 192.168.1.1), since 8.8.8.8 is not on the local network"
    - "No ARP request — IP addresses are sufficient for routing to remote destinations"
    - "An ARP unicast sent directly to 8.8.8.8 asking for its MAC address"
  answer: 1
  explanation: "ARP only operates within a local network segment. When the destination IP is on a different subnet, your computer cannot ARP for the remote host's MAC directly — it is unreachable at Layer 2. Instead, the computer ARPs for the MAC address of its default gateway (the router). The router then handles forwarding the packet toward 8.8.8.8. Option A represents the most common misconception: students assume ARP resolves the actual destination's MAC, but that destination may be thousands of hops away with no shared Ethernet segment."

- question: "A host on a local network receives an unsolicited ARP reply stating that MAC address AA:BB:CC:DD:EE:FF belongs to the default gateway's IP address. What does the host do?"
  type: multiple-choice
  options:
    - "Ignore the reply — ARP only processes replies to its own prior requests"
    - "Update its ARP cache with the new mapping, overwriting any existing entry, since ARP has no authentication mechanism"
    - "Verify the claim by querying a central ARP authority before accepting the mapping"
    - "Discard the reply and send its own ARP request to independently verify the gateway's MAC"
  answer: 1
  explanation: "ARP has no authentication mechanism whatsoever. Any host can send an ARP reply — solicited or unsolicited — and the receiving host will update its cache with the claimed mapping. This is the basis of ARP spoofing (ARP poisoning): an attacker sends forged unsolicited ARP replies to redirect traffic through their machine. The fact that ARP caches accept unsolicited replies is a deliberate design for efficiency, but it creates a fundamental security vulnerability exploitable in man-in-the-middle attacks."

- question: "ARP requests are sent as Ethernet unicast frames to the specific host being queried, conserving network bandwidth."
  type: true-false
  answer: false
  explanation: "ARP requests are sent as Ethernet broadcasts with destination MAC FF:FF:FF:FF:FF:FF. This means every device on the local network segment receives the request. Only the host whose IP address matches the request responds (with a unicast ARP reply directly to the requester). The broadcast is necessary because the sender doesn't yet know the target's MAC address — that's precisely what it's trying to find out. The resulting ARP reply is unicast, and the mapping is cached to avoid repeated broadcasts."

- question: "ARP is only needed for communication with devices on the same local network segment; for packets destined to remote networks, ARP is used to resolve the default gateway's MAC address rather than the remote host's MAC."
  type: true-false
  answer: true
  explanation: "This is correct and represents a key architectural insight. ARP operates at Layer 2 and only bridges IP-to-MAC within a local segment. Ethernet frames can only be delivered to hosts on the same physical network. For remote destinations, the Ethernet frame must be addressed to the default gateway (the router) at Layer 2, even though the IP packet is addressed to the final destination at Layer 3. The router then strips the Ethernet frame, reads the IP destination, and forwards the packet toward its next hop — potentially invoking ARP again on its outbound interface."

- question: "Why does ARP resolve the gateway's MAC address for remote destinations instead of the remote host's MAC address? What would fail if a host tried to send an ARP broadcast for a remote host's MAC?"
  type: short-answer
  answer: "Ethernet frames can only traverse a single network segment — they are not routable across the internet. A remote host (e.g., on a different subnet or across the internet) does not share an Ethernet segment with the sender, so broadcasting 'Who has 8.8.8.8?' would never reach that host. The broadcast would be confined to the local segment, where no device knows that remote IP's MAC. Instead, the host addresses the Ethernet frame to the gateway's MAC (resolved via ARP on the local segment), and the IP packet inside carries the final destination's IP. The router handles everything beyond the local segment."
  explanation: "This reveals the clean separation between Layer 2 (Ethernet/MAC — local segment delivery) and Layer 3 (IP — end-to-end logical addressing). ARP exists only to bridge these two layers locally. Each router hop involves its own Layer 2 ARP lookup for the next hop's MAC, while the Layer 3 IP addresses remain constant end-to-end."
```

## Explainer

You already know that IPv4 addresses identify hosts at the network layer and MAC addresses identify network interface cards at the data link layer. These two addressing systems operate independently — an IP address is assigned by network configuration, while a MAC address is burned into the hardware. The fundamental problem ARP solves is bridging this gap: when your computer wants to send a packet to 192.168.1.50 on the local network, it knows the destination IP address but needs the destination MAC address to construct the Ethernet frame. Without the MAC address, the frame cannot be addressed and the switch will not know which port to forward it to.

The **ARP process** works through a simple broadcast-and-reply mechanism. The sender constructs an ARP request containing its own MAC and IP addresses (so the target knows who is asking) and the target IP address, with the target MAC field set to all zeros. This request is sent as an Ethernet broadcast (destination MAC FF:FF:FF:FF:FF:FF), meaning every device on the local network segment receives it. The device whose IP address matches the request responds with an **ARP reply** — a unicast frame sent directly back to the requester — containing its MAC address. The sender then caches this IP-to-MAC mapping in its **ARP table** (also called the ARP cache) so it does not need to broadcast again for subsequent packets to the same destination.

ARP entries have a finite **time-to-live** (typically 1–20 minutes depending on the operating system), after which they expire and must be refreshed. This ensures that if a device changes its network interface or IP assignment, stale mappings do not persist indefinitely. You can inspect the ARP table on most systems with `arp -a`, and you will see entries for every local host your machine has recently communicated with. When the destination IP address is not on the local network, the sender ARPs for the **default gateway's MAC address** instead — the router will handle forwarding the packet to the remote network, but it still needs to be reached via a local Ethernet frame.

ARP's simplicity is also its vulnerability. Because any device can send an ARP reply — even unsolicited — an attacker can send forged ARP replies claiming that their MAC address corresponds to the gateway's IP address. This **ARP spoofing** (or ARP poisoning) attack redirects traffic through the attacker's machine, enabling man-in-the-middle interception. ARP has no authentication mechanism; it trusts every reply it receives. This is why ARP security extensions like Dynamic ARP Inspection (DAI) exist at the switch level, and why IPv6 replaced ARP entirely with the more secure Neighbor Discovery Protocol (NDP).
