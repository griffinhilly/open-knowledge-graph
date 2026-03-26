---
id: belief-propagation-algorithm
title: Belief Propagation Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: factor-graphs-inference
  type: hard
- id: dynamic-programming-intro
  type: soft
tags:
- inference
- message-passing
- factor-graphs
- loopy-belief-propagation
stage: advanced
status: validated
---

# Belief Propagation Algorithm

## Core Idea
Belief propagation iteratively passes messages between variables and factors in a factor graph to compute marginal probabilities and max-marginals. It is exact on tree-structured graphs and an effective approximation on loopy graphs; the algorithm's convergence and quality depend on the graph structure and message scheduling.

## How It's Best Learned
Implement sum-product belief propagation on a factor graph and trace message updates to understand how beliefs propagate through the network.

## Questions

```yaml
- question: "You run loopy belief propagation on a factor graph with cycles and it converges. What can you say about the resulting marginal probabilities?"
  type: multiple-choice
  options:
    - "They are exact, because convergence proves the algorithm found the true marginals"
    - "They are undefined, because BP cannot converge on any loopy graph"
    - "They are approximate, because cycles allow information to circulate and be counted more than once"
    - "They are exact only for variables not involved in any cycle"
  answer: 2
  explanation: "Convergence in loopy BP does not guarantee correctness. On a graph with cycles, a message traveling around a loop eventually returns to its origin, causing information to be double-counted. The algorithm treats the information as independent when it is not. The result is an approximation — often a very good one in practice (as in LDPC decoding), but not exact. Only on tree-structured graphs, where every path between nodes is unique, does BP compute exact marginals."

- question: "On a tree-structured factor graph, why does belief propagation compute exact marginals?"
  type: multiple-choice
  options:
    - "Tree graphs have fewer variables, so the exact computation is tractable"
    - "Every path between any two nodes is unique, so messages carry truly independent information with no double-counting"
    - "Factor graphs on trees have no cycles, so all variables are independent"
    - "Dynamic programming guarantees exact results on any acyclic computation graph"
  answer: 1
  explanation: "The key is message independence. In a tree, there is exactly one path between any two nodes. When a variable x sends a message toward a factor f, that message summarizes everything 'behind' x — none of which has already influenced f through another path. Because there are no loops, information cannot circulate back. This is precisely the condition that makes the sum-product decomposition exact. Option C is wrong: variables in a tree-shaped factor graph can be highly dependent — the graph structure captures their joint distribution; 'no cycles' enables exact inference, not independence."

- question: "Loopy belief propagation is very likely to converge on any factor graph if run for sufficiently many iterations."
  type: true-false
  answer: false
  explanation: "Convergence is not guaranteed for loopy graphs. On graphs with short, tight cycles (especially small-diameter graphs with dense connections), messages can oscillate indefinitely. Techniques like message damping (mixing new messages with previous ones) can improve convergence behavior, but there is no general guarantee. When BP does fail to converge, practitioners typically detect this by monitoring message changes and either use damping, different scheduling, or a variational inference method instead."

- question: "In belief propagation, a message from variable node x to factor node f is constructed by combining information from all of x's neighboring factors except f itself."
  type: true-false
  answer: true
  explanation: "This exclusion is the core design decision in BP. If x included f's own message in what it sends back to f, the same information would flow in a loop and be double-counted. By excluding f, each message represents genuinely new information from x's perspective — everything x knows from all other sources. On a tree, this means every message is built from independent evidence, guaranteeing exactness. On a loopy graph, independence breaks down as information can reach x via f through roundabout paths."

- question: "Explain why belief propagation is exact on trees but only approximate on loopy graphs, using the concept of message independence."
  type: short-answer
  answer: "On a tree, every path between two nodes is unique, so the messages arriving at any variable from different directions are based on completely independent subsets of the graph. When BP combines these messages to compute a belief, it is correctly weighting non-overlapping evidence. On a loopy graph, cycles create multiple paths between nodes, allowing the same piece of evidence to travel around a loop and arrive at a variable multiple times via different routes — once directly and once (or more times) via the cycle. BP has no mechanism to detect this; it counts the repeated information as if it were independent, producing incorrect (biased toward overconfidence) marginals."
  explanation: "This distinction is why BP is also called 'sum-product on a tree' in the exact case. The loopy case is an approximation to the Bethe free energy minimization in statistical physics, which explains why the approximation can be systematically analyzed and why it works well when cycles are long (information correlations decay over long paths). Short, dense cycles are where loopy BP breaks down most severely."
```

## Explainer

From your study of factor graphs, you know that a joint probability distribution can be represented as a bipartite graph with variable nodes and factor nodes, where each factor encodes a local relationship between a subset of variables. The inference problem is to compute the marginal probability of each variable — that is, to sum out all other variables from the joint distribution. Doing this by brute force is exponential in the number of variables. **Belief propagation** (BP) solves this efficiently by breaking the global computation into local message-passing steps.

The algorithm works by sending **messages** along edges of the factor graph. There are two types. A message from a variable node x to a factor node f summarizes what x "believes" about its own state based on all factors *except* f. A message from a factor node f to a variable node x summarizes what f "thinks" x should be, given the local function and all messages from f's other neighboring variables. Each message is a function over the states of the receiving variable — think of it as an unnormalized probability vector. The **belief** at each variable node is the product of all incoming messages, normalized to sum to one. This gives the estimated marginal distribution.

On **tree-structured** factor graphs (graphs with no cycles), belief propagation is exact and terminates in a number of steps equal to the diameter of the tree. The reason is elegant: in a tree, every path between two nodes is unique, so messages carry independent information. You can think of it as a generalization of the forward-backward algorithm for hidden Markov models or the elimination algorithm for Bayesian networks — both are special cases of BP on tree-shaped graphs. The sum-product variant computes marginals; the closely related **max-product** (or min-sum in log space) variant computes the most probable configuration, analogous to the Viterbi algorithm.

When the factor graph has cycles — the **loopy** case — messages are no longer independent, because information can circulate around loops and be counted multiple times. Nevertheless, **loopy belief propagation** often works remarkably well in practice. The algorithm simply runs the same update rules iteratively until messages converge (or a maximum number of iterations is reached). It is the core inference engine behind turbo codes, LDPC codes in modern communication systems, and stereo vision algorithms in computer vision. Convergence is not guaranteed in general, and when it does converge, the marginals are approximate. Techniques like message damping (averaging new messages with old ones) and careful scheduling (updating messages in a strategic order rather than all at once) improve reliability. Understanding when and why loopy BP fails — for instance, on graphs with short, tight cycles — is an active area of research that connects to variational inference and the Bethe free energy approximation.
