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
- id: graph-adjacency-list-matrix-representations
  type: soft
tags:
- graph-neural-network
- gnn
- node-classification
stage: expert
status: validated
---

# Graph Neural Networks

## Core Idea
Graph neural networks extend deep learning to graph-structured data by propagating information across edges. GNNs learn node representations by iteratively aggregating neighbor information. Variants include GCNs (convolutional), GraphSAGE (sampling), and GATs (attention). Applications span social networks, molecules, knowledge graphs, and recommendations.

## Questions

```yaml
- question: "A GNN is trained to classify nodes in a citation network. After training, you discover the model uses 3 layers of neighborhood aggregation. What information does each node's learned representation capture?"
  type: multiple-choice
  options:
    - "Each node's representation encodes features of all nodes within 3 hops (its 3-hop neighborhood)"
    - "Each node's representation captures only its own features, since layers process nodes independently"
    - "Each node's representation encodes features of its immediate neighbors only, regardless of depth"
    - "Each node's representation is an average of all other nodes in the graph"
  answer: 0
  explanation: "Each GNN layer aggregates information from 1-hop neighbors. After k layers, a node's representation has 'seen' its k-hop neighborhood. With 3 layers, every node incorporates feature information from nodes up to 3 edges away. This is the core mechanism that allows GNNs to capture structural context."

- question: "What is the key difference between a Graph Convolutional Network (GCN) and a Graph Attention Network (GAT) in how they aggregate neighbor information?"
  type: multiple-choice
  options:
    - "GCNs treat all neighbors as equally important (scaled by degree); GATs learn to weight neighbors differently based on their relevance"
    - "GCNs use attention mechanisms; GATs use fixed degree-normalized aggregation"
    - "GCNs work on directed graphs; GATs only work on undirected graphs"
    - "GCNs can handle graph-level tasks; GATs are restricted to node-level tasks"
  answer: 0
  explanation: "GCNs apply a fixed aggregation based on the normalized adjacency matrix — every neighbor contributes equally, scaled by its degree. GATs borrow the attention mechanism to learn per-neighbor importance weights, allowing the model to focus on the most relevant connections. This makes GATs more expressive in settings where neighbor importance varies."

- question: "Stacking more GNN layers allows each node to incorporate feature information from more distant nodes in the graph."
  type: true-false
  answer: true
  explanation: "Each aggregation layer extends the receptive field by one hop. After k layers, each node's representation reflects its k-hop neighborhood. This is directly analogous to how deep convolutional networks capture larger spatial contexts by stacking convolutional layers."

- question: "GNNs handle graph-structured data by first converting each graph to a fixed-length feature vector (flattening the structure), then feeding that vector into a standard neural network."
  type: true-false
  answer: false
  explanation: "This describes the naive (and flawed) approach to graphs. GNNs instead operate directly on the graph structure using neighborhood aggregation — they never flatten the graph. Flattening loses structural information (who is connected to whom) and requires a canonical node ordering, which graphs don't have. The entire point of GNNs is to design operations that respect graph structure."

- question: "Why can't you simply flatten a graph into a fixed-length vector and feed it into a standard feedforward neural network, and how does the message-passing framework address this limitation?"
  type: short-answer
  answer: "Graphs have variable size and no canonical node ordering — the same graph can be described by many different adjacency matrices depending on how nodes are numbered. Flattening destroys structural information about which nodes are connected. Message passing addresses this by defining computations that are invariant to node ordering: each node aggregates information from its neighbors through learned functions, so the representation reflects the actual topology rather than an arbitrary indexing."
  explanation: "The fundamental challenge is that graph isomorphism makes any fixed-length encoding order-dependent and lossy. Message passing is permutation-equivariant: relabeling the nodes produces consistently relabeled representations, not different ones. This structural invariance is what allows GNNs to generalize across graphs of different sizes and structures."
```

## Explainer

Standard neural networks assume their input has a fixed, regular structure — images are grids of pixels, text is a sequence of tokens. But many real-world datasets are naturally represented as **graphs**: social networks (users connected by friendships), molecules (atoms connected by bonds), citation networks (papers connected by references), and knowledge graphs (entities connected by relations). You can't simply flatten a graph into a vector and feed it into a regular neural network because graphs have variable size, no canonical node ordering, and complex connectivity patterns. **Graph neural networks** (GNNs) solve this by designing neural network operations that respect and exploit graph structure directly.

The fundamental operation in a GNN is **neighborhood aggregation** (also called message passing). For each node in the graph, the network collects feature information from its neighbors, combines it (through summation, averaging, or a learned function), and uses the result to update the node's own representation. One round of aggregation lets each node "see" its immediate neighbors; stacking multiple layers lets information propagate further — after k layers, each node's representation encodes information from its k-hop neighborhood. If you're familiar with the adjacency matrix representation of graphs, you can think of one GNN layer as multiplying the feature matrix by the (normalized) adjacency matrix and then applying a nonlinear transformation — similar in spirit to a standard neural network layer, but with the adjacency matrix defining which nodes communicate.

The major GNN variants differ in how they aggregate neighbor information. **Graph Convolutional Networks** (GCNs) use a fixed aggregation scheme based on the normalized adjacency matrix — every neighbor contributes equally, scaled by degree. **GraphSAGE** samples a fixed number of neighbors and applies a learnable aggregation function (mean, LSTM, or max-pool), making it scalable to large graphs where examining all neighbors is expensive. **Graph Attention Networks** (GATs) borrow the attention mechanism from transformers: they learn to assign different importance weights to different neighbors, so the network can focus on the most relevant connections. The choice of variant depends on the application — GCNs are simple and effective for many benchmarks, GraphSAGE scales to graphs with millions of nodes, and GATs excel when the importance of neighbors varies.

GNNs can be applied at three levels of granularity. **Node-level tasks** predict properties of individual nodes (e.g., classifying users in a social network or predicting the function of proteins). **Edge-level tasks** predict relationships between pairs of nodes (e.g., link prediction in knowledge graphs or recommending connections). **Graph-level tasks** predict properties of entire graphs (e.g., predicting whether a molecular graph represents a toxic compound), typically by adding a readout or pooling layer that aggregates all node representations into a single graph-level vector. The key insight across all these applications is that GNNs learn representations that capture both the features of individual entities and the structure of their relationships — something that no amount of feature engineering on flat tabular data can easily achieve.
