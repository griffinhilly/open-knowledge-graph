---
id: ipv6-addressing
title: IPv6 Addressing and Autoconfiguration
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
tags:
- ipv6
- addressing
- 128-bit
- next-generation
stage: advanced
status: draft
---

# IPv6 Addressing and Autoconfiguration

## Core Idea
IPv6 addresses are 128-bit identifiers designed to overcome IPv4 address exhaustion. They are written in hexadecimal with colons (e.g., 2001:db8::1) and include built-in support for address autoconfiguration (SLAAC), allowing hosts to generate globally unique addresses without DHCP.

## How It's Best Learned
Convert IPv6 addresses between full and compressed notation; use IPv6 simulation to test SLAAC and neighbor discovery.

## Common Misconceptions
- IPv6 adoption is near complete; IPv4 still dominates as of 2026.
- IPv6 addresses are all globally routable; link-local and unique-local addresses are not routable globally.

## Questions

```yaml
- question: "A newly connected IPv6 host receives no DHCP response. It has no manually configured address. What does SLAAC allow it to do, and what two pieces of information does it combine to form its address?"
  type: multiple-choice
  options:
    - "It uses ARP to discover an available address on the subnet and claims it by broadcast"
    - "It generates a 64-bit interface ID and waits for a Router Advertisement containing the 64-bit network prefix, then combines the two into a 128-bit global unicast address"
    - "It falls back to a 32-bit IPv4-compatible address automatically converted to IPv6 format"
    - "It assigns itself a link-local address and waits indefinitely until a DHCP server appears"
  answer: 1
  explanation: "SLAAC (Stateless Address Autoconfiguration) is IPv6's plug-and-play address assignment mechanism. The host generates its own 64-bit interface ID (from its MAC address or randomly for privacy), listens for a Router Advertisement (RA) from the local router containing the 64-bit network prefix, and concatenates them to form a 128-bit global unicast address. It then runs Duplicate Address Detection via Neighbor Discovery to verify no other host already uses this address. No server is involved — hence 'stateless.'"

- question: "A packet is destined for fe80::c0a8:1. A router receives it. What should the router do?"
  type: multiple-choice
  options:
    - "Route it normally using the global routing table, since fe80::/10 is a publicly routable prefix"
    - "Drop it or refuse to forward it — link-local addresses are only valid on the local network segment and are not routable beyond the link"
    - "Convert it to an IPv4 address and forward using dual-stack"
    - "Forward it only if the destination is in the same /48 subnet"
  answer: 1
  explanation: "fe80::/10 is the link-local address prefix. Link-local addresses are assigned to every IPv6 interface automatically but are only valid for communication on the same local network segment (link). Routers must not forward packets with link-local source or destination addresses — they have no global meaning beyond the link. This is a common source of confusion: just because a device has an IPv6 address doesn't mean it is globally reachable. Only global unicast addresses (typically 2000::/3) are globally routable."

- question: "In IPv6 compressed notation, the double-colon (::) abbreviation can be used only once per address to avoid ambiguity about how many zero groups are being replaced."
  type: true-false
  answer: true
  explanation: "If two separate runs of all-zero groups could both be compressed to ::, the full address would be unrecoverable — you would not know how many zero groups each :: represented. Allowing :: only once ensures the expansion is unambiguous: the :: represents exactly as many 16-bit all-zero groups as needed to complete the address to eight groups total."

- question: "IPv6 adoption has largely replaced IPv4, and NAT (Network Address Translation) is now obsolete for most modern networks as of 2026."
  type: true-false
  answer: false
  explanation: "Despite decades of effort, IPv4 still dominates internet traffic as of 2026, and NAT remains widespread. While IPv6 deployment has grown substantially, the transition has been far slower than anticipated when IPv4 exhaustion was first projected. Many ISPs, home routers, and enterprise networks operate in dual-stack mode or still run IPv4-only. The predicted full obsolescence of NAT with IPv6 has not arrived — IPv4 addresses continue to circulate through trading markets, and IPv6 deployment remains uneven globally."

- question: "Explain what SLAAC is, why it is a significant improvement over DHCPv4, and what mechanism IPv6 uses to verify that a self-configured address is actually unique."
  type: short-answer
  answer: "SLAAC (Stateless Address Autoconfiguration) lets an IPv6 host configure its own globally routable address without any server: it combines a network prefix from a Router Advertisement with a self-generated 64-bit interface ID. This is a significant improvement over DHCPv4, which requires a dedicated DHCP server to assign and track addresses, creating administrative overhead and a single point of failure. With SLAAC, adding a new host requires no server-side configuration at all. To verify uniqueness, the host performs Duplicate Address Detection (DAD) using Neighbor Discovery Protocol: it sends a Neighbor Solicitation message for its tentative address and listens for any response; if no other device claims the address, it proceeds to use it."
  explanation: "The stateless vs. stateful distinction is key: DHCPv4 requires a server to maintain state (a lease database of which address is assigned to which host). SLAAC distributes that responsibility — each host generates and verifies its own address, with DAD as the collision-avoidance mechanism. DHCPv6 still exists for scenarios requiring central control, but SLAAC is the default in most IPv6 networks."
```

## Explainer

From your study of IPv4 addressing, you know the core problem: IPv4 uses 32-bit addresses, giving roughly 4.3 billion unique addresses. That seemed vast in the 1980s, but the explosion of devices — smartphones, IoT sensors, cloud servers — has long since exhausted the supply. Workarounds like NAT (Network Address Translation) have stretched IPv4's life by letting many devices share a single public address, but NAT breaks the original end-to-end principle of the internet and complicates protocols that need direct peer-to-peer connections. **IPv6** was designed as the long-term solution, expanding the address space to **128 bits** — approximately 3.4 × 10^38 unique addresses, enough to assign trillions of addresses to every human on Earth.

IPv6 addresses are written as eight groups of four hexadecimal digits separated by colons: `2001:0db8:0000:0000:0000:0000:0000:0001`. Because these are cumbersome, two **compression rules** simplify notation. First, leading zeros within any group can be dropped: `2001:db8:0:0:0:0:0:1`. Second, the longest consecutive run of all-zero groups can be replaced by a double colon (`::`) — but only once per address, to avoid ambiguity: `2001:db8::1`. Learning to read and expand compressed IPv6 addresses is an essential mechanical skill.

IPv6 addresses have a structured hierarchy. The most common type is a **global unicast address**, analogous to a public IPv4 address. It typically has a 48-bit routing prefix (assigned by ISPs and registries), a 16-bit subnet ID (for internal network segmentation), and a 64-bit interface identifier (unique to the device on that subnet). **Link-local addresses** (prefix `fe80::/10`) are automatically assigned to every IPv6 interface and are used only for communication on the local network segment — they are not routable beyond the link. **Unique-local addresses** (`fc00::/7`) are the IPv6 equivalent of IPv4 private addresses (10.x.x.x, 192.168.x.x), usable within an organization but not routed on the global internet.

One of IPv6's most significant features is **Stateless Address Autoconfiguration (SLAAC)**. In IPv4, most hosts rely on DHCP to get an address. With SLAAC, an IPv6 host can configure its own globally routable address without any server. The host generates its 64-bit interface ID (often derived from its MAC address or generated randomly for privacy), listens for **Router Advertisement** messages that contain the network's 64-bit prefix, and combines the two to form a complete 128-bit address. The host then performs **Duplicate Address Detection (DAD)** using Neighbor Discovery Protocol to ensure no other device on the link has the same address. This plug-and-play capability simplifies network administration dramatically compared to the DHCP-dependent IPv4 world, though DHCPv6 remains available for scenarios requiring more administrative control.
