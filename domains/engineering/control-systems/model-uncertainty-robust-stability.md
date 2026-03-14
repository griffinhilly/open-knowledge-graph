---
id: model-uncertainty-robust-stability
title: Model Uncertainty and Robust Stability Analysis
domain: engineering
course: control-systems
prerequisites:
- id: gain-phase-margins-stability-robustness
  type: hard
- id: transfer-function-poles-zeros-interpretation
  type: soft
builds-toward:
- sensitivity-and-robustness-functions
tags:
- uncertainty
- robustness
- stability
- model-error
stage: advanced
status: draft
---

# Model Uncertainty and Robust Stability Analysis

## Core Idea
Real plants differ from models due to unmodeled dynamics, parameter variation, and simplification. Uncertainty can be quantified as bounded multiplicative error ΔG(s) such that actual plant = nominal model × (1 + ΔG). Robust stability requires the loop gain to remain stable for all uncertainty within bounds. Gain and phase margins provide conservative robustness measures; more sophisticated μ-synthesis extends these concepts.
