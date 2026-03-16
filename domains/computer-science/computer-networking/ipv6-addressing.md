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

## Explainer

From your study of IPv4 addressing, you know the core problem: IPv4 uses 32-bit addresses, giving roughly 4.3 billion unique addresses. That seemed vast in the 1980s, but the explosion of devices — smartphones, IoT sensors, cloud servers — has long since exhausted the supply. Workarounds like NAT (Network Address Translation) have stretched IPv4's life by letting many devices share a single public address, but NAT breaks the original end-to-end principle of the internet and complicates protocols that need direct peer-to-peer connections. **IPv6** was designed as the long-term solution, expanding the address space to **128 bits** — approximately 3.4 × 10^38 unique addresses, enough to assign trillions of addresses to every human on Earth.

IPv6 addresses are written as eight groups of four hexadecimal digits separated by colons: `2001:0db8:0000:0000:0000:0000:0000:0001`. Because these are cumbersome, two **compression rules** simplify notation. First, leading zeros within any group can be dropped: `2001:db8:0:0:0:0:0:1`. Second, the longest consecutive run of all-zero groups can be replaced by a double colon (`::`) — but only once per address, to avoid ambiguity: `2001:db8::1`. Learning to read and expand compressed IPv6 addresses is an essential mechanical skill.

IPv6 addresses have a structured hierarchy. The most common type is a **global unicast address**, analogous to a public IPv4 address. It typically has a 48-bit routing prefix (assigned by ISPs and registries), a 16-bit subnet ID (for internal network segmentation), and a 64-bit interface identifier (unique to the device on that subnet). **Link-local addresses** (prefix `fe80::/10`) are automatically assigned to every IPv6 interface and are used only for communication on the local network segment — they are not routable beyond the link. **Unique-local addresses** (`fc00::/7`) are the IPv6 equivalent of IPv4 private addresses (10.x.x.x, 192.168.x.x), usable within an organization but not routed on the global internet.

One of IPv6's most significant features is **Stateless Address Autoconfiguration (SLAAC)**. In IPv4, most hosts rely on DHCP to get an address. With SLAAC, an IPv6 host can configure its own globally routable address without any server. The host generates its 64-bit interface ID (often derived from its MAC address or generated randomly for privacy), listens for **Router Advertisement** messages that contain the network's 64-bit prefix, and combines the two to form a complete 128-bit address. The host then performs **Duplicate Address Detection (DAD)** using Neighbor Discovery Protocol to ensure no other device on the link has the same address. This plug-and-play capability simplifies network administration dramatically compared to the DHCP-dependent IPv4 world, though DHCPv6 remains available for scenarios requiring more administrative control.
