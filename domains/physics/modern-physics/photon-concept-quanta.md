---
id: photon-concept-quanta
title: The Photon Concept and Light as Quanta
domain: physics
course: modern-physics
prerequisites:
- id: planck-quantization-hypothesis
  type: hard
- id: photoelectric-effect
  type: hard
builds-toward:
- compton-wavelength-shift
tags:
- quantum
- photons
- light
stage: abstract-reasoning
status: draft
---

# The Photon Concept and Light as Quanta

## Core Idea
Light consists of photons—massless particles carrying energy E = hf and momentum p = h/λ. Each photon behaves as a discrete quantum with properties of both particles and waves. The photoelectric effect demonstrates that energy transfer occurs in quantized units; electrons absorb individual photons and are ejected only if photon energy exceeds the work function.

## Explainer

From Planck's quantization hypothesis you know that oscillators in a blackbody cavity can only exchange energy in discrete packets of size hf. Planck introduced this quantization as a mathematical trick to fix the ultraviolet catastrophe — he did not initially claim that light itself was discrete. Einstein took the radical step of asserting that light *really is* made of discrete quanta: the **photon** is a real particle, not just a bookkeeping device. The photoelectric effect you studied provides the evidence. Classical wave theory predicts that brighter light (more intensity) should eventually eject electrons regardless of frequency. Instead, experiments show a sharp frequency threshold: below a certain frequency, no electrons are ejected no matter how bright the light; above that frequency, electrons emerge instantly even at very low intensity. This makes no sense if energy arrives continuously as a wave, but it follows immediately if each electron absorbs exactly one photon and needs E = hf ≥ φ (the work function) to escape.

The two key photon relations connect wave and particle descriptions. **E = hf** (equivalently E = ℏω) connects particle energy to wave frequency. **p = h/λ** (equivalently p = ℏk) connects particle momentum to wave wavenumber. From these you can derive that E = pc for photons — consistent with the relativistic energy-momentum relation E² = (pc)² + (mc²)² with m = 0. Photons are massless relativistic particles. The combination E = pc also implies that light exerts radiation pressure, since momentum exchange produces force — Einstein's prediction that light pushes on mirrors was confirmed experimentally and is the operating principle of proposed solar sails.

The photon concept forces a profound revision of how we think about light. Light is neither purely a wave nor purely a particle — it exhibits **wave-particle duality**. In the double-slit experiment, individual photons (detected as point-like clicks on a detector) nonetheless build up an interference pattern when accumulated over many detections. Each photon in some sense "goes through both slits" and interferes with itself. The wave description (amplitude, phase, interference) correctly predicts the probability distribution; the particle description (discrete energy, momentum, localized detection) correctly predicts individual detection events. Quantum mechanics reconciles this by treating the photon's wavefunction (the electromagnetic field amplitude) as a probability amplitude: |ψ|² gives the probability of detecting the photon at a given location.

The photon also resolved the crisis of classical atomic stability. An electron in a Bohr orbit is accelerating, and classical electrodynamics (as you will learn in electrodynamics) predicts that accelerating charges must radiate continuously, causing atoms to collapse in nanoseconds. The photon picture resolves this: atoms occupy discrete energy levels, and electromagnetic energy can only be emitted in discrete photon packets. A ground-state electron has nowhere lower to go — there is no smaller allowed photon energy — so it does not radiate. Atoms are stable because energy quantization enforces a minimum energy state. This connection between the photon concept and atomic stability makes the photon one of the linchpins of all modern physics.
