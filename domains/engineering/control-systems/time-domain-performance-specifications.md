---
id: time-domain-performance-specifications
title: Time-Domain Performance Metrics and Specifications
domain: engineering
course: control-systems
prerequisites:
- id: natural-frequency-damping-second-order
  type: hard
- id: first-order-system-response-analysis
  type: soft
builds-toward:
- root-locus-pole-placement
- lead-lag-compensation-design
tags:
- performance
- time-domain
- specifications
- metrics
stage: advanced
status: draft
---

# Time-Domain Performance Metrics and Specifications

## Core Idea
Control system performance is specified by time-domain metrics: rise time (time to reach 90% of final value), settling time (time to stay within ±2% of final value), peak overshoot (maximum deviation above final value), and steady-state error. These metrics tie directly to pole locations: left-shift increases speed (reduces rise and settling time), increased damping reduces overshoot. Trade-offs exist between these metrics—decreasing overshoot typically increases rise time.
