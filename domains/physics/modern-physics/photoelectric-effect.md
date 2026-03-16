---
id: photoelectric-effect
title: Photoelectric Effect
domain: physics
course: modern-physics
prerequisites:
- id: blackbody-radiation
  type: soft
- id: electromagnetic-waves
  type: hard
- id: electric-potential-energy
  type: hard
builds-toward:
- photon-model
- wave-particle-duality
tags:
- quantum
- photon
- work-function
- Einstein
stage: formal-systems
status: validated
---

# Photoelectric Effect

## Core Idea
When light shines on a metal surface, electrons are ejected only if the frequency exceeds a threshold value — no matter how intense the light. Einstein explained this in 1905 by treating light as quanta (photons) each with energy E = hf. An electron is ejected only if a single photon carries enough energy to overcome the metal's work function φ; the maximum kinetic energy of the emitted electron is K_max = hf − φ. The intensity determines the number of photons, not their energy, explaining why a dim high-frequency source ejects electrons while a bright low-frequency source does not.

## How It's Best Learned
Map each experimental observation (threshold frequency, instantaneous emission, K_max independent of intensity) to the wave model's prediction and show each failure. Then explain each using the photon model. Millikan's precise measurements confirm the linear K_max vs. f relationship and yield h.

## Common Misconceptions
- Brighter light always ejects more energetic electrons — intensity affects the number of ejected electrons, not their maximum energy.
- The photoelectric effect proves light is a particle — it shows light behaves as particles in this context; interference still demonstrates wave behavior.
- Electrons are stored energy that light 'heats up' — the interaction is a single-photon, single-electron quantum event.

## Explainer

You know from electromagnetic waves that light carries energy, and from your study of electric potential energy how energy is stored in electric fields and required to move charges. The photoelectric effect sits at the intersection of both: it is the experiment that forced physicists to accept that light energy comes in discrete chunks, not a continuous flow. The result contradicted classical physics so sharply that it was one of the experiments that launched quantum mechanics.

The classical prediction for light hitting a metal surface goes like this: the oscillating electric field of the light wave should gradually push electrons, and if you shine the light long enough or make it bright enough, an electron should eventually accumulate enough energy to escape the surface. The energy delivered to an electron should scale with intensity (brighter light = more energy per second) and with how long you wait — but *not* with frequency. Every experimental result contradicts this. Below a threshold frequency, no electrons are emitted regardless of intensity or exposure time. Above the threshold, electrons are emitted almost instantly, even in extremely dim light. And the maximum kinetic energy of the ejected electrons depends only on frequency, not on intensity.

Einstein's 1905 explanation introduced the **photon**: light of frequency f is composed of discrete energy quanta, each carrying energy E = hf. A single photon interacts with a single electron in an all-or-nothing event. The metal holds its surface electrons with a binding energy called the **work function** φ, which depends on the metal but not on the light. If the photon's energy hf exceeds φ, the electron is ejected with maximum kinetic energy K_max = hf − φ; if hf < φ, the photon cannot free the electron no matter how many photons arrive. Intensity controls the number of photons — more photons eject more electrons, but each photon still carries only hf. This explains every anomaly: threshold frequency (hf_threshold = φ), immediate emission (single quantum event, no accumulation time), and K_max linear in f with slope h.

Millikan spent years trying to disprove Einstein's equation, meticulously measuring K_max versus f for different metals. Instead he confirmed the linear relationship and measured h to five significant figures — the same h that appeared in Planck's blackbody formula. This cross-check was decisive: the same constant governs both thermal radiation and the photoelectric effect. The photon concept was not an isolated trick for one experiment but a consistent feature of electromagnetic radiation. The photoelectric effect thus marks the beginning of the particle picture of light, even though light's wave behavior (interference, diffraction) remained equally real. The reconciliation of both behaviors is wave-particle duality — the next territory you will explore — and the photoelectric effect is its first and most historically important foothold.
