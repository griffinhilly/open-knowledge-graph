---
id: software-mutual-exclusion-solutions
title: Software-Only Mutual Exclusion Solutions
domain: computer-science
course: operating-systems
prerequisites:
- id: critical-section-problem-formalization
  type: hard
builds-toward:
- test-and-set-primitive
tags:
- synchronization
- mutual-exclusion
- software
stage: formal-systems
status: draft
---

# Software-Only Mutual Exclusion Solutions

## Core Idea
Peterson's and Dekker's algorithms solve the two-process critical section problem using only shared variables (flags, turn). While theoretically important, they are impractical on modern CPUs due to weak memory ordering; hardware support is essential in practice.
