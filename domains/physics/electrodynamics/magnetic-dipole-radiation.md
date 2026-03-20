---
id: magnetic-dipole-radiation
title: Magnetic Dipole and Quadrupole Radiation
domain: physics
course: electrodynamics
prerequisites:
- id: electric-dipole-radiation
  type: hard
- id: multipole-expansion-radiation
  type: soft
tags:
- radiation
- multipole
- magnetic
stage: advanced
status: draft
---

# Magnetic Dipole and Quadrupole Radiation

## Core Idea
When electric dipole moment vanishes, magnetic dipole moment m and electric quadrupole moment Q contribute to radiation. These higher multipoles are suppressed by factors of (a/c)² relative to dipole radiation. Important in nuclear and atomic transitions where dipole selection rules forbid dipole transitions.

## Explainer

From electric dipole radiation, you know the dominant term in the multipole expansion: an oscillating electric dipole moment p̈ drives radiation with power P ∝ |p̈|² and a sin²θ angular distribution (the classic donut pattern). But what happens when the electric dipole moment is zero? A charge distribution with this symmetry — for example, two equal positive charges oscillating symmetrically about the origin — still radiates. You must go to the next terms in the expansion.

The **magnetic dipole** contribution comes from an oscillating magnetic dipole moment m — a current loop whose area or current oscillates in time. The radiation fields have the same angular dependence as electric dipole radiation (∝ sin²θ), but the roles of E and B are swapped: it is the magnetic field that has the donut pattern, while the electric field is perpendicular to both the observation direction and m̈. The radiated power is P_M1 ∝ |m̈|²/c². Compared to the electric dipole, there is an extra factor of (v/c)² ∼ (a/λ)² — the suppression comes from the fact that creating oscillating magnetic moments requires oscillating currents, which themselves involve charges moving at speed v ≪ c.

The **electric quadrupole** moment Q involves the second moments of the charge distribution. Physically, it captures how elongated or flattened the charge distribution is along various axes. An oscillating quadrupole (like two opposite dipoles canceling each other) radiates with a different angular pattern (∝ sin²θ cos²θ for the simplest case) and the same (v/c)² suppression relative to electric dipole. Both M1 and E2 radiation are weaker than E1 by the same order of magnitude, but they are not identical — they have different angular distributions and different selection rules governing which quantum states can transition via each mechanism.

This hierarchy — E1 dominant, then M1 and E2, then M2 and E3, etc. — is essential in spectroscopy. In atomic transitions, quantum mechanical **selection rules** forbid the electric dipole transition between certain pairs of states (when Δl ≠ ±1 or ΔS ≠ 0 in the non-relativistic limit). These "forbidden" transitions still occur, but at rates suppressed by (a₀/λ)² ∼ (α)², where α ≈ 1/137 is the fine structure constant. The result is metastable excited states with lifetimes of milliseconds or longer instead of nanoseconds. Astronomers observe such transitions in nebulae (e.g., the green forbidden lines of [O III]) under the ultra-low-collision conditions of interstellar space, where atoms have time to radiate via the slow quadrupole channel.
