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
status: validated
---

# IPSec: Authentication, Encryption, and VPN Tunneling

## Core Idea
IPSec is a suite of protocols for securing IP traffic at the network layer, providing confidentiality (encryption), integrity (authentication), and optionally anti-replay protection. IPSec operates in tunnel mode (wrapping entire packets) or transport mode (encrypting payloads only). IKE (Internet Key Exchange) negotiates security associations, authentication methods, and encryption parameters.

## How It's Best Learned
Configure IPSec tunnels between Linux hosts using strongSwan or openswan. Set up both transport and tunnel modes and observe packet transformations with tcpdump. Implement IKEv2 key exchange and monitor negotiation success/failure.

## Common Misconceptions
IPSec can encrypt all IP traffic, not just TCP. Tunnel mode is not more secure than transport mode; it depends on the authentication and encryption algorithms. IKE is separate from IPSec; it negotiates and manages security associations.

## Questions

```yaml
- question: "Two branch offices want to connect securely over the public internet so that all traffic between the office networks is encrypted, including each office's internal IP addresses. Which IPSec mode and component achieves this?"
  type: multiple-choice
  options:
    - "Transport mode with AH — it authenticates the original IP header, hiding the internal addresses"
    - "Tunnel mode with ESP — it encrypts the entire original packet and wraps it in a new IP packet with gateway addresses"
    - "Transport mode with ESP — it encrypts the payload, leaving only the application data visible to attackers"
    - "Tunnel mode with AH — it authenticates the encapsulated packet, ensuring internal addresses cannot be modified"
  answer: 1
  explanation: "Tunnel mode is designed for gateway-to-gateway VPNs. It encrypts the entire original IP packet — including its header containing the internal 10.x.x.x addresses — and wraps it in a new outer IP packet with the gateways' public IP addresses. An eavesdropper on the internet sees only the outer header; the internal addressing is completely hidden. Transport mode (options A and C) only encrypts or authenticates the payload, leaving the original IP header visible — which would expose the internal addresses. AH (option D) provides authentication and integrity but no encryption — confidentiality would not be achieved."

- question: "IPSec traffic between two hosts fails after one host is placed behind a NAT device. Which explanation is most accurate?"
  type: multiple-choice
  options:
    - "NAT changes the source IP address in the outer IP header, which causes AH integrity verification to fail since AH authenticates the IP header"
    - "NAT cannot forward ESP traffic because ESP is not based on TCP or UDP port numbers"
    - "IKE phase 1 only works over IPv6, which NAT does not support"
    - "Tunnel mode is incompatible with NAT because it adds a second IP header that NAT devices cannot process"
  answer: 0
  explanation: "AH authenticates the entire IP header including the source address. When a NAT device changes the source IP address to route the packet back, the AH integrity check fails because the header no longer matches what was signed. This is why AH and NAT are fundamentally incompatible. ESP has a similar but solvable problem: NAT modifies port numbers (for NAPT), which can interfere with ESP sessions — addressed by NAT-T, which encapsulates ESP inside UDP port 4500. Option B is partially true (ESP is not TCP/UDP-based) but is not the root cause of the authentication failure."

- question: "IPSec operates at the network layer and can therefore protect any IP-based protocol — UDP, ICMP, routing protocols — not just TCP connections."
  type: true-false
  answer: true
  explanation: "This is the key distinction between IPSec and TLS. TLS secures individual TCP connections at the transport layer. IPSec secures IP packets at the network layer, meaning any protocol that rides on IP — TCP, UDP, ICMP, GRE, OSPF, etc. — is protected. This is why IPSec is used for site-to-site VPNs that must carry all traffic between two networks, not just specific application connections."

- question: "IPSec tunnel mode is inherently more secure than transport mode because it encrypts more data, including the IP header."
  type: true-false
  answer: false
  explanation: "Security level depends on the cryptographic algorithms and key lengths used, not on whether the mode is tunnel or transport. Both modes can use ESP with the same AES encryption and HMAC authentication. Tunnel mode hides the internal IP headers, which provides *privacy* (an attacker cannot see internal network topology), but this is a confidentiality/metadata property, not a fundamental security strength. Transport mode with strong encryption is more secure than tunnel mode with weak encryption. The choice of mode should be driven by network topology needs, not a false assumption that tunnel mode has stronger cryptography."

- question: "Why does NAT cause problems for IPSec, and what mechanism does NAT Traversal (NAT-T) use to work around this limitation?"
  type: short-answer
  answer: "NAT devices modify IP addresses (and often port numbers) to route packets between private and public networks. IPSec's AH protocol authenticates the entire IP header including the source address, so any NAT modification breaks the integrity check. ESP avoids modifying authenticated data in the header, but NAPT devices that map ports can still disrupt ESP flows that don't have port numbers. NAT-T solves this by encapsulating the ESP payload inside a UDP packet (on port 4500), giving NAT devices a standard UDP header to modify. The ESP integrity checks are now inside the UDP payload, which NAT does not touch."
  explanation: "NAT-T works by adding a layer of indirection: the ESP packet, which NAT cannot safely modify, is wrapped in a UDP datagram that NAT can handle normally. This is a pragmatic engineering workaround — you sacrifice a small amount of overhead (UDP header per packet) to preserve IPSec's security properties across NAT boundaries. Understanding this interaction helps explain why IKE detects NAT during its negotiation and automatically switches to UDP port 4500 encapsulation when NAT is present."
```

