---
id: dataflow-analysis
title: Dataflow Analysis
domain: computer-science
course: compilers
prerequisites:
- id: control-flow-graphs
  type: hard
- id: fixpoint-computation
  type: hard
builds-toward:
- reaching-definitions-analysis
- live-variable-analysis
- code-optimization
tags:
- dataflow
- program-analysis
- optimization
stage: advanced
status: draft
---

# Dataflow Analysis

## Core Idea
Dataflow analysis computes information about how data flows through a program. It solves systems of constraints on basic blocks, iterating until a fixpoint is reached. Forward analyses (reaching definitions) track properties forward through the CFG; backward analyses (live variables) track them backward. Dataflow results enable optimizations like constant propagation and dead-code elimination.
