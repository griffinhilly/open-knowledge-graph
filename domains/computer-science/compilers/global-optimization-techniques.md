---
id: global-optimization-techniques
title: Global Optimization Techniques
domain: computer-science
course: compilers
prerequisites:
- id: use-definition-chains
  type: hard
- id: code-optimization
  type: hard
builds-toward:
- procedure-inlining-optimization
- array-subscript-optimization
tags:
- optimization
- global-opts
- dataflow
stage: advanced
status: draft
---

# Global Optimization Techniques

## Core Idea
Global optimizations operate across basic block boundaries using data-flow information. Common global optimizations include code hoisting, common subexpression elimination, and copy propagation. These optimizations are more powerful but more complex than local optimizations.

## How It's Best Learned
Implement global common subexpression elimination or code hoisting using reaching definitions and data-flow analysis.
