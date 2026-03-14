---
id: deadlock-banker-algorithm
title: 'Deadlock Avoidance: Banker''s Algorithm'
domain: computer-science
course: operating-systems
prerequisites:
- id: deadlock-prevention-and-avoidance
  type: hard
- id: deadlock-conditions-and-graphs
  type: hard
tags:
- deadlock
- avoidance
- banker
stage: formal-systems
status: draft
---

# Deadlock Avoidance: Banker's Algorithm

## Core Idea
Banker's algorithm grants resource requests only if the resulting state is safe (all processes can eventually finish). It uses maximum claims and simulates allocation; though expensive, it prevents deadlock without breaking any condition or blocking any progress.
