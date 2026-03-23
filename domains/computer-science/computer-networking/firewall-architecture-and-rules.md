---
id: firewall-architecture-and-rules
title: Firewall Architecture and Rules
domain: computer-science
course: computer-networking
prerequisites:
- id: network-security-fundamentals
  type: hard
- id: ip-routing-basics
  type: hard
builds-toward:
- intrusion-detection-and-prevention
tags:
- firewall
- packet-filtering
- stateful-inspection
- access-control
stage: advanced
status: validated
---

# Firewall Architecture and Rules

## Core Idea
Firewalls filter traffic based on rules matching packet headers (stateless) or connection state (stateful), allowing or blocking flows to implement security policies. Stateless firewalls make decisions on individual packets; stateful firewalls track connection state and can make decisions based on the conversation history. Modern firewalls also perform deep packet inspection and application-layer filtering.

## Questions

```yaml
- question: "A network administrator configures a stateless firewall with the rule 'allow inbound TCP from any source on port 80' to permit web browsing return traffic. What security vulnerability does this create?"
  type: multiple-choice
  options:
    - "It inadvertently blocks HTTPS traffic, which uses port 443"
    - "It slows down network performance because every inbound packet must be inspected against the full rule set"
    - "It permits any external host to initiate unsolicited connections to internal machines on port 80, because the stateless firewall cannot distinguish return traffic from attack traffic"
    - "It only creates a vulnerability for HTTP — HTTPS traffic is filtered independently"
  answer: 2
  explanation: "A stateless firewall evaluates each packet in isolation without knowing whether it is part of an established session. The rule 'allow inbound TCP from any source port 80' matches both legitimate web server responses AND packets crafted by an attacker to appear as if they originate from port 80. The firewall cannot tell the difference. A stateful firewall solves this by tracking which internal hosts initiated outbound connections and automatically allowing only the return packets that belong to those sessions — no permissive inbound rule is needed."

- question: "A company places its public web server directly on the internal network and configures the firewall to allow inbound traffic on ports 80 and 443. What is the key security risk compared to placing the web server in a DMZ?"
  type: multiple-choice
  options:
    - "The web server will perform worse because traffic must traverse the firewall twice"
    - "If the web server is compromised, the attacker has direct access to the internal network — a DMZ would isolate the web server so a breach cannot directly reach internal systems"
    - "Port 80 traffic is inherently insecure regardless of where the server is placed in the network"
    - "All architectures without a DMZ carry identical risk — only the firewall rules determine security, not network segmentation"
  answer: 1
  explanation: "The DMZ's purpose is blast radius limitation. A public-facing web server is an attractive attack target; if it is on the internal network, a successful compromise gives the attacker a foothold directly adjacent to sensitive internal systems. A DMZ places the web server in a separate segment that can receive inbound internet connections but cannot initiate connections to the internal network. Even if the web server is fully compromised, the attacker is still separated from the internal network by another firewall layer."

- question: "A stateful firewall requires explicit allow rules for both the outbound request and the corresponding inbound response in order to permit employees to browse websites."
  type: true-false
  answer: false
  explanation: "This describes stateless firewall behavior, not stateful. A stateful firewall maintains a connection table that records active sessions. When an employee's browser sends an outbound HTTP request, the firewall logs the session (source IP, destination IP, source port, destination port). When the web server's response arrives inbound, the firewall checks the connection table, recognizes it as belonging to an established session, and permits it automatically — without any explicit inbound rule. This is precisely the advantage of stateful inspection: return traffic is handled implicitly, eliminating the security hole that explicit inbound port rules create."

- question: "In a firewall rule set evaluated top-to-bottom, placing a broad 'permit all TCP' rule before a specific 'deny port 23 (Telnet)' rule means that Telnet traffic will be permitted despite the deny rule."
  type: true-false
  answer: true
  explanation: "Firewalls use first-match evaluation: the first rule in the list that matches a packet determines its fate. If 'permit all TCP' appears first, every TCP packet — including Telnet on port 23 — matches it and is permitted before the firewall even reaches the deny rule. The deny rule is dead code in this configuration. This is why firewall rules must be ordered from most specific to most general, with broad rules (like 'deny all') at the bottom as defaults. A misplaced broad permit rule can silently allow traffic you intended to block."

- question: "Explain why stateful firewalls are considered more secure than stateless firewalls for protecting internal networks from unsolicited inbound connections."
  type: short-answer
  answer: "Stateful firewalls track connection state in a session table. When an internal host initiates an outbound connection, the firewall records the session details (IPs, ports, sequence numbers). Inbound packets are checked against this table: if they match an established outgoing session, they are permitted; otherwise they are dropped by default. This means no permissive inbound rules are needed — the firewall distinguishes legitimate responses from unsolicited attacks based on whether a session exists. Stateless firewalls evaluate each packet independently and cannot make this distinction, forcing administrators to write permissive inbound rules (e.g., 'allow source port 80') that any attacker can exploit by crafting packets with matching source ports."
  explanation: "The fundamental limitation of stateless firewalls is amnesia: each packet is evaluated as if no prior packets ever existed. Stateful firewalls have memory: they know which internal hosts reached out and expect a response, and they reject everything else. This transforms the security model from 'allow traffic that looks right' to 'allow only traffic that belongs to a known session.'"
```

