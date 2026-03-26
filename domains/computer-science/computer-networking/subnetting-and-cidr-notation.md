---
id: subnetting-and-cidr-notation
title: Subnetting and CIDR Notation
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: binary-arithmetic
  type: soft
- id: number-base-conversion-operations
  type: soft
builds-toward:
- ip-routing-basics
tags:
- subnet
- cidr
- address-aggregation
- prefix-length
stage: advanced
status: validated
---

# Subnetting and CIDR Notation

## Core Idea
Subnetting divides an IP address space into smaller networks by using a subnet mask to separate the network portion from the host portion. CIDR notation (e.g., 192.168.1.0/24) compactly represents a network and its prefix length, replacing older classful addressing and enabling efficient address allocation and routing.

## How It's Best Learned
Practice subnetting exercises: given a network and required number of subnets, determine subnet masks and address ranges; verify with online calculators.

## Common Misconceptions
- Subnet masks must align to class boundaries; CIDR allows arbitrary prefix lengths.
- Subnetting is only for IPv4; IPv6 also uses prefix notation and subnetting principles.

## Questions

```yaml
- question: "A network engineer is assigned the block 10.0.0.0/8 and needs to create subnets with approximately 60 hosts each. Which prefix length should be used for each subnet?"
  type: multiple-choice
  options:
    - "/24, because each /24 provides 254 usable hosts — more than enough for 60"
    - "/26, because 2⁶ = 64 addresses gives 62 usable hosts — the closest fit above 60"
    - "/27, because 2⁵ = 32 addresses gives 30 usable hosts — close enough to 60"
    - "/25, because 2⁷ = 128 addresses provides plenty of capacity for 60 hosts"
  answer: 1
  explanation: "A /26 mask leaves 6 bits for the host portion: 2⁶ = 64 total addresses, minus 2 reserved (network address and broadcast), gives 62 usable host addresses — the smallest subnet that fits 60 hosts. A /25 gives 126 usable hosts but wastes more than half the address space per subnet. A /27 gives only 30 usable hosts — not enough. A /24 gives 254 hosts, which is excessive. CIDR's value is precisely this ability to right-size subnets to actual requirements rather than being forced into classful blocks."

- question: "An ISP assigns 200 customers /24 subnets from the block 10.5.0.0/16. Without route aggregation, upstream routers need 200 routing table entries for these customers. How does CIDR route aggregation improve this?"
  type: multiple-choice
  options:
    - "Aggregation reduces the 200 entries to 200 /16 entries, one per ISP customer"
    - "Aggregation allows the ISP to advertise a single 10.5.0.0/16 route that covers all 200 subnets in one entry"
    - "CIDR automatically aggregates all subnets from the same block at the source router with no configuration needed"
    - "Aggregation has no effect because each /24 is a distinct customer network that must be advertised separately"
  answer: 1
  explanation: "With CIDR route aggregation (sometimes called supernetting), the ISP can advertise a single 10.5.0.0/16 route that summarizes all /24 subnets within that block. Upstream routers see one entry instead of 200. This is one of the primary motivations for CIDR: it allowed the global routing table to remain manageable as the internet grew, rather than exploding with individual subnet routes. The same mechanism scales to ISPs advertising a single /8 or /12 that covers thousands of customer subnets."

- question: "A /25 network contains exactly half the total address space of a /24 network, giving it 128 total addresses (126 usable hosts)."
  type: true-false
  answer: true
  explanation: "Each additional bit in the prefix length halves the address space. A /24 has 2⁸ = 256 total addresses (254 usable). A /25 has 2⁷ = 128 total addresses (126 usable). Conversely, each bit removed from the prefix doubles the address space: a /23 has 2⁹ = 512 total addresses. This binary relationship between prefix length and address count is fundamental to all subnetting calculations — and is why CIDR arithmetic requires solid binary number intuition."

- question: "Under CIDR, subnet masks is expected to correspond to Class A (/8), Class B (/16), or Class C (/24) boundaries to ensure compatibility with modern routers."
  type: true-false
  answer: false
  explanation: "CIDR (Classless Inter-Domain Routing) was specifically designed to eliminate classful constraints. The 'classless' in CIDR means prefix lengths can be any value from /0 to /32, not just the three classful values. An organization needing 300 hosts can receive a /23 (510 usable hosts) rather than being forced into a Class B /16 (65,534 hosts). Classful addressing was the pre-CIDR system that CIDR replaced precisely because rigid class boundaries caused enormous address waste — a Class B wasted 99% of its address space for an organization needing only a few hundred addresses."

- question: "Explain how CIDR notation solves both the address waste problem and the routing table growth problem that plagued classful (Class A/B/C) addressing."
  type: short-answer
  answer: "Classful addressing forced organizations into blocks of /8 (16M hosts), /16 (65K hosts), or /24 (254 hosts). An organization needing 300 hosts had to receive a /16, wasting over 99% of the addresses. CIDR allows any prefix length, so that organization can receive a /23 (510 hosts) — a near-exact fit. For routing table growth: without aggregation, each subnet requires a separate routing table entry. CIDR enables route aggregation — a single /16 advertisement covers 256 individual /24 subnets, keeping routing tables from growing proportionally with the number of networks."
  explanation: "These two benefits — address conservation and routing scalability — are why CIDR allowed IPv4 to survive decades longer than originally projected. Both flow from the same mechanism: flexible, arbitrary prefix lengths that allow both right-sizing of address allocations and hierarchical summarization of routes. IPv6 uses exclusively prefix-based notation for the same reasons."
```

