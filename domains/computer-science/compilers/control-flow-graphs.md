---
id: control-flow-graphs
title: Control Flow Graphs
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: graph-theory-fundamentals
  type: soft
- id: directed-graphs-and-digraphs
  type: soft
builds-toward:
- dataflow-analysis
tags:
- cfg
- program-analysis
- graph-representation
stage: advanced
status: draft
---

# Control Flow Graphs

## Core Idea
A control flow graph (CFG) represents a program's control structure as a directed graph where nodes are basic blocks (straight-line code with one entry/exit) and edges represent jumps. CFGs are the foundation for program analysis: dominance, loops, and dataflow properties are computed on CFGs. Building and analyzing CFGs is essential for optimization and verification.
