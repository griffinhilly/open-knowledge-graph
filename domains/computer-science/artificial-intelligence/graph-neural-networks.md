---
id: graph-neural-networks
title: Graph Neural Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: knowledge-graphs
  type: soft
- id: matrices-intro
  type: soft
- id: graph-theory-intro
  type: soft
- id: graph-adjacency-list-matrix-representations
  type: soft
builds-toward:
- graph-convolutions
- message-passing
tags:
- graph-neural-network
- gnn
- node-classification
stage: advanced
status: draft
---

# Graph Neural Networks

## Core Idea
Graph neural networks extend deep learning to graph-structured data by propagating information across edges. GNNs learn node representations by iteratively aggregating neighbor information. Variants include GCNs (convolutional), GraphSAGE (sampling), and GATs (attention). Applications span social networks, molecules, knowledge graphs, and recommendations.
