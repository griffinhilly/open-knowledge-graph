---
id: routing-table-concepts
title: Routing Table Concepts
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
builds-toward:
- distance-vector-routing-protocols
- link-state-routing-protocols
tags:
- routing-table
- route-lookup
- next-hop
- longest-prefix-match
stage: advanced
status: draft
---

# Routing Table Concepts

## Core Idea
A routing table maps destination addresses to outgoing interfaces and next-hop addresses. Routers use longest-prefix matching to find the most specific route for each packet destination. Efficient routing table lookup requires data structures like tries or hash tables to handle millions of routes at line-rate speeds.
