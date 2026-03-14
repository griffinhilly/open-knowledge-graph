---
id: inapproximability-pcp
title: Inapproximability and the PCP Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: approximation-algorithms
  type: hard
- id: np-completeness-formal
  type: hard
tags:
- approximation
- hardness
- pcp
stage: advanced
status: draft
---

# Inapproximability and the PCP Theorem

## Core Idea
The PCP (Probabilistically Checkable Proofs) theorem equates NP with a class of languages having efficiently verifiable proofs checkable by reading only a constant number of random bits. This has powerful consequences: unless P=NP, many optimization problems admit no polynomial-time approximation schemes, establishing tight inapproximability bounds for TSP, set cover, and other classic problems.
