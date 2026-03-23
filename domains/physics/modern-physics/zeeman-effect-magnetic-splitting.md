---
id: zeeman-effect-magnetic-splitting
title: 'Zeeman Effect: Magnetic Field Splitting of Energy Levels'
domain: physics
course: modern-physics
prerequisites:
- id: electron-spin-magnetic-moment
  type: hard
- id: orbital-angular-momentum-quantum
  type: soft
builds-toward:
- fine-structure-atomic-splitting
tags:
- magnetic-field
- energy-levels
- atomic-physics
stage: advanced
status: validated
---

# Zeeman Effect: Magnetic Field Splitting of Energy Levels

## Core Idea
In an external magnetic field B, the energy shifts by ΔE = μ_z B = −g(e/2m_e)m B where m is m_ℓ or m_s (or a combination in fine structure). This causes level splitting: a state with angular momentum quantum number j splits into 2j+1 sublevels corresponding to different m_j values. The Zeeman effect is a direct manifestation of space quantization.

## How It's Best Learned
Calculate the Zeeman splitting for hydrogen 1s and 2p states in a known magnetic field. Measure the Zeeman shift spectroscopically. Compare normal Zeeman effect (scalar) with anomalous Zeeman effect (where g ≠ 1).

## Common Misconceptions
All 2j+1 sublevels are equally spaced in magnetic field (linear Zeeman effect). The energy shift is proportional to B, not B². In the anomalous Zeeman effect, the apparent 'magnetic mass' is not actually changed by the field.

## Questions

```yaml
- question: "An atomic state has total angular momentum quantum number j = 3/2. How many distinct energy sublevels does it split into when placed in an external magnetic field?"
  type: multiple-choice
  options:
    - "3 sublevels, one for each spatial dimension"
    - "4 sublevels, corresponding to m_j = −3/2, −1/2, +1/2, +3/2"
    - "6 sublevels, equal to twice the value of j"
    - "2 sublevels, corresponding to spin-up and spin-down only"
  answer: 1
  explanation: "A state with total angular momentum quantum number j splits into 2j+1 sublevels in a magnetic field, corresponding to the allowed values of m_j: −j, −j+1, …, +j. For j = 3/2, this gives 2(3/2)+1 = 4 sublevels. Option D (just spin up/down) confuses j with spin quantum number s = 1/2. The 2j+1 formula directly reflects space quantization — the angular momentum can only point in 2j+1 discrete directions relative to the field axis."

- question: "A spectroscopist observes a spectral line splitting into more than three components in a magnetic field. The atom has nonzero electron spin. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The field is strong enough that the energy shifts become proportional to B², adding extra sublevels"
    - "The anomalous Zeeman effect — nonzero spin means the Landé g-factor differs from 1, causing different levels in the multiplet to shift by different amounts"
    - "The photon carries spin-1, which contributes additional magnetic quantum numbers to the splitting"
    - "More than three components indicate an experimental error, since selection rules always limit splitting to three lines"
  answer: 1
  explanation: "When electron spin is nonzero, orbital and spin angular momenta couple into total angular momentum J, with an effective magnetic moment governed by the Landé g-factor g_J = 1 + [J(J+1)+S(S+1)−L(L+1)]/[2J(J+1)]. Because g_J ≠ 1, different levels shift by different amounts, producing complex patterns — the 'anomalous' Zeeman effect. The normal effect (three lines) applies only when S=0 and g=1. A strong-field quadratic shift (option A) is a separate phenomenon (Paschen-Back limit) not expected at moderate fields."

- question: "In the normal Zeeman effect, a single spectral line splits into exactly three lines due to the selection rule Δm_ℓ = 0, ±1."
  type: true-false
  answer: true
  explanation: "In the normal Zeeman effect (S=0, so g=1), transitions between levels with Δm_ℓ = 0, +1, and −1 each produce a distinct photon frequency shifted by ±μ_B·B from the original line or unchanged. The three groups of transitions all merge into just three lines regardless of the ℓ values involved — a striking simplicity that historically made the normal effect easier to interpret than the anomalous case."

- question: "The energy shift of an atomic sublevel in the Zeeman effect is proportional to the square of the external magnetic field strength."
  type: true-false
  answer: false
  explanation: "The Zeeman energy shift is ΔE = g_J m_J μ_B B — linear in B, not B². This is the linear (or first-order) Zeeman effect. A quadratic dependence on B arises only in the quadratic Zeeman effect, which is a much smaller second-order correction relevant in extremely strong fields or for very weakly bound states. The linear dependence is what makes Zeeman splitting so useful for measuring magnetic fields: the splitting directly and simply encodes field strength."

- question: "Why does the anomalous Zeeman effect produce more complex splitting patterns than the normal Zeeman effect? What role does the Landé g-factor play?"
  type: short-answer
  answer: "In the anomalous Zeeman effect, orbital and spin angular momenta combine into total angular momentum J, and the electron's spin magnetic moment has g_s ≈ 2 rather than 1. This means the effective magnetic moment is not simply proportional to the angular momentum magnitude. The Landé g-factor g_J accounts for the mixture of orbital and spin contributions; it differs between different J levels of a multiplet. Because different levels shift by different amounts (g_J varies), the resulting spectral pattern is more complex than the simple three-line pattern of the normal effect."
  explanation: "In the normal Zeeman effect (S=0), g=1 for all levels, so the energy spacing between sublevels is the same in upper and lower states, and transitions neatly produce three lines. In the anomalous case, g_J depends on the specific values of L, S, and J for each level. Upper and lower states have different g_J values, so their sublevel spacings differ. Transitions between all pairs of m_J values that satisfy selection rules then produce a forest of lines at different frequencies, which was historically called 'anomalous' because it defied classical explanation — until electron spin and its g ≈ 2 were understood."
```

