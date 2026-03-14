---
id: system-causality-and-realizability
title: System Causality and Realizability Constraints
domain: engineering
course: signals-and-systems
prerequisites: []
builds-toward:
- lti-systems-and-impulse-response
- transfer-functions-control
tags:
- systems
- causality
- realizability
- constraints
stage: abstract-reasoning
status: draft
---

# System Causality and Realizability Constraints

## Core Idea
A causal system's output depends only on present and past inputs, not future inputs—a fundamental physical requirement. Realizability requires the impulse response to be zero for t<0. For frequency-domain systems, causality imposes a relationship between magnitude and phase (Kramers-Kronig relations) that constrains the achievable performance.

## How It's Best Learned
Compare a non-causal filter (symmetric FIR with center tap) to a causal version; observe the required delay. Examine how pole-zero locations must satisfy causality constraints.

## Common Misconceptions
- Thinking stable systems are automatically causal.
- Assuming any transfer function can be realized causally.
- Misunderstanding that causality limits achievable magnitude response slopes.
