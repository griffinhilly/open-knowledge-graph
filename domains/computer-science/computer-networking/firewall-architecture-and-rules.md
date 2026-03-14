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
