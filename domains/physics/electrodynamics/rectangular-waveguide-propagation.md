---
id: rectangular-waveguide-propagation
title: Propagation in Rectangular Waveguides
domain: physics
course: electrodynamics
prerequisites:
- id: transverse-electric-modes
  type: hard
- id: transverse-magnetic-modes
  type: hard
tags:
- rectangular-waveguide
- tmn-modes
- temn-modes
- dominant-mode
stage: advanced
status: draft
---

# Propagation in Rectangular Waveguides

## Core Idea
In rectangular guides with dimensions a and b, TE and TM modes are labeled by integers m,n. The dominant TE₁₀ mode has the lowest cutoff frequency fc = c/(2a). Field patterns are products of sines/cosines in each transverse direction, satisfying boundary conditions.

## Explainer

From your study of TE and TM modes, you know that inside a metallic waveguide, electromagnetic waves cannot propagate as plane waves — the conducting walls impose boundary conditions that force the transverse field components to vanish at the metal surfaces. The fields must form standing wave patterns in the transverse directions, and only waves whose transverse pattern fits the geometry can propagate. In a rectangular guide of width a (along x) and height b (along y), the transverse structure must satisfy E_tangential = 0 at all four walls.

The solution separates beautifully. For a **TE_mn mode**, the longitudinal magnetic field component H_z takes the form cos(mπx/a) · cos(nπy/b), where m and n are non-negative integers counting the number of half-wave variations in the x and y directions respectively. The boundary conditions (no tangential E at the walls) are automatically satisfied by this cosine form. For **TM_mn modes**, the longitudinal electric field E_z takes the form sin(mπx/a) · sin(nπy/b) — sines, because E_z itself must vanish at the walls (it is tangential there). The transverse field components are derived from these by differentiation.

Each integer pair (m, n) labels a distinct mode with its own transverse field pattern and its own **cutoff frequency**: f_c = (c/2)√[(m/a)² + (n/b)²]. Below f_c, the mode is **evanescent** — it decays exponentially along the guide rather than propagating. Above f_c, the mode propagates with phase velocity v_p = c/√[1 − (f_c/f)²], which exceeds c near cutoff (though the energy velocity, the group velocity, remains less than c). The **propagation constant** is k_z = (2π/λ)√[1 − (f_c/f)²], going to zero at cutoff and approaching the free-space value k at high frequencies.

The **dominant mode** is TE₁₀, which has m = 1, n = 0 — one half-wave variation across the width a and none across the height b. Its cutoff frequency is f_c = c/(2a), and it has the lowest cutoff of all modes. In practical systems, the operating frequency is chosen in the range c/(2a) < f < c/a (or c/(2b) if b < a/2), ensuring only the TE₁₀ mode propagates while all higher modes are cut off. This **single-mode operation** gives clean, predictable transmission: only one field pattern travels down the guide, avoiding the modal dispersion and interference that would occur if multiple modes coexisted. Standard waveguide dimensions (e.g., WR-90 with a = 22.86 mm, used at 8–12 GHz) are chosen precisely to single-mode the frequencies of interest.
