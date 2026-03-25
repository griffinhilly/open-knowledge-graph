---
id: electron-spin-magnetic-moment
title: Electron Spin and Intrinsic Magnetic Moment
domain: physics
course: modern-physics
prerequisites:
- id: spin-angular-momentum
  type: hard
- id: electron-cloud-orbital-shapes
  type: soft
builds-toward:
- zeeman-effect-magnetic-splitting
- stern-gerlach-sequential-measurements
tags:
- spin
- magnetic-moment
- quantum-mechanics
stage: advanced
status: validated
---
# Electron Spin and Intrinsic Magnetic Moment

## Core Idea
Electrons possess intrinsic angular momentum (spin) with magnitude S = ℏ√(s(s+1)) where s = 1/2. The spin z-component is m_s = ±ℏ/2 (spin up or spin down). Spin produces a magnetic moment μ = −g_s(e/2m_e)S, where g_s ≈ 2 (anomalous in comparison to orbital angular momentum). This magnetic moment interacts with magnetic fields and causes level splitting.

## How It's Best Learned
Study spin-1/2 systems using Pauli matrices. Calculate expectation values of spin components. Understand spin as an intrinsic two-state system; appreciate that quantum spin has no classical analog.

## Common Misconceptions
Spin does not mean the electron is literally spinning (quantum spin is intrinsic, not due to rotation). The g-factor ≈ 2 is not exactly 2 due to quantum electrodynamic corrections. Spin-orbit coupling is not due to the spinning electron's magnetic moment interacting with the orbital motion magnetic field (it's a relativistic effect).

## Questions

```yaml
- question: "Suppose the electron's spin g-factor were g_s = 1 instead of g_s ≈ 2. How would the energy splitting of a spin-1/2 electron in a magnetic field B compare to the actual case?"
  type: multiple-choice
  options:
    - "The splitting would be twice as large"
    - "The splitting would be half as large"
    - "The splitting would be unchanged because it depends only on the spin quantum number"
    - "The splitting would vanish because g_s = 1 means no anomalous magnetic moment"
  answer: 1
  explanation: "The energy splitting between spin-up and spin-down states is ΔE = g_s μ_B B. With g_s = 1, this would be μ_B B. With the actual g_s ≈ 2, it is ≈ 2μ_B B — twice as large. The g-factor directly scales the strength of the spin-field interaction relative to the orbital case. This factor of ~2 is why the Stern-Gerlach experiment's observed splitting confirmed that electron spin has an anomalous magnetic moment, not the classical value orbital angular momentum would predict."

- question: "Why do physicists say electron spin has 'no classical analog,' and what breaks the classical spinning-sphere model?"
  type: multiple-choice
  options:
    - "Spin is classical but too small to observe directly with current instruments"
    - "For any reasonable electron radius, the equatorial velocity required to reproduce the observed angular momentum would exceed the speed of light"
    - "Classical physics forbids quantized angular momentum, making any classical model inconsistent"
    - "Spin only exists in quantum field theory and was artificially added to match experiment"
  answer: 1
  explanation: "If the electron were a tiny charged sphere spinning fast enough to produce spin angular momentum ℏ/2, the surface speed at its equator (using the experimentally constrained upper bound on the electron's radius, ~10⁻¹⁸ m) would vastly exceed c. Special relativity makes this physically impossible. This isn't just a limitation of our models — it proves that spin cannot arise from literal rotation. Spin is a genuinely intrinsic property of the relativistic quantum electron, emerging naturally from Dirac's equation, not from any spatial motion."

- question: "Electron spin is called 'intrinsic angular momentum' because the electron physically rotates about its own internal axis, generating angular momentum just as a spinning top does."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about spin. 'Intrinsic' means the angular momentum is a fundamental property of the particle itself, independent of any spatial motion — not that the particle is literally spinning. The spinning-sphere picture fails for the relativistic reasons described above. Spin emerges from Dirac's relativistic quantum mechanics as a consequence of combining special relativity with quantum mechanics; it has no counterpart in classical mechanics. The electron carries angular momentum ℏ/2 just as it carries charge e — as an intrinsic, non-mechanical attribute."

- question: "The anomalous g-factor g_s ≈ 2.002 of the electron cannot be explained by classical electromagnetism and is correctly predicted only by relativistic quantum mechanics, with the small departure from exactly 2 arising from quantum electrodynamic corrections."
  type: true-false
  answer: true
  explanation: "Classical electromagnetism predicts g = 1 for a current loop (orbital angular momentum). Dirac's relativistic quantum mechanics automatically predicts g_s = 2 for spin — a remarkable postdiction that was one of the theory's greatest triumphs. The tiny additional correction (g_s ≈ 2.00231930...) comes from quantum electrodynamic (QED) loop corrections: the electron interacting with virtual photons in the vacuum. This anomalous magnetic moment has been measured to 12 significant figures and matches QED predictions to the same precision, making it the most precisely tested prediction in all of physics."

- question: "Why is the g-factor for electron spin approximately 2 rather than 1 (the value for orbital angular momentum), and what is the physical significance of this difference?"
  type: short-answer
  answer: "The g-factor of 1 for orbital angular momentum follows from classical electrodynamics: a current loop's magnetic moment equals its angular momentum times e/2m. Spin has no classical analog, and its g ≈ 2 emerges from Dirac's relativistic wave equation as an automatic consequence of special relativity combined with quantum mechanics — it was not put in by hand. The factor of ~2 means that for the same magnitude of angular momentum, spin couples to a magnetic field roughly twice as strongly as orbital motion. This difference has measurable consequences in atomic spectra (the anomalous Zeeman effect) and in the fine structure of hydrogen, where spin-orbit coupling strength depends on g_s."
  explanation: "The physical significance extends beyond the factor of 2: the fact that g_s is not exactly 2 but ≈ 2.002 is a signature of quantum electrodynamics — the electron continuously emitting and reabsorbing virtual photons. The 'anomalous magnetic moment' (a_e = (g_s−2)/2 ≈ 0.00116) is one of the most precisely measured and theoretically computed quantities in physics, serving as a fundamental test of QED."
```

