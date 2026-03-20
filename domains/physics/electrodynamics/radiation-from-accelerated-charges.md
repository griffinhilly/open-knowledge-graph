---
id: radiation-from-accelerated-charges
title: Radiation from Accelerated Charges
domain: physics
course: electrodynamics
prerequisites:
- id: lienard-wiechert-potentials
  type: hard
- id: classical-mechanics
  type: soft
builds-toward:
- larmor-formula
- multipole-expansion-radiation
tags:
- radiation
- acceleration
stage: advanced
status: draft
---

# Radiation from Accelerated Charges

## Core Idea
Accelerated charges radiate electromagnetic waves. Lienard-Wiechert fields separate into velocity-dependent (near) and acceleration-dependent (far) components. The far field is the radiation field proportional to 1/r, responsible for energy transport.

## Explainer

From the Liénard-Wiechert potentials, you can compute the exact electric and magnetic fields of a moving point charge — at any position, at any instant, accounting for the fact that the fields propagate at c rather than instantaneously. When you do this for a charge in arbitrary motion, the resulting field splits into two qualitatively different pieces. The **velocity field** (or near field) looks like a distorted Coulomb field: it points from the charge's *current* position (corrected for retardation), falls off as 1/r², and carries no net energy to infinity. The **acceleration field** (or far field or radiation field) is proportional to the acceleration, falls off as 1/r, and is the one responsible for electromagnetic radiation.

Why does 1/r matter so much? The energy flux (Poynting vector) is proportional to E × B, and both radiation field components go as 1/r, so the Poynting vector goes as 1/r². Integrating over a sphere of radius r gives a total power proportional to r² × (1/r²) = constant — the same regardless of how large a sphere you choose. Energy flows outward and never comes back. By contrast, the near-field Poynting vector goes as 1/r⁴ after integration, and the total power it would carry through a large sphere vanishes — it's just reactive, oscillating energy that stays near the charge. **Radiation requires acceleration** precisely because only the acceleration field has the 1/r dependence needed to carry energy to infinity.

The physical picture is illuminating. Imagine a charge at rest: its field lines extend radially outward to infinity. Now suddenly accelerate the charge briefly. The field lines close to the charge quickly learn about the motion and update their configuration, but far-away field lines can't know yet — information travels at c. The result is a "kink" in the field lines at the shell where the disturbance has propagated. This kink is the radiation field, and it propagates outward at c as a genuine electromagnetic wave. The size of the kink — the amplitude of the radiation field — is proportional to the magnitude of the acceleration and to sin θ (the angle from the acceleration axis), giving the characteristic donut-shaped radiation pattern.

The generalization to relativistic motion involves the Liénard-Wiechert fields in their full relativistic form, with relativistic corrections that dramatically concentrate the radiation in the forward direction at high speeds (**relativistic beaming**). This is why synchrotron light sources produce intensely collimated beams: relativistic electrons emit radiation mostly in the direction they're moving, rather than the broad donut pattern of the non-relativistic limit. But whether non-relativistic or relativistic, the fundamental principle is the same — acceleration is the engine of electromagnetic radiation, and the 1/r decay of the far field is what allows energy to escape to infinity.
