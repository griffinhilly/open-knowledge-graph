---
id: static-single-assignment-form
title: Static Single Assignment (SSA) Form
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- dataflow-analysis
- code-optimization
tags:
- ssa
- ir-form
- dataflow
stage: advanced
status: draft
---

# Static Single Assignment (SSA) Form

## Core Idea
SSA form ensures each variable is assigned exactly once. Use-def chains are explicit: each use links to a unique definition. Phi (φ) functions merge definitions at control flow joins. SSA simplifies dataflow analysis, enables sophisticated optimizations, and makes dependencies explicit. Most modern compilers (LLVM, GCC, Java JIT) use SSA as their primary IR.
