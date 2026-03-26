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
- rlc-circuits
tags:
- resonance
- damping
- forced-vibrations
stage: formal-systems
status: validated
---

# Resonance and Damping in Forced Vibrations

## Core Idea
When a spring-mass system is driven by F(t) = F₀cos(ωt), the amplitude of the steady-state solution depends critically on how ω compares to the natural frequency ω₀. Near resonance (ω ≈ ω₀), amplitude becomes very large even for small forcing. Damping reduces amplitude everywhere and prevents infinite amplitude at resonance. Understanding resonance is essential for designing safe structures and devices.

## Questions

```yaml
- question: "An undamped spring-mass system is driven at exactly its natural frequency ω₀. What happens to the amplitude of oscillation over time?"
  type: multiple-choice
  options:
    - "It reaches a finite steady-state value determined by the magnitude of the forcing"
    - "It oscillates at ω₀ but with the same amplitude as the unforced system"
    - "It grows without bound, increasing linearly with time"
    - "It immediately becomes infinite at the first instant of forcing"
  answer: 2
  explanation: "At pure resonance with no damping, the standard particular solution guess (A·cos(ω₀t)) fails because cos(ω₀t) already appears in the homogeneous solution. The correct particular solution is y_p = (F₀/2mω₀)t·sin(ω₀t) — note the factor of t. This means amplitude grows linearly without bound, never reaching a steady state. Option A describes what happens away from resonance; option D is wrong because the growth is gradual, not instantaneous."

- question: "A damped oscillator is driven near its natural frequency. Compared to an identical undamped oscillator at the same driving frequency, the steady-state amplitude is:"
  type: multiple-choice
  options:
    - "Larger — the damping adds energy to the system near resonance"
    - "Always finite and smaller — damping limits the peak and prevents blow-up"
    - "Identical far from resonance but still infinite exactly at ω₀"
    - "Zero — the damping force exactly cancels the driving force"
  answer: 1
  explanation: "With damping, the steady-state amplitude is A = F₀/√((k − mω²)² + (cω)²). The damping term (cω)² in the denominator is always positive, so the denominator is never zero — the amplitude is always finite, even at ω = ω₀. Damping reduces amplitude everywhere (not just at resonance) and prevents the unbounded growth seen in the undamped case. The peak shifts slightly below ω₀ and flattens as damping increases."

- question: "Without damping, the steady-state solution formula for a forced oscillator breaks down when ω = ω₀ because the particular solution must include a factor of t to capture the growing amplitude."
  type: true-false
  answer: true
  explanation: "Correct. When ω = ω₀, the standard undetermined-coefficients guess A·cos(ω₀t) + B·sin(ω₀t) fails because these are already solutions to the homogeneous equation. The correct particular solution multiplies by t, giving y_p = (F₀/2mω₀)t·sin(ω₀t). This t factor is what produces the linearly growing amplitude characteristic of pure resonance — the system absorbs energy every cycle with no mechanism to shed it."

- question: "Adding damping to a forced oscillator shifts the resonance peak to a frequency higher than the natural frequency ω₀."
  type: true-false
  answer: false
  explanation: "The resonance peak shifts slightly BELOW ω₀ for underdamped systems, not above. The peak occurs at ω_peak = √(ω₀² − c²/2m²), which is less than ω₀. As damping increases, the peak shifts further below ω₀ and becomes flatter, until at critical damping the response has no distinct resonance peak at all."

- question: "Physically, why does damping prevent unbounded amplitude growth at resonance?"
  type: short-answer
  answer: "At resonance, the driving force is perfectly in phase with the velocity, so it does maximum positive work on the system every cycle — continuously adding energy. Without damping, this energy accumulates indefinitely and amplitude grows without bound. With damping, energy is dissipated every cycle (proportional to velocity and the damping coefficient). The steady state is reached when energy input from the driving force exactly balances energy dissipation by the damper — a finite amplitude where these two rates are equal."
  explanation: "The key insight is that resonance is an energy balance problem. Damping doesn't just reduce the amplitude of oscillation — it provides the only mechanism by which the system can reach equilibrium under sustained forcing. Larger damping dissipates more energy per cycle, which limits the amplitude more strongly. Without any dissipation pathway, there is no equilibrium and the amplitude must grow forever."
```

## Explainer

From your study of spring-mass systems, you know that an undamped mass on a spring oscillates at its **natural frequency** ω₀ = √(k/m), where k is the spring constant and m is the mass. Now suppose an external periodic force is applied: F(t) = F₀cos(ωt), where ω is the **driving frequency** that you choose. The equation of motion becomes my'' + ky = F₀cos(ωt). Using the method of undetermined coefficients, the particular solution — the **steady-state response** — has the form y_p = A·cos(ωt), where the amplitude A depends on the ratio of ω to ω₀. Specifically, A = F₀/(m(ω₀² − ω²)). When ω is far from ω₀, the denominator is large and the response amplitude is small. As ω approaches ω₀, the denominator approaches zero and A grows without bound.

The case ω = ω₀ exactly is called **pure resonance**. With no damping and a driving frequency exactly matching the natural frequency, the usual guessing form fails (because the homogeneous solution already contains cos(ω₀t)), and the correct particular solution grows with time: y_p = (F₀/2mω₀)t·sin(ω₀t). The factor of t means the amplitude grows linearly forever — the system absorbs energy with every cycle and never reaches a steady state. This is why bridges and buildings are designed so their natural frequencies don't match the frequencies of wind gusts, foot traffic, or ground motion: the Tacoma Narrows Bridge collapse in 1940 is the classic engineering illustration of resonance gone unchecked.

**Damping** changes the picture completely. A realistic spring-mass system includes a damping force proportional to velocity: my'' + cy' + ky = F₀cos(ωt). The damping coefficient c dissipates energy. The steady-state amplitude is now A = F₀/√((k − mω²)² + (cω)²), which is always finite, even at ω = ω₀. The amplitude still peaks near ω₀, but the damping term (cω) in the denominator prevents the amplitude from blowing up. The location of the peak shifts slightly below ω₀ for underdamped systems. As c increases, the peak flattens and shifts further, until at critical damping the response has no resonance peak at all.

The physical intuition is this: at resonance, the driving force is perfectly in phase with the velocity, so it does maximum positive work on the system every cycle. Without damping, all that energy accumulates. With damping, energy is constantly being removed, and the steady state represents a balance between energy input from the driving force and energy dissipation by the damper. Larger damping means more energy is removed per cycle, which limits how large the amplitude can grow. Engineering applications exploit this: shock absorbers in cars are tuned to dissipate energy quickly, radio circuits are tuned so their resonant frequency matches the desired signal frequency, and MRI machines exploit nuclear magnetic resonance at very precise frequencies to image tissue.
