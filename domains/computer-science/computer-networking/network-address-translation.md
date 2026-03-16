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
status: draft
---

# Network Address Translation (NAT)

## Core Idea
NAT translates IP addresses in packet headers as they cross a boundary, allowing multiple devices with private addresses to share a single public address. NAT rewrites source addresses in outgoing packets and destination addresses in incoming replies, maintaining a translation table. While NAT was designed as a workaround for IPv4 address scarcity, it also provides a basic security benefit by hiding internal network structure.

## Explainer

From your work on IPv4 addressing, you know that the address space is finite — roughly 4.3 billion addresses — and that private address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) were carved out for internal use precisely because there aren't enough public addresses for every device on Earth. **Network Address Translation** is the mechanism that bridges private and public addressing, letting an entire home or office network reach the internet through a single public IP address.

The core operation is straightforward. When a device on your local network (say, 192.168.1.50) sends a packet to a web server, the NAT router intercepts the outgoing packet and replaces the private source address with its own public address. Crucially, it also records the mapping — which internal device, which internal port, which external port — in a **translation table**. When the web server's reply comes back addressed to the router's public IP and that external port, the router consults its table, rewrites the destination back to 192.168.1.50, and forwards the packet inward. The internal device never knows the rewriting happened; the external server never sees the private address.

The most common form is **Port Address Translation** (PAT), also called NAT overload, where many internal devices share one public IP by distinguishing connections through unique port numbers. If two devices both browse the web simultaneously, the router assigns each a different external port number in its translation table, so it knows which reply belongs to which internal device. This is why hundreds of devices in a coffee shop can share one public address. Static NAT, by contrast, maps one internal address to one public address permanently — useful for servers that need to be reachable from outside.

NAT has consequences beyond address conservation. Because the translation table only has entries for connections initiated from inside, unsolicited inbound traffic gets dropped — providing a rough firewall effect. But this same behavior creates headaches for protocols that embed IP addresses in their payload (like FTP or SIP), for peer-to-peer connections where both sides are behind NAT, and for end-to-end encryption schemes that assume addresses don't change mid-path. Understanding how NAT interacts with routing — your other prerequisite — is essential: the router must perform translation before or after its routing decision, depending on the direction of traffic, and getting this ordering wrong breaks connectivity.
