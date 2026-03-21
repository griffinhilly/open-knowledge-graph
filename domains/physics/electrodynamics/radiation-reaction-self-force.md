---
id: radiation-reaction-self-force
title: Radiation Reaction Force
domain: physics
course: electrodynamics
prerequisites:
- id: radiation-from-accelerated-charges
  type: hard
- id: larmor-formula
  type: hard
builds-toward:
- classical-electron-radius
- radiation-damping-radiation-reaction
tags:
- radiation-reaction
- self-force
- abraham-lorentz
- runaway-solutions
stage: advanced
status: draft
---

# Radiation Reaction Force

## Core Idea
A radiating charge experiences a self-force due to its own radiated field. The Abraham-Lorentz force F = (q²/6πε₀c³)a̍ opposes acceleration and causes energy loss. This leads to runaway solutions in classical theory, limiting applicability to cases where the radiation damping is perturbative.

## Questions

```yaml
- question: "The Abraham-Lorentz force F_rad = (q²/6πε₀c³)ȧ depends on the jerk ȧ rather than velocity or acceleration. Why does energy balance require this unusual dependence?"
  type: multiple-choice
  options:
    - "The jerk dependence is an empirical fit to experimental data with no theoretical justification"
    - "Because the Larmor formula gives radiated power P ∝ a², and for F·v = -P to hold with F independent of v, F must be proportional to ȧ"
    - "Because the force must be proportional to the charge's velocity to conserve momentum"
    - "Because jerk is the only quantity with the correct units to form a force in classical electrodynamics"
  answer: 1
  explanation: "The derivation is driven by energy conservation. The Larmor formula gives P = q²a²/(6πε₀c³). For the radiation reaction force to account for this energy drain, it must satisfy F·v = -P. Since P ∝ a², and F·v must hold for arbitrary v, dimensional analysis and integration by parts show that F must involve ȧ (the time derivative of a). A force proportional to v (option C) or a (not listed) would give the wrong power dependence. The jerk dependence is not arbitrary — it follows necessarily from requiring consistency with the Larmor formula."

- question: "The Abraham-Lorentz equation of motion produces 'runaway solutions.' What are they, and why do they arise?"
  type: multiple-choice
  options:
    - "Solutions where the particle's charge grows unboundedly due to self-interaction — a quantum effect missing from the classical model"
    - "Solutions where, even with no external force, a particle spontaneously accelerates exponentially — because the equation is third-order in position and the extra initial condition allows unphysical exponential growth"
    - "Solutions where the particle moves backward in time, violating causality — requiring pre-acceleration to fix"
    - "Solutions that diverge only at the classical electron radius, where the point-charge approximation breaks down"
  answer: 1
  explanation: "The equation of motion m·a = F_ext + (q²/6πε₀c³)ȧ is third-order in position (since ȧ = d³r/dt³), requiring three initial conditions: position, velocity, and acceleration. With no external force and a free particle, the equation admits solutions a(t) = a₀ exp(t/τ) where τ = q²/(6πε₀mc³). This exponential growth — the particle accelerating without any applied force, powered by radiation reaction — is the runaway. It signals that the classical point-charge model is internally inconsistent at short distance scales."

- question: "The Abraham-Lorentz radiation reaction force is third-order in position, meaning specifying the initial position and velocity of a particle is sufficient to uniquely determine its subsequent trajectory."
  type: true-false
  answer: false
  explanation: "A third-order ODE requires three initial conditions, not two. Specifying initial position and velocity (as for Newton's second law, which is second-order) is insufficient — initial acceleration must also be specified. This over-specification relative to Newtonian mechanics is part of the problem: it introduces an extra degree of freedom that allows the runaway solutions, and it means the equation does not fit into the standard Newtonian framework where F = ma determines future evolution from position and velocity alone."

- question: "The Abraham-Lorentz force always opposes the direction of the charge's motion, acting like a velocity-dependent drag force."
  type: true-false
  answer: false
  explanation: "The Abraham-Lorentz force is proportional to the *jerk* ȧ = dā/dt, not to velocity. Its direction depends on whether the acceleration is increasing or decreasing, not on the direction of motion. For instance, a charge that is decelerating uniformly has ȧ = 0 and experiences no radiation reaction force at that instant, even though it is moving and radiating. A velocity-dependent drag force is qualitatively wrong — the actual force depends on the rate of change of acceleration, which makes the equation third-order and produces the pathological runaway behavior absent from ordinary drag."

- question: "Why do runaway solutions arise in the Abraham-Lorentz equation, and what does their existence reveal about the limits of classical electrodynamics for point charges?"
  type: short-answer
  answer: "Runaway solutions arise because the Abraham-Lorentz equation is third-order in position, allowing an extra free parameter — initial acceleration — that admits exponentially growing solutions even with no external force. Physically, radiation reaction provides positive feedback: higher acceleration causes more radiation, which requires more force to maintain, which further increases acceleration. This pathology reveals that classical electrodynamics cannot consistently describe a point charge interacting with its own field: the self-energy of a point charge diverges, and the self-force equation breaks down below the classical electron radius r_e ≈ 2.8 × 10⁻¹⁵ m, where quantum effects (and ultimately QED) are required."
  explanation: "The runaway problem is not a minor technical issue — it signals a fundamental inconsistency. The force is derived by assuming the charge is a point, but the self-field of a point charge has infinite energy. QED resolves this via renormalization: the infinite self-energy is absorbed into the measured electron mass, and the remaining finite self-force is well-behaved. The Abraham-Lorentz force is only a valid approximation when used perturbatively, i.e., when the radiation damping is a small correction to the dominant applied force."
```

