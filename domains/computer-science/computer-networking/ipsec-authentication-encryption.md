---
id: ipsec-authentication-encryption
title: 'IPSec: Authentication, Encryption, and VPN Tunneling'
domain: computer-science
course: computer-networking
prerequisites:
- id: https-and-tls
  type: hard
- id: network-security-fundamentals
  type: hard
- id: vpn-virtual-private-networks
  type: soft
builds-toward:
- vpn-virtual-private-networks
- network-security-fundamentals
tags:
- security
- ipsec
- vpn
- encryption
- authentication
stage: advanced
status: draft
---

# IPSec: Authentication, Encryption, and VPN Tunneling

## Core Idea
IPSec is a suite of protocols for securing IP traffic at the network layer, providing confidentiality (encryption), integrity (authentication), and optionally anti-replay protection. IPSec operates in tunnel mode (wrapping entire packets) or transport mode (encrypting payloads only). IKE (Internet Key Exchange) negotiates security associations, authentication methods, and encryption parameters.

## How It's Best Learned
Configure IPSec tunnels between Linux hosts using strongSwan or openswan. Set up both transport and tunnel modes and observe packet transformations with tcpdump. Implement IKEv2 key exchange and monitor negotiation success/failure.

## Common Misconceptions
IPSec can encrypt all IP traffic, not just TCP. Tunnel mode is not more secure than transport mode; it depends on the authentication and encryption algorithms. IKE is separate from IPSec; it negotiates and manages security associations.

## Explainer

From your study of TLS, you know how encryption and authentication can secure communication between two endpoints — but TLS operates at the transport layer, protecting individual TCP connections. **IPSec** solves a different problem: securing all IP traffic between two network points at the network layer itself. This means IPSec can protect not just TCP and HTTP but also UDP, ICMP, routing protocols, and any other protocol that rides on IP. It is the foundation for most site-to-site VPN tunnels, where two office networks need to communicate securely over the public internet.

IPSec is not a single protocol but a **framework** built from several components. The two core protocols are **Authentication Header (AH)**, which provides integrity verification and source authentication but no encryption, and **Encapsulating Security Payload (ESP)**, which provides both encryption and authentication. In practice, ESP is used almost universally because confidentiality is nearly always required. Before any protected traffic flows, the two endpoints must agree on which algorithms to use, exchange keys, and establish a **Security Association (SA)** — a one-way contract defining the encryption algorithm, authentication method, keys, and lifetime. The **Internet Key Exchange (IKE)** protocol handles this negotiation automatically, typically in two phases: phase 1 establishes a secure channel between the endpoints themselves, and phase 2 negotiates the specific SAs for the data traffic.

IPSec operates in two modes that serve fundamentally different use cases. In **transport mode**, only the IP payload is encrypted — the original IP header remains intact and visible. This is used for host-to-host communication where both endpoints are the actual communicating parties (for example, securing traffic between two servers). In **tunnel mode**, the entire original IP packet — header and all — is encrypted and encapsulated inside a new IP packet with new headers. This is the mode used for VPN tunnels between gateways: a packet from 10.1.1.5 destined for 10.2.2.10 is encrypted, wrapped in a new packet from Gateway A's public IP to Gateway B's public IP, and sent across the internet. Gateway B decrypts it and forwards the original packet to 10.2.2.10 on its local network. The internal addresses are completely hidden from anyone observing the traffic on the internet.

The combination of IKE negotiation, ESP encryption, and tunnel mode creates a powerful security architecture, but it comes with complexity. Each direction of communication requires its own SA (since SAs are unidirectional), so a bidirectional tunnel needs at least two SAs plus the IKE SA. NAT traversal adds complications because IPSec authenticates headers that NAT devices modify, which is why **NAT-T** (NAT Traversal) encapsulates ESP inside UDP port 4500. Understanding these moving parts — the negotiation phase, the security associations, the encapsulation modes, and the interaction with NAT — is essential for configuring and troubleshooting real-world VPN deployments.
