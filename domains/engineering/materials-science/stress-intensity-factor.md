---
id: stress-intensity-factor
title: Stress Intensity Factor
domain: engineering
course: materials-science
prerequisites:
  - id: stress-strain-behavior
    type: hard
builds-toward:
  - fracture-mechanics
  - fatigue-in-materials
tags: [stress-intensity-factor, fracture-mechanics, LEFM, crack-propagation, fracture-toughness]
stage: formal-systems
status: validated
---

# Stress Intensity Factor

## Core Idea
The stress intensity factor K quantifies the magnitude of the stress field near the tip of a crack in a material under load, and is the central parameter in linear elastic fracture mechanics (LEFM). It is defined as K = Yσ√(πa), where σ is the applied stress, a is the crack length, and Y is a dimensionless geometry factor that depends on crack shape and specimen configuration. Three fracture modes describe how loads open or shear a crack: Mode I (opening/tensile — by far the most common and dangerous), Mode II (in-plane shear), and Mode III (out-of-plane shear/tearing). Each mode has its own stress intensity factor (K_I, K_II, K_III). Fracture occurs when K reaches the critical stress intensity factor K_c (also called fracture toughness), a material property measured in units of MPa√m. Materials with high K_c (like steel) resist crack propagation; those with low K_c (like glass) fracture catastrophically.

## How It's Best Learned
Start with the physical intuition: stress concentrates at crack tips, and sharper/longer cracks create more intense stress fields. Show how K captures this with a single number. Work through K = Yσ√(πa) with concrete examples — calculate K for a center crack in a plate and compare to the material's K_c to predict whether it will fracture. Introduce the three modes with diagrams showing the direction of loading relative to the crack plane. Compare K_c values across material classes (ceramics, metals, polymers) to build intuition about brittleness vs. toughness. Connect to real engineering failures where cracks propagated because K exceeded K_c.

## Common Misconceptions
- Confusing stress intensity factor K with stress concentration factor K_t — K_t is a dimensionless ratio from elasticity theory, while K has units of MPa√m and predicts fracture.
- Thinking a material fails when stress exceeds yield strength everywhere — with a crack present, local failure occurs when K reaches K_c even if the average stress is well below yield.
- Assuming longer cracks are always more dangerous at the same load — K depends on both crack length and geometry factor Y, which varies with configuration.
- Believing K_c is a fixed universal constant for a material — it varies with thickness (plane stress vs. plane strain), temperature, and loading rate.
