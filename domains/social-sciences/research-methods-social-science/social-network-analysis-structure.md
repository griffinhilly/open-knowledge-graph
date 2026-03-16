---
id: social-network-analysis-structure
title: Social Network Analysis
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: graph-theory-fundamentals
  type: hard
- id: adjacency-matrix
  type: hard
- id: degree-sequences
  type: soft
- id: graph-theory-intro
  type: soft
- id: connected-components
  type: soft
builds-toward:
- computational-social-science-intro
tags:
- networks
- centrality
- clustering
- social-capital
stage: advanced
status: draft
---

# Social Network Analysis

## Core Idea
Introduces network analysis as both theory and method for studying social relationships, structures, and flows. Covers centrality measures (degree, betweenness, closeness, eigenvector), clustering and community detection, exponential random graph models, and applications to organizational networks, information diffusion, and social capital.

## How It's Best Learned
Construct network datasets from relational data, calculate centrality measures and interpret, visualize networks, estimate ERGM models, analyze how network position shapes outcomes.

## Common Misconceptions
- Network measures always have substantive meaning
- Clustering automatically reveals communities
- Network effects cannot be causal without randomization

## Explainer

From graph theory, you already have the mathematical vocabulary: nodes, edges, adjacency matrices, degree sequences, connected components. Social network analysis takes those tools and applies them to a specific empirical question: how does the structure of social relationships shape individual and collective outcomes? The key insight is that social position is not just a property of an individual — it is a property of their location in a network. Two people with identical individual attributes can face vastly different opportunities and constraints depending on where they sit in the web of connections around them.

**Centrality** is the family of measures that capture social position. **Degree centrality** is the simplest: how many direct connections does a node have? In a citation network, a highly cited paper has high degree centrality. But degree misses something important — connections to well-connected nodes are more valuable than connections to isolated nodes. **Eigenvector centrality** (the basis of Google's PageRank) captures this: your centrality is proportional to the centrality of your neighbors. **Betweenness centrality** measures how often a node lies on the shortest path between other pairs — a node with high betweenness is a broker or gatekeeper, controlling information flows even if it has relatively few direct ties. **Closeness centrality** captures how quickly a node can reach all others in the network. Each measure captures a different theory of why position matters, and choosing among them should be driven by your substantive question, not just convenience.

**Clustering** and **community detection** identify subgroups of nodes that are more densely connected internally than to the rest of the network. The **clustering coefficient** of a node measures the fraction of its neighbors who are also connected to each other — how clique-like is the local neighborhood? High clustering indicates tight-knit communities with redundant information flows; low clustering with high betweenness indicates bridge positions. Community detection algorithms (modularity maximization, stochastic block models) try to partition the network into meaningful groups, but the result is always a function of the algorithm's assumptions. Communities aren't naturally "out there" waiting to be discovered — they are model-dependent constructs.

**Exponential random graph models (ERGMs)** address a subtle but critical problem: network data is not a collection of independent observations. Whether the edge from A to B exists is correlated with whether the edge from A to C exists (transitivity) and whether B and C are connected (triangles). Standard regression assumes independence; applying it to network edges gives biased standard errors. ERGMs model the probability of observing an entire network as a function of local structural patterns — triangles, reciprocity, degree distribution — and allow you to ask whether a particular structural feature appears more often than chance would predict given the network's overall density. They are the standard tool for statistical inference on network structure.

The sociological concept that unifies much of this is **social capital** — the resources accessible through social ties. But social capital comes in forms that correspond to different structural positions. **Bonding social capital** comes from dense, homogeneous clusters (strong ties, high clustering): good for trust, coordination, and support. **Bridging social capital** comes from connections that span different clusters (weak ties, high betweenness): good for novel information and access to diverse resources. Mark Granovetter's famous finding that people more often find jobs through acquaintances than close friends — "the strength of weak ties" — is a network argument: weak ties tend to span different social circles, so they carry non-redundant information that your close ties (who know the same people you do) cannot provide.
