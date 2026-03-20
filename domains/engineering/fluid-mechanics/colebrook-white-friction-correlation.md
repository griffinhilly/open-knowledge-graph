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
stage: advanced
status: draft
---

# Colebrook-White Friction Factor Correlation

## Core Idea
The Colebrook-White equation implicitly relates friction factor f to Reynolds number Re and relative roughness ε/D for turbulent pipe flow: 1/√f = -2 log₁₀[(ε/D)/3.7 + 2.51/(Re√f)]. This equation bridges laminar and turbulent regimes and forms the basis of the Moody diagram. Explicit approximations (Swamee-Jain, Haaland) permit direct calculation without iterative solving, facilitating hand calculations and code implementation.

## Explainer

From your study of the Moody diagram, you know that friction factor f depends on two quantities: the **Reynolds number** Re (which captures the ratio of inertial to viscous forces) and the **relative roughness** ε/D (the ratio of pipe wall roughness height to pipe diameter). The Moody diagram is essentially a visual plot of the Colebrook-White equation — learning this equation means understanding the mathematical relationship that was used to draw every curve on that chart.

The equation 1/√f = −2 log₁₀[(ε/D)/3.7 + 2.51/(Re√f)] has a critical structural feature: **f appears on both sides**. This makes it implicit — you cannot simply rearrange it to isolate f on the left and compute it directly. The right-hand side contains √f in the denominator, so any attempt to solve for f algebraically leads in circles. The standard approach is iterative: guess a starting value of f (often from the fully turbulent limit, where the Re-dependent term is negligible), substitute into the right side to get a new f, and repeat until successive values converge — typically within 3–5 iterations.

The equation's two-term structure inside the logarithm has a physical interpretation. The first term, (ε/D)/3.7, represents the contribution of **surface roughness**: at high Reynolds numbers, the viscous sublayer shrinks to nothing and the rough pipe surface dominates friction loss. The second term, 2.51/(Re√f), represents the **viscous sublayer contribution**: at low turbulent Reynolds numbers, the sublayer is thick enough to smooth over the roughness, and the pipe behaves closer to a hydraulically smooth wall. As Re increases, this second term shrinks, and the friction factor becomes independent of Re — the horizontal lines at the right edge of the Moody diagram. As Re decreases toward the critical regime (~4,000), both terms matter and f depends on both Re and ε/D.

The impracticality of hand-iterating the implicit equation motivated **explicit approximations**. The Swamee-Jain formula (f = 0.25/[log₁₀(ε/(3.7D) + 5.74/Re⁰·⁹)]²) has error below 3% for the valid range. The Haaland equation is slightly more accurate and is common in software. For engineering calculations where 1–3% error is acceptable — which is nearly always, given that pipe roughness itself is uncertain by more than that — these explicit forms are entirely appropriate. The Colebrook-White equation remains the standard for understanding and for validating numerical solvers, but practical pipe design uses explicit approximations without apology.
