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
stage: expert
status: draft
---

# Root Locus Method and Pole Placement Design

## Core Idea
Root locus plots closed-loop pole locations as a function of controller gain K, showing how poles move with tuning. Designer specifies desired pole locations (based on rise time, overshoot, settling time specs) and reads required gain from the locus. Root locus enables interactive design: visualizing stability boundaries, identifying achievable performance limits, and systematically trading off performance metrics.

## Questions

```yaml
- question: "A designer wants closed-loop poles with ζ = 0.7 (≤10% overshoot) and settling time under 1 second. After drawing the root locus, the designer finds the locus passes only through regions with ζ < 0.4. The correct next step is:"
  type: multiple-choice
  options:
    - "Continue increasing gain K; the locus will eventually bend into the desired region at sufficiently high gain"
    - "Accept the nearest achievable poles since ζ = 0.4 is close enough to the specification"
    - "Add a compensator — a lead controller or PD element — to introduce a zero that attracts the locus branches toward the desired region"
    - "Reduce gain K toward zero, because K=0 places poles at the open-loop locations which may be closer to the target"
  answer: 2
  explanation: "The root locus is determined by the plant's open-loop poles and zeros, plus any compensator poles and zeros. Once the locus is drawn, K only moves the closed-loop poles along it — you cannot bend the locus by changing K. If the locus misses the target region entirely, no value of K will work. Adding a zero (via a lead compensator or PD controller) attracts locus branches toward it, reshaping the locus so it passes through the desired performance region. This is the fundamental design cycle: specify target region, draw locus, check intersection, add compensation to reshape if needed."

- question: "A second-order system's dominant poles are at −2 ± 4j. Two additional poles are at −3 ± j. Compared to a system with the same dominant poles but additional poles at −25 ± j, the time-domain response of the first system will:"
  type: multiple-choice
  options:
    - "Be identical, because dominant poles fully determine the transient response in all cases"
    - "Show noticeably different behavior because the additional poles at −3 are only 1.5× further left than the dominant poles and contribute significantly to the transient"
    - "Settle faster because more poles contribute energy to the decay"
    - "Have lower overshoot because the additional poles add damping"
  answer: 1
  explanation: "The dominant-pole approximation is valid only when non-dominant poles are at least 3–5 times further left than the dominant poles. With dominant poles at −2 ± 4j (real part −2), non-dominant poles at −3 are only 1.5× further left — well within the range where their contributions to the transient decay are still significant. By contrast, poles at −25 are more than 12× further left, decaying so rapidly that they contribute negligibly. This check — verifying the dominant-pole assumption by simulation — is the closing step of the design cycle."

- question: "For a second-order closed-loop system, percent overshoot is determined solely by the damping ratio ζ, which corresponds to the angle of the closed-loop poles measured from the negative real axis."
  type: true-false
  answer: true
  explanation: "This is the geometric translation of time-domain specs into the s-plane that makes root locus design possible. The damping ratio ζ = cos(θ) where θ is the angle from the negative real axis (0° = pure real, 90° = purely imaginary). Overshoot = exp(−πζ/√(1−ζ²))×100%. A spec of ≤10% overshoot maps to ζ ≥ 0.59, which means poles must lie within a cone defined by θ ≤ 54° from the negative real axis. This allows you to draw a forbidden angular region in the s-plane and check whether the root locus avoids it."

- question: "If the root locus does not pass through the desired performance region in the s-plane, continuously increasing the controller gain K will eventually move the closed-loop poles into that region."
  type: true-false
  answer: false
  explanation: "The root locus is a fixed geometric path determined entirely by the positions of the open-loop poles and zeros (and any compensator poles/zeros). Gain K only moves the closed-loop poles along that path — it cannot bend or redirect the locus. If the locus passes through a region of high overshoot and never enters the desired ζ ≥ 0.7 cone, no gain value will place the poles there. The solution is to reshape the locus by modifying the open-loop transfer function — adding a zero pulls the locus toward it, adding a pole pushes the locus away from it."

- question: "How do time-domain performance specifications (rise time, percent overshoot, settling time) translate into a target region in the s-plane, and what determines whether proportional gain alone can achieve those specifications?"
  type: short-answer
  answer: "Each specification maps to a geometric constraint on the closed-loop pole locations. Overshoot determines a minimum damping ratio ζ, which maps to an angular cone from the negative real axis (ζ = cos θ). Settling time determines a minimum real part σ (settling time ≈ 4/σ for a 2% criterion). Rise time is inversely proportional to the imaginary part ωd. Together these constraints define a feasible region in the s-plane. Proportional gain can achieve the specifications if and only if the root locus passes through that feasible region — because K only moves poles along the existing locus. If the locus misses the region, a compensator must be added to reshape the locus first."
  explanation: "This translation from time-domain specs to s-plane geometry is the core skill of root locus design. The root locus is the tool that shows which poles are achievable with a given plant and controller structure. Understanding that K moves poles along a fixed path — and that the path itself must be reshaped when specs aren't achievable — is what separates a designer who understands root locus from one who just cranks through rules."
```

## Explainer

From your study of the root locus method, you know that as controller gain K varies from zero to infinity, the closed-loop poles trace continuous paths in the s-plane — starting at the open-loop poles (K=0) and ending at the open-loop zeros (K→∞) or going to infinity along asymptotes. Root locus **pole placement** turns this observation into a design procedure: instead of accepting whatever poles a given K produces, you specify where you *want* the closed-loop poles to be, then determine what K (and possibly what controller structure) achieves them.

The connection to your time-domain performance specifications is direct. From that prerequisite, you know that a second-order closed-loop system with poles at σ ± jω_d has rise time ∝ 1/(ω_d), percent overshoot determined by the **damping ratio** ζ = cos(θ) where θ is the angle of the pole from the negative real axis, and settling time ∝ 1/σ. These geometric relationships transform performance specs into a target region in the s-plane. "No more than 10% overshoot" means the poles must lie within a cone defined by ζ ≥ 0.59 (angle ≤ 54° from the negative real axis). "Settling time under 2 seconds" means the real part of the poles must satisfy σ ≥ 2. The intersection of these constraints defines a **feasible region** for the desired poles.

The design question is then: does the root locus pass through (or near) that feasible region? If yes, read off the value of K where the locus crosses the region and you're done — proportional gain alone achieves the desired poles. If no, the locus misses the target region entirely, which means proportional gain is insufficient and you need to reshape the locus by adding poles or zeros via a **lead**, **lag**, or **PD controller**. Adding a zero to the open-loop transfer function attracts the locus branches toward it; adding a pole pushes branches away. The design cycle is: draw the locus, check if it hits the target region, if not add compensation to reshape the locus, repeat.

A critical insight is that root locus only controls where the **dominant poles** land — the poles closest to the imaginary axis that dominate the transient response. If other poles lie far to the left, their contribution decays so fast that the time-domain response is governed almost entirely by the dominant pair. This approximation is valid when non-dominant poles are at least 3–5 times further left than the dominant poles. If additional poles crowd near the dominant pair, the higher-order terms contribute meaningfully and the second-order approximations from your specifications will be inaccurate. Verifying the dominant-pole assumption — by simulating the full system response — is the check that closes the design loop.
