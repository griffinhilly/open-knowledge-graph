---
id: alpha-beta-pruning
title: Alpha-Beta Pruning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: minimax-algorithm
  type: hard
tags:
- search-optimization
- adversarial-search
- pruning
stage: advanced
status: draft
---

# Alpha-Beta Pruning

## Core Idea
Alpha-beta pruning optimizes minimax by eliminating branches that provably cannot affect the final decision. Alpha represents the best score max can guarantee; beta represents the best score min can guarantee. When alpha >= beta, the branch can be pruned without changing results.

## How It's Best Learned
Trace minimax and alpha-beta on identical game trees, highlighting pruned branches and comparing node counts.

## Common Misconceptions
Alpha-beta does not change minimax results, only reduces computation. Move ordering dramatically affects pruning efficiency without requiring algorithmic changes.
