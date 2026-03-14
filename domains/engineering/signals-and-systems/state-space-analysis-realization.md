---
id: state-space-analysis-realization
title: State-Space Representation and Realization
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
tags:
- state-space
- system-representation
- control
stage: advanced
status: draft
---

# State-Space Representation and Realization

## Core Idea
State-space representation uses first-order differential (or difference) equations: ẋ = Ax + Bu, y = Cx + Du. This form generalizes to MIMO systems, handles initial conditions naturally, and is preferred for numerical simulation and control design. Realization converts transfer functions into canonical state-space forms (observable, controllable, diagonal).
