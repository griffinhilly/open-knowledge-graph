---
id: divide-conquer-recurrence-analysis
title: Divide-and-Conquer Recurrences and the Master Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: nonhomogeneous-recurrence-solutions
  type: soft
tags:
- recurrence-relations
- algorithms
stage: formal-systems
status: draft
---

# Divide-and-Conquer Recurrences and the Master Theorem

## Core Idea
Divide-and-conquer algorithms produce recurrences T(n) = aT(n/b) + f(n), where a subproblems of size n/b are solved plus f(n) work. The Master Theorem provides closed-form solutions by comparing f(n) to n^(log_b a).
