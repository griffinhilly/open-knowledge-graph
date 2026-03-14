---
id: directed-acyclic-graphs
title: Directed Acyclic Graphs (DAGs)
domain: mathematics
course: discrete-math
prerequisites:
- id: directed-graphs-and-digraphs
  type: hard
- id: cycle-detection-directed-graphs
  type: soft
builds-toward:
- topological-sorting
tags:
- directed-graphs
- acyclic
- dags
stage: formal-systems
status: draft
---

# Directed Acyclic Graphs (DAGs)

## Core Idea
A directed acyclic graph (DAG) is a digraph with no directed cycles. DAGs are fundamental in computer science for modeling dependencies, partial orders, and data flow. The absence of cycles guarantees that topological orderings exist.