## Explainer

From your understanding of IPv4 addressing, you know that every device on a network has a 32-bit IP address written in dotted-decimal form (like 192.168.1.50). But an IP address alone does not tell you which part identifies the network and which part identifies the specific host on that network. That is the job of the **subnet mask** — a 32-bit value where the leading 1-bits mark the network portion and the trailing 0-bits mark the host portion. For example, the mask 255.255.255.0 in binary is 24 ones followed by 8 zeros, meaning the first 24 bits are the network address and the last 8 bits identify hosts within that network.

**CIDR notation** (Classless Inter-Domain Routing) expresses this compactly by appending a slash and the number of network bits: 192.168.1.0/24 means "the network where the first 24 bits are fixed (192.168.1) and the remaining 8 bits vary." The /24 is called the **prefix length**. A /24 network has 2⁸ = 256 addresses (254 usable, since the all-zeros address identifies the network and the all-ones address is the broadcast). A /25 splits that in half — 128 addresses each — and a /16 gives you 65,536 addresses. Your binary arithmetic background is directly useful here: every additional prefix bit halves the number of available host addresses, and every bit removed doubles it.

**Subnetting** is the practice of taking a network and dividing it into smaller subnetworks. Suppose your organization is assigned 10.0.0.0/16 (65,534 usable hosts). You do not want all 65,534 devices on one broadcast domain — that would be chaos. Instead, you subnet: divide /16 into 256 /24 subnets (10.0.0.0/24, 10.0.1.0/24, ..., 10.0.255.0/24), each with 254 hosts. Or divide it into 16 /20 subnets if departments need more hosts per subnet. The process always involves borrowing bits from the host portion to create a longer network prefix.

CIDR replaced the original **classful addressing** system that rigidly divided addresses into Class A (/8), Class B (/16), and Class C (/24) networks. Classful addressing was enormously wasteful — an organization that needed 300 addresses had to receive a Class B with 65,534, wasting over 99%. CIDR allows a prefix of any length, so that organization could receive a /23 (510 usable addresses) — just enough, with minimal waste. This flexibility also enables **route aggregation**: instead of advertising hundreds of individual /24 routes, a router can advertise a single /16 that covers all of them, keeping global routing tables small. Subnetting and CIDR are the tools that made the IPv4 address space last decades longer than it otherwise would have.
