---
id: relativistic-doppler-shift
title: Relativistic Doppler Effect
domain: physics
course: modern-physics
prerequisites:
- id: special-relativity-postulates
  type: hard
- id: doppler-effect
  type: hard
tags:
- special-relativity
- waves
- doppler
stage: advanced
status: validated
---

# Relativistic Doppler Effect

## Core Idea
The relativistic Doppler formula for light is f' = f√[(1−β)/(1+β)] for motion along the line of sight (β = v/c). Unlike the classical Doppler effect, relativistic shift includes time dilation effects and is symmetric—observers in different frames calculate the shift consistently. Transverse Doppler shift (motion perpendicular to line of sight) arises purely from time dilation.

## Questions

```yaml
- question: "A star moves directly away from Earth at v = 0.6c. Observer A treats the star as moving away from a stationary Earth; Observer B treats Earth as moving away from a stationary star. What do the two observers calculate for the redshift factor f'/f?"
  type: multiple-choice
  options:
    - "Different values — one is treating a moving source, the other a moving observer, which give different classical results"
    - "The same value — special relativity depends only on relative velocity, not on who is 'really' moving"
    - "A is correct and B is wrong — the Earth is the inertial reference frame, so the star moves"
    - "B is correct and A is wrong — stars are more massive and thus define the true rest frame"
  answer: 1
  explanation: "This symmetry is the key relativistic departure from classical Doppler. In classical physics, 'moving source' and 'moving observer' give different formulas because the medium (e.g., air for sound) defines a preferred frame. Light has no medium, so there is no preferred frame — only relative velocity matters. Both observers calculate f' = f√[(1−β)/(1+β)] with the same β = 0.6, getting the same result. Options C and D both invoke the idea of a 'true' rest frame, which special relativity explicitly rejects."

- question: "A spacecraft moves exactly perpendicular to your line of sight at a relativistic speed. What does each theory predict for the frequency of light it emits toward you?"
  type: multiple-choice
  options:
    - "Classical theory: zero shift. Relativistic theory: a blueshift, because the spacecraft is approaching along the curved path"
    - "Classical theory: zero shift. Relativistic theory: a redshift, because the spacecraft's clock runs slow due to time dilation"
    - "Classical theory: a redshift. Relativistic theory: zero shift, since motion is transverse"
    - "Both theories predict the same redshift, since transverse motion affects wavefront spacing equally"
  answer: 1
  explanation: "The classical Doppler formula involves the component of velocity along the line of sight; purely transverse motion contributes nothing, so the classical prediction is zero shift. But relativistically, the moving spacecraft's clock is time-dilated — it ticks more slowly by a factor γ. You therefore receive fewer wave cycles per second even though the spacecraft is momentarily moving perpendicular to your line of sight. The result is a redshift f' = f/γ — purely a time-dilation effect with no classical analogue. This transverse Doppler shift was a key experimental confirmation of special relativity."

- question: "The relativistic Doppler formula predicts the same frequency shift regardless of whether you model the source as moving toward a stationary observer, or the observer as moving toward a stationary source at the same relative speed."
  type: true-false
  answer: true
  explanation: "This symmetry is a direct consequence of the first postulate of special relativity: the laws of physics are the same in all inertial frames. Since only the relative velocity matters, the formula f' = f√[(1+β)/(1−β)] (for approach) is the same whether you assign the motion to the source or the observer. This contrasts with the classical Doppler effect for sound, where the medium defines a rest frame and 'moving source' versus 'moving observer' give different formulas even for the same relative speed."

- question: "Because the relativistic Doppler formula includes a time-dilation correction, it predicts noticeably different results from the classical Doppler formula even at everyday speeds like v = 100 m/s."
  type: true-false
  answer: false
  explanation: "At speeds much less than c (β << 1), the relativistic formula reduces to approximately the classical result. The time-dilation factor γ ≈ 1 + β²/2 + ..., which deviates from 1 only at second order in β. At v = 100 m/s, β ≈ 3×10⁻⁷, so the relativistic correction is of order β² ≈ 10⁻¹³ — completely undetectable. The differences become significant only at a substantial fraction of c, which is why relativistic Doppler matters for astrophysics (distant galaxies, particle accelerators) but not for everyday acoustics."

- question: "What physical effect causes the transverse Doppler shift, and why does this effect have no analogue in classical Doppler theory?"
  type: short-answer
  answer: "The transverse Doppler shift is caused entirely by time dilation: a source moving perpendicular to your line of sight has a clock that runs slow by a factor γ relative to your frame, so it emits fewer wave cycles per second as measured by you. The result is a pure redshift f' = f/γ. Classical Doppler theory has no such effect because it assumes absolute time — clocks tick at the same rate regardless of motion. The classical formula only depends on the component of velocity along the line of sight (wavefront compression or stretching); transverse motion contributes nothing classically. Time dilation is a purely relativistic phenomenon, so the transverse shift is a distinctly relativistic prediction."
  explanation: "The transverse Doppler effect was one of the earliest proposed tests of special relativity that could distinguish it from the classical theory, since the classical prediction is exactly zero while the relativistic prediction is a measurable redshift. It was confirmed experimentally by Ives and Stilwell in 1938 using fast-moving atoms, and later with great precision using atomic clocks in particle accelerators. It is now routinely observed whenever relativistic particles emit radiation perpendicular to their direction of travel."
```

## Explainer

You already know the classical Doppler effect: a source moving toward you compresses the wavefronts, raising the observed frequency; one moving away stretches them, lowering it. The formula depends on the velocities of both source and medium. But light has no medium, and here special relativity changes the picture fundamentally. Two effects are at play simultaneously — the geometric compression of wavefronts and **time dilation** — and both must be accounted for to get the right answer.

Consider a source moving directly toward you at speed v (β = v/c). In the source's frame, it emits waves at frequency f. But from your frame, the source's clock is time-dilated: it ticks more slowly by a factor γ = 1/√(1−β²). This slowing acts like a lower emission frequency. Simultaneously, because the source is approaching, each successive crest is emitted from a position closer to you, compressing the wavelength. These two effects combine — one tending to lower the frequency, one to raise it — and the net result is f' = f√[(1+β)/(1−β)] for an approaching source, which is always larger than the classical prediction for the same speed.

The formula becomes especially illuminating for recession: f' = f√[(1−β)/(1+β)]. This is the **cosmological redshift** formula in its pure Doppler form. When astronomers observe distant galaxies with spectral lines shifted to longer wavelengths, they're measuring β directly from this formula. Notice the deep symmetry: the formula is the same whether you think of the source as moving away from a stationary observer or the observer moving away from a stationary source. In classical Doppler, these two cases give different answers (because the medium defines a preferred frame). In special relativity they are identical — there is no preferred frame, and the physics depends only on relative velocity.

The most conceptually novel piece is **transverse Doppler shift**: when the source moves perpendicular to your line of sight, the classical formula predicts zero frequency shift (no compression or stretching of wavefronts). But relativistically, there is still a shift — a pure time-dilation redshift of f' = f/γ. The source's clock runs slow, so you receive fewer cycles per second even though it's not moving toward or away from you at the moment of emission. This effect has no classical analogue and was one of the first experimental confirmations of relativistic time dilation, observed using fast-moving atomic clocks and later by precise measurements in particle accelerators.
