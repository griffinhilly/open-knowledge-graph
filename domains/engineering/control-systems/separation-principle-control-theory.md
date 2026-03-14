---
id: separation-principle-control-theory
title: Separation Principle and Output Feedback
domain: engineering
course: control-systems
prerequisites:
- id: state-feedback-control-design
  type: hard
- id: observer-state-estimation-design
  type: hard
tags:
- separation-principle
- output-feedback
- state-space
- theory
stage: advanced
status: draft
---

# Separation Principle and Output Feedback

## Core Idea
The separation principle states that state feedback design and observer design can be done independently, then combined without loss of closed-loop stability (if both are stable individually). This allows decomposition of the control problem: stabilize the plant (state feedback), then estimate unmeasured states (observer), then combine them for output feedback. Closed-loop poles are union of state feedback and observer poles.
