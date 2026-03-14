---
id: igmp-internet-group-management
title: IGMP (Internet Group Management Protocol)
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
builds-toward:
- multicast-routing-protocols
tags:
- igmp
- multicast
- group-management
- membership
stage: advanced
status: draft
---

# IGMP (Internet Group Management Protocol)

## Core Idea
IGMP allows hosts to join and leave IP multicast groups and informs routers about active group memberships on each link. Routers use IGMP information to decide which multicast groups to forward on each interface. Without IGMP, routers would have to flood all multicast traffic to all links, wasting bandwidth significantly.
