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

## Explainer

Standard neural networks assume their input has a fixed, regular structure — images are grids of pixels, text is a sequence of tokens. But many real-world datasets are naturally represented as **graphs**: social networks (users connected by friendships), molecules (atoms connected by bonds), citation networks (papers connected by references), and knowledge graphs (entities connected by relations). You can't simply flatten a graph into a vector and feed it into a regular neural network because graphs have variable size, no canonical node ordering, and complex connectivity patterns. **Graph neural networks** (GNNs) solve this by designing neural network operations that respect and exploit graph structure directly.

The fundamental operation in a GNN is **neighborhood aggregation** (also called message passing). For each node in the graph, the network collects feature information from its neighbors, combines it (through summation, averaging, or a learned function), and uses the result to update the node's own representation. One round of aggregation lets each node "see" its immediate neighbors; stacking multiple layers lets information propagate further — after k layers, each node's representation encodes information from its k-hop neighborhood. If you're familiar with the adjacency matrix representation of graphs, you can think of one GNN layer as multiplying the feature matrix by the (normalized) adjacency matrix and then applying a nonlinear transformation — similar in spirit to a standard neural network layer, but with the adjacency matrix defining which nodes communicate.

The major GNN variants differ in how they aggregate neighbor information. **Graph Convolutional Networks** (GCNs) use a fixed aggregation scheme based on the normalized adjacency matrix — every neighbor contributes equally, scaled by degree. **GraphSAGE** samples a fixed number of neighbors and applies a learnable aggregation function (mean, LSTM, or max-pool), making it scalable to large graphs where examining all neighbors is expensive. **Graph Attention Networks** (GATs) borrow the attention mechanism from transformers: they learn to assign different importance weights to different neighbors, so the network can focus on the most relevant connections. The choice of variant depends on the application — GCNs are simple and effective for many benchmarks, GraphSAGE scales to graphs with millions of nodes, and GATs excel when the importance of neighbors varies.

GNNs can be applied at three levels of granularity. **Node-level tasks** predict properties of individual nodes (e.g., classifying users in a social network or predicting the function of proteins). **Edge-level tasks** predict relationships between pairs of nodes (e.g., link prediction in knowledge graphs or recommending connections). **Graph-level tasks** predict properties of entire graphs (e.g., predicting whether a molecular graph represents a toxic compound), typically by adding a readout or pooling layer that aggregates all node representations into a single graph-level vector. The key insight across all these applications is that GNNs learn representations that capture both the features of individual entities and the structure of their relationships — something that no amount of feature engineering on flat tabular data can easily achieve.