## Explainer

From the Larmor formula and your study of radiation from accelerated charges, you know that an accelerating charge radiates electromagnetic energy at rate P = q²a²/(6πε₀c³). But where does this energy come from? It must come from the kinetic energy of the charge — the charge must be slowing down, or require extra force to maintain acceleration, due to the energy it is radiating away. This means the charge's own radiation field exerts a force back on the charge itself: the **radiation reaction force** or **self-force**. Capturing this force is one of the deepest and most troublesome problems in classical electrodynamics.

The result is the **Abraham-Lorentz force**: F_rad = (q²/6πε₀c³) ȧ, where ȧ = dā/dt is the **jerk** — the time derivative of acceleration. Notice the unusual structure: this force depends not on position, velocity, or even acceleration, but on the *rate of change* of acceleration. This makes physical sense dimensionally — we need a force that drains power P = F·v proportional to a², and working backwards from the Larmor formula to find a force F such that F·v = −P leads directly to this expression involving ȧ. The coefficient q²/(6πε₀c³) = (2/3)(r_e/c) involves the **classical electron radius** r_e = q²/(4πε₀m_ec²), a characteristic length scale that marks where classical electrodynamics breaks down.

The trouble with this force is that it generates pathological solutions. The equation of motion m·a = F_external + F_rad becomes a third-order ODE in position (since ȧ = d³r/dt³). Third-order ODEs require three initial conditions, and specifying the initial position and velocity is not enough — you must also specify the initial acceleration. This over-specification leads to **runaway solutions**: even with no external force, a free particle can spontaneously accelerate exponentially, with radiation reaction providing positive feedback rather than damping. This is unphysical and signals a fundamental breakdown of the classical point-charge model at very short distance scales (below r_e ≈ 2.8 × 10⁻¹⁵ m for electrons, where quantum effects dominate).

In practice, the Abraham-Lorentz force is only used perturbatively. When the radiation damping is small compared to the applied force (the radiation power is much less than the applied force times the velocity), the runaway instability is suppressed and the equation gives sensible results. For example, an oscillating charge loses energy to radiation, and the damping can be treated as a small correction to the oscillation. This perturbative approach underlies the classical theory of spectral line widths and the damping of antenna radiation. The full resolution of the self-force problem requires quantum electrodynamics, where mass renormalization absorbs the divergent self-energy and the Abraham-Lorentz pathology disappears — a key motivation for the development of quantum field theory.
