---
id: reaching-definitions-analysis
title: Reaching Definitions Analysis
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
builds-toward:
- common-subexpression-elimination
- constant-propagation
tags:
- dataflow
- reaching-definitions
- optimization
stage: advanced
status: draft
---

# Reaching Definitions Analysis

## Core Idea
Reaching definitions analysis determines which variable assignments (definitions) can reach a given program point without being overwritten. A definition 'd' reaches point p if there exists a path from d's block to p where the variable is not reassigned. Results enable constant propagation, copy propagation, and other optimizations.
