---
id: vpn-virtual-private-networks
title: VPN (Virtual Private Networks)
domain: computer-science
course: computer-networking
prerequisites:
- id: network-security-fundamentals
  type: hard
- id: https-and-tls
  type: hard
tags:
- vpn
- encryption
- tunneling
- privacy
stage: advanced
status: draft
---

# VPN (Virtual Private Networks)

## Core Idea
VPNs create encrypted tunnels through untrusted networks, protecting confidentiality and integrity of traffic and allowing remote access to private networks. Site-to-site VPNs connect networks; client-to-site VPNs allow individual users to access networks remotely. VPNs use encryption and authentication protocols like IPsec, TLS, or WireGuard.

## Explainer

From network security fundamentals and TLS, you understand that data traversing the internet can be intercepted, and that encryption protects confidentiality while authentication verifies identity. A VPN applies these principles to create the illusion that geographically separated networks — or a remote user and a corporate office — are directly connected on the same private network, even though all traffic actually crosses the public internet. The key concept is **tunneling**: wrapping an entire private packet inside an encrypted outer packet that can traverse untrusted infrastructure without exposing its contents.

Consider a concrete scenario. A company has offices in New York and London, each with its own private network (10.1.0.0/16 and 10.2.0.0/16). Without a VPN, a computer in New York cannot send packets to 10.2.0.5 in London because private addresses are not routable on the public internet. A **site-to-site VPN** solves this by configuring a VPN gateway at each office. When a New York machine sends a packet to 10.2.0.5, the New York gateway intercepts it, encrypts the entire original packet (headers and all), wraps it in a new IP packet addressed to the London gateway's public IP, and sends it across the internet. The London gateway receives this outer packet, strips the encryption, recovers the original packet addressed to 10.2.0.5, and forwards it onto the London network. To the endpoints, it appears as if they are on the same network — the VPN tunnel is invisible.

**Client-to-site VPNs** (also called remote access VPNs) work similarly but connect an individual device rather than an entire network. A remote worker's laptop runs VPN client software that establishes an encrypted tunnel to the corporate VPN gateway. Once connected, the laptop is assigned an IP address from the corporate network range and can access internal resources as if physically present in the office. The client typically routes either all traffic through the tunnel (**full tunnel**) or only traffic destined for corporate addresses (**split tunnel**), with split tunneling offering better performance for internet-bound traffic but providing less security oversight.

The major VPN protocols differ in where they operate and how they achieve encryption. **IPsec** works at the network layer (Layer 3) and can operate in transport mode (encrypting only the payload) or tunnel mode (encrypting the entire inner packet). It uses IKE (Internet Key Exchange) for establishing shared keys and supports strong authentication via certificates or pre-shared keys. **TLS-based VPNs** (like OpenVPN) work at the application layer, leveraging the same TLS handshake you studied in HTTPS to establish encrypted channels — this makes them easier to deploy through firewalls since they use standard HTTPS ports. **WireGuard** is a newer protocol that dramatically simplifies VPN implementation with a minimal codebase, modern cryptographic primitives, and a design that treats peers as having fixed public keys rather than negotiating complex key exchanges. Each protocol makes different tradeoffs between security, performance, complexity, and compatibility.
