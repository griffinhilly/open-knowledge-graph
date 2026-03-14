---
id: feedback-control-and-stability
title: Feedback Control Systems and Stability Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: frequency-response-analysis-bode
  type: hard
builds-toward:
- feedback-control-fundamentals
tags:
- feedback
- control-systems
- stability
stage: formal-systems
status: draft
---

# Feedback Control Systems and Stability Analysis

## Core Idea
Feedback modifies circuit behavior by returning a portion of the output to the input. Loop gain T(jω) = β·A(jω) (feedback fraction times forward gain) determines closed-loop behavior. Negative feedback reduces gain but improves linearity, bandwidth, and noise; positive feedback increases gain or causes oscillation if |T| ≥ 1. Stability requires |T(jω)| < 1 at frequencies where the phase of T crosses -180°.
