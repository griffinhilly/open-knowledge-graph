---
id: waveguide-equations-general
title: Waveguide Field Equations
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-differential-form
  type: hard
- id: separation-of-variables-elliptic-equations
  type: hard
builds-toward:
- transverse-electric-modes
- transverse-magnetic-modes
tags:
- waveguides
- guided-modes
- dispersion-relations
stage: advanced
status: draft
---

# Waveguide Field Equations

## Core Idea
Waveguide modes satisfy Maxwell's equations with boundary conditions on conductor walls. Separating longitudinal and transverse components, modes are determined by transverse field patterns, leading to dispersion relations relating ω and k_z and cutoff frequencies.

## Explainer

A waveguide is a metal tube — rectangular, circular, or other cross-section — designed to guide electromagnetic waves along its length. Unlike a coaxial cable which has two conductors, a simple hollow waveguide has only one conductor (the outer tube). This changes the physics fundamentally: a waveguide cannot support a simple TEM (transverse electromagnetic) wave where both E and B are purely transverse, because that mode requires a second conductor for the return current. Instead, waveguides support modes where at least one field component points along the propagation direction.

The general strategy is to write E and B as products of a transverse profile function and a longitudinal traveling wave: **E(x,y,z,t) = E_t(x,y) e^(ikz − iωt)**. Substituting into Maxwell's equations and separating longitudinal (z) and transverse (x,y) components gives a 2D eigenvalue problem for the transverse profile. For **TE modes** (transverse electric, B_z ≠ 0, E_z = 0), you solve ∇²_t B_z + k_c² B_z = 0 with Neumann boundary conditions on the walls. For **TM modes** (transverse magnetic, E_z ≠ 0, B_z = 0), you solve ∇²_t E_z + k_c² E_z = 0 with Dirichlet conditions. Each eigenvalue k_c is a **cutoff wavenumber**, and all transverse components can be derived algebraically from the single z-component once it is known.

The **dispersion relation** for a waveguide mode is k_z² = (ω/c)² − k_c², where k_c is the cutoff wavenumber from the transverse eigenvalue problem. This is the central result. Below the **cutoff frequency** ω_c = k_c · c, the quantity (ω/c)² − k_c² is negative, so k_z is imaginary — the mode does not propagate but decays exponentially (it is evanescent). Above cutoff, k_z is real and the mode propagates. Each geometry has a discrete ladder of cutoff frequencies; the dominant mode (lowest k_c) propagates by itself over a frequency band before the next mode turns on. Microwave engineers design waveguide dimensions specifically so that the operating frequency sits above the dominant mode cutoff but below the next mode cutoff, ensuring single-mode propagation.

The connection to your prerequisites is direct. Separation of variables — which you know for elliptic equations — is precisely what separates the transverse eigenvalue problem from the longitudinal propagation. The transverse equation is a Helmholtz equation on the cross-sectional geometry, and the boundary conditions enforce perfect-conductor conditions (E_tan = 0, B_n = 0). Each solution (mode) is like an eigenfunction of the transverse problem, carrying energy independently of the other modes. When you move to cavity resonators, you add end-cap boundary conditions in the z-direction, quantizing k_z as well and replacing the continuous propagation spectrum with a discrete set of resonant frequencies.
