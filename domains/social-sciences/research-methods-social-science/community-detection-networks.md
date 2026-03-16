---
id: community-detection-networks
title: Community Detection in Social Networks
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: network-centrality-measures
  type: hard
- id: social-network-analysis-structure
  type: hard
- id: graph-theory-fundamentals
  type: hard
builds-toward:
- modularity-optimization
- stochastic-block-models
tags:
- networks
- community-structure
- clustering
- algorithms
stage: advanced
status: draft
---

# Community Detection in Social Networks

## Core Idea
Communities are groups of densely interconnected nodes with sparse connections between groups. Community detection algorithms partition networks to maximize modularity or minimize cut size. Methods range from greedy algorithms (fast, approximate) to spectral methods (mathematically grounded) to probabilistic models (interpretable). Sociologically, communities may represent factions, subcultures, or organizational divisions; detecting them reveals social structure underlying network data.

## Explainer

Your prerequisites give you the building blocks. From graph theory, you know that a network is a set of nodes connected by edges, and from centrality measures you can characterize individual nodes — their degree, betweenness, closeness. Community detection asks a higher-level question: not "who is the most central node?" but "does this network organize itself into meaningful clusters?" Where centrality describes positions within a network, community detection describes the network's **mesoscale structure** — the layer of organization between individual nodes and the network as a whole.

A **community** in a network is a set of nodes that are densely connected to each other and sparsely connected to nodes outside the set. Think of a high school social network: there are likely clusters of friend groups with many ties within each group but few ties bridging between groups. Detecting these clusters from the edge data alone — without knowing who belongs to what group — is the challenge of community detection. The naive approach (just try all possible partitions) is computationally impossible for networks of any size, since the number of possible partitions grows exponentially with the number of nodes. Efficient algorithms are therefore essential.

The standard quality measure for a partition is **modularity** (written Q), which compares the actual density of edges within communities to the density expected in a random network with the same degree sequence. A high modularity score means the detected communities have significantly more internal edges than chance would predict. The widely-used **Louvain algorithm** works by greedily assigning nodes to communities that maximize the local modularity gain, then treating each community as a single node and repeating the process. These greedy approaches are fast and scale to networks with millions of nodes, but they have a known limitation called the **resolution limit**: they may fail to detect communities smaller than a characteristic size, merging genuine small clusters into larger ones.

**Spectral methods** take a mathematically different route. They use the eigenvalues and eigenvectors of matrices derived from the network — typically the Laplacian or modularity matrix — to embed nodes in a low-dimensional geometric space where communities become separable. Because spectral methods use global structural information, they can detect communities that greedy algorithms miss. **Probabilistic models** like stochastic block models (SBMs) go further by treating community membership as a latent variable: each node is assigned to a block, and edge probabilities are a function of block membership. This gives you not just a partition but a generative model of how the network was produced — a principled way to assess whether any community structure exists at all, or whether the observed clustering could have arisen by chance.

Sociologically, the communities you detect must be interpreted with care. A detected community is a structural signature — a pattern of connectivity — not a self-identified group. It may correspond to a real social unit like a team, a faction, or a friendship circle, or it may be an artifact of the algorithm or sampling procedure. Always validate detected communities against substantive knowledge: do members share attributes, organizational roles, or interaction contexts that would explain the dense connectivity? The real value of community detection is as a discovery tool — it surfaces structure that is invisible from individual node properties alone, revealing the mesoscale organization of a social system in a way that bridges your network analysis skills with substantive sociological questions about how groups and coalitions form.

