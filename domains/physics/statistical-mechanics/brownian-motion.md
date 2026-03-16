---
id: brownian-motion
title: Brownian Motion
domain: physics
course: statistical-mechanics
prerequisites:
- id: kinetic-theory-basics
  type: soft
- id: maxwell-boltzmann-distribution
  type: soft
builds-toward:
- langevin-equation-stochastic
- fokker-planck-equation
tags:
- stochastic
- noise
- fluctuations
stage: advanced
status: draft
---

# Brownian Motion

## Core Idea
Brownian motion is the erratic random motion of a colloidal particle in a fluid, caused by collisions with thermal fluctuations of solvent molecules. Einstein showed that ⟨x²⟩ ∝ t, relating the diffusion coefficient to molecular properties and temperature, connecting macroscopic transport to microscopic thermal motion.

## Explainer

Drop a grain of pollen into still water and watch it under a microscope: it jitters randomly in all directions, never settling, executing a restless walk with no apparent pattern. This is **Brownian motion**, first described by botanist Robert Brown in 1827. For decades it was a curiosity; Einstein's 1905 paper turned it into one of the strongest proofs that atoms exist.

The physical picture, which you can construct from kinetic theory, is straightforward. The pollen grain is large compared to a water molecule but still small enough that, at any instant, the random thermal collisions from all sides don't exactly cancel. The net force fluctuates randomly, pushing the grain a little one way, then another. From the Maxwell-Boltzmann distribution you know that solvent molecules have a wide spread of speeds; the rare fast ones deliver large impulses. The result is a trajectory that is continuous but nowhere smooth — it changes direction constantly on every timescale, producing a path that looks the same under any magnification.

Einstein's insight was to ask not about the trajectory but about the **mean squared displacement** ⟨x²⟩. He showed that ⟨x²⟩ = 2Dt, where D is the **diffusion coefficient**. The square-root-of-time scaling is the signature of a random walk: after N random steps of size ℓ, the typical displacement is ℓ√N, not Nℓ as in directed motion. Time enters as √t, so displacement grows slowly — a factor of 4 in time gives only a factor of 2 in typical distance. Einstein further connected D to molecular properties through D = kT/γ, where γ is the drag coefficient (Stokes' law gives γ = 6πηr for a sphere of radius r in a fluid of viscosity η). This **Einstein relation** links the diffusion constant to temperature and viscosity using only macroscopic measurables, allowing Jean Perrin to deduce Avogadro's number from Brownian motion experiments — a decisive confirmation that the molecular picture was real.

The deeper principle at work is the **fluctuation-dissipation theorem**: the same molecular collisions that cause random fluctuations also cause systematic drag. A large particle moving through a fluid loses momentum to collisions (drag), but in equilibrium those same random collisions also kick the particle around (Brownian noise). The two effects are not independent — they are two faces of the same molecular reality. This connection runs throughout statistical mechanics and reappears in the Langevin equation and Fokker-Planck equation, the subjects you will encounter next.
