---
id: cavity-resonator-solutions
title: Electromagnetic Field Solutions in Cavities
domain: physics
course: electrodynamics
prerequisites:
- id: cavity-resonators
  type: hard
- id: rectangular-waveguide-propagation
  type: soft
builds-toward:
- cavity-resonator-quality-factor
tags:
- cavity-resonators
- resonant-modes
- standing-waves
stage: advanced
status: draft
---

# Electromagnetic Field Solutions in Cavities

## Core Idea
Cavity resonators confine standing wave patterns through metal boundaries. Resonant frequencies ωₙₘₚ are determined by boundary conditions; TMₙₘₚ modes have all three field components while TEₙₘₚ modes have zero Ez or Hz. Field patterns are spatial modes with time-harmonic oscillation.

## Explainer

A waveguide is an open channel — fields travel down it indefinitely. A **cavity resonator** is a waveguide sealed at both ends, creating a metal box. When you close the ends, the forward-traveling and backward-traveling waves reflect back and forth and interfere. At most frequencies this interference is destructive and the field quickly dies out. But at specific frequencies the reflections reinforce constructively, creating a stable **standing wave** pattern. These are the resonant modes of the cavity — the electromagnetic analog of the harmonics of a vibrating string.

For a rectangular cavity of dimensions a × b × d, the resonant frequencies take the form ωₙₘₚ = c·π√[(n/a)² + (m/b)² + (p/d)²]. Each triplet of integers (n, m, p) labels a distinct mode, and each mode has its own spatial field pattern. The integers count half-wavelengths that fit along each dimension — exactly the same standing-wave quantization you know from a vibrating string fixed at both ends. The lowest resonant frequency (dominant mode) is set by the largest dimension of the cavity.

The **TM** and **TE** mode classification that applied to waveguides extends naturally to cavities. **TE modes** (transverse electric) have no electric field component along the propagation axis; **TM modes** (transverse magnetic) have no magnetic field component along that axis. In a closed cavity, all three spatial directions must satisfy boundary conditions simultaneously — the tangential E-field must vanish at every conductor wall. This constraint is why the resonant frequencies are discrete: only field patterns that simultaneously satisfy E_tan = 0 on all six walls can exist as standing modes.

The physical importance of cavities is that they store electromagnetic energy at a precise frequency with very low loss. A microwave oven cavity confines energy to heat food; a microwave cavity in a particle accelerator stores energy to kick particles to higher speed; an atomic clock uses a cavity to define a precise frequency reference. In each case the cavity's geometry determines which frequencies are resonant, and the quality of the conducting walls determines how well energy is retained between driving cycles — a quantity captured by the cavity Q-factor, which you'll study next.
