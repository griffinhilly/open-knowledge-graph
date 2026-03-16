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

## Explainer

From your understanding of IPv4 addressing, you know that unicast sends a packet to one specific host and broadcast sends it to every host on a network. **Multicast** sits between these extremes — it delivers a packet to a specific group of interested hosts, and only those hosts. Think of it like a radio station: the station broadcasts once, and only the radios tuned to that frequency receive the signal. IP multicast uses the Class D address range (224.0.0.0 to 239.255.255.255) to identify these groups. But routers need a way to know which groups have interested listeners on each of their interfaces — that is the role of **IGMP** (Internet Group Management Protocol).

IGMP operates between hosts and their **local router** (the first-hop router on the same network segment). It does not route multicast traffic across the Internet — that is handled by multicast routing protocols. IGMP answers a simpler question: "Are there any hosts on this link that want to receive traffic for multicast group X?" The protocol works through a query-response mechanism. The router periodically sends an **IGMP Membership Query** to the all-hosts address (224.0.0.1), asking "who is listening to what?" Hosts that have joined a multicast group respond with a **Membership Report** identifying the group. If at least one host on the link reports membership in a group, the router continues forwarding that group's traffic to the link. If no host responds after several queries, the router stops forwarding — saving bandwidth.

When a host wants to join a multicast group, it sends an **unsolicited Membership Report** immediately, without waiting for a query. This ensures the router starts forwarding the group's traffic right away. Leaving is handled differently across IGMP versions. In **IGMPv2**, a host sends an explicit **Leave Group** message, and the router responds with a **Group-Specific Query** to check if any other hosts on the link still want the traffic. If none respond, forwarding stops. **IGMPv3** adds **source filtering**, allowing a host to say "I want traffic for group G, but only from source S" — this supports Source-Specific Multicast (SSM), which is more efficient and secure for applications like IPTV.

A practical detail is the **report suppression** mechanism in IGMPv1 and v2. When a host hears another host on the same link report membership in the same group, it cancels its own report to avoid flooding the router with duplicate messages. Each host sets a random timer when it receives a query, and only sends its report if no other host reported first. This keeps IGMP traffic minimal even on links with hundreds of hosts in the same group. Understanding IGMP is essential before studying multicast routing protocols, because those protocols build inter-router multicast trees based on the per-link membership information that IGMP provides.
