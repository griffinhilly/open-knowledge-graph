---
id: sat-canonical-problem
title: 'Satisfiability Problem: The Canonical NP-Complete Problem'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-theorem
  type: hard
builds-toward:
- three-sat-reductions
tags:
- satisfiability
- boolean-satisfiability
- sat-solvers
- completeness
stage: advanced
status: draft
---

# Satisfiability Problem: The Canonical NP-Complete Problem

## Core Idea
The Boolean satisfiability problem (SAT) asks whether a Boolean formula has an assignment making it true. SAT is the prototypical NP-complete problem and appears across logic, AI, hardware verification, and combinatorics. The complexity of SAT directly connects to fundamental questions about problem-solving and the limits of efficient computation.

## How It's Best Learned
Experiment with SAT solvers (e.g., MiniSat) on small instances. Convert a graph coloring instance to SAT to see the encoding.
