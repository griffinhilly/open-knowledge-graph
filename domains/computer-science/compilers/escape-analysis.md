---
id: escape-analysis
title: Escape Analysis for Allocation Optimization
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- alias-analysis
tags:
- optimization
- memory
- allocation
stage: advanced
status: draft
---

# Escape Analysis for Allocation Optimization

## Core Idea
Escape analysis determines whether objects escape a function's scope. Objects that don't escape can be stack-allocated instead of heap-allocated, or scalarized (fields separated and stored directly), improving memory performance by reducing allocation and garbage collection pressure.
