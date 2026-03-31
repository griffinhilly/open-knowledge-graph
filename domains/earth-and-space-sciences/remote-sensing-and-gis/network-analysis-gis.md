---
id: network-analysis-gis
title: Network Analysis in GIS
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: gis-fundamentals
  type: hard
- id: spatial-analysis-gis
  type: hard
builds-toward:
- web-gis
tags:
- network-analysis
- routing
- shortest-path
- service-areas
stage: advanced
status: validated
---

# Network Analysis in GIS

## Core Idea
Network analysis applies graph theory to geographic linear features (roads, rivers, pipelines, utilities) to solve routing, allocation, and connectivity problems. Unlike Euclidean spatial analysis that measures straight-line distances, network analysis respects the constraints of the network: travel occurs along edges (road segments) between nodes (intersections), and costs (distance, time, impedance) accumulate along the path. Core operations include shortest path routing (finding the least-cost route between two points), service area delineation (finding all locations reachable within a time or distance threshold), closest facility analysis, and location-allocation (optimally placing facilities to serve demand).

## Questions

```yaml
- question: "An ambulance service needs to determine which hospital each neighborhood should be assigned to for the fastest emergency response. Why would network-based analysis give a fundamentally different answer than simple straight-line distance?"
  type: multiple-choice
  options:
    - "Network analysis accounts for road connectivity, one-way streets, speed limits, and turn restrictions, while straight-line distance ignores barriers like rivers, highways, and terrain"
    - "Network analysis is always faster to compute"
    - "Straight-line distance overestimates travel time in all cases"
    - "Network analysis only works for rural areas"
  answer: 0
  explanation: "A neighborhood may be physically close to Hospital A (straight-line) but separated by a river with no nearby bridge, making Hospital B -- farther by straight-line but connected by direct highway -- actually faster to reach. Network analysis models the actual travel paths, including road speeds, connectivity, one-way streets, and barriers, producing service areas that reflect real-world accessibility rather than geometric proximity."

- question: "Network analysis is only useful for transportation applications like routing vehicles."
  type: true-false
  answer: false
  explanation: "Network analysis applies to any system that can be modeled as a connected graph. Hydrologists use it to trace stream networks and model upstream/downstream connectivity. Utilities use it to model water, gas, and electrical networks for flow analysis and outage tracing. Ecologists model wildlife corridors as habitat connectivity networks. Epidemiologists trace disease transmission networks. Any system where flow, connectivity, or path-dependent processes matter can benefit from network analysis."

- question: "Explain the difference between a shortest-path analysis and a service area analysis in the context of emergency management."
  type: short-answer
  answer: "Shortest-path finds the optimal route between a specific origin and destination (e.g., routing an ambulance from its station to a reported emergency). Service area analysis finds all locations reachable from a facility within a specified cost (e.g., all areas a fire station can reach within 5 minutes). Shortest-path solves a one-to-one routing problem; service area solves a one-to-many accessibility problem. Both use the same network and cost model, but they answer different questions: 'how do I get there?' versus 'where can I reach?'"
  explanation: "Service areas are the network-based equivalent of buffers -- they define zones of accessibility, but following the network rather than straight-line distance."
```

## Explainer

Spatial analysis typically operates in continuous space -- buffering, overlay, and interpolation assume that distance and movement work in all directions. But much of human activity is constrained to networks: we drive on roads, water flows through pipes, electricity follows wires, data travels through cables. Network analysis brings GIS into this structured, path-constrained world.

A network data model represents the system as a graph: nodes (intersections, junctions) connected by edges (road segments, pipe sections) with attributes encoding cost (travel time, distance, friction). The cost of traversing an edge can be asymmetric (one-way streets, uphill vs downhill flow), time-dependent (rush hour congestion), or multi-dimensional (optimizing for both time and distance). Dijkstra's algorithm and its variants (A*, contraction hierarchies) efficiently find least-cost paths through networks with millions of edges.

Service area analysis extends shortest-path computation to find the frontier of reachable locations within a cost threshold. The 5-minute service area of a fire station includes every road segment and address reachable within 5 minutes of travel along the road network. These service areas are typically irregular shapes reflecting the network structure, not concentric circles. Comparing service areas from multiple facilities identifies coverage gaps and overlaps, guiding facility planning.

Location-allocation problems combine demand modeling with network accessibility to optimally place facilities. Given a set of candidate locations and a demand distribution, the algorithm finds the placement that minimizes total travel cost, maximizes coverage, or satisfies a service standard. This powers decisions about where to locate warehouses, clinics, schools, and emergency facilities -- problems where network distance rather than straight-line distance determines real-world service quality.
