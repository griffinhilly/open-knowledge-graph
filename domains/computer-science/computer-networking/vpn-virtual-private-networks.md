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
status: validated
---

# VPN (Virtual Private Networks)

## Core Idea
VPNs create encrypted tunnels through untrusted networks, protecting confidentiality and integrity of traffic and allowing remote access to private networks. Site-to-site VPNs connect networks; client-to-site VPNs allow individual users to access networks remotely. VPNs use encryption and authentication protocols like IPsec, TLS, or WireGuard.

## Questions

```yaml
- question: "A remote employee connects to the corporate network via a full-tunnel VPN, then opens a web browser to visit a public news website. Where does the web traffic go first?"
  type: multiple-choice
  options:
    - "Directly to the news website's server — only corporate-bound traffic is tunneled"
    - "To the employee's ISP, which forwards it to the VPN gateway before reaching the internet"
    - "Through the encrypted tunnel to the corporate VPN gateway, which then forwards the request to the news website"
    - "To a DNS resolver chosen by the VPN client, which routes traffic based on domain name"
  answer: 2
  explanation: "In a full-tunnel VPN, ALL traffic — including requests to public websites — is routed through the encrypted tunnel to the corporate gateway. The gateway then forwards the request to the internet on the employee's behalf. This is why full-tunnel VPNs create a performance bottleneck (all internet traffic makes a detour through corporate infrastructure) but give the organization complete visibility and control over employee traffic. Option A describes split tunneling, not full tunneling. Option B incorrectly describes how the traffic reaches the gateway."

- question: "What makes a site-to-site VPN essential for connecting two offices that use private IP address ranges (e.g., 10.1.0.0/16 and 10.2.0.0/16)?"
  type: multiple-choice
  options:
    - "Private IP addresses are blocked by firewalls and must be translated before internet transit"
    - "Private IP addresses are not routable on the public internet, so traffic must be encapsulated inside packets with routable public addresses"
    - "The offices need a dedicated leased line, and a VPN provides the same physical infrastructure"
    - "VPN encryption prevents ISPs from throttling inter-office traffic based on IP range"
  answer: 1
  explanation: "Private IP address ranges (RFC 1918: 10.x.x.x, 172.16–31.x.x, 192.168.x.x) are reserved for internal networks and are not routable on the public internet — routers discard packets with private destination addresses. A site-to-site VPN solves this by encapsulating (tunneling) the entire original private-IP packet inside a new packet with public IP addresses. The VPN gateways have public IPs; the original packet is hidden inside as payload. When the destination gateway receives and decrypts the outer packet, it recovers the private-IP packet and routes it onto its internal network. Option A is about NAT, which is a related but different mechanism. Option C is wrong — VPNs use shared public internet infrastructure, not dedicated lines."

- question: "A VPN makes users substantially anonymous online because most their traffic is encrypted and can seldom be traced back to them."
  type: true-false
  answer: false
  explanation: "False. A VPN shifts trust, not eliminates it. With a VPN, your ISP can no longer see the content of your traffic — they only see that you are connecting to a VPN server. However, the VPN provider (or corporate gateway) now sees all your traffic and knows your identity. You are trusting the VPN operator instead of your ISP. Additionally, many other tracking mechanisms (browser fingerprinting, cookies, account logins) operate above the network layer and are completely unaffected by a VPN. The common consumer marketing claim that VPNs provide anonymity is an oversimplification."

- question: "In IPsec tunnel mode (the mode used in site-to-site VPNs), the VPN gateway encrypts the entire original IP packet — including its source and destination addresses — before adding a new outer IP header."
  type: true-false
  answer: true
  explanation: "True. This is the defining characteristic of IPsec tunnel mode and the key to how VPNs handle private IP addresses. The complete original packet (header + payload) is treated as the inner payload, encrypted, and encapsulated inside a new outer IP packet. The outer packet carries the public IP addresses of the two VPN gateways. This is what hides the private address space from the public internet — the inner packet's private IPs are invisible to any routers between the gateways. In contrast, IPsec transport mode only encrypts the payload, leaving the IP header intact — transport mode is used for host-to-host encryption, not site-to-site tunneling."

- question: "Explain what 'tunneling' means in the context of a site-to-site VPN, and why it is necessary when connecting two offices that use private IP address ranges."
  type: short-answer
  answer: "Tunneling means taking an entire network packet (including its headers) and wrapping it as the payload of another packet. In a site-to-site VPN, the VPN gateway encrypts and encapsulates each private-IP packet inside a new packet with public IP addresses. The public internet routes the outer packet to the remote gateway, which strips the outer layer, decrypts, and delivers the original private-IP packet to its destination. This is necessary because private IP addresses are not routable on the public internet — without encapsulation, routers would discard packets destined for 10.x.x.x or 192.168.x.x addresses."
  explanation: "The term 'virtual' in VPN captures this mechanism: the private network connection is virtual (simulated through encapsulation) rather than physical (a dedicated leased line). The public internet carries the outer packets without knowing about the inner private network structure. Both encryption (for confidentiality) and encapsulation (for routing) are required — encryption alone would not solve the private-IP routing problem."
```

## Explainer

From network security fundamentals and TLS, you understand that data traversing the internet can be intercepted, and that encryption protects confidentiality while authentication verifies identity. A VPN applies these principles to create the illusion that geographically separated networks — or a remote user and a corporate office — are directly connected on the same private network, even though all traffic actually crosses the public internet. The key concept is **tunneling**: wrapping an entire private packet inside an encrypted outer packet that can traverse untrusted infrastructure without exposing its contents.

Consider a concrete scenario. A company has offices in New York and London, each with its own private network (10.1.0.0/16 and 10.2.0.0/16). Without a VPN, a computer in New York cannot send packets to 10.2.0.5 in London because private addresses are not routable on the public internet. A **site-to-site VPN** solves this by configuring a VPN gateway at each office. When a New York machine sends a packet to 10.2.0.5, the New York gateway intercepts it, encrypts the entire original packet (headers and all), wraps it in a new IP packet addressed to the London gateway's public IP, and sends it across the internet. The London gateway receives this outer packet, strips the encryption, recovers the original packet addressed to 10.2.0.5, and forwards it onto the London network. To the endpoints, it appears as if they are on the same network — the VPN tunnel is invisible.

**Client-to-site VPNs** (also called remote access VPNs) work similarly but connect an individual device rather than an entire network. A remote worker's laptop runs VPN client software that establishes an encrypted tunnel to the corporate VPN gateway. Once connected, the laptop is assigned an IP address from the corporate network range and can access internal resources as if physically present in the office. The client typically routes either all traffic through the tunnel (**full tunnel**) or only traffic destined for corporate addresses (**split tunnel**), with split tunneling offering better performance for internet-bound traffic but providing less security oversight.

The major VPN protocols differ in where they operate and how they achieve encryption. **IPsec** works at the network layer (Layer 3) and can operate in transport mode (encrypting only the payload) or tunnel mode (encrypting the entire inner packet). It uses IKE (Internet Key Exchange) for establishing shared keys and supports strong authentication via certificates or pre-shared keys. **TLS-based VPNs** (like OpenVPN) work at the application layer, leveraging the same TLS handshake you studied in HTTPS to establish encrypted channels — this makes them easier to deploy through firewalls since they use standard HTTPS ports. **WireGuard** is a newer protocol that dramatically simplifies VPN implementation with a minimal codebase, modern cryptographic primitives, and a design that treats peers as having fixed public keys rather than negotiating complex key exchanges. Each protocol makes different tradeoffs between security, performance, complexity, and compatibility.
