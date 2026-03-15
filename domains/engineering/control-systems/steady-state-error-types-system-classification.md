---
id: steady-state-error-types-system-classification
title: 'Steady-State Error: System Type and Error Constants'
domain: engineering
course: control-systems
prerequisites:
- id: standard-test-signals-control
  type: hard
- id: laplace-transform-properties-inverse
  type: soft
builds-toward:
- response-specifications-performance-metrics
- compensation-design-tradeoffs-cascadefeedback
tags:
- steady-state-error
- system-type
- error-constant
- accuracy
stage: concrete-operations
status: draft
---

# Steady-State Error: System Type and Error Constants

## Core Idea
System type (number of integrators in forward path) determines SSE to standard inputs: Type 0 has infinite error to ramp; Type 1 tracks ramps with finite error but infinite error to parabola. Error constants Kp, Kv, Ka quantify SSE magnitude. System type and gain must be chosen to meet steady-state accuracy specifications.
