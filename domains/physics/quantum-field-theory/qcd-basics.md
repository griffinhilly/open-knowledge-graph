---
id: qcd-basics
title: Quantum Chromodynamics (QCD) Basics
domain: physics
course: quantum-field-theory
prerequisites:
- id: non-abelian-gauge-theories
  type: hard
- id: dirac-field-quantization
  type: hard
tags:
- qcd
- color-charge
- quarks
- gluons
stage: expert
status: validated
---

# Quantum Chromodynamics (QCD) Basics

## Core Idea
QCD is the SU(3) gauge theory of the strong interaction. Quarks carry color charge (red, green, blue) and interact via eight massless gluons that themselves carry color. The QCD Lagrangian is structurally similar to QED but with three colors, eight gluons, and gluon self-interactions that produce qualitatively different physics.

## Questions

```yaml
- question: "Quarks come in three colors (red, green, blue) and interact via gluons. Gluons carry one unit of color and one unit of anti-color. Why are there 8 gluons rather than 9 (3 colors times 3 anti-colors)?"
  type: multiple-choice
  options:
    - "One of the nine combinations is unphysical due to negative norm"
    - "The color-singlet combination (r r-bar + g g-bar + b b-bar)/sqrt(3) does not couple to color charge and must be excluded — it would mediate a long-range color force, which is not observed"
    - "Three of the nine combinations are redundant due to symmetry"
    - "The ninth gluon has been observed but is too heavy to be relevant"
  answer: 1
  explanation: "The nine combinations of color-anticolor decompose under SU(3) as 3 x 3-bar = 8 + 1: an octet and a singlet. The octet states are the eight gluons — they carry net color charge and couple to quarks. The singlet (r r-bar + g g-bar + b b-bar)/sqrt(3) is color-neutral and would not be confined; if it existed as a physical gluon, it would mediate a long-range force between all hadrons. The absence of such a force is evidence that the gauge group is SU(3) (which has 8 generators) rather than U(3) (which has 9). The mathematical reason is that SU(3) is the group of 3x3 unitary matrices with determinant 1, excluding the U(1) phase."

- question: "The QCD coupling constant alpha_s is approximately 0.12 at the Z boson mass (91 GeV). At the scale of a proton (approximately 1 GeV), alpha_s is approximately 0.5. Why does this large coupling make proton structure calculations fundamentally different from QED calculations of hydrogen?"
  type: multiple-choice
  options:
    - "Because the proton has three quarks while hydrogen has only one electron"
    - "Because alpha_s ~ 0.5 means the perturbative expansion in powers of alpha_s converges slowly or not at all — each higher-order correction is comparable to the previous one, so Feynman diagram perturbation theory is unreliable for low-energy QCD"
    - "Because quarks are heavier than electrons"
    - "Because gluons are massless like photons, so the calculations are equivalent"
  answer: 1
  explanation: "In QED, alpha ~ 1/137, so each loop adds a correction of order 1% — perturbation theory converges rapidly. In QCD at GeV scales, alpha_s ~ 0.5, so a one-loop correction is 50% of the tree level, a two-loop correction is 25%, etc. — the series does not converge reliably. This is why non-perturbative methods (lattice QCD, sum rules, chiral perturbation theory) are needed for hadron physics. At high energies (asymptotic freedom regime), alpha_s is small enough for perturbative QCD to work, which is why jet cross sections and deep inelastic scattering are calculable."

- question: "QCD is an exact copy of QED with the replacement U(1) -> SU(3), and all differences between electromagnetism and the strong force follow from this single change."
  type: true-false
  answer: true
  explanation: "This is correct at the level of the Lagrangian structure. QCD's Lagrangian is L = sum_f q-bar_f(i gamma^mu D_mu - m_f)q_f - (1/4)G^a_{mu nu}G^{a mu nu}, where D_mu = partial_mu - ig_s T^a A^a_mu is the covariant derivative with SU(3) generators T^a, and G^a_{mu nu} is the non-abelian field strength tensor. Replacing SU(3) -> U(1), T^a -> 1, and g_s -> e gives QED. All the differences — gluon self-interactions, asymptotic freedom, confinement, color neutrality of hadrons — follow from the non-abelian structure of SU(3) versus the abelian structure of U(1). The gauge principle and minimal coupling are identical."

- question: "Explain what color confinement means physically and why it makes free quarks unobservable, despite quarks being confirmed as real constituents of protons and neutrons."
  type: short-answer
  answer: "Color confinement means that all observable particles must be color-neutral (color singlets). No free quark (which carries color charge) has ever been observed. When you try to separate two quarks, the energy stored in the color flux tube between them grows linearly with distance (unlike the Coulomb potential which falls off). At some point, the energy is sufficient to create a new quark-antiquark pair from the vacuum, producing two color-neutral hadrons rather than two free quarks. Quarks are real (they explain deep inelastic scattering, jet production, and the hadron spectrum) but are always confined inside hadrons — mesons (quark-antiquark) or baryons (three quarks). Confinement is a non-perturbative phenomenon that cannot be derived from Feynman diagrams."
  explanation: "Proving confinement rigorously from the QCD Lagrangian is one of the seven Millennium Prize Problems. Lattice QCD simulations confirm it numerically, and the linear potential has been verified, but an analytical proof remains elusive."
```

## Explainer

**Quantum chromodynamics** is the theory of the strong interaction, built as an SU(3) Yang-Mills gauge theory. Quarks come in six flavors (up, down, strange, charm, bottom, top) and three **colors** (red, green, blue). Color is the charge of the strong force, analogous to electric charge in QED. The gauge bosons are eight **gluons**, each carrying one unit of color and one unit of anti-color. The QCD Lagrangian couples quarks to gluons through the covariant derivative, just as QED couples electrons to photons, but with SU(3) replacing U(1).

The crucial structural difference from QED is the **self-interaction of gluons**. Because gluons carry color charge, they interact with each other through three-gluon and four-gluon vertices. This has no analog in QED (photons are electrically neutral). The self-interaction makes QCD enormously richer: it produces asymptotic freedom (the coupling weakens at short distances), confinement (quarks cannot be isolated), and a complex vacuum structure. The gluon field contributes most of the proton mass (the quark masses account for only about 1% of the proton mass; the rest is gluon field energy and quark kinetic energy).

At high energies, **asymptotic freedom** means the strong coupling alpha_s is small and perturbative calculations are reliable. This regime is probed by deep inelastic scattering, jet production in collider experiments, and heavy quarkonium systems. The predictions of perturbative QCD — scaling violations in structure functions, the three-jet cross section at electron-positron colliders, the running of alpha_s — have been verified with percent-level precision.

At low energies (below about 1 GeV), alpha_s becomes large and **confinement** takes over. Quarks and gluons are permanently bound into color-neutral hadrons: mesons (quark-antiquark pairs) and baryons (three quarks). The mechanism of confinement is not fully understood analytically but has been confirmed by lattice QCD simulations, which show that the potential energy between a quark-antiquark pair grows linearly with separation. The transition from the perturbative to the non-perturbative regime — from quarks and gluons to protons and pions — is one of the central challenges of theoretical physics.
