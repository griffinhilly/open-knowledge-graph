---
id: network-centrality-measures
title: Network Centrality Measures and Node Importance
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: network-analysis-sociology
  type: hard
- id: social-network-analysis-structure
  type: hard
- id: graph-theory-fundamentals
  type: hard
builds-toward:
- community-detection-networks
- network-influence-spreading
tags:
- networks
- centrality
- influence
- graph-theory
stage: advanced
status: draft
---

# Network Centrality Measures and Node Importance

## Core Idea
Centrality measures quantify the structural importance of actors in a network. Degree centrality counts direct connections; betweenness centrality identifies brokers between groups; closeness centrality captures distance to others; eigenvector centrality recognizes connections to important alters. Different centrality measures identify different roles: hubs (degree), connectors (betweenness), leaders (eigenvector). Choosing the right centrality depends on the research question—e.g., disease transmission uses degree, while information flow uses betweenness.

## Explainer

From your work with graph theory and social network analysis, you already know that a network is a set of **nodes** (actors) and **edges** (relationships between them), and that the structure of the network shapes social behavior. Centrality measures are tools for answering a specific question about that structure: which nodes matter most, and in what sense? The catch is that "mattering" is not one thing — it depends on what is flowing through the network and what kind of power or influence you are trying to capture. Each centrality metric operationalizes a different theory of importance.

**Degree centrality** is the simplest: it counts how many edges a node has. In a friendship network, degree centrality is just the number of friends. In a disease network, it predicts exposure risk — the more contacts you have, the more ways a pathogen can reach you. Degree centrality captures local activity but is blind to where in the network those connections lead. A node with ten connections in an isolated corner of the graph may be less strategically important than a node with five connections that bridge major clusters.

**Betweenness centrality** corrects for this by measuring how often a node lies on the shortest path between other node pairs. Imagine every pair of nodes sending a message along the shortest route — betweenness counts how many of those messages pass through a given node. Nodes with high betweenness are **brokers**: they connect communities that would otherwise be isolated. Remove a high-betweenness node and information routes break down; in organizational research, such nodes are often informal coordinators who are far more critical than their formal titles suggest. **Closeness centrality** complements this by measuring the average shortest-path distance from one node to all others — a node that can reach everyone quickly (low average distance, high closeness) can spread information or access resources efficiently.

**Eigenvector centrality** takes a recursive view: a node is important if it is connected to other important nodes. Your connections inherit their importance from your connections' connections. This is the logic behind Google's original PageRank algorithm — a webpage matters not just because many pages link to it, but because important pages link to it. In social networks, eigenvector centrality identifies **prestige nodes** — actors embedded in the core of influential clusters. Choosing among these measures is a substantive decision, not just a technical one. If you are modeling disease spread, degree centrality tells you who to vaccinate first. If you are studying information gatekeeping, betweenness centrality tells you who can suppress or distort rumors. If you are studying elite influence, eigenvector centrality tells you who is embedded in the core of power. The network structure is the same in all cases; centrality is your lens.
