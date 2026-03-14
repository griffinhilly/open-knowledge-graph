---
id: data-dependence-analysis
title: Data Dependence Analysis
domain: computer-science
course: compilers
prerequisites:
- id: basic-block-analysis
  type: hard
- id: dataflow-analysis
  type: hard
builds-toward:
- use-definition-chains
- loop-detection-analysis
tags:
- analysis
- data-flow
- dependencies
stage: advanced
status: draft
---

# Data Dependence Analysis

## Core Idea
Data dependence analysis determines which instructions depend on results from earlier instructions. Dependencies include true dependencies (a use depends on a write), anti-dependencies (a write depends on an earlier read), and output dependencies. Understanding dependencies is essential for safe code motion and parallelization.

## How It's Best Learned
Compute data dependence sets for small programs and draw dependence graphs. Understand how dependences limit parallelization.

## Common Misconceptions
All dependencies must be respected (anti and output dependencies can often be eliminated through renaming). Dependence analysis only matters for parallelization (it affects all optimizations that move code).
