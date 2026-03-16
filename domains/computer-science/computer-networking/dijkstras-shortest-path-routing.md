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

## Explainer

From your overview of routing algorithms, you know that routers must decide which interface to forward each packet through, and that link-state protocols work by giving every router a complete map of the network. Dijkstra's algorithm is the engine that turns that map into actual forwarding decisions. It answers the question: given a weighted graph where nodes are routers and edge weights represent link costs (delay, bandwidth, or administrative metrics), what is the least-cost path from me to every other router?

The algorithm works by maintaining two sets: a **confirmed set** of routers whose shortest path is already known, and a **tentative set** of candidates. Initially, only the source router (you) is confirmed, with cost 0. You examine all links from confirmed routers to unconfirmed neighbors, recording the total cost to reach each neighbor through the best known path. Then you move the lowest-cost tentative node into the confirmed set — this is the greedy step, and it works because all link costs are non-negative, so no cheaper path to that node can exist through an unvisited router. You then examine that newly confirmed node's neighbors and update their tentative costs if a cheaper path through the new node exists. This process repeats until every router is confirmed.

The result is a **shortest-path tree (SPT)** rooted at the source router. Each branch of this tree represents the optimal forwarding path to a destination. The router only needs the first hop of each path to build its **forwarding table**: to reach destination X, send the packet out the interface that leads to the next hop on the shortest path to X. Because every router in the network has the same topology database (synchronized via link-state advertisements), every router independently computes its own SPT, and the forwarding decisions are globally consistent — packets follow optimal paths without loops.

In practice, OSPF (Open Shortest Path First) runs Dijkstra every time the topology changes — a link goes down, a cost changes, or a new router joins. The algorithm's time complexity is O(N² ) for a simple implementation or O(N log N + E) with a priority queue, where N is the number of routers and E is the number of links. For networks of hundreds or even thousands of routers, this runs in milliseconds. The real cost is not computation but **convergence** — the time for all routers to receive the updated topology information and recompute their trees. During convergence, routers may briefly have inconsistent views, potentially causing transient loops or packet drops until the network stabilizes.
