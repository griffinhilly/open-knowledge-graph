---
id: periodic-trends
title: Periodic Trends
domain: chemistry
course: general-chemistry
prerequisites:
- id: electron-configuration
  type: hard
- id: periodic-table-overview
  type: hard
builds-toward:
- ionic-bonding
- covalent-bonding
- metallic-bonding
- molecular-polarity
tags:
- electronegativity
- ionization-energy
- atomic-radius
- electron-affinity
- effective-nuclear-charge
stage: advanced
status: validated
---

# Periodic Trends

## Core Idea
Several properties of elements vary predictably across the periodic table due to changes in effective nuclear charge (Zeff) and electron shielding. Atomic radius decreases across a period (increasing nuclear charge pulls electrons inward) and increases down a group (additional electron shells). Ionization energy and electronegativity increase across periods and decrease down groups for the same reasons. These trends emerge from the competition between nuclear charge attracting electrons and inner-shell electrons shielding outer electrons from that attraction.

## How It's Best Learned
Learn the trends by understanding their physical cause rather than memorizing them. Compare pairs of elements: why is fluorine more electronegative than oxygen? Why is cesium larger than lithium? Use Zeff as the unifying explanation for multiple trends.

## Common Misconceptions
- Electron affinity is not the same as electronegativity: electron affinity is a measured energy for adding an electron to a gaseous atom, while electronegativity is a relative scale for bond polarity.
- Ionic radius does not follow the same trend as atomic radius: cations are smaller and anions are larger than their neutral parent atoms.

## Questions

```yaml
- question: "Moving from sodium (Na) to chlorine (Cl) across period 3 of the periodic table, what happens to atomic radius?"
  type: multiple-choice
  options: ["Increases steadily because more electrons are added", "Decreases steadily because nuclear charge increases faster than shielding", "Stays roughly constant because each new electron cancels the new proton", "First decreases then increases due to d-orbital effects"]
  answer: 1
  explanation: "Across a period, protons are added to the nucleus one at a time, but the new electrons go into the same principal energy level (same shell) and provide only weak shielding of each other. The effective nuclear charge (Zeff) therefore increases across the period, pulling all electrons inward and shrinking the atomic radius. This is why Cl (atomic radius ~99 pm) is much smaller than Na (~186 pm) despite having more electrons."

- question: "Electronegativity and electron affinity measure the same property of an atom."
  type: true-false
  answer: false
  explanation: "They are related but distinct. Electron affinity is a measured thermodynamic quantity: the energy change when a gaseous atom gains one electron (in kJ/mol). Electronegativity is a dimensionless relative scale (like the Pauling scale) describing an atom's tendency to attract electron density within a covalent bond. An atom can have a high electron affinity but electronegativity is defined only in a bonding context, and the two scales are not numerically equivalent."

- question: "Explain why atomic radius increases going down a group in the periodic table, using effective nuclear charge and electron shielding."
  type: short-answer
  answer: "Each successive element in a group adds a new electron shell. The inner shells (core electrons) shield the outer electrons from the nucleus very effectively, so the effective nuclear charge felt by the outermost electrons stays roughly constant down the group. With each new shell farther from the nucleus, the valence electrons are simply further away, making the atom larger."
  explanation: "The key is that inner shells shield very well — each core electron roughly cancels one unit of nuclear charge for the valence electrons. So even though the nucleus gains more protons going down a group, the valence electrons see approximately the same Zeff (roughly +1 for alkali metals, for example). The dominant effect is that valence electrons occupy higher and higher principal quantum number shells (n=2, 3, 4...), which are intrinsically larger orbitals farther from the nucleus."
```

## Explainer

Periodic trends are not a list of facts to memorize — they are consequences of one underlying physics principle: effective nuclear charge. As you build up the periodic table by adding protons and electrons, the outermost (valence) electrons experience a tug-of-war between the full nuclear charge pulling them in and the inner (core) electrons partially shielding them from that attraction. The net charge felt by the valence electrons is the effective nuclear charge, Zeff ≈ Z − shielding. Every major periodic trend flows from how Zeff changes across periods and down groups.

Across a period (left to right), you add one proton and one electron at a time, but the new electron enters the same principal energy level — the same shell — as the previous electrons. Electrons in the same shell shield each other poorly (roughly 35% as effectively as inner-shell electrons). So Zeff increases steadily across a period, pulling all electrons inward. This causes atomic radius to decrease, ionization energy to increase (harder to remove an electron being pulled more strongly), and electronegativity to increase (the atom pulls shared electrons more forcefully). Fluorine, at the far right of period 2, is simultaneously the smallest, hardest to ionize (relatively, among nonmetals), and most electronegative element.

Down a group, you add a new electron shell with each element. The new core electrons shield the valence electrons very effectively — essentially canceling the additional nuclear charge almost one-for-one. So Zeff stays roughly constant down a group, while the valence electrons occupy shells that are progressively farther from the nucleus (n=2, 3, 4...). The result is the opposite of across a period: atomic radius increases down a group, ionization energy decreases, and electronegativity decreases. Cesium, at the bottom of group 1, is one of the largest and least electronegative elements for exactly this reason.

A useful check: compare fluorine (top-right of the main block, smallest atomic radius, highest electronegativity) with francium (bottom-left, largest atomic radius, lowest electronegativity). These extremes neatly illustrate that the trends are coherent and predictable. For any pair of elements, you can reason about their relative properties from their position in the table without memorization — just ask: who has the higher Zeff?

One distinction to keep clear: electron affinity and electronegativity are related but not the same thing. Electron affinity is the energy released (or absorbed) when a gaseous atom gains one electron in isolation — a measured thermodynamic quantity. Electronegativity is a relative scale describing how strongly an atom pulls electron density toward itself within a covalent bond. Both generally increase across a period and decrease down a group, which is why they are often conflated, but they are conceptually and numerically distinct.
