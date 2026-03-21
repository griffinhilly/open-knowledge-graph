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

## Questions

```yaml
- question: "An electron has spin quantum number s = ½. What is the magnitude of its spin angular momentum vector?"
  type: multiple-choice
  options:
    - "ℏ/2, since the spin quantum number directly gives the angular momentum in units of ℏ"
    - "ℏ√(3)/2, since the magnitude is ℏ√(s(s+1)) = ℏ√(3/4)"
    - "ℏ, since the two projections +½ and −½ together account for a total angular momentum of 1"
    - "Zero, since spin has no spatial extent and therefore no angular momentum"
  answer: 1
  explanation: "The magnitude of any quantum angular momentum is ℏ√(j(j+1)), not ℏj. For s = ½, this gives ℏ√(½ · 3/2) = ℏ√(3)/2. The value ±ℏ/2 is only the z-component (projection) of the spin vector — what you measure along a chosen axis. The spin vector is never fully aligned with any axis; its total magnitude ℏ√(3)/2 is always larger than either projection ±ℏ/2. Confusing the projection with the magnitude is the most common error in this topic."

- question: "In the Stern–Gerlach experiment, a beam of silver atoms splits into exactly two spots in an inhomogeneous magnetic field. Why does this result require a half-integer angular momentum quantum number?"
  type: multiple-choice
  options:
    - "Half-integer quantum numbers only apply to intrinsic properties, while integer values apply to orbital motion"
    - "An angular momentum quantum number l produces 2l+1 projection values; to get exactly 2 projections requires l = ½"
    - "The magnetic field was too weak to split a beam into more than two parts, regardless of the quantum number"
    - "Silver atoms are electrically neutral, and neutral particles can only have two spin states"
  answer: 1
  explanation: "For orbital angular momentum with integer l, the number of allowed m projections is 2l+1: l=0 gives 1, l=1 gives 3, l=2 gives 5, and so on — always an odd number. There is no integer l that gives exactly 2. To produce exactly two projection values, you need 2s+1 = 2, which requires s = ½. This is precisely why the Stern–Gerlach result was inexplicable with existing orbital quantum numbers and required the postulate of a new half-integer quantum number — spin."

- question: "Electron spin can be understood physically as the electron rotating about its own axis, analogous to Earth spinning on its axis."
  type: true-false
  answer: false
  explanation: "This classical picture leads to irreconcilable contradictions. If you try to model spin as a literal rotation of a charged sphere, you can calculate the surface velocity needed to produce the observed magnetic moment — it exceeds the speed of light. Furthermore, the electron has no known spatial extent at the scale relevant to spin. Spin is a purely quantum mechanical, relativistic property with no classical analog; it emerges from the Dirac equation as an intrinsic feature of relativistic quantum fields. The word 'spin' is historical, not descriptive of physical rotation."

- question: "Two electrons can occupy the same orbital (same n, l, m_l quantum numbers) provided they have opposite spin projections (m_s = +½ and m_s = −½)."
  type: true-false
  answer: true
  explanation: "The Pauli exclusion principle forbids two electrons from sharing all four quantum numbers. If two electrons share n, l, and m_l (same orbital), they must differ in m_s. Since m_s can only be +½ or −½, an orbital can hold at most two electrons — one spin-up and one spin-down. This is why spin is called the 'fourth quantum number' and why the electron's two-valued spin directly determines the shell-filling structure of the periodic table."

- question: "Why can't electron spin be explained as a classical rotation, and what does 'spin ½' actually mean mathematically?"
  type: short-answer
  answer: "Treating spin as literal rotation fails because the required surface velocity would exceed the speed of light, and the electron has no measurable spatial extent at the relevant scale — there is no surface to rotate. 'Spin ½' means the quantum number s = ½ is a fixed intrinsic property of all electrons. It determines the magnitude of the spin angular momentum vector, ℏ√(s(s+1)) = ℏ√(3)/2, and restricts the allowed projections onto any measurement axis to exactly two eigenvalues: m_s = +½ or m_s = −½, corresponding to +ℏ/2 and −ℏ/2 respectively. These are eigenvalues of the spin projection operator, not descriptions of physical rotation."
  explanation: "The key distinction is between the quantum number s (which sets the magnitude of the spin vector) and the projection m_s (which is what any single measurement along a chosen axis will yield). The full spin vector has magnitude ℏ√(3)/2 and points in some direction in 'spin space,' but when you measure its component along any axis, you always get one of the two eigenvalues ±ℏ/2 — never any intermediate value. This two-state discreteness is the hallmark of a spin-½ particle."
```

## Explainer

You already know that electrons in an atom are described by quantum numbers n, l, and m_l — the principal, angular momentum, and magnetic quantum numbers. These three numbers completely specify the orbital state of an electron. Yet when Stern and Gerlach fired a beam of silver atoms through an inhomogeneous magnetic field in 1922, they found the beam split into exactly two spots, not three or five or some other integer-spaced set. This is the problem spin solves: no integer value of l could produce a two-way split. To get two and only two projection values, you need m_s = +½ and m_s = −½, which requires a new quantum number s = ½.

**Spin** is an intrinsic angular momentum — it is not the electron rotating about its own axis, and no classical picture can save you here. If you tried to model spin as literal rotation, you would need the electron's surface to move faster than light, which is impossible. Instead, spin is a fundamental property that emerges naturally from combining quantum mechanics with special relativity (from the Dirac equation), but in non-relativistic QM it is simply introduced as a postulate: every electron carries spin-½, always. The **spin quantum number** s = ½ is fixed for all electrons; what varies is the **spin projection** m_s, which can be +½ (spin-up, written |↑⟩) or −½ (spin-down, written |↓⟩).

The magnitude of the spin angular momentum vector is not ℏ/2 — a common confusion. It is ℏ√(s(s+1)) = ℏ√(3)/2. The value ±ℏ/2 is only the z-component, the projection along whatever axis you measure. This distinction matters: the spin vector is never fully aligned with the measurement axis, just as the orbital angular momentum vector in atomic physics has magnitude ℏ√(l(l+1)) while its z-component is m_l·ℏ. Spin is a vector in a two-dimensional internal space — a **spinor** — and superpositions like α|↑⟩ + β|↓⟩ are perfectly valid quantum states.

Because spin is a form of angular momentum, it comes with a **magnetic moment**: μ = −g_s(eℏ/2m_e)S, where g_s ≈ 2 is the electron's spin g-factor. This is why spin-up and spin-down states have different energies in a magnetic field (the **Zeeman effect**). It is also why spin is the direct input into the next topic: the Pauli exclusion principle. No two electrons in an atom can share all four quantum numbers n, l, m_l, m_s. Spin provides the fourth quantum number that allows two electrons — one spin-up and one spin-down — to coexist in the same orbital.
