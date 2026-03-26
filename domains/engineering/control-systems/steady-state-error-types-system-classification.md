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
stage: expert
status: validated
---

# Steady-State Error: System Type and Error Constants

## Core Idea
System type (number of integrators in forward path) determines SSE to standard inputs: Type 0 has infinite error to ramp; Type 1 tracks ramps with finite error but infinite error to parabola. Error constants Kp, Kv, Ka quantify SSE magnitude. System type and gain must be chosen to meet steady-state accuracy specifications.

## Questions

```yaml
- question: "A Type 0 closed-loop position control system is given a step (constant position) command. What is its steady-state response?"
  type: multiple-choice
  options:
    - "The output reaches and holds the commanded position with zero steady-state error"
    - "The output approaches the commanded position but maintains a finite, nonzero steady-state error"
    - "The output falls increasingly far behind the command over time, with error growing without bound"
    - "The output oscillates indefinitely around the commanded position without settling"
  answer: 1
  explanation: "A Type 0 system has no open-loop integrators and tracks a step with a finite steady-state error given by SSE = 1/(1 + Kp), where Kp is the position error constant. It cannot achieve zero SSE to a step — that requires at least one integrator (Type 1 or higher). Option C describes the response of any system to an input one order higher than it can track (e.g., a Type 0 system to a ramp). Option A would require Type 1 or above."

- question: "An engineer needs to track a ramp input with zero steady-state error. She considers two options: (a) increasing the gain of a Type 0 system, or (b) adding one integrator to the forward path to make it Type 1. Which approach actually achieves zero SSE to a ramp?"
  type: multiple-choice
  options:
    - "Either option — sufficiently high gain in a Type 0 system can drive ramp error to zero"
    - "Option (a) only — gain can always be increased to eliminate steady-state error to any input"
    - "Option (b) only — only a Type 1 or higher system can track a ramp with zero steady-state error"
    - "Neither — ramp tracking with zero SSE requires at least a Type 2 system"
  answer: 2
  explanation: "For a ramp input, SSE = 1/Kv, where Kv = lim(s→0) s·G(s). In a Type 0 system, G(s) has no poles at s=0, so s·G(s) → 0 as s→0, meaning Kv = 0 and SSE = 1/0 = ∞ regardless of gain. Increasing gain does not change the system type — it cannot turn an infinite error finite. Adding one integrator creates a Type 1 system with Kv = finite, giving SSE = 1/Kv. Increasing the gain of a Type 1 system reduces this finite error but only another integrator (Type 2) eliminates it entirely."

- question: "A Type 1 system tracks a constant position (step) command with zero steady-state error and tracks a constant velocity (ramp) command with a finite steady-state error."
  type: true-false
  answer: true
  explanation: "System type N guarantees zero SSE to all polynomial inputs of degree less than N, and finite SSE to the Nth-degree input. A Type 1 system (N=1) achieves zero error to a step (degree 0) and finite error to a ramp (degree 1), characterized by the velocity error constant Kv = lim(s→0) s·G(s), with SSE = 1/Kv. A parabolic (degree 2) input produces infinite error for a Type 1 system. This hierarchy is the central result of system type analysis."

- question: "Increasing loop gain is typically sufficient to eliminate steady-state error for any input, regardless of system type."
  type: true-false
  answer: false
  explanation: "Gain can reduce finite steady-state errors but cannot eliminate them or convert infinite errors to finite ones. For a Type 0 system tracking a step, SSE = 1/(1+Kp), and Kp grows with gain — so high gain reduces SSE toward zero but never reaches it. For a Type 0 system tracking a ramp, SSE is infinite regardless of gain because the system lacks the integrating action needed to follow a moving reference. Only adding an integrator (increasing system type) can eliminate an SSE class entirely."

- question: "A Type 1 system tracks a step with zero error and a ramp with finite error. Why does adding a second integrator (making it Type 2) help with ramp tracking — and what is the cost?"
  type: short-answer
  answer: "A Type 2 system has two open-loop integrators. For a ramp input, the velocity error constant Kv = lim(s→0) s·G(s) becomes infinite (since G(s) has two poles at s=0, s·G(s) → ∞), giving SSE = 1/Kv = 0. The Type 2 system can also track a parabolic (acceleration) input with finite error. The cost is stability: each integrator adds 90° of phase lag to the open-loop transfer function, reducing the phase margin. A Type 2 system is harder to stabilize and requires careful compensator design — more integrators means the loop is closer to instability."
  explanation: "This tradeoff is the central tension in steady-state error vs. stability design. Adding integrators improves tracking accuracy but erodes phase margin, potentially causing oscillations or instability. Compensation design (lead, lag, PID) exists precisely to manage this tradeoff: lag compensation adds low-frequency gain to reduce SSE without moving the gain crossover frequency much; lead compensation restores phase margin after integrators are added. The system type framework tells you what accuracy is theoretically achievable; compensation tells you how to achieve it while keeping the loop stable."
```

## Explainer

**System type** is simply a count: how many pure integrators (poles at s = 0) appear in the open-loop forward path? A Type 0 system has none; a Type 1 system has one; a Type 2 has two. This number is the single biggest predictor of long-run tracking accuracy because integrators accumulate error over time — they effectively "remember" whether the output is keeping up. You already know from standard test signals that step, ramp, and parabolic inputs represent position, velocity, and acceleration commands respectively. System type determines which of these a closed-loop system can follow with zero steady-state error and which produce a persistent offset.

The rule is clean: a system of Type N tracks inputs of polynomial order up to N−1 with zero SSE, and order N with finite SSE. So a Type 0 system tracks a step (position) with finite error but a ramp with infinite error — the output falls further and further behind a moving reference. A Type 1 system cancels the position error completely and tracks a ramp with a finite lag, but cannot keep up with an accelerating reference. A Type 2 system handles position and velocity commands with zero error and acceleration with finite error. Each integrator in the forward path "uses up" one level of the tracking hierarchy.

**Error constants** quantify exactly how large the finite errors are. The **position error constant** Kp = lim(s→0) G(s) for Type 0 gives SSE = 1/(1+Kp) to a unit step. For Type 1 and above, Kp = ∞, confirming zero SSE to a step. The **velocity error constant** Kv = lim(s→0) sG(s) gives SSE = 1/Kv to a unit ramp for Type 1 systems. The **acceleration error constant** Ka = lim(s→0) s²G(s) gives SSE = 1/Ka to a unit parabola for Type 2 systems. All three constants derive directly from the Final Value Theorem applied to the error signal E(s) = R(s)/(1 + G(s)).

The practical implication is that you can hit steady-state accuracy specs by either raising the system type or increasing the gain. Increasing gain for a Type 0 system reduces its step error (since SSE = 1/(1+Kp) and Kp = K·...) but can never eliminate it. Adding an integrator to the forward path bumps the system to Type 1 and eliminates step error entirely — but at the cost of reduced phase margin and potentially destabilizing the loop. This tradeoff between accuracy and stability is precisely why compensator design exists, and it leads directly into the compensation design topic this node builds toward.


