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
status: validated
---

# ICMPv6 and Neighbor Discovery Protocol

## Core Idea
ICMPv6 Neighbor Discovery Protocol (NDP) replaces IPv4's ARP and provides host and router discovery, address autoconfiguration, and prefix announcement. Router Advertisement messages announce prefixes and configuration parameters, while Neighbor Solicitation/Advertisement messages resolve IPv6 addresses to link-layer addresses. NDP is integral to IPv6's stateless address autoconfiguration.

## How It's Best Learned
Monitor NDP traffic using tcpdump on an IPv6 network or test environment. Configure stateless address autoconfiguration and observe RA/NS/NA message sequences. Test duplicate address detection and understand default router selection.

## Common Misconceptions
NDP is more complex than ARP; it integrates address resolution, router discovery, and configuration. Neighbor Solicitation is not broadcast; it uses IPv6 multicast to the solicited-node multicast group. ICMPv6 cannot be fully blocked without breaking IPv6 functionality.

## Questions

```yaml
- question: "A network administrator blocks all ICMPv6 traffic on an IPv6 network, reasoning that 'ICMP is non-essential and a security risk.' What will happen?"
  type: multiple-choice
  options:
    - "IPv6 will function normally — NDP uses a separate protocol layer independent of ICMPv6"
    - "Address resolution will fail, autoconfiguration will break, and IPv6 connectivity will be lost"
    - "Security will improve because NDP spoofing attacks will be prevented"
    - "Only ping functionality will be disabled; all other IPv6 traffic will continue normally"
  answer: 1
  explanation: "NDP is built on ICMPv6, not on a separate protocol. Neighbor Solicitation/Advertisement messages (address resolution), Router Advertisement messages (prefix announcements and SLAAC), and Duplicate Address Detection all use specific ICMPv6 types. Blocking all ICMPv6 is equivalent to blocking both ARP and DHCP simultaneously in IPv4 — IPv6 becomes non-functional. This is a critical operational difference from IPv4 networks where ICMP can often be partially blocked. IPv6 firewalls must explicitly permit essential NDP message types (types 133–137) while filtering only genuinely unnecessary ones."

- question: "How does IPv6 Neighbor Solicitation differ fundamentally from IPv4 ARP in its addressing approach?"
  type: multiple-choice
  options:
    - "Neighbor Solicitation uses link-layer broadcast, just like ARP, to reach all hosts on the segment"
    - "Neighbor Solicitation uses solicited-node multicast, so only hosts sharing the target's last 24 address bits receive it"
    - "Neighbor Solicitation is sent as unicast directly to the target's known MAC address"
    - "Neighbor Solicitation is forwarded to the subnet router, which responds on the target's behalf"
  answer: 1
  explanation: "The solicited-node multicast address is derived from the last 24 bits of the target IPv6 address. Since most implementations have unique interface identifiers, typically only the intended target receives the Neighbor Solicitation — rather than every host on the segment, as ARP's broadcast requires. In a network with thousands of hosts, ARP's broadcast forces every single host to wake up and process each address resolution request. NDP's solicited-node multicast targets only the relevant host, dramatically reducing per-host interrupt overhead at scale."

- question: "NDP's Duplicate Address Detection works by sending a Neighbor Solicitation for an address a host wants to use; if no host responds, the address is considered safe to assign."
  type: true-false
  answer: true
  explanation: "Before using any newly configured IPv6 address — whether from SLAAC or manual configuration — a host sends a Neighbor Solicitation for that address addressed to its solicited-node multicast group. If another host already has that address, it responds with a Neighbor Advertisement. Silence means the address is unique and safe to use. This is exactly the DAD mechanism: the host is effectively asking 'does anyone already own this address?' and interpreting silence as 'no.'"

- question: "IPv6's Stateless Address Autoconfiguration (SLAAC) requires a DHCPv6 server to be present on the network, because no host can configure a valid address without external assignment."
  type: true-false
  answer: false
  explanation: "SLAAC is specifically designed to be stateless — hosts configure themselves without any server maintaining allocation records. A host receives the network prefix from a Router Advertisement, then constructs its own interface identifier (from its MAC address or a random privacy value) and combines them to form a complete IPv6 address. No server is needed, and no server tracks the assignment. DHCPv6 is an alternative for environments requiring centralized control, but SLAAC operates entirely without it — this is the meaning of 'stateless.'"

- question: "Why can ICMPv6 not be fully blocked in an IPv6 network, and how does this differ from the treatment of ICMPv4 in many IPv4 networks?"
  type: short-answer
  answer: "ICMPv6 carries NDP — the protocol responsible for address resolution (replacing ARP), router discovery, prefix announcement, and duplicate address detection. These are essential functions for any IPv6 communication, so blocking ICMPv6 disables IPv6 entirely. In IPv4, ARP operates at layer 2 independently of IP, and ICMP is a separate optional layer-3 protocol; many IPv4 functions work even with ICMP blocked. IPv6 consolidated all these functions into ICMPv6, making it inseparable from basic connectivity."
  explanation: "The design choice to build NDP on ICMPv6 rather than a separate layer-2 protocol (like ARP) gives NDP access to IPv6's routing and security features, including SEND (Secure Neighbor Discovery). But it creates an operational consequence: IPv6 firewall rules cannot simply 'block ICMP' as IPv4 admins sometimes do. A properly secured IPv6 network must whitelist essential NDP message types (Router Solicitation 133, Router Advertisement 134, Neighbor Solicitation 135, Neighbor Advertisement 136, Redirect 137) while filtering other ICMPv6 types. Carrying IPv4 firewall habits into IPv6 environments causes immediate connectivity failures."
```