## Explainer

You already know that the electron carries a magnetic moment — both from its orbital motion and from its intrinsic spin. A magnetic dipole placed in an external field has energy U = −**μ** · **B**. Since the electron's magnetic moment is proportional to its angular momentum, and angular momentum is quantized, the energy shift in a magnetic field must also be quantized. That is the Zeeman effect in one sentence: a magnetic field turns a single energy level into a ladder of equally spaced sublevels.

For a pure orbital state (spin neglected), the energy shift is **ΔE = m_ℓ μ_B B**, where μ_B = eℏ/2m_e is the **Bohr magneton** and m_ℓ runs from −ℓ to +ℓ. A state with angular momentum quantum number ℓ splits into 2ℓ + 1 equally spaced sublevels. This is the **normal Zeeman effect** — it occurs cleanly for states with zero total spin (S = 0), which happens in two-electron systems where spins pair up. Spectroscopically, you see a single spectral line split into three lines (the Δm_ℓ = 0, ±1 selection rules). The splitting is directly proportional to B, making Zeeman splitting a powerful tool for measuring magnetic field strengths in laboratory and astronomical contexts.

When spin is present, the situation becomes the **anomalous Zeeman effect**, and the pattern is more complex. The issue is that the electron's spin magnetic moment has g_s ≈ 2, not g_s = 1 like the orbital contribution. When orbital and spin angular momenta are coupled into total angular momentum **J**, the effective magnetic moment is neither the purely orbital nor purely spin value — it is set by the **Landé g-factor**, g_J = 1 + [J(J+1) + S(S+1) − L(L+1)] / [2J(J+1)]. The energy shift is then ΔE = g_J m_J μ_B B, where m_J runs from −J to +J. Because g_J differs from 1, different levels within a multiplet shift by different amounts, producing the "anomalous" — meaning non-trivial — splitting pattern that historically caused great confusion until electron spin was properly understood.

The Zeeman effect is a direct experimental demonstration of **space quantization** — the idea that angular momentum can only point in discrete directions relative to an external field axis, not continuously as classical physics would predict. Before the full quantum theory was developed, this splitting was one of the clearest indicators that something fundamentally non-classical was happening in atoms. Today it is used in MRI machines (nuclear Zeeman effect in nuclei), in laser cooling of atoms (exploiting level shifts to create position-dependent forces), and in astrophysics to measure stellar magnetic fields from spectral line splitting observed in light from distant stars.
