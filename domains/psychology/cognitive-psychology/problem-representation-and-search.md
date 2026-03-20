---
id: problem-representation-and-search
title: Problem Representation and Solution Search
domain: psychology
course: cognitive-psychology
prerequisites:
- id: mental-model-construction
  type: hard
- id: problem-solving-strategies
  type: soft
builds-toward:
- expert-cognition-knowledge-organization
tags:
- problem-solving
- representation
- search
- heuristics
stage: advanced
status: draft
---

# Problem Representation and Solution Search

## Core Idea
Problem-solving depends critically on how problems are represented. The problem space includes initial states, goal states, and operators connecting them. Effective problem-solving requires both good representation and efficient search strategies like means-ends analysis, working backward, and using heuristics to reduce the search space.

## Explainer

From your study of mental models, you know that the mind represents situations not as raw sensory data but as structured internal models that capture the relationships and affordances relevant to goals. Problem-solving begins with constructing exactly this kind of internal model: the **problem space**. The problem space is defined by three components — an **initial state** (where you start), a **goal state** (where you want to be), and **operators** (the legal moves that transform one state into another). Good problem-solving requires first building an accurate problem space, then searching it efficiently.

Why does representation matter so much? Consider the classic **mutilated chessboard** problem: a standard chessboard has two opposite corner squares removed, leaving 62 squares. Can you tile all 62 squares with 31 dominoes (each domino covers exactly two adjacent squares)? Most people approach this by imagining different domino placements — searching for a valid tiling. They search for a long time and fail. But the right representation makes the answer immediate: a standard chessboard alternates black and white squares, so two opposite corners are the same color (say, both black). Removing them leaves 32 squares of one color and 30 of the other. Each domino must cover exactly one black and one white square, so 31 dominoes would require 31 of each color — which is impossible. The problem is solved in seconds once you represent it in terms of color constraints rather than spatial positions. The search effort was wasted because the representation was wrong.

This example illustrates the central principle: **problem representation determines the difficulty of search**. A representation that encodes the problem's deep structure rather than its surface features makes the solution visible; a representation that maps onto surface features forces exhaustive search through an unnecessarily large problem space. Experts in a domain typically solve problems faster not because they search faster but because their representations are better — they immediately encode problems in terms of underlying principles, collapsing the search space before search begins.

When the problem space cannot be collapsed by better representation, **search strategies** come into play. **Means-ends analysis** is the most general strategy: at each step, identify the largest difference between the current state and the goal state, then select the operator that reduces that difference. It recursively breaks the problem into subproblems — "to get from A to Z, first get from A to M" — and is the logic underlying GPS (General Problem Solver), an early AI system. **Working backward** from the goal is effective when the goal state is well-defined and the operators are reversible. **Heuristics** are rules of thumb that do not guarantee a solution but drastically prune search: in chess, "control the center" is a heuristic that eliminates vast swaths of the move tree without evaluating them. The cost of heuristics is occasional failure; the benefit is tractable search in spaces too large for exhaustive exploration.
