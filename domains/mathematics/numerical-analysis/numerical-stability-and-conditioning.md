---
id: numerical-stability-and-conditioning
title: Numerical Stability and Conditioning
domain: mathematics
course: numerical-analysis
prerequisites:
- id: floating-point-representation
  type: soft
builds-toward:
- condition-number-of-a-problem
- condition-number-of-a-matrix
tags:
- stability
- conditioning
- well-posed-problems
stage: advanced
status: draft
---

# Numerical Stability and Conditioning

## Core Idea
An algorithm is numerically stable if small perturbations in input produce small perturbations in output. A problem is well-conditioned if small input changes lead to small output changes, and ill-conditioned if they lead to large output changes. Stability is a property of algorithms, while conditioning is a property of problems themselves.
