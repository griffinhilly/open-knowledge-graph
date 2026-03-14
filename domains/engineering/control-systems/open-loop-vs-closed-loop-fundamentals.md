---
id: open-loop-vs-closed-loop-fundamentals
title: Open-Loop vs Closed-Loop Control
domain: engineering
course: control-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
builds-toward:
- error-signal-feedback-configuration
- gain-phase-margins-stability-robustness
tags:
- fundamentals
- feedback
- system-structure
stage: advanced
status: draft
---

# Open-Loop vs Closed-Loop Control

## Core Idea
Open-loop systems apply predetermined control inputs without sensing output, while closed-loop systems measure output and adjust input based on error to achieve desired behavior. Closed-loop control enables systems to automatically compensate for disturbances and model uncertainties, but introduces stability risks if feedback gains are improperly tuned. Understanding the tradeoffs between simplicity (open-loop) and robustness (closed-loop) is fundamental to control system design.

## How It's Best Learned
Compare simple examples like manual vs cruise control, or thermostat behavior. Simulate both architectures and observe response to disturbances (speed bump, outdoor temperature change).

## Common Misconceptions
- Closed-loop is always better; actually, simpler open-loop designs are preferable when disturbances are predictable.
- Closing the loop always stabilizes a system; incorrect feedback can destabilize even stable open-loop plants.
- Feedback eliminates all steady-state error; error type depends on system order and controller structure.
