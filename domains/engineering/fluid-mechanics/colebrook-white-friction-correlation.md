---
id: colebrook-white-friction-correlation
title: Colebrook-White Friction Factor Correlation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: moody-diagram-friction-factor
  type: hard
- id: reynolds-number
  type: soft
builds-toward:
- pipe-networks-series-parallel-analysis
tags:
- friction
- correlation
- turbulent
stage: formal-systems
status: draft
---

# Colebrook-White Friction Factor Correlation

## Core Idea
The Colebrook-White equation implicitly relates friction factor f to Reynolds number Re and relative roughness ε/D for turbulent pipe flow: 1/√f = -2 log₁₀[(ε/D)/3.7 + 2.51/(Re√f)]. This equation bridges laminar and turbulent regimes and forms the basis of the Moody diagram. Explicit approximations (Swamee-Jain, Haaland) permit direct calculation without iterative solving, facilitating hand calculations and code implementation.
