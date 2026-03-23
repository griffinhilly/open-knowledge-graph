---
id: network-address-translation
title: Network Address Translation (NAT)
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: ip-routing-basics
  type: hard
builds-toward:
- firewall-architecture-and-rules
tags:
- nat
- address-translation
- private-addressing
- port-forwarding
stage: advanced
status: validated
---

# Network Address Translation (NAT)

## Core Idea
NAT translates IP addresses in packet headers as they cross a boundary, allowing multiple devices with private addresses to share a single public address. NAT rewrites source addresses in outgoing packets and destination addresses in incoming replies, maintaining a translation table. While NAT was designed as a workaround for IPv4 address scarcity, it also provides a basic security benefit by hiding internal network structure.

## Questions

```yaml
- question: "A device at 192.168.1.100 sends an HTTP request to a web server. The server replies to the NAT router's public IP address. How does the router know to forward the reply to 192.168.1.100 rather than any other internal device?"
  type: multiple-choice
  options:
    - "The web server records the originating private IP in its response headers"
    - "The router's translation table maps the external port used for this connection back to the correct internal device and port"
    - "IPv4 routing automatically routes packets addressed to public IPs back to the originating private device"
    - "The internal device sends a follow-up packet to claim the reply before the router can deliver it elsewhere"
  answer: 1
  explanation: "The translation table is the core mechanism of NAT. When the device initiates the connection, the router records the mapping: internal IP + internal port ↔ external (public) IP + external port. When the server's reply arrives addressed to the public IP and external port, the router looks up that external port in its table, finds the corresponding internal entry, rewrites the destination to 192.168.1.100:internal-port, and forwards the packet inward. Without this stateful table, the router would have no way to determine which internal device originated the flow."

- question: "A game server on the internet wants to initiate a direct connection to a gaming PC behind a home NAT router. What problem does NAT create?"
  type: multiple-choice
  options:
    - "NAT blocks all UDP traffic, which games rely on for low-latency communication"
    - "No translation table entry exists for an unsolicited inbound connection, so the router drops the packet with no destination to forward it to"
    - "The game server can still reach the PC directly by using the PC's private IP address through the public router"
    - "NAT blocks all connections on port numbers above 1024, which most game servers use"
  answer: 1
  explanation: "NAT translation table entries are created when connections are initiated from inside. When the game server sends an unsolicited packet to the router's public IP, no matching entry exists in the table, so the router has no internal address to forward it to and drops the packet. This is often called the 'NAT traversal' problem. Solutions include port forwarding (manually configuring a permanent table entry for a specific internal server), UPnP (letting the internal device request a port mapping automatically), or NAT hole-punching techniques where both peers coordinate through a third party."

- question: "With Port Address Translation (PAT), each device on an internal network must be assigned a unique public IP address to connect to the internet simultaneously."
  type: true-false
  answer: false
  explanation: "PAT's entire purpose is to let many internal devices share a single public IP address simultaneously. It distinguishes concurrent connections by assigning each a unique external port number in the translation table. When two devices both connect to port 80 of web servers, the router maps their connections to different external port numbers (e.g., 192.168.1.100:43210 ↔ public-IP:54001 and 192.168.1.101:49150 ↔ public-IP:54002). The external port number identifies which internal flow a reply belongs to, allowing hundreds of simultaneous connections through one public address."

- question: "NAT provides a basic security benefit by preventing unsolicited inbound connections from reaching internal hosts."
  type: true-false
  answer: true
  explanation: "Because the translation table only contains entries for connections initiated from inside, packets arriving from outside with no matching entry are dropped. This means external hosts cannot spontaneously connect to internal devices — they have no way to reach a device that hasn't already reached out. This is a side effect of NAT's address-translation mechanism, not a designed security feature (for that, you want a proper stateful firewall), but it provides meaningful protection against unsolicited inbound probes and connection attempts."

- question: "Explain step by step how a NAT router routes a reply packet from an external web server back to the correct internal device."
  type: short-answer
  answer: "1) An internal device (e.g., 192.168.1.100:49200) sends a request to an external web server. 2) The NAT router intercepts the outgoing packet, replaces the source address with its own public IP and assigns an external port (e.g., public-IP:54001), and records the mapping (public-IP:54001 ↔ 192.168.1.100:49200) in its translation table. 3) The web server sends its reply to public-IP:54001. 4) The router receives the reply, looks up port 54001 in its translation table, finds the mapping to 192.168.1.100:49200, rewrites the destination IP and port accordingly, and forwards the packet to the internal device. The internal device receives the reply as if no translation occurred."
  explanation: "The statefulness of this mechanism — maintaining the table of active mappings — is what distinguishes NAT from simple routing. It also explains NAT's limitations: the table entry expires when the connection closes, so there is no persistent way to reach an internal host from outside. Static NAT or port forwarding adds permanent entries to solve this for servers."
```

## Explainer

From your work on IPv4 addressing, you know that the address space is finite — roughly 4.3 billion addresses — and that private address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) were carved out for internal use precisely because there aren't enough public addresses for every device on Earth. **Network Address Translation** is the mechanism that bridges private and public addressing, letting an entire home or office network reach the internet through a single public IP address.

The core operation is straightforward. When a device on your local network (say, 192.168.1.50) sends a packet to a web server, the NAT router intercepts the outgoing packet and replaces the private source address with its own public address. Crucially, it also records the mapping — which internal device, which internal port, which external port — in a **translation table**. When the web server's reply comes back addressed to the router's public IP and that external port, the router consults its table, rewrites the destination back to 192.168.1.50, and forwards the packet inward. The internal device never knows the rewriting happened; the external server never sees the private address.

The most common form is **Port Address Translation** (PAT), also called NAT overload, where many internal devices share one public IP by distinguishing connections through unique port numbers. If two devices both browse the web simultaneously, the router assigns each a different external port number in its translation table, so it knows which reply belongs to which internal device. This is why hundreds of devices in a coffee shop can share one public address. Static NAT, by contrast, maps one internal address to one public address permanently — useful for servers that need to be reachable from outside.

NAT has consequences beyond address conservation. Because the translation table only has entries for connections initiated from inside, unsolicited inbound traffic gets dropped — providing a rough firewall effect. But this same behavior creates headaches for protocols that embed IP addresses in their payload (like FTP or SIP), for peer-to-peer connections where both sides are behind NAT, and for end-to-end encryption schemes that assume addresses don't change mid-path. Understanding how NAT interacts with routing — your other prerequisite — is essential: the router must perform translation before or after its routing decision, depending on the direction of traffic, and getting this ordering wrong breaks connectivity.
