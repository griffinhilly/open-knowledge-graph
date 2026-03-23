---
id: ipv4-addressing
title: IPv4 Addressing and Address Classes
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-ip-model
  type: hard
- id: binary-number-system
  type: soft
builds-toward:
- ipv6-addressing
- subnetting-and-cidr-notation
- ip-routing-basics
tags:
- ipv4
- addressing
- classes
- layer-3
stage: advanced
status: validated
---

# IPv4 Addressing and Address Classes

## Core Idea
IPv4 addresses are 32-bit identifiers for hosts on the Internet, typically written in dotted-decimal notation (e.g., 192.168.1.1). Classful addressing (now obsolete) divided addresses into Classes A–E; modern networking uses Classless Inter-Domain Routing (CIDR) for more flexible address allocation.

## How It's Best Learned
Convert IPv4 addresses between decimal and binary; practice identifying address classes and private address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).

## Common Misconceptions
- All IP addresses are globally routable; private addresses (RFC 1918) are only routable within private networks.
- IPv4 address space is infinite; address exhaustion is real and motivated the transition to IPv6.

## Questions

```yaml
- question: "Why can't a device with the private address 192.168.1.50 be directly reached from the public Internet?"
  type: multiple-choice
  options: ["Private addresses use a different protocol than public addresses", "Public Internet routers are configured to drop packets destined for RFC 1918 private ranges", "Private addresses are only 16 bits long and too short for Internet routing", "Private addresses require IPv6 tunneling to be reachable"]
  answer: 1
  explanation: "RFC 1918 defines address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) as private. Internet backbone routers are configured not to route packets destined for these ranges, so traffic to 192.168.1.50 is dropped at the edge of the public Internet. This is why home networks can reuse the same private address space without conflict."

- question: "IPv4 address exhaustion is a theoretical concern only — the 4.3 billion available addresses are more than enough for all devices that need Internet access."
  type: true-false
  answer: false
  explanation: "IPv4 has exactly 2^32 ≈ 4.3 billion addresses, and IANA allocated the last free blocks in 2011. With billions of smartphones, IoT devices, and servers all needing connectivity, the address space ran out. Workarounds like NAT (Network Address Translation) delay the problem, and IPv6 (with 2^128 addresses) is the long-term solution."

- question: "An IPv4 address is written as four decimal numbers separated by dots, such as 10.0.0.1. How many total bits make up the full address, and how many bits does each dot-separated number (octet) represent?"
  type: short-answer
  answer: "32 bits total; each octet is 8 bits. Four octets × 8 bits = 32 bits."
  explanation: "Each number between dots can range from 0 to 255, which is exactly 2^8 = 256 values — 8 bits. Four such octets give 4 × 8 = 32 bits. This is why IPv4 addresses are called 32-bit addresses and why understanding binary is helpful: 192 in binary is 11000000, and so on for each octet."
```

## Explainer

You already know from the TCP/IP model that the Network layer is responsible for delivering packets from one machine to another across multiple networks. IPv4 addressing is the mechanism that makes this possible: every device on an IP network is assigned a 32-bit address that uniquely identifies it, and routers use these addresses to decide where to forward each packet.

IPv4 addresses are written in dotted-decimal notation — four groups of decimal numbers separated by dots, such as 192.168.1.1. Each group (called an octet) represents 8 bits, so the full address is 32 bits. Because you've seen binary, you can see how each octet maps to binary: 192 = 11000000, 168 = 10101000, and so on. This binary representation matters when you later study subnetting and CIDR notation, where you split the address into a network portion and a host portion using a bitmask.

Early IPv4 design used "classful" addressing: Class A addresses started with a 0 bit and used the first octet as the network ID (supporting 16 million hosts per network); Class B used the first two octets; Class C used the first three. This rigid scheme wasted enormous amounts of address space — a company needing 300 addresses had to get a Class B block of 65,536. CIDR (Classless Inter-Domain Routing) replaced classful addressing by allowing any prefix length, written as an address followed by a slash and the number of network bits (e.g., 192.168.1.0/24 for a 24-bit network prefix).

A critical concept is private versus public addresses. RFC 1918 reserves three ranges — 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 — as private. These are not routed on the public Internet; backbone routers simply drop packets destined for them. This lets millions of home networks all use 192.168.1.x without conflict. Network Address Translation (NAT) then allows devices with private addresses to communicate with the public Internet by sharing one public IP.

With only 2^32 ≈ 4.3 billion addresses and billions of Internet-connected devices, IPv4 exhaustion became real (IANA ran out in 2011). IPv6 addresses this by expanding to 128 bits, providing 2^128 addresses — effectively unlimited. Understanding IPv4 fully — its addressing, classes, and limitations — provides the essential foundation for understanding why IPv6 is structured the way it is.
