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
status: draft
---

# Firewall Architecture and Rules

## Core Idea
Firewalls filter traffic based on rules matching packet headers (stateless) or connection state (stateful), allowing or blocking flows to implement security policies. Stateless firewalls make decisions on individual packets; stateful firewalls track connection state and can make decisions based on the conversation history. Modern firewalls also perform deep packet inspection and application-layer filtering.

## Explainer

From your study of network security fundamentals and IP routing, you know that packets traverse networks based on destination addresses and that security requires controlling which traffic is permitted between network segments. A **firewall** is the enforcement point for that control — it sits at a network boundary (typically between an internal network and the internet, or between security zones) and applies an ordered list of rules to every packet passing through it. Each rule specifies matching criteria (source/destination IP, port numbers, protocol) and an action (allow, deny, or log). Rules are evaluated top-to-bottom, and the first matching rule determines the packet's fate. A **default rule** at the bottom (usually "deny all") catches everything that no explicit rule matched.

A **stateless packet filter** evaluates each packet in isolation against the rule set. It examines header fields — source and destination IP addresses, source and destination ports, protocol type — and decides whether to forward or drop the packet. This is fast and simple but creates an awkward problem for return traffic. If you allow outbound HTTP connections (destination port 80), you must also explicitly allow inbound packets from port 80 — but this opens a hole that an attacker could exploit by crafting packets that appear to be HTTP responses but are actually unsolicited. A **stateful firewall** solves this by maintaining a **connection table** that tracks active sessions. When an internal host initiates a TCP connection, the firewall records the session (source IP, destination IP, source port, destination port, sequence numbers). Return packets are automatically permitted if they belong to an established session, and no explicit inbound rule is needed. This dramatically simplifies rule management and closes the return-traffic vulnerability.

Modern **next-generation firewalls (NGFWs)** go further with **deep packet inspection** — examining not just headers but the actual payload content. This allows application-layer filtering: the firewall can distinguish between HTTP traffic that is web browsing and HTTP traffic that is a file transfer or a tunneled SSH session, even though they use the same port. NGFWs can enforce policies like "allow web browsing but block file uploads" or "permit Zoom but block BitTorrent," which is impossible with header-only inspection. They often integrate intrusion prevention, URL filtering, and malware scanning into the same appliance.

Firewall rule design follows the principle of **least privilege**: permit only the traffic that is explicitly required and deny everything else. Rules should be ordered from most specific to most general, since the first match wins. A common architecture places the firewall between three zones — the **internal network**, the **internet**, and a **DMZ** (demilitarized zone) for public-facing servers. The DMZ can receive inbound connections from the internet (to reach web servers, for example) but cannot initiate connections to the internal network, limiting the damage if a DMZ server is compromised. Understanding rule ordering, stateful tracking, and zone-based architecture is essential for designing security policies that are both effective and maintainable.
