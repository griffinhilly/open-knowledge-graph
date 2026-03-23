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

## Questions

```yaml
- question: "An engineer calculates the friction factor for fully turbulent flow in a rough pipe and finds that ignoring the Reynolds number term in the Colebrook-White equation introduces negligible error. When is this simplification valid?"
  type: multiple-choice
  options:
    - "Only when the pipe is hydraulically smooth (ε/D → 0)"
    - "When Re is very high, so the viscous sublayer is thinner than the roughness elements"
    - "When the flow is laminar, so viscous effects dominate"
    - "This simplification is never valid—both terms must always be included"
  answer: 1
  explanation: "At very high Reynolds numbers, the viscous sublayer shrinks to a thickness smaller than the roughness elements, so rough-wall form drag dominates. The term 2.51/(Re√f) becomes negligible, and f depends only on ε/D—the 'fully rough' or 'complete turbulence' regime. This corresponds to the horizontal lines at the far right of the Moody diagram, where curves for different ε/D are flat, indicating Re-independence."

- question: "Why must the Colebrook-White equation be solved iteratively rather than by direct algebraic manipulation?"
  type: multiple-choice
  options:
    - "The equation involves transcendental functions that have no closed-form solutions under any circumstances"
    - "f appears inside the logarithm on the right-hand side as well as on the left, making direct isolation impossible"
    - "The equation is only valid for specific ranges of ε/D and Re, making algebra unreliable outside those ranges"
    - "Because the Moody diagram was derived empirically without algebraic structure"
  answer: 1
  explanation: "The equation has the form 1/√f = [expression containing √f in the denominator], so any attempt to algebraically isolate f leads in circles. Iteration—starting from an initial guess (often the fully turbulent limit) and repeatedly substituting—converges in 3–5 steps. Explicit approximations like Swamee-Jain sidestep this by sacrificing exact agreement for algebraic tractability, at a cost of less than 3% error."

- question: "Using the Swamee-Jain or Haaland explicit approximation instead of iterating the Colebrook-White equation is acceptable for most engineering pipe flow calculations."
  type: true-false
  answer: true
  explanation: "Explicit approximations have errors below 2–3% relative to the Colebrook-White equation, which is well within the uncertainty introduced by pipe roughness itself (which varies by surface preparation, aging, and corrosion). Engineering decisions based on friction factor rarely require more than ~5% accuracy; the explicit formulas provide this while allowing direct calculation without iteration."

- question: "In the Colebrook-White equation, increasing Reynolds number always decreases the friction factor, regardless of pipe roughness."
  type: true-false
  answer: false
  explanation: "In the fully turbulent (completely rough) regime at high Reynolds numbers, friction factor becomes independent of Re—it plateaus at a value determined only by ε/D. Increasing Re further has no effect because the viscous sublayer is already too thin to matter. The friction factor decreases with Re only in the transitionally rough regime where both terms in the equation matter. This Re-independence of f at high Re is visible as the flat lines on the right side of the Moody diagram."

- question: "What physical phenomena do the two terms inside the logarithm in the Colebrook-White equation represent, and why does their relative importance shift with Reynolds number?"
  type: short-answer
  answer: "The first term, (ε/D)/3.7, represents pipe wall roughness: when roughness elements protrude through the viscous sublayer, they add form drag and dominate friction loss. The second term, 2.51/(Re√f), represents the viscous sublayer's smoothing effect: at lower Re, the sublayer is thick enough to submerge the roughness elements, making the pipe behave hydraulically smooth. As Re increases, the sublayer thins; when it disappears entirely, only roughness matters and f becomes Re-independent. At intermediate Re, both effects coexist."
  explanation: "This physical duality is why the Colebrook-White equation has its specific form—it unifies the smooth-pipe law (Prandtl) and the rough-pipe law (von Kármán) into a single interpolating formula describing the transition between them."
```

## Explainer

From your study of the Moody diagram, you know that friction factor f depends on two quantities: the **Reynolds number** Re (which captures the ratio of inertial to viscous forces) and the **relative roughness** ε/D (the ratio of pipe wall roughness height to pipe diameter). The Moody diagram is essentially a visual plot of the Colebrook-White equation — learning this equation means understanding the mathematical relationship that was used to draw every curve on that chart.

The equation 1/√f = −2 log₁₀[(ε/D)/3.7 + 2.51/(Re√f)] has a critical structural feature: **f appears on both sides**. This makes it implicit — you cannot simply rearrange it to isolate f on the left and compute it directly. The right-hand side contains √f in the denominator, so any attempt to solve for f algebraically leads in circles. The standard approach is iterative: guess a starting value of f (often from the fully turbulent limit, where the Re-dependent term is negligible), substitute into the right side to get a new f, and repeat until successive values converge — typically within 3–5 iterations.

The equation's two-term structure inside the logarithm has a physical interpretation. The first term, (ε/D)/3.7, represents the contribution of **surface roughness**: at high Reynolds numbers, the viscous sublayer shrinks to nothing and the rough pipe surface dominates friction loss. The second term, 2.51/(Re√f), represents the **viscous sublayer contribution**: at low turbulent Reynolds numbers, the sublayer is thick enough to smooth over the roughness, and the pipe behaves closer to a hydraulically smooth wall. As Re increases, this second term shrinks, and the friction factor becomes independent of Re — the horizontal lines at the right edge of the Moody diagram. As Re decreases toward the critical regime (~4,000), both terms matter and f depends on both Re and ε/D.

The impracticality of hand-iterating the implicit equation motivated **explicit approximations**. The Swamee-Jain formula (f = 0.25/[log₁₀(ε/(3.7D) + 5.74/Re⁰·⁹)]²) has error below 3% for the valid range. The Haaland equation is slightly more accurate and is common in software. For engineering calculations where 1–3% error is acceptable — which is nearly always, given that pipe roughness itself is uncertain by more than that — these explicit forms are entirely appropriate. The Colebrook-White equation remains the standard for understanding and for validating numerical solvers, but practical pipe design uses explicit approximations without apology.