## Explainer

From your study of network security fundamentals and IP routing, you know that packets traverse networks based on destination addresses and that security requires controlling which traffic is permitted between network segments. A **firewall** is the enforcement point for that control — it sits at a network boundary (typically between an internal network and the internet, or between security zones) and applies an ordered list of rules to every packet passing through it. Each rule specifies matching criteria (source/destination IP, port numbers, protocol) and an action (allow, deny, or log). Rules are evaluated top-to-bottom, and the first matching rule determines the packet's fate. A **default rule** at the bottom (usually "deny all") catches everything that no explicit rule matched.

A **stateless packet filter** evaluates each packet in isolation against the rule set. It examines header fields — source and destination IP addresses, source and destination ports, protocol type — and decides whether to forward or drop the packet. This is fast and simple but creates an awkward problem for return traffic. If you allow outbound HTTP connections (destination port 80), you must also explicitly allow inbound packets from port 80 — but this opens a hole that an attacker could exploit by crafting packets that appear to be HTTP responses but are actually unsolicited. A **stateful firewall** solves this by maintaining a **connection table** that tracks active sessions. When an internal host initiates a TCP connection, the firewall records the session (source IP, destination IP, source port, destination port, sequence numbers). Return packets are automatically permitted if they belong to an established session, and no explicit inbound rule is needed. This dramatically simplifies rule management and closes the return-traffic vulnerability.

Modern **next-generation firewalls (NGFWs)** go further with **deep packet inspection** — examining not just headers but the actual payload content. This allows application-layer filtering: the firewall can distinguish between HTTP traffic that is web browsing and HTTP traffic that is a file transfer or a tunneled SSH session, even though they use the same port. NGFWs can enforce policies like "allow web browsing but block file uploads" or "permit Zoom but block BitTorrent," which is impossible with header-only inspection. They often integrate intrusion prevention, URL filtering, and malware scanning into the same appliance.

Firewall rule design follows the principle of **least privilege**: permit only the traffic that is explicitly required and deny everything else. Rules should be ordered from most specific to most general, since the first match wins. A common architecture places the firewall between three zones — the **internal network**, the **internet**, and a **DMZ** (demilitarized zone) for public-facing servers. The DMZ can receive inbound connections from the internet (to reach web servers, for example) but cannot initiate connections to the internal network, limiting the damage if a DMZ server is compromised. Understanding rule ordering, stateful tracking, and zone-based architecture is essential for designing security policies that are both effective and maintainable.
