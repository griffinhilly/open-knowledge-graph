---
id: matter-wave-de-broglie-momentum
title: Matter Waves and de Broglie Wavelength
domain: physics
course: modern-physics
prerequisites:
- id: photon-concept-quanta
  type: hard
- id: momentum-and-impulse
  type: hard
builds-toward:
- electron-diffraction-matter
tags:
- quantum
- matter-waves
- duality
stage: advanced
status: validated
---

# Matter Waves and de Broglie Wavelength

## Core Idea
All particles, including electrons and atoms, possess an associated wavelength λ = h/p. This de Broglie wavelength decreases as momentum increases. Matter waves are not classical mechanical waves but rather a manifestation of quantum superposition; the wavelength relates to the uncertainty in a particle's position through the uncertainty principle.

## Questions

```yaml
- question: "A dust particle (mass ~10⁻¹⁵ kg, speed ~0.01 m/s) and an electron (mass ~9×10⁻³¹ kg, speed ~10⁶ m/s) are both described by de Broglie wavelengths. Which would exhibit observable wave behavior such as diffraction?"
  type: multiple-choice
  options:
    - "The dust particle, because its slow speed gives it more time to interact with nearby surfaces"
    - "The electron, because its de Broglie wavelength (~0.7 nm) is comparable to atomic spacings, enabling diffraction from crystal lattices"
    - "Both equally, because the formula λ = h/p applies to all matter without distinction"
    - "Neither, because wave behavior is exclusive to photons and massless particles"
  answer: 1
  explanation: "The de Broglie relation applies to all matter, but observable wave behavior (diffraction, interference) only occurs when λ is comparable to the scale of the physical interaction. The electron's wavelength (~0.7 nm at 10⁶ m/s) is close to atomic spacings (~0.1–0.5 nm), so electrons diffract from crystal lattices — exactly what Davisson and Germer demonstrated. The dust particle's wavelength would be enormous compared to atomic spacings in the other direction... actually, let's compute: λ = h/mv = 6.6×10⁻³⁴/(10⁻¹⁵ × 0.01) = 6.6×10⁻¹⁷ m — far smaller than an atomic nucleus. Its wave character is utterly undetectable. The formula applies universally; detectability depends on relative scale."

- question: "A particle is prepared so that its momentum is known exactly (Δp = 0). The de Broglie relation assigns it a precise wavelength λ = h/p. What does this imply about the particle's position?"
  type: multiple-choice
  options:
    - "Its position is also precisely defined, since both momentum and position can be determined from the wavefunction"
    - "Its position is completely indefinite — the wavefunction is a plane wave spread uniformly throughout all space"
    - "Its position is uncertain by one wavelength on either side of its classical trajectory"
    - "The particle has no position because it is purely a wave with no particle-like localization"
  answer: 1
  explanation: "A particle with definite momentum p has a wavefunction ψ ∝ e^{ipx/ℏ} — a plane wave extending throughout all space with equal amplitude everywhere. The probability density |ψ|² is uniform: the particle is equally likely to be anywhere. This is the Heisenberg uncertainty principle: Δx·Δp ≥ ℏ/2. With Δp = 0, we get Δx → ∞. A precise de Broglie wavelength (definite momentum) is mathematically incompatible with any localization. Option D is a misconception: the particle still has particle-like properties (it is detected at a single point), but its position before measurement is maximally uncertain."

- question: "A baseball has a de Broglie wavelength that is, in principle, nonzero, but its wave behavior is completely unobservable in practice."
  type: true-false
  answer: true
  explanation: "The de Broglie relation λ = h/p applies to all matter, including baseballs. For a 0.15 kg baseball at 40 m/s, λ = h/mv ≈ 6.6×10⁻³⁴/(0.15×40) ≈ 10⁻³⁴ m — roughly 20 orders of magnitude smaller than an atomic nucleus (10⁻¹⁵ m). No instrument or physical phenomenon could resolve structure at this scale. The wavelength is technically nonzero but physically meaningless. This is why classical mechanics describes macroscopic objects exactly: quantum effects scale with λ, and at 10⁻³⁴ m those effects are indistinguishable from zero."

- question: "A de Broglie matter wave is a classical mechanical wave — a physical disturbance propagating through a medium, similar to sound or water waves."
  type: true-false
  answer: false
  explanation: "A de Broglie wave is the quantum mechanical wavefunction ψ(x, t), not a classical wave in any medium. Its squared amplitude |ψ|² gives the probability density for finding the particle at a given position — there is no physical disturbance propagating through space. Unlike sound (pressure oscillations) or water waves (surface displacement), the wavefunction is not a directly observable field; it is a mathematical object encoding probabilistic information. The confusion between 'matter waves' and classical waves leads to mistaken pictures of particles oscillating in space."

- question: "A thrown baseball is described by the de Broglie relation λ = h/p, yet it shows no observable wave behavior. Explain why, using the formula to support your reasoning."
  type: short-answer
  answer: "For a 0.15 kg baseball thrown at 40 m/s, λ = h/mv ≈ (6.6×10⁻³⁴)/(0.15×40) ≈ 10⁻³⁴ m. This is roughly 20 orders of magnitude smaller than an atomic nucleus. Wave behavior (diffraction, interference) is only observable when the wavelength is comparable to the scale of the physical system. No material exists with structure at 10⁻³⁴ m, so the baseball cannot diffract or interfere with anything. The larger the momentum, the shorter the wavelength, and the less observable the wave character — which is why quantum effects vanish at macroscopic scales."
  explanation: "This question directly addresses the most natural misconception: if λ = h/p applies to everything, why doesn't everything exhibit wave behavior? The answer is that observability requires λ to be comparable to the relevant physical scale. For electrons, λ ~ atomic spacings, enabling crystal diffraction. For a baseball, λ is fantastically smaller than anything real, so quantum behavior is undetectable. The boundary between quantum and classical behavior is not a sharp line but a practical limit set by the ratio of de Broglie wavelength to the scale of the interaction."
```

