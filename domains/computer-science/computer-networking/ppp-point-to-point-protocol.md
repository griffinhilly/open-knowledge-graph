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
status: validated
---

# PPP: Point-to-Point Protocol

## Core Idea
PPP (Point-to-Point Protocol) is a link-layer protocol for direct serial connections, widely used in dialup modems, leased lines, and wireless links. It provides framing, link negotiation (LCP), and network protocol negotiation (NCP) to support multiple network layers. PPP includes authentication (PAP, CHAP), compression, and error detection mechanisms.

## How It's Best Learned
Set up a PPP connection between two Linux systems using pppd. Monitor LCP and NCP negotiation in debug logs. Test authentication methods and compression to understand negotiation outcomes.

## Common Misconceptions
PPP is not just for dialup; it is used on modern serial and wireless links. LCP negotiates link parameters; NCP negotiates network protocols (IP, IPX, etc.). PPP frames use HDLC-like framing with flag bytes and escape sequences.

## Questions

```yaml
- question: "Two routers connect via a serial leased line. Before IP traffic can flow, they must agree on the maximum frame size and whether to use compression. Which PPP component handles this negotiation?"
  type: multiple-choice
  options:
    - "NCP (Network Control Protocol), which negotiates all parameters including link-layer options"
    - "CHAP, which authenticates both sides before any other negotiation can begin"
    - "LCP (Link Control Protocol), which negotiates link-layer parameters like MRU and compression"
    - "HDLC framing, which embeds frame size preferences in the 0x7E flag bytes"
  answer: 2
  explanation: "LCP (Link Control Protocol) is specifically responsible for link-layer parameter negotiation — it is the 'handshake' phase where both sides agree on maximum receive unit (MRU), compression settings, authentication method, and other link properties. NCP (Network Control Protocol) comes after LCP and negotiates which network-layer protocols to run (e.g., IPCP for IPv4). CHAP is one authentication method that LCP may negotiate, not a separate negotiation phase. HDLC-like framing provides byte boundaries but carries no negotiation semantics."

- question: "Why is CHAP more secure than PAP for PPP authentication?"
  type: multiple-choice
  options:
    - "CHAP uses longer minimum password lengths than PAP allows"
    - "CHAP encrypts the entire PPP session with a shared key, while PAP only protects the authentication exchange"
    - "CHAP uses a challenge-response mechanism where a hash of the shared secret is sent instead of the password itself"
    - "CHAP operates at the network layer (Layer 3), making it harder to intercept than PAP's link-layer operation"
  answer: 2
  explanation: "CHAP's security advantage is that the password is never transmitted. Instead, the authenticator sends a random challenge, and the peer responds with a hash (typically MD5) of the challenge combined with the shared secret. An eavesdropper who captures the exchange sees only the challenge and the hash, not the password. PAP sends credentials in plaintext — anyone monitoring the line gets the password directly. CHAP also periodically re-challenges during the session, so capturing one exchange does not give permanent access."

- question: "PPP is an obsolete protocol used only during the dial-up modem era and has no relevance to modern networking infrastructure."
  type: true-false
  answer: false
  explanation: "PPP remains widely deployed in modern networks through PPPoE (PPP over Ethernet), which encapsulates PPP frames inside Ethernet frames. DSL providers use PPPoE to authenticate subscribers and assign IP addresses over broadband connections. PPP is also used on serial leased lines between routers and on some wireless backhaul links. Its clean separation of framing, link negotiation (LCP), and network-layer negotiation (NCP) makes it a versatile and still-relevant protocol wherever a point-to-point connection needs more structure than raw bit delivery."

- question: "LCP negotiates link-layer parameters (such as frame size and compression), while NCPs negotiate which network-layer protocols (such as IP) will be carried over the PPP link."
  type: true-false
  answer: true
  explanation: "This is the core architectural design of PPP. LCP runs first and establishes the link parameters that both sides agree to use — without successful LCP negotiation, no data flows. After LCP completes, one or more NCPs run to bring up network-layer protocols: IPCP configures IPv4, IPv6CP configures IPv6, and legacy NCPs handled IPX or AppleTalk. This layered negotiation approach is what makes PPP flexible enough to carry any network-layer protocol over any point-to-point serial link."

- question: "What three problems does PPP solve that a raw serial byte stream cannot handle, and why is each necessary for reliable network communication?"
  type: short-answer
  answer: "First, framing: a raw serial stream is a continuous sequence of bytes with no boundaries. PPP uses flag bytes (0x7E) and byte-stuffing to delimit frames so the receiver knows where each packet begins and ends. Without framing, the receiver cannot tell which bytes belong together. Second, link parameter negotiation via LCP: before data flows, both sides must agree on maximum frame size, compression, and authentication method. Mismatched parameters would cause silent failures. Third, network-layer protocol negotiation via NCP: the link may carry IP, IPv6, or other protocols. NCPs allow both sides to agree on which protocols to activate and configure them (e.g., IPCP assigns IP addresses). Together these three phases make PPP a complete, interoperable link-layer protocol."
  explanation: "Raw serial lines provide only a bit pipe — they transmit whatever bytes they receive with no interpretation. PPP adds the minimal structure needed for reliable, negotiated, authenticated communication between exactly two devices: boundaries (framing), rules (LCP), and payload type (NCP). This is why PPP persists in modern infrastructure despite being designed in the dial-up era."
```

## Explainer

From your study of the OSI model, you know that the link layer (Layer 2) is responsible for moving frames between two directly connected devices. Ethernet handles this on local area networks, but what about a direct serial connection between two routers, a dial-up modem link, or a DSL line? These are point-to-point links — just two devices at each end of a wire — and they need their own Layer 2 protocol. That protocol is **PPP (Point-to-Point Protocol)**.

PPP solves three problems that raw serial lines leave open. First, it provides **framing** — marking where one packet starts and another ends on a continuous stream of bytes. PPP frames begin and end with a special flag byte (0x7E), similar to HDLC framing. If the flag byte happens to appear inside the data, PPP uses byte-stuffing (escape sequences) to avoid confusion. Second, PPP handles **link negotiation** through the **Link Control Protocol (LCP)**. When a PPP session starts, LCP messages fly back and forth to agree on parameters like maximum frame size, whether to use compression, and which authentication method to require. Think of LCP as the handshake where both sides agree on the rules of conversation. Third, once the link parameters are settled, **Network Control Protocols (NCPs)** negotiate which network-layer protocols will run over the link — most commonly IPCP for IPv4, but PPP can carry IPX, AppleTalk, or IPv6 as well.

Authentication is a key feature that distinguishes PPP from simpler framing schemes. **PAP (Password Authentication Protocol)** sends credentials in cleartext — simple but insecure. **CHAP (Challenge-Handshake Authentication Protocol)** uses a challenge-response mechanism: the authenticator sends a random challenge, the peer hashes it with the shared secret and responds, and the authenticator verifies the hash. CHAP never sends the password over the wire and periodically re-challenges during the session, making it far more secure than PAP.

Although PPP is often associated with the dial-up era, it remains relevant in modern networking. **PPPoE (PPP over Ethernet)** encapsulates PPP frames inside Ethernet frames and is widely used by DSL providers to authenticate subscribers and assign IP addresses. PPP's clean separation of link negotiation, authentication, and network-layer configuration makes it a versatile building block wherever a point-to-point connection needs structure beyond raw bit delivery.
