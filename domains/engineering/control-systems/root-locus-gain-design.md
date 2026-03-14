---
id: root-locus-gain-design
title: Root Locus Gain Design
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-construction-rules
  type: hard
- id: time-domain-response-second-order
  type: soft
tags:
- root-locus
- gain-selection
- damping-ratio
- natural-frequency
- dominant-poles
- performance-specs
stage: advanced
status: draft
---

# Root Locus Gain Design

## Core Idea
Root locus gain design selects the controller gain K so that the closed-loop poles lie at desired locations in the s-plane, meeting time-domain performance specifications such as percent overshoot, settling time, and rise time. The design procedure maps performance specs into s-plane regions: a damping ratio ζ requirement defines lines of constant angle θ = cos⁻¹(ζ) from the negative real axis, a natural frequency ωn requirement defines a circle of radius ωn centered at the origin, and a settling time requirement defines a vertical boundary at σ = −4/t_s (for 2% criterion). The designer identifies where the root locus crosses the desired damping line or enters the acceptable region, then computes the corresponding K using the magnitude condition |G(s)H(s)| = 1/K at that point. When the locus does not pass through the desired region, a compensator (adding poles or zeros) must reshape the locus before gain selection — pure gain adjustment alone cannot place poles arbitrarily. The dominant pole approximation assumes that the closed-loop response is primarily governed by the poles nearest the imaginary axis, provided other poles are at least five times farther to the left.

## How It's Best Learned
Given a plant transfer function with specified overshoot and settling time requirements, convert the specs to a target region in the s-plane, sketch the root locus, and graphically determine the gain K at the intersection point. Verify by computing the closed-loop step response and checking whether higher-order poles violate the dominant-pole assumption. Repeat for systems where the locus does not intersect the desired region to motivate compensator design.

## Common Misconceptions
- Meeting the damping ratio specification by placing dominant poles on the correct ζ line does not guarantee the predicted overshoot if there are nearby zeros or non-dominant poles that are not sufficiently far to the left — the dominant-pole approximation has limits.
- The gain K found from the root locus is the open-loop gain parameter, not the closed-loop DC gain — the steady-state value of the step response depends on the closed-loop transfer function and may require separate steady-state error analysis.
- Increasing K to speed up the response (higher ωn) eventually drives branches into the right half-plane for most systems, so there is a fundamental tradeoff between speed and stability that gain alone cannot resolve.
