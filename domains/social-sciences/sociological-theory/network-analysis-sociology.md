---
id: network-analysis-sociology
title: Network Analysis in Sociology
domain: social-sciences
course: sociological-theory
prerequisites:
- id: sociological-imagination
  type: hard
- id: graph-theory-fundamentals
  type: hard
- id: degree-sequences
  type: soft
builds-toward:
- granovetter-weak-ties
tags:
- network
- social-networks
- graph-theory
- relations
stage: abstract-reasoning
status: draft
---

# Network Analysis in Sociology

## Core Idea
Network analysis studies social structure as patterns of connections between actors (individuals, organizations, nations). Sociologists examine centrality, clustering, brokerage, and diffusion to understand how networks constrain opportunity, transmit information, and shape outcomes.

## Explainer

You bring two prerequisite frameworks to network analysis that are now in direct conversation. From the sociological imagination, you know that individual lives are shaped by social structures that individuals cannot fully see or control. From graph theory, you know how to represent relationships formally: nodes, edges, paths, components, and the mathematical properties that follow from those structures. Network analysis in sociology is what happens when you apply graph-theoretic tools to social structures — it gives the sociological imagination a formal vocabulary.

The foundational move is representing social actors as **nodes** and their relationships as **edges**. But which relationships? This choice is sociologically loaded. You can map friendship ties, advice-seeking, co-authorship, financial transactions, phone calls, or sexual contact — each captures a different social process and will produce a different structural picture. The network you analyze must be selected based on a theory of what kind of connection matters for the outcome you are trying to explain. Choosing the wrong relational substrate produces misleading structural conclusions.

Three concepts do most of the explanatory work. **Centrality** measures how well-positioned an actor is within the network. Degree centrality (raw number of connections) captures popularity; betweenness centrality measures how often an actor lies on the shortest path between other pairs — these are the **brokers** who sit at critical information bridges. Eigenvector centrality (the basis of PageRank) captures whether your connections are themselves well-connected. **Clustering** measures how often your connections are connected to each other — high clustering means you are embedded in a tight-knit community where information circulates densely but redundantly. **Path length** measures how many steps separate any two nodes — short average path lengths mean information diffuses quickly across the whole network.

These structural properties explain outcomes that individual-level attributes cannot. A person with modest credentials but high betweenness centrality can wield disproportionate influence by controlling information flow between otherwise disconnected groups. A highly talented person isolated within a dense cluster may accomplish less than a well-connected broker who can link knowledge across different communities. Granovetter's famous finding — that **weak ties** (acquaintances rather than close friends) are often more valuable for job searches than strong ties — follows directly from this logic: your close friends are in your cluster and know what you know, while weak ties reach into other clusters where novel information resides. Network analysis makes this structural insight precise, measurable, and portable across domains.
