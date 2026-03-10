---
id: steady-state-error-analysis
title: Steady-State Error Analysis
domain: engineering
course: control-systems
prerequisites:
- id: block-diagram-algebra
  type: hard
- id: time-domain-response-first-order
  type: hard
builds-toward:
- pid-control
- root-locus-controller-design
tags:
- steady-state-error
- system-type
- error-constants
- position-error
- velocity-error
stage: advanced
status: draft
---

# Steady-State Error Analysis

## Core Idea
Steady-state error quantifies how closely a stable control system tracks its reference input after transients die out, determined by the number of free integrators in the open-loop forward path (system type). A Type 0 system has finite position constant Kp and nonzero steady-state error to a step; a Type 1 system (one integrator) tracks steps perfectly but has finite velocity constant Kv and error to a ramp; a Type 2 system tracks ramps perfectly but has finite acceleration constant Ka. Errors are given by ess = R/(1+Kp), ess = R/Kv, and ess = R/Ka respectively, derived using the final value theorem applied to E(s) = R(s)/(1 + G(s)).

## How It's Best Learned
Apply error constant formulas to example open-loop transfer functions with varying numbers of origin poles. Verify using the final value theorem on the closed-loop error transfer function — the two approaches must agree for a stable closed-loop system.

## Common Misconceptions
- Steady-state error formulas only apply to stable closed-loop systems; an unstable system does not have a meaningful steady-state.
- High gain reduces steady-state error but does not change system type — only adding integrators changes the fundamental error to polynomial inputs.
- Disturbance rejection steady-state error and reference tracking error have different expressions and should not be confused.
