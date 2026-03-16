---
id: mac-addressing
title: MAC Addressing and Hardware Identification
domain: computer-science
course: computer-networking
prerequisites:
- id: ethernet-protocol
  type: hard
builds-toward:
- switching-basics
- arp-address-resolution-protocol
- vlans-virtual-area-networks
tags:
- mac-address
- layer-2
- hardware-address
- identification
stage: advanced
status: draft
---

# MAC Addressing and Hardware Identification

## Core Idea
A Media Access Control (MAC) address is a 48-bit identifier assigned to network interface cards to uniquely identify devices on a local network segment. MAC addresses are hierarchical: the first 24 bits identify the manufacturer (OUI), and the remaining 24 bits are assigned by the manufacturer. They are used at Layer 2 to deliver frames within a LAN.

## How It's Best Learned
Use `ip link show` (Linux) or `ipconfig /all` (Windows) to view your machine's MAC address; use ARP tools to see MAC-to-IP mappings on your local network.

## Common Misconceptions
- MAC addresses are globally unique; the OUI is globally assigned, but the lower 24 bits are only unique within a manufacturer and can be spoofed.
- MAC addresses work across the Internet; they only identify devices on the same link segment.

## Explainer

From your understanding of the Ethernet protocol, you know that Ethernet frames carry data between devices on the same local network. But for a frame to reach the right device, there must be a way to identify the sender and receiver at the hardware level — that is the purpose of the **MAC address** (Media Access Control address). Every network interface card (NIC) is assigned a 48-bit MAC address, typically written as six pairs of hexadecimal digits separated by colons or hyphens: `00:1A:2B:3C:4D:5E`. This address uniquely identifies the interface on the local network segment.

The 48-bit address is divided into two halves with distinct roles. The first 24 bits form the **OUI** (Organizationally Unique Identifier), which is assigned by the IEEE to each manufacturer. For example, all Intel NICs share the same OUI prefix, and all Cisco NICs share a different one. The remaining 24 bits are assigned by the manufacturer to individual interfaces, making each address globally unique in principle (though in practice, MAC addresses can be changed in software — a technique called **MAC spoofing**). Two special bits in the first byte carry additional meaning: the **least significant bit** indicates whether the address is unicast (0) or multicast (1), and the **second bit** indicates whether the address is universally administered (0, assigned by the manufacturer) or locally administered (1, assigned by software).

When a device sends an Ethernet frame, it places its own MAC address in the **source address** field and the destination device's MAC address in the **destination address** field. A switch on the network examines the destination MAC address to decide which port to forward the frame to — this is the foundation of Layer 2 switching. The special broadcast address `FF:FF:FF:FF:FF:FF` tells the switch to forward the frame to all ports, reaching every device on the segment. This is how protocols like ARP work: a device broadcasts "who has IP address 192.168.1.5?" and the device with that IP responds with its MAC address, creating a MAC-to-IP mapping.

A critical distinction is that MAC addresses operate only within a **single network segment** (a LAN or VLAN). When a packet crosses a router to reach a different network, the router strips off the original Ethernet frame (and its MAC addresses) and creates a new frame with its own MAC address as the source and the next-hop device's MAC address as the destination. The IP addresses in the packet remain unchanged end-to-end, but the MAC addresses change at every hop. This is why MAC addresses and IP addresses serve complementary roles: IP addresses identify the final destination across the entire Internet, while MAC addresses identify the next device the frame needs to reach on the current link.
