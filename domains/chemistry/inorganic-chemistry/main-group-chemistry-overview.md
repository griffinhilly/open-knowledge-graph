---
id: main-group-chemistry-overview
title: Main Group Chemistry Overview
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: periodic-trends
  type: hard
- id: lewis-structures
  type: hard
- id: bond-classification
  type: soft
builds-toward:
- solid-state-chemistry-fundamentals
- materials-chemistry-zeolites-mofs
tags:
- main group elements
- s-block
- p-block
- diagonal relationships
- inert pair effect
stage: formal-systems
status: validated
---

# Main Group Chemistry Overview

## Core Idea
Main group chemistry encompasses the s-block and p-block elements, whose chemistry is governed by trends in electronegativity, ionization energy, atomic radius, and oxidation states across and down the periodic table. Key organizing concepts include diagonal relationships (similarities between elements diagonally adjacent in the periodic table), the inert pair effect (reluctance of heavier elements to use their outermost s-electrons in bonding), and the unique first-row anomaly (the lightest element in each group often behaves differently from its heavier congeners).

## Questions

```yaml
- question: "Thallium (Tl) most commonly forms Tl⁺ compounds rather than Tl³⁺, even though it is in Group 13 and has three valence electrons. Which concept explains this?"
  type: multiple-choice
  options:
    - "The diagonal relationship between Tl and a lighter Group 12 element"
    - "The inert pair effect — the 6s² electrons in Tl are stabilized by relativistic contraction and poor shielding, making them reluctant to participate in bonding"
    - "Thallium's high electronegativity prevents it from losing more than one electron"
    - "Crystal field stabilization energy favors the +1 oxidation state"
  answer: 1
  explanation: "The inert pair effect describes the increasing stability of the oxidation state two less than the group valence for heavier p-block elements. For Tl (Group 13), the 6s² electrons are stabilized by relativistic effects (the 6s orbital contracts and lowers in energy due to the high nuclear charge experienced by inner-shell electrons traveling at relativistic speeds) and by poor shielding from the filled 4f and 5d subshells. These stabilized 6s² electrons are reluctant to participate in bonding, making Tl⁺ (using only the 6p electron) more stable than Tl³⁺. The same effect explains Pb²⁺ over Pb⁴⁺ and Bi³⁺ over Bi⁵⁺."

- question: "Lithium and magnesium show a diagonal relationship — they share similar properties despite being in different groups and periods."
  type: true-false
  answer: true
  explanation: "Diagonal relationships arise because moving one step right and one step down in the periodic table produces opposing trends that approximately cancel: electronegativity and ionization energy decrease going down a group but increase going across a period. Li and Mg have similar charge densities (Li⁺ is small and singly charged; Mg²⁺ is slightly larger but doubly charged). Both form covalent organometallic compounds, both have carbonate and fluoride salts that decompose on heating (unlike their group congeners), and both form nitrides directly. Similar diagonal relationships exist between Be/Al and B/Si."

- question: "Nitrogen forms stable N≡N triple bonds while phosphorus does not form analogous P≡P triple bonds under normal conditions. This is an example of the first-row anomaly."
  type: true-false
  answer: true
  explanation: "First-row elements in each p-block group have uniquely small atomic radii, which allows effective lateral overlap of p-orbitals to form strong pi-bonds. N₂ has a bond energy of 945 kJ/mol — one of the strongest bonds in chemistry. Phosphorus, being larger, has poor p-orbital overlap for pi-bonding and instead forms single bonds to multiple neighbors (P₄ tetrahedra with P-P single bonds). This first-row anomaly extends across the p-block: carbon forms strong C=C and C≡C bonds while silicon prefers single bonds; nitrogen and oxygen form pi-bonds easily while their heavier congeners do not."

- question: "Explain why boron chemistry is dominated by electron-deficient compounds and cluster structures, while aluminum — in the same group — forms conventional ionic and covalent compounds."
  type: short-answer
  answer: "Boron has three valence electrons but four valence orbitals (2s + three 2p), making it inherently electron-deficient — it cannot form enough conventional two-center, two-electron bonds to fill its octet. This forces boron into unconventional bonding: three-center two-electron bonds (as in diborane B₂H₆), electron-deficient bridge bonds, and polyhedral cluster compounds (boranes, carboranes). Aluminum, though also in Group 13 with three valence electrons, is much larger and more electropositive. It readily forms Al³⁺ in ionic compounds or uses its size to achieve higher coordination numbers (6 in Al₂O₃) through conventional bonding. Al can also form electron-deficient bridges (Al₂Cl₆ is a dimer with bridging chlorides), but this tendency is less dominant than in boron because aluminum's larger size and lower ionization energy favor ionic character."
  explanation: "This contrast between boron and aluminum is one of the clearest examples of the first-row anomaly combined with size effects. Boron's small size forces it into exotic bonding arrangements that are characteristic of its chemistry but unusual for the rest of the group."
```

## Explainer

Inorganic chemistry is often associated with transition metals, but the main group elements — Groups 1-2 (s-block) and 13-18 (p-block) — display chemistry that is equally rich and arguably more diverse. These elements form the backbone of materials science (silicon, carbon), biological chemistry (nitrogen, oxygen, phosphorus, sulfur), and industrial chemistry (chlorine, aluminum, sodium). Understanding their periodic trends and the exceptions to those trends is essential for navigating inorganic chemistry.

Three organizing principles structure main group chemistry. First, the periodic trends you learned in general chemistry — atomic radius increases down a group, ionization energy and electronegativity increase across a period — create predictable gradients in bonding character. Moving from left to right, bonding shifts from metallic to ionic to covalent to van der Waals. Moving down a group, elements become more metallic, less electronegative, and more willing to adopt lower oxidation states. These trends are the foundation, but the interesting chemistry often lies in the exceptions.

Second, diagonal relationships reveal unexpected similarities between elements in different groups. Lithium resembles magnesium more than it resembles sodium; beryllium resembles aluminum more than it resembles calcium; boron resembles silicon more than it resembles aluminum. These relationships arise because the opposing effects of moving right (increasing charge, decreasing size) and down (increasing size, decreasing ionization energy) roughly cancel, producing elements with similar charge densities and bonding preferences. Diagonal relationships are particularly useful for predicting the behavior of the lightest elements in each group, which often deviate from the trends established by their heavier congeners.

Third, the inert pair effect and the first-row anomaly create systematic deviations from simple group trends. The inert pair effect — the reluctance of the outermost s-electrons to participate in bonding for heavy p-block elements — explains why Tl⁺ is more stable than Tl³⁺, Pb²⁺ more stable than Pb⁴⁺, and Bi³⁺ more stable than Bi⁵⁺. It arises from a combination of relativistic stabilization of the 6s orbital and poor shielding by the intervening 4f electrons. The first-row anomaly — the uniquely strong pi-bonding ability of second-period elements (C, N, O) due to their small atomic radii — explains why nitrogen forms N₂ triple bonds while phosphorus polymerizes, and why carbon chemistry (organic chemistry) is dominated by double and triple bonds while silicon chemistry is dominated by single bonds to oxygen.