## Explainer

You know from the photon concept that light carries both energy E = hf and momentum p = h/λ — quantized packets that behave like particles under some conditions and like waves under others. De Broglie's bold generalization runs this relationship in the opposite direction: if light with wavelength λ has momentum p = h/λ, then by symmetry, any matter with momentum p should have an associated wavelength λ = h/p. The same Planck constant h that quantizes light also governs the wave character of electrons, protons, atoms — all material particles.

The formula λ = h/p = h/mv makes an immediate, testable prediction about where wave behavior will be observable. An electron moving at a few percent of the speed of light has a de Broglie wavelength on the order of 0.1 nm — comparable to the spacing between atoms in a crystal lattice. This is in the X-ray range, and just as X-rays diffract from crystal planes, so should electrons with this wavelength. A baseball, by contrast, has a mass of 0.15 kg and a typical speed of 40 m/s, giving λ ≈ 10^(−34) m — roughly 20 orders of magnitude smaller than an atomic nucleus. Its wave character is utterly undetectable by any physical measurement. The larger the momentum, the shorter the wavelength, and the less observable the wave behavior.

The phrase "matter wave" must be interpreted carefully. The de Broglie wavelength is not a sound wave or a pressure wave — it is the spatial period of the quantum **wavefunction** ψ(x). For a particle with definite momentum p, the wavefunction is a plane wave ψ ∝ e^{ipx/ℏ} oscillating with wavelength h/p spread uniformly throughout space. Since |ψ|² gives the probability density for finding the particle, a plane wave corresponds to completely indefinite position — the particle is equally likely to be anywhere. This is the uncertainty principle in action: definite momentum (Δp = 0) implies infinite positional uncertainty (Δx → ∞), and ΔxΔp ≥ ℏ/2 is satisfied with equality for a pure plane wave.

The experimental confirmation came from the Davisson-Germer experiment, where electrons scattered from a crystal lattice produced diffraction maxima at precisely the angles predicted by Bragg's law using λ = h/p. This was a decisive test: only a wave phenomenon can produce diffraction, yet the electrons were unambiguously particles arriving one at a time at the detector. Today, neutron diffraction uses the same principle to determine protein structures, and atom interferometry uses matter waves to measure gravitational acceleration and fundamental constants with extraordinary precision. The de Broglie relation λ = h/p is the entry point into the full quantum mechanical framework: it is the first clue that the language of physics at small scales is not position and velocity, but wavefunctions and probability amplitudes.
