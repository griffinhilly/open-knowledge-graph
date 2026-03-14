---
id: byzantine-agreement-algorithms
title: Byzantine Agreement Algorithms
domain: computer-science
course: distributed-systems
prerequisites:
- id: byzantine-fault-tolerance
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- view-change-protocols
tags:
- byzantine
- consensus
- fault-tolerance
- malicious
stage: concrete-techniques
status: draft
---

# Byzantine Agreement Algorithms

## Core Idea
Byzantine agreement handles both crash failures and arbitrary (malicious) failures where replicas may lie. Algorithms like PBFT (Practical Byzantine Fault Tolerance) require f < N/3 honest replicas and use rounds of voting to ensure all honest replicas agree, even if up to f replicas are corrupted.
