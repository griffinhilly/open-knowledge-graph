---
id: spin-quantum-number
title: Electron Spin
domain: physics
course: modern-physics
prerequisites:
- id: quantum-numbers
  type: hard
builds-toward:
- pauli-exclusion-principle
tags:
- quantum
- spin
- stern-gerlach
- angular-momentum
- fermion
stage: advanced
status: validated
---

# Electron Spin

## Core Idea
Electrons possess an intrinsic angular momentum called spin with quantum number s = ½, taking projection values m_s = +½ ('spin-up') or m_s = −½ ('spin-down'). Spin has no classical analog — it is not the electron literally spinning — but it gives rise to a magnetic moment and is revealed by the Stern–Gerlach experiment, where a beam of silver atoms splits into two discrete spots in an inhomogeneous magnetic field. Spin is a relativistic quantum effect; its full explanation comes from the Dirac equation, but it can be treated as a postulate in non-relativistic quantum mechanics.

## How It's Best Learned
Start with the Stern–Gerlach experiment: show that the two-valued outcome cannot be explained by any integer angular momentum quantum number and requires a half-integer value. Introduce spin-up and spin-down as a two-state system.

## Common Misconceptions
- Spin is the electron rotating about its own axis — the electron has no spatial extent at the level of spin; this classical picture leads to contradictions.
- Spin ½ means half a rotation — spin quantum number ½ means the spin angular momentum magnitude is ℏ√(3)/2; it describes the projection values ±ℏ/2.

## Explainer

You already know that electrons in an atom are described by quantum numbers n, l, and m_l — the principal, angular momentum, and magnetic quantum numbers. These three numbers completely specify the orbital state of an electron. Yet when Stern and Gerlach fired a beam of silver atoms through an inhomogeneous magnetic field in 1922, they found the beam split into exactly two spots, not three or five or some other integer-spaced set. This is the problem spin solves: no integer value of l could produce a two-way split. To get two and only two projection values, you need m_s = +½ and m_s = −½, which requires a new quantum number s = ½.

**Spin** is an intrinsic angular momentum — it is not the electron rotating about its own axis, and no classical picture can save you here. If you tried to model spin as literal rotation, you would need the electron's surface to move faster than light, which is impossible. Instead, spin is a fundamental property that emerges naturally from combining quantum mechanics with special relativity (from the Dirac equation), but in non-relativistic QM it is simply introduced as a postulate: every electron carries spin-½, always. The **spin quantum number** s = ½ is fixed for all electrons; what varies is the **spin projection** m_s, which can be +½ (spin-up, written |↑⟩) or −½ (spin-down, written |↓⟩).

The magnitude of the spin angular momentum vector is not ℏ/2 — a common confusion. It is ℏ√(s(s+1)) = ℏ√(3)/2. The value ±ℏ/2 is only the z-component, the projection along whatever axis you measure. This distinction matters: the spin vector is never fully aligned with the measurement axis, just as the orbital angular momentum vector in atomic physics has magnitude ℏ√(l(l+1)) while its z-component is m_l·ℏ. Spin is a vector in a two-dimensional internal space — a **spinor** — and superpositions like α|↑⟩ + β|↓⟩ are perfectly valid quantum states.

Because spin is a form of angular momentum, it comes with a **magnetic moment**: μ = −g_s(eℏ/2m_e)S, where g_s ≈ 2 is the electron's spin g-factor. This is why spin-up and spin-down states have different energies in a magnetic field (the **Zeeman effect**). It is also why spin is the direct input into the next topic: the Pauli exclusion principle. No two electrons in an atom can share all four quantum numbers n, l, m_l, m_s. Spin provides the fourth quantum number that allows two electrons — one spin-up and one spin-down — to coexist in the same orbital.
