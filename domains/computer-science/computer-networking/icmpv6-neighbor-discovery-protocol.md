---
id: icmpv6-neighbor-discovery-protocol
title: ICMPv6 and Neighbor Discovery Protocol
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv6-addressing
  type: hard
- id: ipv4-ipv6-comparison
  type: hard
- id: icmp-internet-control-message-protocol
  type: soft
builds-toward:
- ipv6-addressing
- network-security-fundamentals
tags:
- network-layer
- ipv6
- neighbor-discovery
- icmp
stage: advanced
status: draft
---

# ICMPv6 and Neighbor Discovery Protocol

## Core Idea
ICMPv6 Neighbor Discovery Protocol (NDP) replaces IPv4's ARP and provides host and router discovery, address autoconfiguration, and prefix announcement. Router Advertisement messages announce prefixes and configuration parameters, while Neighbor Solicitation/Advertisement messages resolve IPv6 addresses to link-layer addresses. NDP is integral to IPv6's stateless address autoconfiguration.

## How It's Best Learned
Monitor NDP traffic using tcpdump on an IPv6 network or test environment. Configure stateless address autoconfiguration and observe RA/NS/NA message sequences. Test duplicate address detection and understand default router selection.

## Common Misconceptions
NDP is more complex than ARP; it integrates address resolution, router discovery, and configuration. Neighbor Solicitation is not broadcast; it uses IPv6 multicast to the solicited-node multicast group. ICMPv6 cannot be fully blocked without breaking IPv6 functionality.

## Explainer

From your knowledge of IPv6 addressing and the differences between IPv4 and IPv6, you know that IPv6 eliminated ARP and broadcast traffic. But if there is no ARP, how does an IPv6 host figure out the link-layer (MAC) address of a neighbor on the same network segment? And without DHCP being mandatory, how does a host configure its own address automatically? The answer to both questions is the **Neighbor Discovery Protocol (NDP)**, a set of ICMPv6 message types that replaces ARP, DHCP (for basic configuration), and router discovery — functions that were separate and unrelated protocols in IPv4.

NDP uses five ICMPv6 message types, but the most important are **Router Solicitation (RS)**, **Router Advertisement (RA)**, **Neighbor Solicitation (NS)**, and **Neighbor Advertisement (NA)**. When a host comes online, it sends an RS message asking any routers on the link to identify themselves. Routers respond with RA messages that contain the network prefix, the default gateway address, and flags indicating whether the host should use stateless autoconfiguration (SLAAC) or contact a DHCPv6 server. The host then constructs its own IPv6 address by combining the announced prefix with an identifier derived from its MAC address (or a random value for privacy). This is **stateless address autoconfiguration** — the host configures itself without any server maintaining state about the assignment.

Address resolution — the IPv6 equivalent of ARP — works through NS and NA messages. When a host needs the MAC address for a known IPv6 address, it sends an NS message, but not as a broadcast. Instead, it sends to the **solicited-node multicast group**, a special multicast address derived from the last 24 bits of the target IPv6 address. Only hosts whose addresses share those final bits receive the message, which is typically just one host. That host replies with an NA message containing its MAC address. This is far more efficient than ARP's broadcast approach, which interrupts every host on the segment. NDP also performs **Duplicate Address Detection (DAD)**: before using a newly configured address, a host sends an NS for that address. If no one replies, the address is unique and safe to use.

Because NDP is built on ICMPv6 rather than being a separate layer-2 protocol like ARP, it benefits from IPv6's security extensions and can be protected with mechanisms like **SEND (Secure Neighbor Discovery)**, which uses cryptographic signatures to prevent spoofing. However, this tight integration also means that ICMPv6 cannot be firewall-blocked the way ICMP sometimes is in IPv4 networks. Blocking ICMPv6 Neighbor Solicitation or Router Advertisement messages would break address resolution and autoconfiguration entirely, effectively disabling IPv6 on the network. Any security policy for IPv6 must permit essential NDP message types while filtering only the specific ICMPv6 types that are genuinely unnecessary.
