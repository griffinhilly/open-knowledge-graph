---
id: multicast-routing-protocols
title: Multicast Routing Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: igmp-internet-group-management
  type: hard
- id: routing-algorithms-overview
  type: hard
tags:
- multicast
- pim
- routing
- group-communication
stage: advanced
status: draft
---

# Multicast Routing Protocols

## Core Idea
Multicast routing forwards packets from a sender to all members of a group using minimal spanning trees, avoiding unnecessary duplication. Protocol Independent Multicast (PIM) is a widely deployed multicast routing protocol that supports both source-specific and shared trees. Multicast is essential for bandwidth-efficient delivery of video, audio, and other one-to-many applications.
