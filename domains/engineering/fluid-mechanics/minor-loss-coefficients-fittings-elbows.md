---
id: minor-loss-coefficients-fittings-elbows
title: Minor Loss Coefficients in Fittings and Elbows
domain: engineering
course: fluid-mechanics
prerequisites:
- id: moody-diagram-friction-factor
  type: hard
- id: pipe-system-losses
  type: hard
builds-toward:
- pipe-networks-series-parallel-analysis
tags:
- losses
- fittings
- design
stage: formal-systems
status: draft
---

# Minor Loss Coefficients in Fittings and Elbows

## Core Idea
Local losses in elbows, tees, reducers, expansions, and other fittings are quantified by a loss coefficient K such that h_L = K(V²/2g). These coefficients depend on geometry, Reynolds number, and flow-separation patterns. For expansions, K relates to the area ratio; for elbows, K depends on the bend radius-to-diameter ratio. Proper accounting of these often-overlooked losses can equal or exceed friction losses in pipe systems.

## How It's Best Learned
Measure pressure drop across various fittings in a laboratory setup at different flow rates to determine K values experimentally. Compare results to published tables and correlations. Use K values in system head calculations to see their cumulative impact on pump selection.

## Common Misconceptions
Loss coefficients are not constant across all Reynolds numbers—they vary significantly in laminar and transitional regimes. Fittings far from the discharge point contribute to total system loss and cannot be neglected in design calculations.
