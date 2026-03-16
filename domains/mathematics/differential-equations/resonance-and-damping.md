---
id: resonance-and-damping
title: Resonance and Damping in Forced Vibrations
domain: mathematics
course: differential-equations
prerequisites:
- id: spring-mass-systems
  type: hard
- id: undetermined-coefficients
  type: hard
builds-toward:
- rlc-circuit-applications
tags:
- resonance
- damping
- forced-vibrations
stage: formal-systems
status: draft
---

# Resonance and Damping in Forced Vibrations

## Core Idea
When a spring-mass system is driven by F(t) = F₀cos(ωt), the amplitude of the steady-state solution depends critically on how ω compares to the natural frequency ω₀. Near resonance (ω ≈ ω₀), amplitude becomes very large even for small forcing. Damping reduces amplitude everywhere and prevents infinite amplitude at resonance. Understanding resonance is essential for designing safe structures and devices.

## Explainer

From your study of spring-mass systems, you know that an undamped mass on a spring oscillates at its **natural frequency** ω₀ = √(k/m), where k is the spring constant and m is the mass. Now suppose an external periodic force is applied: F(t) = F₀cos(ωt), where ω is the **driving frequency** that you choose. The equation of motion becomes my'' + ky = F₀cos(ωt). Using the method of undetermined coefficients, the particular solution — the **steady-state response** — has the form y_p = A·cos(ωt), where the amplitude A depends on the ratio of ω to ω₀. Specifically, A = F₀/(m(ω₀² − ω²)). When ω is far from ω₀, the denominator is large and the response amplitude is small. As ω approaches ω₀, the denominator approaches zero and A grows without bound.

The case ω = ω₀ exactly is called **pure resonance**. With no damping and a driving frequency exactly matching the natural frequency, the usual guessing form fails (because the homogeneous solution already contains cos(ω₀t)), and the correct particular solution grows with time: y_p = (F₀/2mω₀)t·sin(ω₀t). The factor of t means the amplitude grows linearly forever — the system absorbs energy with every cycle and never reaches a steady state. This is why bridges and buildings are designed so their natural frequencies don't match the frequencies of wind gusts, foot traffic, or ground motion: the Tacoma Narrows Bridge collapse in 1940 is the classic engineering illustration of resonance gone unchecked.

**Damping** changes the picture completely. A realistic spring-mass system includes a damping force proportional to velocity: my'' + cy' + ky = F₀cos(ωt). The damping coefficient c dissipates energy. The steady-state amplitude is now A = F₀/√((k − mω²)² + (cω)²), which is always finite, even at ω = ω₀. The amplitude still peaks near ω₀, but the damping term (cω) in the denominator prevents the amplitude from blowing up. The location of the peak shifts slightly below ω₀ for underdamped systems. As c increases, the peak flattens and shifts further, until at critical damping the response has no resonance peak at all.

The physical intuition is this: at resonance, the driving force is perfectly in phase with the velocity, so it does maximum positive work on the system every cycle. Without damping, all that energy accumulates. With damping, energy is constantly being removed, and the steady state represents a balance between energy input from the driving force and energy dissipation by the damper. Larger damping means more energy is removed per cycle, which limits how large the amplitude can grow. Engineering applications exploit this: shock absorbers in cars are tuned to dissipate energy quickly, radio circuits are tuned so their resonant frequency matches the desired signal frequency, and MRI machines exploit nuclear magnetic resonance at very precise frequencies to image tissue.
