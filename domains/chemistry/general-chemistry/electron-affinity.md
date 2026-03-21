---
id: electron-affinity
title: Electron Affinity
domain: chemistry
course: general-chemistry
prerequisites:
- id: periodic-trends
  type: hard
builds-toward:
- ion-formation
- electronegativity
tags:
- electron affinity
- periodic trends
- anions
stage: advanced
status: draft
---

# Electron Affinity

## Core Idea
Electron affinity is the energy change when an atom gains an electron. Nonmetals generally have higher electron affinity than metals, reflecting their tendency to gain electrons.

## Questions

```yaml
- question: "An atom has an electron affinity of −349 kJ/mol. Which statement best explains why this value is negative?"
  type: multiple-choice
  options:
    - "The atom had excess electrons it needed to release, making the process exothermic"
    - "The added electron enters a more stable configuration, and energy is released to the surroundings"
    - "The nucleus repels the incoming electron, requiring energy input from the surroundings"
    - "A negative electron affinity means the atom resists gaining electrons"
  answer: 1
  explanation: "A negative electron affinity means the process X(g) + e⁻ → X⁻(g) is exothermic — energy is released because the resulting anion is more stable than the neutral atom. The extra electron is attracted by the nuclear charge and enters an available orbital at lower potential energy, releasing that energy difference. A more negative value means a stronger tendency to gain electrons, not a weaker one."

- question: "Which element would you expect to have a near-zero or positive electron affinity?"
  type: multiple-choice
  options:
    - "Fluorine — small and highly electronegative"
    - "Nitrogen — has a half-filled 2p subshell"
    - "Neon — has a completely filled valence shell"
    - "Chlorine — one electron short of a noble gas configuration"
  answer: 2
  explanation: "Noble gases like neon have completely filled valence shells. An incoming electron would have to enter the next higher energy shell with no gain in stability, so the process is endothermic (positive electron affinity) or essentially zero. Fluorine and chlorine have strong tendencies to gain electrons (very negative EA). Nitrogen has an anomalously low EA but still negative — the half-filled 2p shell creates repulsion with the incoming electron, but the nuclear attraction still wins slightly."

- question: "Electron affinity generally becomes more negative (more exothermic) moving from left to right across a period."
  type: true-false
  answer: true
  explanation: "Across a period, nuclear charge increases while the principal quantum number stays the same, so the nucleus pulls incoming electrons more strongly and atomic radius shrinks. This makes electron gain progressively more favorable — the electron affinity trend increases (becomes more negative) across a period. Exceptions exist (e.g., nitrogen's half-filled 2p, noble gases' filled shells), but the general trend holds."

- question: "Fluorine has a more negative electron affinity than chlorine, consistent with the periodic trend that smaller atoms attract incoming electrons more strongly."
  type: true-false
  answer: false
  explanation: "This is the key exception: chlorine (−349 kJ/mol) actually has a more negative electron affinity than fluorine (−328 kJ/mol), despite fluorine being smaller and more electronegative. Fluorine's 2p orbitals are so compact that adding an electron creates significant electron-electron repulsion, partially offsetting the nuclear attraction. Chlorine's larger 3p orbitals accommodate the extra electron with less repulsion. This exception shows that the periodic trend for electron affinity has important nuances driven by orbital size."

- question: "Why does nitrogen have a lower (less negative) electron affinity than the elements on either side of it in the same period?"
  type: short-answer
  answer: "Nitrogen's 2p subshell is exactly half-filled, with one electron in each of the three 2p orbitals (parallel spins). An incoming electron must pair with one of these existing electrons, introducing electron-electron repulsion in that orbital. This pairing energy partially offsets the stabilization from nuclear attraction, resulting in a lower electron affinity than carbon (which has a partially empty 2p orbital with room for the electron) or oxygen (where the pairing still occurs but is outweighed by greater nuclear charge)."
  explanation: "The half-filled subshell is an unusually stable configuration because of exchange energy. Disrupting it by adding an electron is energetically penalized by the pairing repulsion, making nitrogen's electron affinity anomalously low. The same logic applies to elements with half-filled d subshells."
```

## Explainer

From your study of periodic trends, you know that atomic properties like atomic radius and ionization energy change systematically across periods and down groups because of how nuclear charge and electron shielding interact. **Electron affinity** adds another dimension to this picture: instead of asking how hard it is to *remove* an electron (ionization energy), it asks how much energy is released or absorbed when a neutral atom *gains* an electron to form an anion. Specifically, it is the energy change for the process X(g) + e⁻ → X⁻(g).

For most nonmetals, this process releases energy — the atom is more stable with the extra electron than without it. By convention, a negative electron affinity value means energy is released (exothermic), and a more negative value means the atom has a stronger "desire" to gain that electron. Think of it this way: a chlorine atom is one electron short of a filled valence shell. When it gains that electron, it achieves the stable electron configuration of argon, and the system drops to a lower energy state, releasing 349 kJ/mol. This is one of the highest electron affinities in the periodic table, which explains why chlorine so readily forms Cl⁻ ions.

The **periodic trend** generally mirrors what you saw with ionization energy but in reverse perspective. Electron affinity becomes more negative (stronger) as you move from left to right across a period, because increasing nuclear charge pulls the incoming electron more strongly while atomic radius shrinks. Moving down a group, electron affinity generally becomes less negative (weaker) because the incoming electron is added to a shell farther from the nucleus, where it feels less nuclear attraction and more shielding from inner electrons. However, this trend has notable exceptions. The noble gases have essentially zero or positive electron affinities because their valence shells are already full — adding an electron would mean starting a new, higher-energy shell with no stabilization. Nitrogen, with its half-filled 2p subshell, also has a surprisingly low electron affinity because the incoming electron must pair with an existing electron, introducing repulsion.

Understanding electron affinity alongside ionization energy gives you a complete picture of an element's tendency to form ions. Elements with high ionization energies *and* strongly negative electron affinities (like the halogens) are eager electron acceptors — they form anions easily. Elements with low ionization energies *and* weak electron affinities (like the alkali metals) are eager electron donors — they form cations easily. This complementary relationship is what drives ionic bond formation and underpins the concept of electronegativity that you will encounter next.
