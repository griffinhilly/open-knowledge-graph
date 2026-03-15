---
id: dijkstras-shortest-path-routing
title: Dijkstra's Shortest Path Algorithm in Routing
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
builds-toward:
- ospf-open-shortest-path-first
tags:
- dijkstra
- link-state
- shortest-path
- ospf
stage: advanced
status: draft
---

# Dijkstra's Shortest Path Algorithm in Routing

## Core Idea
Dijkstra's algorithm is used in link-state routing protocols like OSPF to compute the shortest path from a router to all other routers in a network. Each router runs Dijkstra independently on its synchronized view of the network topology, producing a shortest-path tree rooted at that router.
