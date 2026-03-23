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
stage: expert
status: validated
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

## Questions

```yaml
- question: "A company has Employee A with 20 direct contacts and Employee B with only 8 contacts. Yet B consistently learns news from different departments before A does. Which centrality concept best explains B's informational advantage?"
  type: multiple-choice
  options:
    - "B must have higher eigenvector centrality because B's few contacts are each highly connected to important people"
    - "B has high betweenness centrality — B sits on the shortest paths between otherwise disconnected groups, making B an information broker across the network"
    - "B has higher degree centrality than A when weighted by connection quality rather than quantity"
    - "B has lower closeness centrality, which paradoxically means information reaches B faster"
  answer: 1
  explanation: "This is the classic betweenness centrality scenario. A node with high betweenness lies on many shortest paths between other pairs of nodes — it is a structural bridge or broker. Even with few direct connections, a broker hears information from multiple disconnected clusters before anyone else does, because all information passing between those clusters must route through the broker. B's advantage is structural (positional), not attributional (more contacts). Degree centrality would favor A; eigenvector centrality would depend on the quality of connections; closeness centrality would indicate how quickly B can reach others — but betweenness directly explains information brokerage."

- question: "Granovetter's 'strength of weak ties' finding — that people find jobs through acquaintances more often than close friends — is best explained by which network mechanism?"
  type: multiple-choice
  options:
    - "Weak ties involve less social obligation, so acquaintances help more freely with job referrals"
    - "Close friends are more focused on their own job searches and less willing to help"
    - "Weak ties tend to bridge different social clusters, so they carry non-redundant information about job openings that your close-tie cluster (who already know the same people you do) cannot provide"
    - "Acquaintances have more formal professional connections than close friends who are typically in the same social context"
  answer: 2
  explanation: "The network explanation of Granovetter's finding is structural, not motivational. Your close friends are likely drawn from the same social cluster as you — same school, workplace, or neighborhood. Because you all know the same people, they tend to know about the same job openings. Your weak ties (acquaintances) are more likely to span different clusters — different industries, cities, or social contexts. These cross-cluster bridges carry information your strong-tie cluster doesn't have. The 'strength' of weak ties is their structural position bridging different parts of the network, not their relational strength."

- question: "Betweenness centrality can be high for a node with relatively few direct connections, because betweenness measures not how many connections a node has but whether it lies on the shortest paths between other pairs of nodes."
  type: true-false
  answer: true
  explanation: "This captures the key insight that distinguishes betweenness from degree centrality. A node with only 3 connections could have maximum betweenness if those 3 connections each link to otherwise isolated clusters — every path between those clusters must pass through the node. Conversely, a node with many connections could have low betweenness if all its neighbors are already densely interconnected (and can route around it). This is why betweenness captures 'brokerage' or 'gatekeeping' power rather than simply 'popularity.'"

- question: "Standard regression can be applied to network edges directly — treating each edge as an independent observation — to test whether structural features like triangles or reciprocity appear more often than expected by chance."
  type: true-false
  answer: false
  explanation: "Network data fundamentally violates the independence assumption of standard regression. Whether the edge A→B exists is correlated with whether A→C and B→C exist (transitivity), whether B→A exists (reciprocity), and so on throughout the network. Applying standard regression treats edges as independent when they are structurally interdependent. Exponential random graph models (ERGMs) address this by modeling the probability of the entire observed network as a function of local structural patterns, properly accounting for the dependence structure. Using standard regression on network data produces biased standard errors and unreliable inference."

- question: "Why is social position a structural rather than individual property, and what does this mean for studying outcomes like career success or access to information?"
  type: short-answer
  answer: "Social position is structural because it describes where an individual sits within a web of relationships — their pattern of connections to others and to others' connections — not just their personal attributes. Two people with identical skills, education, and personality can face radically different opportunities depending on whether they occupy a central, brokering position or a peripheral, redundant one. This means studying outcomes like career success requires measuring relational data (who is connected to whom) rather than just individual-level attributes. Network position shapes what information you receive, which opportunities you hear about, and whether others can bypass you — none of which is visible from individual-level data alone."
  explanation: "The fundamental premise of social network analysis is that social structure has independent causal power over outcomes. This challenges methodological individualism — the default assumption in much social science that outcomes are explained by individual attributes. A sociology of careers informed by SNA would look at whether someone bridges different professional clusters, not just their credentials. A public health study informed by SNA would map information diffusion paths, not just individual risk factors. The relational, structural view reveals mechanisms that individual-level analysis misses entirely."
```

## Explainer

From graph theory, you already have the mathematical vocabulary: nodes, edges, adjacency matrices, degree sequences, connected components. Social network analysis takes those tools and applies them to a specific empirical question: how does the structure of social relationships shape individual and collective outcomes? The key insight is that social position is not just a property of an individual — it is a property of their location in a network. Two people with identical individual attributes can face vastly different opportunities and constraints depending on where they sit in the web of connections around them.

**Centrality** is the family of measures that capture social position. **Degree centrality** is the simplest: how many direct connections does a node have? In a citation network, a highly cited paper has high degree centrality. But degree misses something important — connections to well-connected nodes are more valuable than connections to isolated nodes. **Eigenvector centrality** (the basis of Google's PageRank) captures this: your centrality is proportional to the centrality of your neighbors. **Betweenness centrality** measures how often a node lies on the shortest path between other pairs — a node with high betweenness is a broker or gatekeeper, controlling information flows even if it has relatively few direct ties. **Closeness centrality** captures how quickly a node can reach all others in the network. Each measure captures a different theory of why position matters, and choosing among them should be driven by your substantive question, not just convenience.

**Clustering** and **community detection** identify subgroups of nodes that are more densely connected internally than to the rest of the network. The **clustering coefficient** of a node measures the fraction of its neighbors who are also connected to each other — how clique-like is the local neighborhood? High clustering indicates tight-knit communities with redundant information flows; low clustering with high betweenness indicates bridge positions. Community detection algorithms (modularity maximization, stochastic block models) try to partition the network into meaningful groups, but the result is always a function of the algorithm's assumptions. Communities aren't naturally "out there" waiting to be discovered — they are model-dependent constructs.

**Exponential random graph models (ERGMs)** address a subtle but critical problem: network data is not a collection of independent observations. Whether the edge from A to B exists is correlated with whether the edge from A to C exists (transitivity) and whether B and C are connected (triangles). Standard regression assumes independence; applying it to network edges gives biased standard errors. ERGMs model the probability of observing an entire network as a function of local structural patterns — triangles, reciprocity, degree distribution — and allow you to ask whether a particular structural feature appears more often than chance would predict given the network's overall density. They are the standard tool for statistical inference on network structure.

The sociological concept that unifies much of this is **social capital** — the resources accessible through social ties. But social capital comes in forms that correspond to different structural positions. **Bonding social capital** comes from dense, homogeneous clusters (strong ties, high clustering): good for trust, coordination, and support. **Bridging social capital** comes from connections that span different clusters (weak ties, high betweenness): good for novel information and access to diverse resources. Mark Granovetter's famous finding that people more often find jobs through acquaintances than close friends — "the strength of weak ties" — is a network argument: weak ties tend to span different social circles, so they carry non-redundant information that your close ties (who know the same people you do) cannot provide.
