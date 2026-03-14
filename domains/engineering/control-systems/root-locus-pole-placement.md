---
id: root-locus-pole-placement
title: Root Locus Method and Pole Placement Design
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-method
  type: hard
- id: time-domain-performance-specifications
  type: hard
builds-toward:
- state-feedback-control-design
tags:
- root-locus
- pole-placement
- design
- controller
stage: advanced
status: draft
---

# Root Locus Method and Pole Placement Design

## Core Idea
Root locus plots closed-loop pole locations as a function of controller gain K, showing how poles move with tuning. Designer specifies desired pole locations (based on rise time, overshoot, settling time specs) and reads required gain from the locus. Root locus enables interactive design: visualizing stability boundaries, identifying achievable performance limits, and systematically trading off performance metrics.