## Explainer

From your study of TLS, you know how encryption and authentication can secure communication between two endpoints — but TLS operates at the transport layer, protecting individual TCP connections. **IPSec** solves a different problem: securing all IP traffic between two network points at the network layer itself. This means IPSec can protect not just TCP and HTTP but also UDP, ICMP, routing protocols, and any other protocol that rides on IP. It is the foundation for most site-to-site VPN tunnels, where two office networks need to communicate securely over the public internet.

IPSec is not a single protocol but a **framework** built from several components. The two core protocols are **Authentication Header (AH)**, which provides integrity verification and source authentication but no encryption, and **Encapsulating Security Payload (ESP)**, which provides both encryption and authentication. In practice, ESP is used almost universally because confidentiality is nearly always required. Before any protected traffic flows, the two endpoints must agree on which algorithms to use, exchange keys, and establish a **Security Association (SA)** — a one-way contract defining the encryption algorithm, authentication method, keys, and lifetime. The **Internet Key Exchange (IKE)** protocol handles this negotiation automatically, typically in two phases: phase 1 establishes a secure channel between the endpoints themselves, and phase 2 negotiates the specific SAs for the data traffic.

IPSec operates in two modes that serve fundamentally different use cases. In **transport mode**, only the IP payload is encrypted — the original IP header remains intact and visible. This is used for host-to-host communication where both endpoints are the actual communicating parties (for example, securing traffic between two servers). In **tunnel mode**, the entire original IP packet — header and all — is encrypted and encapsulated inside a new IP packet with new headers. This is the mode used for VPN tunnels between gateways: a packet from 10.1.1.5 destined for 10.2.2.10 is encrypted, wrapped in a new packet from Gateway A's public IP to Gateway B's public IP, and sent across the internet. Gateway B decrypts it and forwards the original packet to 10.2.2.10 on its local network. The internal addresses are completely hidden from anyone observing the traffic on the internet.

The combination of IKE negotiation, ESP encryption, and tunnel mode creates a powerful security architecture, but it comes with complexity. Each direction of communication requires its own SA (since SAs are unidirectional), so a bidirectional tunnel needs at least two SAs plus the IKE SA. NAT traversal adds complications because IPSec authenticates headers that NAT devices modify, which is why **NAT-T** (NAT Traversal) encapsulates ESP inside UDP port 4500. Understanding these moving parts — the negotiation phase, the security associations, the encapsulation modes, and the interaction with NAT — is essential for configuring and troubleshooting real-world VPN deployments.
