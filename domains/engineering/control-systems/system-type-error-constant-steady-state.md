---
id: system-type-error-constant-steady-state
title: System Type and Steady-State Error Constants
domain: engineering
course: control-systems
prerequisites:
- id: steady-state-error-analysis
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- control-loop-design-via-bode-plots
tags:
- system-type
- error-constant
- zero-steady-state-error
- tracking
- regulation
stage: abstract-reasoning
status: draft
---

# System Type and Steady-State Error Constants

## Core Idea
System type is the number of free integrators in the open-loop transfer function. Type 0 systems cannot track ramps with zero error; Type 1 can track ramps; Type 2 can track parabolas. Error constants Kₚ, Kᵥ, and Kₐ (position, velocity, acceleration) determine steady-state error to reference inputs.
