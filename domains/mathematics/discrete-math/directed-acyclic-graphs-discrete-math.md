---
id: directed-acyclic-graphs-discrete-math
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

## Explainer

You already know that a **directed graph** (digraph) has edges with a direction — an arrow from A to B means something different from an arrow from B to A. Now add one constraint: no directed cycles. A **directed acyclic graph**, or **DAG**, is simply a digraph where you can never follow edges in their direction and return to where you started. That one restriction turns out to have profound consequences.

The easiest way to build intuition for DAGs is to think about prerequisites. In this knowledge graph, topics point to the topics that require them. You can't learn Gaussian elimination before you learn systems of equations. This dependency structure is a DAG — if topic A is a prerequisite for B, and B for C, then C cannot also be a prerequisite for A without creating circular reasoning. Real dependency systems (software packages, build steps, course sequences, task pipelines) are almost always DAGs for exactly this reason: cycles represent impossible orderings.

The absence of cycles has a direct structural payoff: every DAG has at least one **source** (a vertex with no incoming edges) and at least one **sink** (a vertex with no outgoing edges). This is easy to see — if every vertex had at least one incoming edge, you could always walk backwards along edges indefinitely, eventually revisiting a vertex and forming a cycle. Since that can't happen, sources must exist. The symmetric argument gives sinks.

This is why **topological sorting** is possible in DAGs but not in general digraphs. A topological ordering is a linear sequence of all vertices such that every directed edge goes from earlier to later in the sequence. It's the formal version of "do all prerequisites before the topic they unlock." Your prerequisite on cycle detection in directed graphs connects here: a digraph has a topological ordering if and only if it contains no directed cycle — i.e., if and only if it is a DAG. Any DFS-based cycle check on a directed graph is simultaneously a test for DAG-ness. If no back-edge is found, you have a DAG and can read off a topological order from the DFS finish times in reverse.
