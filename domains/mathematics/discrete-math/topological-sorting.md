---
id: topological-sorting
title: Topological Sorting and Ordering
domain: mathematics
course: discrete-math
prerequisites:
- id: directed-graphs-and-digraphs
  type: hard
- id: directed-acyclic-graphs
  type: hard
builds-toward:
- depth-first-search-graphs
tags:
- directed-graphs
- ordering
- algorithms
stage: formal-systems
status: draft
---

# Topological Sorting and Ordering

## Core Idea
Topological sorting arranges vertices of a directed acyclic graph (DAG) in a linear order such that for every directed edge from u to v, u comes before v. This ordering is useful for scheduling tasks with dependencies, resolving symbol dependencies in compilers, and determining precedence.
