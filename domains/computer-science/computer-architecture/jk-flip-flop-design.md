---
id: jk-flip-flop-design
title: 'JK Flip-Flop: Universal Sequential Element'
domain: computer-science
course: computer-architecture
prerequisites:
- id: sr-flip-flop-design
  type: hard
builds-toward:
- counters-design-analysis
- registers-and-register-files
tags:
- flip-flops
- jk
- toggle
- sequential
stage: formal-systems
status: draft
---

# JK Flip-Flop: Universal Sequential Element

## Core Idea
JK flip-flops resolve the SR flip-flop's undefined state by making simultaneous Set and Reset cause a toggle (state inversion). They are more versatile than SR flip-flops and can implement all sequential logic functions.
