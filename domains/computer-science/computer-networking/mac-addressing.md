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
status: validated
---

# MAC Addressing and Hardware Identification

## Core Idea
A Media Access Control (MAC) address is a 48-bit identifier assigned to network interface cards to uniquely identify devices on a local network segment. MAC addresses are hierarchical: the first 24 bits identify the manufacturer (OUI), and the remaining 24 bits are assigned by the manufacturer. They are used at Layer 2 to deliver frames within a LAN.

## How It's Best Learned
Use `ip link show` (Linux) or `ipconfig /all` (Windows) to view your machine's MAC address; use ARP tools to see MAC-to-IP mappings on your local network.

## Common Misconceptions
- MAC addresses are globally unique; the OUI is globally assigned, but the lower 24 bits are only unique within a manufacturer and can be spoofed.
- MAC addresses work across the Internet; they only identify devices on the same link segment.

## Questions

```yaml
- question: "Your laptop sends a packet to a web server three router hops away. What is the destination MAC address in the very first Ethernet frame your laptop sends?"
  type: multiple-choice
  options:
    - "The web server's MAC address"
    - "The first router's (default gateway's) MAC address"
    - "The broadcast address FF:FF:FF:FF:FF:FF"
    - "The IP address of the web server, converted to hexadecimal"
  answer: 1
  explanation: "MAC addresses are local to a single network segment. Your laptop has no way to know the web server's MAC address (it may be on a completely different continent), and MAC addresses are not routable across the internet. Your laptop only needs to get the packet to the next hop — its default gateway (the router). The router's MAC address is discovered via ARP. The router then creates a new frame for the next hop, with its own MAC as source and the next router's MAC as destination. This process repeats at every hop — only the IP addresses remain constant end-to-end."

- question: "Two NICs from different manufacturers happen to have identical lower 24 bits in their MAC addresses (the manufacturer-assigned portion). What is the consequence for a network containing both devices?"
  type: multiple-choice
  options:
    - "They cannot communicate with each other and must use IP addresses instead"
    - "Both must undergo MAC spoofing to obtain unique addresses"
    - "They can coexist without conflict on the same network because their different OUIs make their full 48-bit addresses distinct"
    - "The network switch will block one of them until the address collision is resolved"
  answer: 2
  explanation: "A MAC address is 48 bits total: 24-bit OUI (manufacturer identifier) plus 24-bit device identifier. Two NICs with the same lower 24 bits but different OUIs have completely different full MAC addresses — there is no collision. The OUI is globally assigned by the IEEE to each manufacturer, ensuring that addresses from different manufacturers are always distinguishable. A conflict would only occur if two devices on the same segment share the same full 48-bit address, which could happen via MAC spoofing."

- question: "When an Ethernet frame passes through a router from one network to another, the source and destination MAC addresses in the frame are replaced, while the source and destination IP addresses in the packet remain unchanged."
  type: true-false
  answer: true
  explanation: "This is the fundamental distinction between Layer 2 and Layer 3 operation. A router decapsulates the incoming Ethernet frame, reads the IP destination, decides on the next hop, then creates an entirely new Ethernet frame with its own outgoing interface MAC as the source and the next-hop device's MAC as the destination. The IP packet inside is forwarded unchanged. MAC addresses are local — they describe the current link. IP addresses are global — they describe the final endpoint. This is why you can't trace a path across the internet using only MAC addresses."

- question: "A MAC address uniquely and permanently identifies a specific physical device, regardless of which network it is connected to or what software changes are made."
  type: true-false
  answer: false
  explanation: "MAC addresses can be changed in software — a technique called MAC spoofing — so they are not permanent identifiers tied to hardware in practice. More importantly, MAC addresses are only meaningful within a single local network segment: once a frame crosses a router, the original MAC addresses are discarded and replaced. The 'uniqueness' of MAC addresses is also only guaranteed in principle by the OUI assignment system; manufacturers control the lower 24 bits and can (rarely) produce duplicates, and locally-administered bits explicitly signal software-assigned addresses."

- question: "Why do MAC addresses change at every router hop while IP addresses remain constant end-to-end? What does this reveal about the distinct roles of these two addressing systems?"
  type: short-answer
  answer: "IP addresses identify the final destination across the entire internetwork — they are global, persistent, and used for routing decisions. MAC addresses identify only the next device the frame must reach on the current link — they are local, transient, and discarded when a frame leaves a segment. Routers strip the old Ethernet frame (and its MACs) and create a new one for the next segment because the addressing scheme appropriate for getting from A to B on a local wire is completely different from the scheme needed to route packets across heterogeneous networks worldwide."
  explanation: "The split is intentional and powerful: it allows the internet to work across completely different Layer 2 technologies (Ethernet, Wi-Fi, fiber, etc.) without requiring each to use the same hardware addressing scheme. IP provides a uniform logical addressing layer on top of diverse physical media. MACs are the physical-layer glue that gets a frame from one interface to the next on a single medium, while IP handles the end-to-end routing abstraction above."
```

## Explainer

From your understanding of the Ethernet protocol, you know that Ethernet frames carry data between devices on the same local network. But for a frame to reach the right device, there must be a way to identify the sender and receiver at the hardware level — that is the purpose of the **MAC address** (Media Access Control address). Every network interface card (NIC) is assigned a 48-bit MAC address, typically written as six pairs of hexadecimal digits separated by colons or hyphens: `00:1A:2B:3C:4D:5E`. This address uniquely identifies the interface on the local network segment.

The 48-bit address is divided into two halves with distinct roles. The first 24 bits form the **OUI** (Organizationally Unique Identifier), which is assigned by the IEEE to each manufacturer. For example, all Intel NICs share the same OUI prefix, and all Cisco NICs share a different one. The remaining 24 bits are assigned by the manufacturer to individual interfaces, making each address globally unique in principle (though in practice, MAC addresses can be changed in software — a technique called **MAC spoofing**). Two special bits in the first byte carry additional meaning: the **least significant bit** indicates whether the address is unicast (0) or multicast (1), and the **second bit** indicates whether the address is universally administered (0, assigned by the manufacturer) or locally administered (1, assigned by software).

When a device sends an Ethernet frame, it places its own MAC address in the **source address** field and the destination device's MAC address in the **destination address** field. A switch on the network examines the destination MAC address to decide which port to forward the frame to — this is the foundation of Layer 2 switching. The special broadcast address `FF:FF:FF:FF:FF:FF` tells the switch to forward the frame to all ports, reaching every device on the segment. This is how protocols like ARP work: a device broadcasts "who has IP address 192.168.1.5?" and the device with that IP responds with its MAC address, creating a MAC-to-IP mapping.

A critical distinction is that MAC addresses operate only within a **single network segment** (a LAN or VLAN). When a packet crosses a router to reach a different network, the router strips off the original Ethernet frame (and its MAC addresses) and creates a new frame with its own MAC address as the source and the next-hop device's MAC address as the destination. The IP addresses in the packet remain unchanged end-to-end, but the MAC addresses change at every hop. This is why MAC addresses and IP addresses serve complementary roles: IP addresses identify the final destination across the entire Internet, while MAC addresses identify the next device the frame needs to reach on the current link.
