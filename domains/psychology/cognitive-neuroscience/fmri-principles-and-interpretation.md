---
id: fmri-principles-and-interpretation
title: fMRI Principles and Interpretation
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: fmri-blood-oxygen-signaling
  type: hard
- id: neuroimaging-methods
  type: hard
- id: normal-distribution
  type: soft
- id: hypothesis-testing-framework
  type: soft
- id: statistical-inference-significance-testing
  type: soft
builds-toward:
- visual-cortex-hierarchical-organization
- dorsolateral-prefrontal-cortex-cognitive-control
- memory-systems-neural-imaging
tags:
- neuroimaging
- methods
- fMRI
- BOLD
stage: advanced
status: draft
---

# fMRI Principles and Interpretation

## Core Idea
fMRI measures blood oxygen level-dependent (BOLD) signals as an indirect proxy for neural activity through neurovascular coupling. While offering excellent spatial resolution (~2-3mm), fMRI has temporal resolution on the order of seconds, limiting inference about precise neural dynamics and causal mechanisms. Interpreting fMRI requires understanding its hemodynamic basis, temporal filtering, and the gap between statistical activation and functional necessity.

## How It's Best Learned
Begin with BOLD physics and the neurovascular coupling mechanisms that link neural activity to blood flow changes. Study actual fMRI datasets examining different cognitive processes (motor, visual, language) to develop intuition for signal characteristics, noise patterns, and preprocessing artifacts.

## Common Misconceptions
- Activation in fMRI means that region causes the behavior; instead it correlates with the task. Use TMS or lesion data for causal claims.
- Higher voxel activation means more neural activity; BOLD signal is saturating and nonlinear.
- fMRI reveals the function of a brain region by itself; function emerges from network interactions.
