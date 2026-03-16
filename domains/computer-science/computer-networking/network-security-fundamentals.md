---
id: network-security-fundamentals
title: 'Network Security: Firewalls, Filtering, and Threat Models'
domain: computer-science
course: computer-networking
prerequisites:
- id: https-and-tls
  type: soft
tags:
- security
- firewall
- access-control
- threats
- defense
stage: advanced
status: draft
---

# Network Security: Firewalls, Filtering, and Threat Models

## Core Idea
Network security addresses threats like eavesdropping, spoofing, and denial of service. Firewalls filter traffic based on IP addresses and ports; encryption protects confidentiality; authentication prevents spoofing; rate limiting mitigates denial-of-service attacks. Effective security requires defense in depth across multiple layers.

## Explainer

Network security starts with a simple question: what are you defending against? A **threat model** identifies the adversaries (script kiddies, nation-states, insiders), their capabilities, and their goals (stealing data, disrupting service, impersonating users). Without a threat model, security measures are arbitrary — you might encrypt everything but leave a management port wide open. From your understanding of TLS, you already know how encryption protects data in transit. Network security extends that thinking to every layer of the stack and every point of entry.

The most fundamental defense tool is the **firewall**, which inspects packets and decides whether to allow, drop, or reject them based on rules. A simple packet-filtering firewall examines headers — source and destination IP addresses, port numbers, and protocol type — and matches them against an ordered rule list. For example, a rule might say "allow TCP traffic to port 443 from any source" (permitting HTTPS) while blocking everything else by default. **Stateful firewalls** go further: they track active connections, so a reply packet from a web server is automatically permitted because the firewall remembers the outbound request that initiated the connection. This is far more secure than trying to write static rules for return traffic.

Beyond firewalls, network security relies on **layered defenses** — a principle called defense in depth. No single mechanism is sufficient. Encryption (TLS) protects confidentiality and integrity on the wire, but it does not prevent a compromised internal machine from attacking other internal machines. Authentication mechanisms like certificates, tokens, or mutual TLS verify that communicating parties are who they claim to be, preventing **spoofing** attacks where an adversary forges source addresses or identities. Rate limiting and traffic shaping mitigate **denial-of-service (DoS)** attacks by capping the volume of requests a single source can generate, though distributed attacks (DDoS) require additional techniques like traffic scrubbing and content delivery networks.

The key insight is that security is not a feature you bolt on — it is a property of the entire system design. A network with perfect encryption but no access controls on its management interfaces is insecure. A firewall with correct rules but no logging provides no visibility into attacks. Effective network security combines prevention (firewalls, encryption, authentication), detection (intrusion detection systems, logging, anomaly monitoring), and response (incident playbooks, automated blocking). Each layer compensates for the weaknesses of the others, and the overall security posture is determined by how well these layers work together rather than by any single technology.
