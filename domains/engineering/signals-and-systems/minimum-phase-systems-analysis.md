---
id: minimum-phase-systems-analysis
title: Minimum Phase Systems and Factorization
domain: engineering
course: signals-and-systems
prerequisites:
- id: all-pass-filters-phase-shaping
  type: hard
- id: transfer-function-poles-zeros
  type: hard
tags:
- minimum-phase
- all-pass
- transfer-function
- stability
stage: advanced
status: draft
---

# Minimum Phase Systems and Factorization

## Core Idea
A minimum-phase system has all poles and zeros inside the unit circle (digital) or left half-plane (analog), resulting in minimum group delay for its magnitude response. Any transfer function factors as H(z) = Hmin(z)·Hap(z), where Hmin is minimum-phase and Hap is all-pass. This decomposition enables simultaneous specification of magnitude response and phase characteristics.

## Questions

```yaml
- question: "A discrete-time channel has transfer function H(z) = (z – 2)/(z – 0.5). An engineer wants to design a stable causal equalizer E(z) such that E(z)·H(z) = 1. What problem arises?"
  type: multiple-choice
  options:
    - "No problem — any rational system has a rational inverse that is also stable and causal"
    - "The inverse E(z) = (z – 0.5)/(z – 2) has a pole at z = 2, outside the unit circle, making the equalizer unstable"
    - "The channel pole at z = 0.5 prevents inversion because poles cannot be canceled"
    - "Equalization is only possible if the channel has no poles at all"
  answer: 1
  explanation: "Inverting H(z) = (z–2)/(z–0.5) gives E(z) = (z–0.5)/(z–2), which places a pole at z = 2 — outside the unit circle, making E(z) unstable. The zero at z = 2 in H(z) becomes a pole in E(z). This is exactly why minimum-phase is the key criterion for stable invertibility: only when all zeros lie inside the unit circle will the inverse have all poles inside the unit circle too, preserving stability. H(z) here is non-minimum-phase, so no stable causal inverse exists."

- question: "Two causal stable systems A and B have exactly the same magnitude response |H(e^jω)| for all frequencies, but system A is minimum-phase while system B is not. What must be true about their transfer functions?"
  type: multiple-choice
  options:
    - "Their transfer functions are identical — magnitude response uniquely determines a causal system"
    - "System B has the same minimum-phase factor as A but an additional all-pass component that adds phase lag without changing magnitude"
    - "System B must be unstable, since a non-minimum-phase system sharing the same magnitude as a stable system is impossible"
    - "The two systems differ in pole locations but have identical zeros"
  answer: 1
  explanation: "By the min-phase factorization theorem, any stable causal system factors as H = H_min · H_ap, where H_min is minimum-phase and H_ap is all-pass (|H_ap| = 1 everywhere). If A and B share the same magnitude response, they share the same minimum-phase factor H_min. B differs only in having a non-trivial all-pass component that moves some zeros outside the unit circle (to conjugate-reciprocal positions), keeping magnitude unchanged but adding phase lag. Both remain stable (poles inside unit circle)."

- question: "A minimum-phase system introduces less phase lag at every frequency than any other stable, causal system with the same magnitude response."
  type: true-false
  answer: true
  explanation: "This is the defining property of minimum-phase systems — the name means 'minimum group delay.' An all-pass factor has unit magnitude everywhere but introduces additional phase lag. Any non-minimum-phase system with the same magnitude has a non-trivial all-pass component H_ap, contributing extra phase lag beyond what H_min alone introduces. The minimum-phase system has no all-pass component (H_ap = 1), making its phase response the smallest possible for that magnitude profile."

- question: "Moving a zero from inside to outside the unit circle (to its conjugate-reciprocal position) changes both the magnitude and phase responses of the system."
  type: true-false
  answer: false
  explanation: "Moving a zero z₀ (inside the unit circle) to its conjugate reciprocal 1/z₀* (outside the unit circle) changes only the phase response — the magnitude response |H(e^jω)| is unchanged. This is exactly the all-pass substitution: the factor (z – 1/z₀*)/(1 – z₀*z⁻¹) has unit magnitude everywhere. This is why two systems can share an identical magnitude spectrum yet have different phase responses — they have the same minimum-phase factor but differ in their all-pass components."

- question: "Why are minimum-phase systems called 'stably invertible,' and what goes wrong when you attempt to invert a non-minimum-phase system with a stable causal filter?"
  type: short-answer
  answer: "A minimum-phase system has all zeros inside the unit circle. Its causal inverse 1/H_min(z) has poles exactly where H_min has zeros — all inside the unit circle — so the inverse is also stable and causal. For a non-minimum-phase system, at least one zero lies outside the unit circle; inverting it places a pole outside the unit circle, making the equalizer unstable. You cannot perfectly equalize a non-minimum-phase channel with a stable causal filter; you must either accept instability, use non-causal processing, or apply regularized approximations."
  explanation: "This has direct practical consequences: channel equalization, echo cancellation, and seismic deconvolution are feasible with a stable causal inverse only when the system is minimum-phase. The first diagnostic question in any equalization problem is therefore: are all zeros inside the unit circle? If yes, perfect causal inversion is achievable. If no, the engineer must choose between approximation methods — there is no exact stable causal solution."
```

