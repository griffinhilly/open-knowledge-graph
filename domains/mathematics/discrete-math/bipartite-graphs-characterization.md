---
id: bipartite-graphs-characterization
title: Bipartite Graphs and 2-Colorability
domain: mathematics
course: discrete-math
prerequisites:
- id: degree-sequences-graphs
  type: soft
builds-toward:
- graph-matching-halls-theorem
tags:
- graph-theory
- bipartite
- coloring
stage: formal-systems
status: draft
---

# Bipartite Graphs and 2-Colorability

## Core Idea
A graph is bipartite if its vertex set can be partitioned into two independent sets (no edges within each set). A graph is bipartite if and only if it contains no odd-length cycles. Bipartite graphs are 2-colorable and arise naturally in matching problems.

## Explainer

A **bipartite graph** is one whose vertices can be split into two camps — call them "red" and "blue" — such that every edge runs between the camps, never within one. Job-applicant matchings are the classic image: one set of vertices represents jobs, the other represents applicants, and edges represent compatible pairs. No job connects directly to another job; no applicant to another applicant. The structure is clean and the two sets are the natural "sides."

The **two-colorability** framing is just a restatement: can you color every vertex red or blue so that no two neighbors share a color? If yes, the graph is bipartite — the two color classes are the two independent sets. This reframing is powerful because it gives you an algorithm: start at any vertex, color it red, then try to consistently color its neighbors blue, their neighbors red, and so on using BFS or DFS. If you ever encounter an edge whose both endpoints would need the same color, the graph is not bipartite.

The **odd cycle theorem** explains exactly when coloring fails. If you traverse a cycle of odd length, you will always return to the starting vertex needing the opposite color from what it already has — a contradiction. Even-length cycles cause no such problem: you can alternate colors around them cleanly. So odd cycles are precisely the obstruction to bipartiteness. If a graph has no odd cycle, it is bipartite; if it does, it is not. This is the graph-theoretic equivalent of "you can't properly 2-color a triangle."

Using what you know about **degree sequences**: in a bipartite graph with parts U and V, counting edges from the U-side and the V-side are both valid ways to count all edges — a preview of double counting ideas. The degree sequence alone does not determine bipartiteness, but understanding degree structure in each part informs matching analysis. This topic directly prepares you for Hall's theorem, which gives a precise condition for when a bipartite graph has a perfect matching: every subset S of one part has at least |S| neighbors in the other part.
