---
id: root-locus-controller-design
title: Controller Design via Root Locus
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-method
  type: hard
- id: steady-state-error-analysis
  type: soft
builds-toward:
- lead-lag-compensators
tags:
- compensator-design
- root-locus
- dominant-poles
- angle-condition
- design-specs
stage: advanced
status: draft
---

# Controller Design via Root Locus

## Core Idea
Controller design via root locus involves adding compensator poles and zeros to reshape the locus so it passes through desired closed-loop pole locations corresponding to performance specifications. The design maps specifications (settling time, overshoot) to a desired dominant pole location in the s-plane, then determines the phase angle contribution the compensator must provide to satisfy the angle condition at that point. Lead compensators (zero closer to imaginary axis than pole) add phase to increase speed; lag compensators improve steady-state accuracy by adding low-frequency gain. The dominant pole assumption — that poles closest to the imaginary axis govern the step response — underpins the method but must be verified post-design.

## How It's Best Learned
Calculate the required angle contribution at the desired pole location before determining compensator zero and pole placement. Always verify the dominant pole assumption by checking that non-dominant poles are at least 5× further left in the s-plane, and simulate the full response.

## Common Misconceptions
- Satisfying the angle condition ensures the desired poles lie on the locus, but the gain K must then be set separately to place them at the exact desired locations.
- The dominant pole approximation fails when non-dominant poles create closed-loop zeros that nearly cancel them — always simulate the full closed-loop response.
- Lead and lag compensators serve fundamentally different purposes and are not interchangeable in terms of their effect on the locus shape.
