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
status: draft
---

# Subnetting and CIDR Notation

## Core Idea
Subnetting divides an IP address space into smaller networks by using a subnet mask to separate the network portion from the host portion. CIDR notation (e.g., 192.168.1.0/24) compactly represents a network and its prefix length, replacing older classful addressing and enabling efficient address allocation and routing.

## How It's Best Learned
Practice subnetting exercises: given a network and required number of subnets, determine subnet masks and address ranges; verify with online calculators.

## Common Misconceptions
- Subnet masks must align to class boundaries; CIDR allows arbitrary prefix lengths.
- Subnetting is only for IPv4; IPv6 also uses prefix notation and subnetting principles.

## Explainer

From your understanding of IPv4 addressing, you know that every device on a network has a 32-bit IP address written in dotted-decimal form (like 192.168.1.50). But an IP address alone does not tell you which part identifies the network and which part identifies the specific host on that network. That is the job of the **subnet mask** — a 32-bit value where the leading 1-bits mark the network portion and the trailing 0-bits mark the host portion. For example, the mask 255.255.255.0 in binary is 24 ones followed by 8 zeros, meaning the first 24 bits are the network address and the last 8 bits identify hosts within that network.

**CIDR notation** (Classless Inter-Domain Routing) expresses this compactly by appending a slash and the number of network bits: 192.168.1.0/24 means "the network where the first 24 bits are fixed (192.168.1) and the remaining 8 bits vary." The /24 is called the **prefix length**. A /24 network has 2⁸ = 256 addresses (254 usable, since the all-zeros address identifies the network and the all-ones address is the broadcast). A /25 splits that in half — 128 addresses each — and a /16 gives you 65,536 addresses. Your binary arithmetic background is directly useful here: every additional prefix bit halves the number of available host addresses, and every bit removed doubles it.

**Subnetting** is the practice of taking a network and dividing it into smaller subnetworks. Suppose your organization is assigned 10.0.0.0/16 (65,534 usable hosts). You do not want all 65,534 devices on one broadcast domain — that would be chaos. Instead, you subnet: divide /16 into 256 /24 subnets (10.0.0.0/24, 10.0.1.0/24, ..., 10.0.255.0/24), each with 254 hosts. Or divide it into 16 /20 subnets if departments need more hosts per subnet. The process always involves borrowing bits from the host portion to create a longer network prefix.

CIDR replaced the original **classful addressing** system that rigidly divided addresses into Class A (/8), Class B (/16), and Class C (/24) networks. Classful addressing was enormously wasteful — an organization that needed 300 addresses had to receive a Class B with 65,534, wasting over 99%. CIDR allows a prefix of any length, so that organization could receive a /23 (510 usable addresses) — just enough, with minimal waste. This flexibility also enables **route aggregation**: instead of advertising hundreds of individual /24 routes, a router can advertise a single /16 that covers all of them, keeping global routing tables small. Subnetting and CIDR are the tools that made the IPv4 address space last decades longer than it otherwise would have.
