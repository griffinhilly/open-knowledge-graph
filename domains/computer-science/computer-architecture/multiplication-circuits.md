---
id: multiplication-circuits
title: Multiplication Circuit Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: full-adder-circuit-design
  type: hard
tags:
- multiplier
- arithmetic-circuits
stage: formal-systems
status: draft
---

# Multiplication Circuit Design

## Core Idea
Binary multiplication uses shift-and-add: each multiplier bit masks partial products (via AND), which are accumulated and shifted. Booth's algorithm and other optimizations reduce partial products and improve speed.
