---
id: dhcp-dynamic-host-configuration
title: DHCP (Dynamic Host Configuration Protocol)
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
builds-toward:
- network-management-and-monitoring
tags:
- dhcp
- address-assignment
- dynamic-configuration
- leasing
stage: advanced
status: draft
---

# DHCP (Dynamic Host Configuration Protocol)

## Core Idea
DHCP automatically assigns IP addresses and network configuration to clients from a pool of addresses managed by a server. Clients request a lease for a specific duration and must renew it to maintain their address; leases expiring return addresses to the pool. DHCP eliminates manual configuration errors and simplifies network management, especially in environments with mobile or frequently-changing devices.

## Explainer

From your understanding of IPv4 addressing, you know that every device on an IP network needs a unique IP address, a subnet mask, and typically a default gateway and DNS server address to communicate. On a small home network with three devices, you could configure these manually. But imagine a university campus with thousands of laptops, phones, and tablets connecting and disconnecting throughout the day — manual configuration would be impossible. **DHCP** (Dynamic Host Configuration Protocol) solves this by automating the entire process: a device plugs into the network, asks for an address, and receives one automatically within seconds.

The protocol follows a four-step exchange known as **DORA**: Discover, Offer, Request, Acknowledge. When a new device joins the network, it has no IP address yet, so it broadcasts a **DHCP Discover** message to the entire local network (destination 255.255.255.255) asking if any DHCP server is available. Any DHCP server that receives this broadcast responds with a **DHCP Offer**, proposing an IP address from its configured pool along with the subnet mask, gateway, DNS servers, and a **lease duration**. The client selects one offer (if multiple servers respond) and broadcasts a **DHCP Request** announcing which offer it accepts. Finally, the chosen server sends a **DHCP Acknowledge** confirming the assignment. The entire exchange typically completes in milliseconds.

The **lease** mechanism is what makes DHCP scalable. Rather than permanently assigning addresses, the server loans each address for a fixed period — commonly 8 hours or 24 hours. When half the lease time has elapsed, the client automatically attempts to **renew** by sending a request directly to the server that issued the lease. If the server confirms, the lease timer resets. If the client leaves the network without releasing its address (a laptop carried to another building, for example), the lease eventually expires and the address returns to the pool for reassignment. This recycling ensures that a network with 1,000 addresses can serve 5,000 devices over the course of a day, as long as no more than 1,000 are connected simultaneously.

Beyond IP addresses, DHCP delivers a bundle of configuration parameters in a single transaction: subnet mask, default gateway, DNS server addresses, domain name, NTP server, and many more via extensible **DHCP options**. This centralization is the real operational win — when the DNS server address changes, an administrator updates it in one place (the DHCP server configuration), and every client picks up the change at its next lease renewal. Without DHCP, that same change would require touching every device individually, an error-prone process that scales poorly and virtually guarantees misconfiguration on at least some machines.
