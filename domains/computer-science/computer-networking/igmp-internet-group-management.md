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

## Questions

```yaml
- question: "A host on a LAN segment sends an IGMP Membership Report for group 239.1.1.1. Which device's behavior is directly affected by this message?"
  type: multiple-choice
  options:
    - "The multicast source, which will now start sending traffic to the host"
    - "The first-hop router on the same LAN segment, which will start forwarding group traffic to that link"
    - "All routers on the Internet that handle multicast routing for group 239.1.1.1"
    - "The DNS server, which will resolve the group address to a hostname"
  answer: 1
  explanation: "IGMP operates only between hosts and their local (first-hop) router on the same link. The Membership Report tells that router 'at least one host on my link wants group 239.1.1.1,' causing the router to start forwarding that group's traffic to the link. IGMP does NOT communicate with the multicast source, with distant routers, or with DNS. Inter-router multicast distribution is handled separately by multicast routing protocols like PIM, which build trees based on the local IGMP membership information."

- question: "In IGMPv2, a host is receiving traffic for multicast group 224.2.2.2. It decides to leave the group. What sequence of events follows?"
  type: multiple-choice
  options:
    - "The host simply stops listening; the router detects this when its next membership report times out"
    - "The host sends a Leave Group message; the router may send a Group-Specific Query; if no other hosts respond, forwarding stops"
    - "The host sends an IGMP Membership Report for a different group to override its previous report"
    - "The host must contact the multicast source directly to unsubscribe"
  answer: 1
  explanation: "IGMPv2 introduced explicit Leave Group messages so that group departure is prompt rather than waiting for a query timeout. When the router receives the Leave, it sends a Group-Specific Query to check if any other hosts on the segment still want the group. If no Membership Reports are received within the query interval, the router stops forwarding to that link. This 'fast-leave' mechanism was a major improvement over IGMPv1, where the router had to wait for multiple query cycles (potentially minutes) before realizing no host needed the group."

- question: "IGMP is responsible for routing multicast traffic between routers across the Internet."
  type: true-false
  answer: false
  explanation: "IGMP is strictly a local protocol — it operates only between hosts and their first-hop router on the same network segment. Its job is to tell the local router which multicast groups have interested listeners on that link. Routing multicast traffic between routers across the Internet is the job of multicast routing protocols such as PIM (Protocol Independent Multicast). IGMP provides the per-link membership information that those routing protocols use to build distribution trees, but IGMP itself never crosses a router boundary."

- question: "In a subnet with 100 hosts all listening to the same multicast group, all 100 hosts will send IGMP Membership Reports in response to a router's Membership Query."
  type: true-false
  answer: false
  explanation: "IGMP includes a report suppression mechanism (in IGMPv1 and v2) to prevent exactly this scenario. When a host receives a query, it starts a random timer. If it hears another host on the same segment report the same group before its timer expires, it cancels its own report — the router only needs one confirmation that the group is active on the link. This random back-off ensures that only one (or a few) reports are sent per group per query cycle, keeping IGMP overhead minimal even on densely populated segments."

- question: "Why does the router send a Group-Specific Query after receiving an IGMPv2 Leave Group message, rather than immediately stopping multicast forwarding for that group?"
  type: short-answer
  answer: "Because the Leave Group message comes from one host, but there may be other hosts on the same link still listening to that group. The router cannot safely stop forwarding based on one host's departure — doing so would cut off any remaining listeners. The Group-Specific Query asks 'does anyone else on this link still want this group?' Only if no Membership Reports are received does the router stop forwarding. This ensures correct behavior in multi-host environments while still achieving fast leave compared to waiting for a full query cycle."
  explanation: "This design reflects IGMP's core operating model: the router maintains per-link group state based on whether *any* host on the link wants the group, not which specific hosts do. It cannot track individual host memberships — it only needs to know if forwarding is needed at all. The Group-Specific Query is the minimum-cost mechanism to verify that forwarding can safely stop."
```

## Explainer

From your understanding of IPv4 addressing, you know that unicast sends a packet to one specific host and broadcast sends it to every host on a network. **Multicast** sits between these extremes — it delivers a packet to a specific group of interested hosts, and only those hosts. Think of it like a radio station: the station broadcasts once, and only the radios tuned to that frequency receive the signal. IP multicast uses the Class D address range (224.0.0.0 to 239.255.255.255) to identify these groups. But routers need a way to know which groups have interested listeners on each of their interfaces — that is the role of **IGMP** (Internet Group Management Protocol).

IGMP operates between hosts and their **local router** (the first-hop router on the same network segment). It does not route multicast traffic across the Internet — that is handled by multicast routing protocols. IGMP answers a simpler question: "Are there any hosts on this link that want to receive traffic for multicast group X?" The protocol works through a query-response mechanism. The router periodically sends an **IGMP Membership Query** to the all-hosts address (224.0.0.1), asking "who is listening to what?" Hosts that have joined a multicast group respond with a **Membership Report** identifying the group. If at least one host on the link reports membership in a group, the router continues forwarding that group's traffic to the link. If no host responds after several queries, the router stops forwarding — saving bandwidth.

When a host wants to join a multicast group, it sends an **unsolicited Membership Report** immediately, without waiting for a query. This ensures the router starts forwarding the group's traffic right away. Leaving is handled differently across IGMP versions. In **IGMPv2**, a host sends an explicit **Leave Group** message, and the router responds with a **Group-Specific Query** to check if any other hosts on the link still want the traffic. If none respond, forwarding stops. **IGMPv3** adds **source filtering**, allowing a host to say "I want traffic for group G, but only from source S" — this supports Source-Specific Multicast (SSM), which is more efficient and secure for applications like IPTV.

A practical detail is the **report suppression** mechanism in IGMPv1 and v2. When a host hears another host on the same link report membership in the same group, it cancels its own report to avoid flooding the router with duplicate messages. Each host sets a random timer when it receives a query, and only sends its report if no other host reported first. This keeps IGMP traffic minimal even on links with hundreds of hosts in the same group. Understanding IGMP is essential before studying multicast routing protocols, because those protocols build inter-router multicast trees based on the per-link membership information that IGMP provides.
