---
id: radioactive-decay
title: Radioactive Decay
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-structure
  type: hard
- id: differential-equations-intro-separable
  type: soft
- id: quantum-tunneling
  type: soft
builds-toward:
- half-life-decay-law
- nuclear-fission-fusion
tags:
- nuclear
- radioactivity
- alpha
- beta
- gamma
- decay
stage: advanced
status: validated
---
# Radioactive Decay

## Core Idea
Unstable nuclei spontaneously transform to lower-energy configurations through radioactive decay. Alpha decay emits a helium-4 nucleus (2 protons + 2 neutrons), reducing mass number by 4 and atomic number by 2; it occurs in heavy nuclei and proceeds via quantum tunneling through the Coulomb barrier. Beta-minus decay converts a neutron to a proton with emission of an electron and antineutrino; beta-plus decay converts a proton to a neutron with emission of a positron and neutrino. Gamma decay releases excess nuclear energy as a high-energy photon with no change in nucleon number. Each decay mode conserves charge, lepton number, and mass-energy.

## How It's Best Learned
Write out balanced decay equations for representative nuclides (Ra-226, C-14, Co-60). Verify conservation laws. Distinguish the penetrating power of each radiation type (alpha: blocked by paper; beta: by aluminum; gamma: requires lead/concrete).

## Common Misconceptions
- Beta decay is the nucleus emitting an electron that was inside it — the electron is created at the moment of decay when a neutron transforms; there are no electrons inside the nucleus.
- Gamma decay changes the nucleus — gamma decay only releases energy from an excited nuclear state; the composition is unchanged.

## Questions

```yaml
- question: "Uranium-238 undergoes alpha decay. What are the mass number and atomic number of the daughter nucleus?"
  type: multiple-choice
  options: ["Mass 234, atomic 90", "Mass 236, atomic 92", "Mass 238, atomic 90", "Mass 234, atomic 92"]
  answer: 0
  explanation: "Alpha decay emits a helium-4 nucleus (mass number 4, atomic number 2). So the daughter has mass number 238 − 4 = 234 and atomic number 92 − 2 = 90, which is thorium-234. This is a direct application of conservation of mass number and charge."

- question: "In beta-minus decay, the electron emitted comes from the innermost electron shell of the atom, which is disrupted by the nuclear instability."
  type: true-false
  answer: false
  explanation: "The electron in beta-minus decay is created at the instant of decay when a neutron converts to a proton. There are no electrons inside the nucleus — they cannot exist there. The emitted electron (and antineutrino) are newly created particles, not pre-existing ones that were stored in the nucleus or electron shells."

- question: "A nucleus undergoes gamma decay. How do its atomic number and mass number change, and why?"
  type: short-answer
  answer: "Neither changes. Gamma decay releases energy as a high-energy photon from an excited nuclear state but does not change the number of protons or neutrons."
  explanation: "Gamma emission is purely an energy transition — like an atom emitting light when an electron drops to a lower shell, except it happens at the nuclear level. No particles are added or removed, so both the proton count (atomic number) and nucleon count (mass number) remain the same. The element and isotope are unchanged."
```

## Explainer

You know from nuclear structure that a nucleus is held together by the strong nuclear force competing against electromagnetic repulsion between protons. Not all combinations of protons and neutrons form stable nuclei — those that are too heavy, too neutron-rich, or too proton-rich will spontaneously reorganize to reach a lower-energy state. This spontaneous reorganization is radioactive decay.

There are three main decay modes, each addressing a different kind of nuclear instability. **Alpha decay** occurs in very heavy nuclei (typically Z > 82) where the nucleus is simply too large for the strong force to hold together stably. It ejects a helium-4 nucleus (two protons, two neutrons), reducing the mass number by 4 and atomic number by 2. Crucially, the alpha particle can only escape by *tunneling* through the Coulomb energy barrier — it does not have enough energy to classically surmount the barrier, but quantum mechanics allows a finite probability of it appearing on the other side. This is quantum tunneling applied directly.

**Beta decay** addresses a wrong ratio of neutrons to protons. In beta-minus decay, a neutron converts to a proton via the weak nuclear force, emitting an electron and an antineutrino. In beta-plus decay, a proton converts to a neutron, emitting a positron and a neutrino. A common misconception is that the electron was somehow stored in the nucleus — it was not. The electron is created from the energy released by the mass difference between the original neutron and the resulting proton plus electron. Conservation of lepton number requires the antineutrino to accompany the electron.

**Gamma decay** is different in character: no particles are emitted, only a high-energy photon. After alpha or beta decay, the daughter nucleus often remains in an excited energy state. It sheds this excess energy as a gamma ray, transitioning to its ground state. Nothing about the nuclear composition changes — the atomic number and mass number are the same before and after.

All three modes obey strict conservation laws: charge, mass-energy, lepton number, and baryon number are all conserved in every decay. Writing balanced decay equations — verifying that the numbers on both sides match — is the most reliable way to check your understanding of each mode.