## Explainer

You've studied spin angular momentum as an abstract two-state quantum system. Now the physical stakes become clearer: spin isn't just a mathematical curiosity — it generates a real **magnetic dipole moment** that interacts measurably with external magnetic fields and with the electron's own orbital motion. The connection between spin and magnetism is what makes the electron a tiny magnet, and it drives much of the structure of atomic spectra.

The **intrinsic magnetic moment** of the electron is μ = −g_s (e/2m_e) S, where S is the spin angular momentum vector. The factor e/2m_e is the same that appears for orbital angular momentum (the **gyromagnetic ratio**), but the factor g_s ≈ 2 is not — it's the anomalous g-factor. For orbital angular momentum, the magnetic moment and angular momentum have g_L = 1; for spin, g_s ≈ 2.002. This factor of 2 was a complete mystery classically and was correctly predicted only by Dirac's relativistic quantum mechanics. The tiny departure from exactly 2 (the 0.002) is a quantum electrodynamic correction — one of the most precisely measured quantities in physics, tested to 12 significant figures.

In a magnetic field B, the interaction energy is U = −μ·B = g_s (e/2m_e) S·B. Since the z-component of spin is quantized as m_s = ±ℏ/2, the energy levels split into two: E = ±g_s (eℏ/2m_e) B/2 = ±μ_B g_s B/2, where μ_B = eℏ/2m_e is the **Bohr magneton** (≈ 9.27 × 10⁻²⁴ J/T). This splitting is the magnetic energy scale for electrons in atoms. The Stern-Gerlach experiment demonstrated exactly this splitting: silver atoms passed through an inhomogeneous magnetic field split into two beams, corresponding to m_s = +1/2 and m_s = −1/2.

Why does spin have g_s ≈ 2 and not 1, like orbital angular momentum? The short answer is that spin is an intrinsic property of the relativistic electron — it emerges naturally from Dirac's relativistic wave equation as a consequence of special relativity combined with quantum mechanics. There is no classical model: attempts to picture the electron as a spinning charged sphere fail because the equatorial velocity would exceed c for any reasonable electron radius. Spin is genuinely quantum mechanical with no classical analog. This is why the language is "intrinsic angular momentum" — it's a property the electron carries independent of any spatial motion, as fundamental to what an electron is as its charge or mass.
