---
id: dhcp-relay-snooping-security
title: DHCP Relay Agents and DHCP Snooping Security
domain: computer-science
course: computer-networking
prerequisites:
- id: dhcp-dynamic-host-configuration
  type: hard
- id: network-security-fundamentals
  type: hard
builds-toward:
- network-security-fundamentals
- network-management-and-monitoring
tags:
- security
- dhcp
- snooping
- link-layer
stage: advanced
status: draft
---

# DHCP Relay Agents and DHCP Snooping Security

## Core Idea
DHCP relay agents forward DHCP broadcasts across subnets to centralized DHCP servers, adding the giaddr field to requests. DHCP snooping, a switch-level security mechanism, learns the binding between MAC addresses, IP addresses, and ports by listening to DHCP messages. It prevents rogue DHCP servers and prevents clients from receiving addresses from untrusted sources.

## How It's Best Learned
Configure a DHCP relay agent on a router and observe giaddr insertion. Set up DHCP snooping on a switch and observe binding database. Attempt to set up a rogue DHCP server and confirm snooping blocks it. Monitor DHCP starvation attacks.

## Common Misconceptions
DHCP relay is not the same as a DHCP server; it forwards requests to a server elsewhere. DHCP snooping does not prevent DHCP requests from reaching trusted DHCP servers. Port security and DHCP snooping are complementary, not redundant.

## Explainer

From your study of DHCP, you know that clients discover servers by broadcasting DHCP Discover messages on their local subnet. The problem is that broadcasts do not cross router boundaries — they are confined to the local Layer 2 domain. In an enterprise network with dozens of subnets, deploying a separate DHCP server on every subnet is impractical. A **DHCP relay agent**, typically running on the subnet's router, solves this by intercepting DHCP broadcast messages and forwarding them as unicast packets to a centralized DHCP server on another subnet. Crucially, the relay inserts its own interface IP address into the **giaddr** (gateway IP address) field of the DHCP message, which tells the DHCP server which subnet the request came from so it can allocate an address from the correct pool.

The relay process is transparent to the client. The client broadcasts a Discover, the relay catches it, fills in giaddr, and forwards it to the configured server. The server sees the giaddr, selects an address from the matching scope, and sends the Offer back to the relay agent's IP address. The relay then forwards the Offer as a broadcast (or unicast, depending on the flags) on the client's subnet. This round-trip continues through the full DORA sequence (Discover, Offer, Request, Acknowledge). From the client's perspective, a DHCP server appears to be on the local network — the relay is invisible.

**DHCP snooping** addresses a different problem: security. Because DHCP clients accept the first Offer they receive, an attacker can plug a rogue DHCP server into the network and hand out malicious configurations — pointing clients to a fake default gateway (enabling man-in-the-middle attacks) or assigning a rogue DNS server. DHCP snooping is a Layer 2 switch feature that classifies ports as **trusted** (connected to legitimate DHCP servers or uplinks) or **untrusted** (connected to end hosts). The switch inspects every DHCP message: it permits server-originated messages (Offer, Acknowledge) only on trusted ports and drops them on untrusted ports. This prevents any rogue device on an untrusted port from acting as a DHCP server.

As the switch processes legitimate DHCP transactions, it builds a **binding database** — a table mapping each client's MAC address, assigned IP address, lease duration, and switch port. This binding database is valuable beyond DHCP security: it feeds into other security features like Dynamic ARP Inspection (DAI), which validates ARP packets against the DHCP snooping database to prevent ARP spoofing, and IP Source Guard, which drops packets from hosts using IP addresses that do not match their DHCP-assigned binding. Together, these mechanisms form a layered defense at the access switch that ensures hosts use only legitimately assigned addresses.
