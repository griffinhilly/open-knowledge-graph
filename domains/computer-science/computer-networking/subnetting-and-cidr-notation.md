---
id: subnetting-and-cidr-notation
title: Subnetting and CIDR Notation
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
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
