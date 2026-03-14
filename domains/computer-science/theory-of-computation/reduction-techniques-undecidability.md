---
id: reduction-techniques-undecidability
title: Reduction Techniques for Proving Undecidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: undecidability-reductions
  type: hard
- id: undecidable-language-examples
  type: soft
builds-toward:
- post-correspondence-problem
tags:
- reduction
- many-one-reduction
- undecidability
- proof-technique
stage: advanced
status: draft
---

# Reduction Techniques for Proving Undecidability

## Core Idea
A many-one reduction from A to B is a computable function f where x ∈ A ⟺ f(x) ∈ B. If B is undecidable, so is A. Reduction is the primary technique for proving undecidability: map the halting problem to your problem, showing it's hard. Reductions also apply to NP-completeness in complexity theory, making them a fundamental proof technique across CS.