## Explainer

You know from transfer function poles and zeros that a system's frequency response is determined by the locations of poles and zeros in the complex plane. Poles set the resonances and stability properties; zeros shape the amplitude response by introducing nulls and notches. What is less obvious is that a system's magnitude response |H(e^jω)| and phase response ∠H(e^jω) are not independent — for a certain special class of systems, the phase is entirely determined by the magnitude. Those systems are the **minimum-phase** systems, and understanding them is the key to understanding how phase and magnitude can be specified independently.

A system is minimum-phase if all of its zeros lie inside the unit circle (discrete-time) or in the left half-plane (continuous-time). The name comes from the comparison: among all stable, causal systems with the same magnitude spectrum |H(e^jω)|, the minimum-phase system introduces the smallest possible phase lag at every frequency — it has minimum **group delay**. From your study of all-pass filters, you know that an all-pass system has unit magnitude at all frequencies but introduces frequency-dependent phase shifts by placing zeros outside the unit circle (with corresponding poles inside). If you take a minimum-phase system and move one of its zeros from inside to outside the unit circle (to the conjugate reciprocal position 1/z*), the magnitude response is unchanged but the phase lag increases. The minimum-phase system is the uniquely "most efficient" phase choice for a given magnitude response.

Every stable, causal transfer function factors as H(z) = H_min(z) · H_ap(z), where H_min is minimum-phase and H_ap is all-pass (|H_ap(e^jω)| = 1 ∀ω). H_ap is constructed by taking all zeros outside the unit circle, reflecting them inside to their conjugate reciprocal positions to form H_min, and placing the original outside-unit-circle zeros in H_ap along with stabilizing poles. Because |H_ap| = 1 everywhere, the magnitude of H equals the magnitude of H_min alone — all magnitude shaping comes from the minimum-phase factor. All excess phase (beyond what H_min would introduce) comes from H_ap. This decomposition is not just algebraic bookkeeping: it separates the "what does this system do to amplitudes" question from the "how much extra phase delay does it introduce" question.

This factorization has profound practical consequences. Minimum-phase systems are **stably invertible**: their causal inverse H_min⁻¹(z) = 1/H_min(z) has all poles inside the unit circle (since H_min's zeros are inside the unit circle). This means a minimum-phase channel or filter can be perfectly equalized with a stable causal filter. Non-minimum-phase systems cannot be causally inverted stably — attempting to equalize a zero outside the unit circle requires placing a pole outside, producing an unstable inverse. Applications include communications channel equalization (remove the channel's distortion at the receiver), acoustic echo cancellation (invert the room impulse response), and seismic deconvolution (remove the source wavelet from recorded reflections). In each case, the first diagnostic question is: is this system minimum-phase? If yes, perfect causal inversion is feasible. If no, approximations, acausal processing, or regularized inversion are required.
