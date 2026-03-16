---
id: network-analysis-structural-positions
title: 'Social Network Analysis: Structural Positions and Dynamics'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: network-analysis-sociology
  type: hard
- id: graph-theory-fundamentals
  type: hard
- id: adjacency-matrix
  type: hard
- id: eigenvalues-eigenvectors
  type: soft
- id: graph-theory-intro
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
tags:
- network-analysis
- centrality
- structural-holes
stage: advanced
status: draft
---

# Social Network Analysis: Structural Positions and Dynamics

## Core Idea
Social network analysis models relationships as graphs and examines structural properties: centrality (importance of nodes), clustering (dense subgroups), structural holes (bridging). These properties predict information flow, influence, and resilience. Temporal network analysis adds dynamics.

## Explainer

From your work on graph theory and adjacency matrices, you have the formal machinery: actors are nodes, relationships are edges, and the adjacency matrix encodes who is connected to whom. Social network analysis uses this structure to ask: where is this actor positioned relative to others, and what does that position give them? The answer depends on which structural properties you measure, and different measures capture fundamentally different aspects of "importance."

**Degree centrality** is the simplest: how many direct connections does a node have? A person with many friends has high degree centrality. **Betweenness centrality** captures something different: how often does this node lie on the shortest path between other pairs of nodes? A person who connects two otherwise-separate friend groups has high betweenness even if they have relatively few connections total. **Eigenvector centrality** (the concept your eigenvalue knowledge unlocks) asks not just how many connections you have but how well-connected your connections are — being linked to high-centrality nodes amplifies your own centrality. Google's original PageRank algorithm is a direct application of this logic.

**Structural holes** — Ronald Burt's key contribution — are gaps between dense clusters that are not directly connected. The person who bridges two such clusters occupies a **broker** position: they control information flow between groups that don't otherwise communicate, giving them an informational and strategic advantage. This is distinct from being highly central within a single dense cluster (what Burt calls **closure**), which builds trust and social capital of a different kind. Research consistently finds that bridge positions predict career advancement, innovation, and influence — not because brokers are individually superior but because their structural position gives them earlier access to diverse information.

**Clustering coefficients** measure how densely connected a node's neighbors are to each other. High clustering means you're embedded in a tight-knit group where everyone knows everyone; low clustering means your contacts don't know each other. **Temporal network analysis** adds a time dimension: edges appear and disappear, and the sequence of connections matters. A rumor that starts at time T1 can only spread through edges that exist at T1 or later — the static graph ignores this. These dynamic properties help explain diffusion of information, disease, and innovation through social systems, connecting structural positions to actual behavioral outcomes like adoption, mobilization, or radicalization.
