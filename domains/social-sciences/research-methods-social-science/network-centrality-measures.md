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

## Questions

```yaml
- question: "Public health officials want to prioritize vaccination to most efficiently slow the spread of a contagious disease through a social contact network. Which centrality measure should guide their prioritization?"
  type: multiple-choice
  options:
    - "Eigenvector centrality — targeting those connected to important people disrupts elite transmission chains"
    - "Closeness centrality — vaccinating those who can reach everyone quickly prevents rapid spread"
    - "Degree centrality — vaccinating the most-connected individuals removes the nodes with the most transmission routes"
    - "Betweenness centrality — vaccinating bridges between communities is always the most efficient strategy"
  answer: 2
  explanation: "For disease spread, degree centrality (number of contacts) is the primary predictor of exposure risk and transmission potential — each contact is an independent transmission route. Degree centrality is the right lens because the question is about direct exposure, not about information gatekeeping or elite influence. Betweenness centrality becomes more relevant for inter-community spread (like halting a disease that has reached one cluster from reaching others), but degree is the foundational answer for individual transmission risk."

- question: "Node X has 15 connections, all within a single densely connected clique. Node Y has 5 connections but serves as the only link between three otherwise disconnected communities. Which statement best describes their centrality profiles?"
  type: multiple-choice
  options:
    - "Node X is more important by every measure because it has more connections"
    - "Node Y has higher betweenness centrality despite lower degree centrality"
    - "Node Y has both higher betweenness and higher eigenvector centrality than X"
    - "Neither node is strategically important unless both are high on all centrality measures"
  answer: 1
  explanation: "Betweenness centrality measures how often a node lies on shortest paths between other pairs — Node Y, spanning three disconnected communities, sits on virtually every cross-community path and thus has extremely high betweenness. Node X, though highly connected, sits within a clique where every member can reach every other without passing through X. This demonstrates that degree and betweenness measure different things: local activity versus structural bridging. Eigenvector centrality depends on the centrality of Y's neighbors, not addressed here."

- question: "A node with the highest degree centrality in a network will necessarily also have the highest betweenness centrality."
  type: true-false
  answer: false
  explanation: "Degree and betweenness measure fundamentally different structural properties. A highly connected hub within a dense, isolated cluster can have low betweenness because all its connections stay within that cluster — other node pairs can reach each other without routing through it. Conversely, a modestly connected node that bridges otherwise disconnected communities can have very high betweenness with low degree. Knowing one centrality value tells you very little about a node's score on other measures."

- question: "Eigenvector centrality scores a node higher if it is connected to other high-centrality nodes, meaning a single connection to a very central node can outweigh many connections to peripheral nodes."
  type: true-false
  answer: true
  explanation: "Eigenvector centrality is recursive — your score depends on your neighbors' scores, which depend on their neighbors' scores, and so on. This is the logic behind Google's PageRank: a page linked by many prestigious pages scores higher than one linked by many obscure pages. In social networks, this captures prestige and embeddedness in influential clusters, which degree centrality misses entirely."

- question: "Why does the choice of centrality measure constitute a substantive research decision rather than a purely technical one?"
  type: short-answer
  answer: "Each centrality measure embeds a different theory of what 'importance' means in a network — degree assumes importance = number of contacts, betweenness assumes importance = control over flows between groups, eigenvector assumes importance = connection to other important actors. The right measure depends on what is flowing through the network and what question you are asking. Choosing the wrong measure can lead to identifying the wrong actors as key targets for intervention."
  explanation: "For disease transmission, high-degree nodes are the targets. For understanding information gatekeeping and who can suppress or distort rumors, betweenness identifies the brokers. For understanding elite influence and social capital, eigenvector identifies the core. The network structure is identical in all cases — the centrality measure is the analytical lens you apply based on your theoretical assumptions about how influence or spread operates."
```

## Explainer

From your work with graph theory and social network analysis, you already know that a network is a set of **nodes** (actors) and **edges** (relationships between them), and that the structure of the network shapes social behavior. Centrality measures are tools for answering a specific question about that structure: which nodes matter most, and in what sense? The catch is that "mattering" is not one thing — it depends on what is flowing through the network and what kind of power or influence you are trying to capture. Each centrality metric operationalizes a different theory of importance.

**Degree centrality** is the simplest: it counts how many edges a node has. In a friendship network, degree centrality is just the number of friends. In a disease network, it predicts exposure risk — the more contacts you have, the more ways a pathogen can reach you. Degree centrality captures local activity but is blind to where in the network those connections lead. A node with ten connections in an isolated corner of the graph may be less strategically important than a node with five connections that bridge major clusters.

**Betweenness centrality** corrects for this by measuring how often a node lies on the shortest path between other node pairs. Imagine every pair of nodes sending a message along the shortest route — betweenness counts how many of those messages pass through a given node. Nodes with high betweenness are **brokers**: they connect communities that would otherwise be isolated. Remove a high-betweenness node and information routes break down; in organizational research, such nodes are often informal coordinators who are far more critical than their formal titles suggest. **Closeness centrality** complements this by measuring the average shortest-path distance from one node to all others — a node that can reach everyone quickly (low average distance, high closeness) can spread information or access resources efficiently.

**Eigenvector centrality** takes a recursive view: a node is important if it is connected to other important nodes. Your connections inherit their importance from your connections' connections. This is the logic behind Google's original PageRank algorithm — a webpage matters not just because many pages link to it, but because important pages link to it. In social networks, eigenvector centrality identifies **prestige nodes** — actors embedded in the core of influential clusters. Choosing among these measures is a substantive decision, not just a technical one. If you are modeling disease spread, degree centrality tells you who to vaccinate first. If you are studying information gatekeeping, betweenness centrality tells you who can suppress or distort rumors. If you are studying elite influence, eigenvector centrality tells you who is embedded in the core of power. The network structure is the same in all cases; centrality is your lens.
