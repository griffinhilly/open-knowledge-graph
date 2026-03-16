---
id: ppp-point-to-point-protocol
title: 'PPP: Point-to-Point Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: osi-model-layers
  type: hard
- id: ethernet-protocol
  type: soft
builds-toward:
- pppoe-protocol-over-ethernet
- network-topologies
tags:
- link-layer
- dialup
- serial
- protocols
stage: advanced
status: draft
---

# PPP: Point-to-Point Protocol

## Core Idea
PPP (Point-to-Point Protocol) is a link-layer protocol for direct serial connections, widely used in dialup modems, leased lines, and wireless links. It provides framing, link negotiation (LCP), and network protocol negotiation (NCP) to support multiple network layers. PPP includes authentication (PAP, CHAP), compression, and error detection mechanisms.

## How It's Best Learned
Set up a PPP connection between two Linux systems using pppd. Monitor LCP and NCP negotiation in debug logs. Test authentication methods and compression to understand negotiation outcomes.

## Common Misconceptions
PPP is not just for dialup; it is used on modern serial and wireless links. LCP negotiates link parameters; NCP negotiates network protocols (IP, IPX, etc.). PPP frames use HDLC-like framing with flag bytes and escape sequences.

## Explainer

From your study of the OSI model, you know that the link layer (Layer 2) is responsible for moving frames between two directly connected devices. Ethernet handles this on local area networks, but what about a direct serial connection between two routers, a dial-up modem link, or a DSL line? These are point-to-point links — just two devices at each end of a wire — and they need their own Layer 2 protocol. That protocol is **PPP (Point-to-Point Protocol)**.

PPP solves three problems that raw serial lines leave open. First, it provides **framing** — marking where one packet starts and another ends on a continuous stream of bytes. PPP frames begin and end with a special flag byte (0x7E), similar to HDLC framing. If the flag byte happens to appear inside the data, PPP uses byte-stuffing (escape sequences) to avoid confusion. Second, PPP handles **link negotiation** through the **Link Control Protocol (LCP)**. When a PPP session starts, LCP messages fly back and forth to agree on parameters like maximum frame size, whether to use compression, and which authentication method to require. Think of LCP as the handshake where both sides agree on the rules of conversation. Third, once the link parameters are settled, **Network Control Protocols (NCPs)** negotiate which network-layer protocols will run over the link — most commonly IPCP for IPv4, but PPP can carry IPX, AppleTalk, or IPv6 as well.

Authentication is a key feature that distinguishes PPP from simpler framing schemes. **PAP (Password Authentication Protocol)** sends credentials in cleartext — simple but insecure. **CHAP (Challenge-Handshake Authentication Protocol)** uses a challenge-response mechanism: the authenticator sends a random challenge, the peer hashes it with the shared secret and responds, and the authenticator verifies the hash. CHAP never sends the password over the wire and periodically re-challenges during the session, making it far more secure than PAP.

Although PPP is often associated with the dial-up era, it remains relevant in modern networking. **PPPoE (PPP over Ethernet)** encapsulates PPP frames inside Ethernet frames and is widely used by DSL providers to authenticate subscribers and assign IP addresses. PPP's clean separation of link negotiation, authentication, and network-layer configuration makes it a versatile building block wherever a point-to-point connection needs structure beyond raw bit delivery.
