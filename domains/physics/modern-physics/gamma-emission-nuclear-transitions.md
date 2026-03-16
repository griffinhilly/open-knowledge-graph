---
id: gamma-emission-nuclear-transitions
title: Gamma Radiation and Nuclear Transitions
domain: physics
course: modern-physics
prerequisites:
- id: photon-particle-properties
  type: soft
- id: nuclear-structure
  type: hard
tags:
- nuclear-physics
- radiation
stage: advanced
status: draft
---

# Gamma Radiation and Nuclear Transitions

## Core Idea
Gamma decay (A* → A + γ) occurs when a nucleus transitions from an excited state to a lower energy state, emitting a high-energy photon (gamma ray). Unlike alpha and beta decay, Z and A unchanged. Gamma rays have MeV energies, making them highly penetrating and dangerous. Gamma emission often follows alpha or beta decay, removing excess excitation energy. Selection rules based on angular momentum and parity govern allowed transitions, similar to atomic spectroscopy but at nuclear energy scales.

## Explainer

You know from atomic physics that electrons in atoms occupy discrete energy levels, and when an electron falls from a higher level to a lower one it emits a photon whose energy equals the gap. The nucleus obeys the same quantum mechanical principle. Protons and neutrons inside the nucleus occupy quantized energy levels (shell model states), and a nucleus can exist in **nuclear excited states** — configurations with higher internal energy than the ground state. When the nucleus de-excites, it emits a photon. Because nuclear energy spacings are millions of times larger than atomic ones (MeV versus eV), the emitted photons are gamma rays rather than visible light or UV.

The process notation A* → A + γ encapsulates the key distinction from alpha and beta decay: neither the mass number A nor the atomic number Z changes. The same nucleus — same element, same isotope — simply loses internal energy by emitting a photon. This is why gamma emission almost always accompanies other decay modes: alpha or beta decay typically leaves the daughter nucleus in an excited state, and that excitation is then shed by gamma emission within nanoseconds. The gamma ray carries away both energy and angular momentum, which determines which transitions are allowed.

The **selection rules** for gamma emission arise from conservation of angular momentum and parity. The gamma photon carries angular momentum of at least one unit (photons are spin-1 particles), so the nuclear spin must change by at least ΔJ = 1 for emission to occur — a 0⁺ → 0⁺ transition is forbidden by gamma. The photon's angular momentum quantum number L determines the **multipole order** of the radiation: dipole (L=1), quadrupole (L=2), octupole (L=3), and so on. Electric multipoles (EL) and magnetic multipoles (ML) have opposite parity behaviors. For an EL photon, parity changes by (−1)^L; for ML, by (−1)^(L+1). The transition rate falls rapidly with increasing L — roughly by a factor of 10⁻⁵ per additional unit — so the lowest allowed multipole usually dominates.

Sometimes the selection rules forbid rapid emission, and the nucleus remains stuck in its excited state for much longer than typical (nanoseconds to microseconds or longer). Such long-lived excited states are called **nuclear isomers**, and their decay is called **isomeric transition** (IT). The most famous example is Tc-99m, used in medical imaging: it decays by emitting a 140 keV gamma ray with a 6-hour half-life. An alternative to gamma emission is **internal conversion**, where the excitation energy is transferred directly to an inner shell electron, ejecting it from the atom instead of emitting a photon. This process competes with gamma emission and is favored when the nuclear transition is forbidden by selection rules or when the transition energy is close to an electron binding energy.

## Questions

```yaml
- question: "A nucleus undergoes beta decay to an excited daughter state, then the daughter emits a gamma ray. How many changes in Z and A occur in total?"
  type: short-answer
  answer: "Beta decay changes Z by ±1 (and A stays constant). Gamma emission changes neither Z nor A. Total: Z changes by ±1, A unchanged."
  explanation: "Beta-minus decay converts a neutron to a proton (Z increases by 1), beta-plus converts a proton to neutron (Z decreases by 1), while A = Z + N is unchanged in both. Gamma emission is purely an energy release — no nucleon number or charge changes. The sequence is extremely common in nuclear decay chains: a nucleus beta-decays to an excited daughter, which then gamma-decays to the daughter's ground state."

- question: "Why does a 0⁺ → 0⁺ nuclear transition (both initial and final states have spin 0 and even parity) not proceed by gamma emission?"
  type: short-answer
  answer: "A photon carries at minimum one unit of angular momentum (L ≥ 1). A 0 → 0 transition requires ΔJ = 0, but no photon with angular momentum 0 exists — the electromagnetic field cannot carry zero angular momentum. Therefore single-photon emission is strictly forbidden for 0⁺ → 0⁺ transitions."
  explanation: "This selection rule is absolute, not just a suppression. The transition can still proceed via internal conversion (where the nucleus's energy is transferred to an atomic electron) or by rare two-photon emission, but these are much slower. The 0⁺ → 0⁺ case arises notably in even-even nuclei and is an important test of nuclear structure models."
```
