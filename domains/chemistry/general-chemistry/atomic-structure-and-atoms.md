---
id: atomic-structure-and-atoms
title: 'Atomic Structure: Protons, Neutrons, and Electrons'
domain: chemistry
course: general-chemistry
prerequisites:
- id: matter-classification-and-properties
  type: hard
- id: atomic-structure-basics
  type: soft
- id: bohr-model
  type: soft
builds-toward:
- isotopes-and-atomic-mass
- electron-configuration-principles
tags:
- atomic structure
- subatomic particles
- nuclear structure
stage: formal-systems
status: draft
---

# Atomic Structure: Protons, Neutrons, and Electrons

## Core Idea
Atoms consist of a nucleus containing protons and neutrons, surrounded by electrons in orbitals. Protons are positively charged, neutrons are neutral, and electrons are negatively charged. The identity of an element is determined by the number of protons (atomic number), while the mass is primarily from protons and neutrons.

## How It's Best Learned
Use Rutherford's scattering experiment to motivate the nuclear model. Build physical models of atoms. Draw Bohr models initially, then transition to orbital representations.

## Common Misconceptions
- Thinking electrons orbit the nucleus like planets (they exist as probability clouds). 
- Confusing atomic number with mass number.

## Questions

```yaml
- question: "An atom has 6 protons, 6 neutrons, and 6 electrons. Another atom has 6 protons, 8 neutrons, and 6 electrons. What is the relationship between these two atoms?"
  type: multiple-choice
  options: ["They are different elements", "They are ions of the same element", "They are isotopes of the same element", "They are identical atoms"]
  answer: 2
  explanation: "Both atoms have 6 protons, so they are both carbon (the atomic number defines the element). They differ in neutron count (6 vs. 8), which changes the mass number but not the element's identity. Atoms of the same element with different numbers of neutrons are called isotopes. They are not ions because the electron count equals the proton count in both cases."

- question: "Electrons travel around the nucleus in fixed circular orbits, like planets orbiting the sun."
  type: true-false
  answer: false
  explanation: "This is the Bohr model, which is a useful first approximation but physically incorrect. Quantum mechanics shows that electrons occupy orbitals — regions of space described by wave functions where an electron has a certain probability of being found. Electrons do not have well-defined trajectories; their positions are fundamentally probabilistic until measured."

- question: "What is the difference between atomic number and mass number, and which one determines an element's chemical identity?"
  type: short-answer
  answer: "Atomic number is the number of protons in the nucleus; mass number is the total number of protons plus neutrons. Atomic number determines chemical identity."
  explanation: "Because electrons in chemical bonding are determined by the number of protons (through charge balance), the atomic number dictates how an atom bonds and which element it is. Mass number varies among isotopes of the same element without changing chemical behavior. For example, carbon-12 and carbon-14 both have atomic number 6 and behave chemically the same way, but have mass numbers 12 and 14 respectively."
```

## Explainer

If you have studied matter classification, you know that elements are pure substances that cannot be broken down further by chemical means. But what makes one element different from another at the subatomic level? The answer lies in the structure of the atom — specifically, in the number of protons.

Every atom contains a **nucleus** — a tiny, dense core — surrounded by a diffuse cloud of electrons. The nucleus holds **protons** (positively charged) and **neutrons** (electrically neutral). **Electrons** (negatively charged) occupy the space around the nucleus. In a neutral atom, the number of electrons equals the number of protons, so the atom carries no net charge. The **atomic number (Z)** is the count of protons, and it completely defines which element you have: 1 proton = hydrogen, 6 protons = carbon, 79 protons = gold, no exceptions. If you change the proton count, you have a different element.

The **mass number (A)** counts the total number of protons plus neutrons. Since protons and neutrons each have roughly 1 atomic mass unit (amu) and electrons contribute almost nothing to mass, the mass number is a good approximation of atomic mass. The number of neutrons in an atom can vary without changing its element — atoms of the same element with different neutron counts are called **isotopes**. Carbon-12 has 6 protons and 6 neutrons; carbon-14 has 6 protons and 8 neutrons. Both are chemically carbon, but carbon-14 is radioactive, which is the basis of radiocarbon dating.

A persistent misconception, reinforced by textbook diagrams, is that electrons orbit the nucleus like tiny planets — this is the **Bohr model**, useful for introductory calculations but ultimately wrong. Quantum mechanics tells a different story: electrons exist as **probability distributions**, or orbitals, defined by wave functions. You cannot know simultaneously where an electron is and how fast it is moving (Heisenberg uncertainty principle). When we draw an orbital, we are drawing a region of space within which there is a high probability (typically ~90%) of finding the electron. The electron does not trace a path; it is delocalized.

The three particles differ sharply in mass. Protons and neutrons each weigh approximately 1.67 × 10⁻²⁷ kg. An electron weighs roughly 1/1836 as much — so tiny that electrons contribute essentially nothing to atomic mass, but everything to chemistry, since it is the electrons that participate in bonding, reactions, and energy absorption.
