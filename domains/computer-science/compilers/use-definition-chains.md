---
id: use-definition-chains
title: Use-Definition Chains
domain: computer-science
course: compilers
prerequisites:
- id: data-dependence-analysis
  type: hard
- id: reaching-definitions-analysis
  type: hard
builds-toward:
- global-optimization-techniques
tags:
- analysis
- use-def-chains
- optimization
stage: advanced
status: draft
---

# Use-Definition Chains

## Core Idea
A use-definition chain links each use of a variable to all definitions that could reach it. U-D chains enable efficient dependence queries for sparse analysis and targeted optimizations. Constructing U-D chains requires solving the reaching definitions problem.

## How It's Best Learned
Implement reaching definitions analysis and use it to construct U-D chains. Trace chains through programs with multiple definitions.

## Common Misconceptions
U-D chains are only useful for optimization (they enable many forms of analysis). All uses must have a unique definition (a use can have multiple definitions in control flow).
