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
stage: advanced
status: draft
---

# Steady-State Error: System Type and Error Constants

## Core Idea
System type (number of integrators in forward path) determines SSE to standard inputs: Type 0 has infinite error to ramp; Type 1 tracks ramps with finite error but infinite error to parabola. Error constants Kp, Kv, Ka quantify SSE magnitude. System type and gain must be chosen to meet steady-state accuracy specifications.

## Explainer

**System type** is simply a count: how many pure integrators (poles at s = 0) appear in the open-loop forward path? A Type 0 system has none; a Type 1 system has one; a Type 2 has two. This number is the single biggest predictor of long-run tracking accuracy because integrators accumulate error over time — they effectively "remember" whether the output is keeping up. You already know from standard test signals that step, ramp, and parabolic inputs represent position, velocity, and acceleration commands respectively. System type determines which of these a closed-loop system can follow with zero steady-state error and which produce a persistent offset.

The rule is clean: a system of Type N tracks inputs of polynomial order up to N−1 with zero SSE, and order N with finite SSE. So a Type 0 system tracks a step (position) with finite error but a ramp with infinite error — the output falls further and further behind a moving reference. A Type 1 system cancels the position error completely and tracks a ramp with a finite lag, but cannot keep up with an accelerating reference. A Type 2 system handles position and velocity commands with zero error and acceleration with finite error. Each integrator in the forward path "uses up" one level of the tracking hierarchy.

**Error constants** quantify exactly how large the finite errors are. The **position error constant** Kp = lim(s→0) G(s) for Type 0 gives SSE = 1/(1+Kp) to a unit step. For Type 1 and above, Kp = ∞, confirming zero SSE to a step. The **velocity error constant** Kv = lim(s→0) sG(s) gives SSE = 1/Kv to a unit ramp for Type 1 systems. The **acceleration error constant** Ka = lim(s→0) s²G(s) gives SSE = 1/Ka to a unit parabola for Type 2 systems. All three constants derive directly from the Final Value Theorem applied to the error signal E(s) = R(s)/(1 + G(s)).

The practical implication is that you can hit steady-state accuracy specs by either raising the system type or increasing the gain. Increasing gain for a Type 0 system reduces its step error (since SSE = 1/(1+Kp) and Kp = K·...) but can never eliminate it. Adding an integrator to the forward path bumps the system to Type 1 and eliminates step error entirely — but at the cost of reduced phase margin and potentially destabilizing the loop. This tradeoff between accuracy and stability is precisely why compensator design exists, and it leads directly into the compensation design topic this node builds toward.


