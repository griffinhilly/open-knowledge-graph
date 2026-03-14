---
id: post-correspondence-problem
title: Post Correspondence Problem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: computability-reductions
  type: soft
tags:
- computability
- undecidability
- formal-languages
stage: formal-systems
status: draft
---

# Post Correspondence Problem

## Core Idea
The Post Correspondence Problem (PCP) asks, given a finite set of domino-like pairs of strings (u_i, v_i), whether there exists a nonempty sequence of indices i_1, ..., i_k such that u_{i_1}...u_{i_k} = v_{i_1}...v_{i_k}. Despite its deceptively simple formulation, PCP is undecidable — there is no algorithm that can solve it for all instances. PCP is a workhorse for proving undecidability of other problems: many undecidability results in formal language theory (ambiguity of CFGs, equivalence of CFGs) are established by reduction from PCP rather than directly from the halting problem.

## How It's Best Learned
Work through small PCP instances by hand — some with solutions and some without — to develop intuition for the matching constraint. Then study the reduction from the halting problem to PCP, which encodes a TM computation as a growing sequence of domino matches. Finally, see how PCP is reduced to prove undecidability of CFG ambiguity.

## Common Misconceptions
- PCP is undecidable in general, but specific restricted variants (e.g., over a unary alphabet, or with only two pairs under certain constraints) may be decidable.
- The difficulty is not finding a short solution — it is that no algorithm can determine whether any solution exists at all, regardless of length.