## Explainer

From your knowledge of IPv6 addressing and the differences between IPv4 and IPv6, you know that IPv6 eliminated ARP and broadcast traffic. But if there is no ARP, how does an IPv6 host figure out the link-layer (MAC) address of a neighbor on the same network segment? And without DHCP being mandatory, how does a host configure its own address automatically? The answer to both questions is the **Neighbor Discovery Protocol (NDP)**, a set of ICMPv6 message types that replaces ARP, DHCP (for basic configuration), and router discovery — functions that were separate and unrelated protocols in IPv4.

NDP uses five ICMPv6 message types, but the most important are **Router Solicitation (RS)**, **Router Advertisement (RA)**, **Neighbor Solicitation (NS)**, and **Neighbor Advertisement (NA)**. When a host comes online, it sends an RS message asking any routers on the link to identify themselves. Routers respond with RA messages that contain the network prefix, the default gateway address, and flags indicating whether the host should use stateless autoconfiguration (SLAAC) or contact a DHCPv6 server. The host then constructs its own IPv6 address by combining the announced prefix with an identifier derived from its MAC address (or a random value for privacy). This is **stateless address autoconfiguration** — the host configures itself without any server maintaining state about the assignment.

Address resolution — the IPv6 equivalent of ARP — works through NS and NA messages. When a host needs the MAC address for a known IPv6 address, it sends an NS message, but not as a broadcast. Instead, it sends to the **solicited-node multicast group**, a special multicast address derived from the last 24 bits of the target IPv6 address. Only hosts whose addresses share those final bits receive the message, which is typically just one host. That host replies with an NA message containing its MAC address. This is far more efficient than ARP's broadcast approach, which interrupts every host on the segment. NDP also performs **Duplicate Address Detection (DAD)**: before using a newly configured address, a host sends an NS for that address. If no one replies, the address is unique and safe to use.

Because NDP is built on ICMPv6 rather than being a separate layer-2 protocol like ARP, it benefits from IPv6's security extensions and can be protected with mechanisms like **SEND (Secure Neighbor Discovery)**, which uses cryptographic signatures to prevent spoofing. However, this tight integration also means that ICMPv6 cannot be firewall-blocked the way ICMP sometimes is in IPv4 networks. Blocking ICMPv6 Neighbor Solicitation or Router Advertisement messages would break address resolution and autoconfiguration entirely, effectively disabling IPv6 on the network. Any security policy for IPv6 must permit essential NDP message types while filtering only the specific ICMPv6 types that are genuinely unnecessary.
