---
id: work-function-photoelectric-analysis
title: Work Function and Photoelectric Energy Analysis
domain: physics
course: modern-physics
prerequisites:
- id: photoelectric-effect
  type: hard
- id: photon-model
  type: hard
builds-toward:
- stopping-potential-kinetic-energy
tags:
- quantum-mechanics
- photons
- photoelectric-effect
stage: advanced
status: draft
---

# Work Function and Photoelectric Energy Analysis

## Core Idea
The work function W is the minimum energy needed to remove an electron from a metal surface. When a photon of energy hf hits the surface, the maximum kinetic energy of the emitted electron is KE_max = hf − W. This relationship (Einstein's photoelectric equation) was central to proving the photon hypothesis; no amount of low-frequency light will cause emission, no matter how intense.

## How It's Best Learned
Plot stopping potential (and thus maximum kinetic energy) versus frequency; the slope gives h and the intercept gives W/e. Measure work functions for different metals and relate to periodic table properties.

## Common Misconceptions
Photon intensity affects the number of electrons emitted, not their maximum kinetic energy (energy comes from the photon, not the intensity). Electrons are emitted instantaneously (within femtoseconds), not built up over time.

## Explainer

From your study of the photoelectric effect and the photon model, you know that light arrives in discrete packets — **photons** — each carrying energy E = hf, where h is Planck's constant and f is the frequency. When a photon strikes a metal surface, it interacts with a single electron in an all-or-nothing transaction: either the photon's energy is absorbed entirely or it isn't. This one-photon, one-electron picture is the starting point for understanding how much energy the emitted electron carries away.

Electrons inside a metal are bound — they require a minimum energy to escape the surface entirely. This minimum is the **work function** W, which is a property of the specific metal (typically 2–5 eV, varying by surface composition and crystal structure). Think of W as the depth of the energy well that the electron must climb out of. The metal's outermost electrons sit closest to the top of this well; inner electrons need more energy to escape. When a photon of energy hf arrives, it first pays the escape cost W. Whatever energy remains after that becomes the kinetic energy of the freed electron.

This gives Einstein's **photoelectric equation**: KE₍ₘₐₓ₎ = hf − W. The subscript "max" is important: most electrons don't escape from the outermost layer — they originate deeper in the metal and lose additional energy in collisions before reaching the surface. The maximum kinetic energy corresponds to electrons at the surface that escape with the minimum energy penalty. If hf < W, no electrons are emitted regardless of how intense the light is — you simply haven't provided enough energy per photon to overcome the barrier.

To measure KE₍ₘₐₓ₎ experimentally, physicists use a **stopping potential** V₀: an opposing voltage applied to decelerate the photoelectrons. The electrons just barely stopped by the voltage have converted all their kinetic energy to electric potential energy, so eV₀ = KE₍ₘₐₓ₎ = hf − W. If you plot V₀ against f for a series of different light frequencies, you get a straight line. The slope is h/e — this gives you Planck's constant — and the x-intercept is the threshold frequency f₀ = W/h below which no emission occurs. Millikan performed this experiment precisely, measuring h and confirming Einstein's equation to high accuracy.

The intensity distinction is the conceptual payoff. Intensity tells you how many photons per second arrive, not how much energy each carries. Doubling the intensity doubles the number of emitted electrons (the photocurrent), but each individual electron still gets exactly one photon's worth of energy, so KE₍ₘₐₓ₎ is unchanged. This is completely unlike the classical wave picture, where more intense waves would gradually build up energy in the surface electron until it could escape — the wave picture predicted a time delay and an intensity-dependent KE, neither of which is observed. The clean separation of "how many electrons" (intensity) from "how much energy each carries" (frequency) is one of the clearest signatures that light is quantized.


