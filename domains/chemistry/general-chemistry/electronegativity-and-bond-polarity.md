---
id: electronegativity-and-bond-polarity
title: Electronegativity and Bond Polarity
domain: chemistry
course: general-chemistry
prerequisites:
- id: periodic-trends
  type: hard
- id: covalent-bonding
  type: hard
builds-toward:
- molecular-polarity
- vsepr-theory
tags:
- electronegativity
- bond polarity
- polar covalent
stage: advanced
status: draft
---

# Electronegativity and Bond Polarity

## Core Idea
Electronegativity is an atom's ability to attract bonding electrons. The difference in electronegativity between bonded atoms determines bond polarity, ranging from nonpolar covalent to ionic.

## How It's Best Learned
Compare electronegativities from a periodic table to classify bonds and predict molecular behavior.

## Common Misconceptions
Confusing electronegativity with electron affinity; thinking all C-H bonds are identical regardless of context.

## Questions

```yaml
- question: "Consider a C–O bond (C electronegativity: 2.5, O: 3.5, ΔEN = 1.0) and an N–N bond (ΔEN = 0). Which statement correctly classifies these bonds?"
  type: multiple-choice
  options:
    - "Both are nonpolar covalent because both involve only nonmetal atoms"
    - "C–O is polar covalent with partial negative charge on oxygen; N–N is nonpolar covalent"
    - "C–O is ionic because oxygen has high electronegativity"
    - "N–N is slightly polar because nitrogen's lone pairs create an asymmetric electron distribution"
  answer: 1
  explanation: "Bond polarity depends on the electronegativity difference between bonded atoms, not on the identity of the elements as metals or nonmetals. C and O are both nonmetals, but their ΔEN of 1.0 is large enough to create a meaningfully polar bond — the shared electrons are pulled toward the more electronegative oxygen, creating δ– on O and δ+ on C. N–N bonds two identical atoms (ΔEN = 0), so electrons are shared equally: nonpolar covalent. The misconception in option A — that 'nonmetal + nonmetal = nonpolar' — is one of the most common errors in bond classification."

- question: "H–F has ΔEN = 1.9 and H–Cl has ΔEN = 0.9. A student claims H–Cl is more polar because chlorine is a larger atom with more electrons, creating stronger London dispersion interactions. Why is this reasoning incorrect?"
  type: multiple-choice
  options:
    - "It is correct — larger atoms always form more polar bonds"
    - "London dispersion forces are intermolecular, not intramolecular — they do not determine bond polarity. Bond polarity is determined by electronegativity difference, so H–F (ΔEN = 1.9) is more polar"
    - "Both bonds are equally polar because they both involve hydrogen bonded to a halogen"
    - "Polarity depends on bond length, not electronegativity, and H–Cl is longer than H–F"
  answer: 1
  explanation: "London dispersion forces are attractions between temporary dipoles in different molecules — they describe intermolecular interactions, not the polarity of a covalent bond within a molecule. Bond polarity is determined entirely by electronegativity difference: how unequally the bonded atoms attract the shared electrons. Fluorine (EN = 4.0) is the most electronegative element; the H–F ΔEN of 1.9 produces a highly polar bond with significant δ– on F and δ+ on H. H–Cl (ΔEN = 0.9) is polar, but less so. Atomic size affects London dispersion forces (more electrons = stronger dispersion), but this is independent of bond polarity."

- question: "The classification of bonds as 'nonpolar covalent,' 'polar covalent,' and 'ionic' represents three fundamentally distinct types of bonding with sharp boundaries between them."
  type: true-false
  answer: false
  explanation: "Bond polarity exists on a continuous spectrum, and the cutoffs used to label bonds (e.g., ΔEN < 0.4 for nonpolar, ΔEN > 1.7 for ionic) are approximate guidelines, not sharp physical boundaries. As ΔEN increases, electron density shifts more and more toward the electronegative atom — from equal sharing to slight asymmetry to nearly complete transfer — without any discontinuous jump. Most ionic compounds retain partial covalent character, and many 'covalent' compounds have partial ionic character. The labels are useful shorthand for a continuous underlying variable."

- question: "Electronegativity and electron affinity are different names for the same atomic property and follow identical periodic trends."
  type: true-false
  answer: false
  explanation: "They are related but distinct properties. Electron affinity measures the energy change when an isolated, gas-phase atom gains one electron — it is a property of the free atom under specific conditions. Electronegativity measures an atom's ability to attract shared bonding electrons within a covalent bond — it is a property of the atom in the context of a bond. Both generally increase up and to the right on the periodic table (more protons, smaller radius, tighter electron hold), but they are not numerically identical, differ in units and measurement, and can rank elements differently. Confusing them leads to incorrect reasoning about bonding in molecules."

- question: "Why does the polarity of a covalent bond matter for predicting how a molecule will behave chemically and physically?"
  type: short-answer
  answer: "A polar bond creates partial charges — δ+ on the less electronegative atom and δ– on the more electronegative one. These partial charges make specific atoms in the molecule susceptible to attack: nucleophiles (electron-rich species) are attracted to δ+ centers, and electrophiles (electron-poor species) are attracted to δ– centers. For example, the polar C=O bond in a carbonyl group makes the carbon a nucleophilic target, directing reactivity in addition and substitution reactions. Physically, polar bonds allow molecules to participate in dipole–dipole interactions and hydrogen bonding (when H is bonded to F, O, or N), dramatically raising boiling points and increasing solubility in polar solvents like water. Bond polarity is therefore not just a bookkeeping property — it is the primary driver of where and how a molecule reacts."
```

## Explainer

From periodic trends, you know that atomic properties change systematically across periods and down groups. **Electronegativity** is one of the most consequential of these trends: it measures how strongly an atom attracts the electrons in a covalent bond toward itself. On the Pauling scale, fluorine is the most electronegative element (4.0), and electronegativity generally increases going up and to the right on the periodic table — the same direction as ionization energy, and for the same fundamental reason: smaller atoms with more protons hold their electrons more tightly.

When two atoms with different electronegativities form a covalent bond, the shared electrons are not shared equally. The more electronegative atom pulls the electron density toward itself, creating an uneven distribution of charge. This produces a **polar covalent bond** — a bond with a partial negative charge (δ−) on the more electronegative atom and a partial positive charge (δ+) on the less electronegative one. Think of it as a tug-of-war for electrons: if both sides pull equally, the rope stays centered (nonpolar); if one side is stronger, the rope shifts toward that side (polar).

The electronegativity difference (ΔEN) between bonded atoms provides a rough guide to bond character. When ΔEN is close to zero (typically < 0.4), the bond is essentially **nonpolar covalent** — as in H₂ or Cl₂, where identical atoms share electrons equally. When ΔEN is moderate (roughly 0.4 to 1.7), the bond is **polar covalent** — as in H–Cl (ΔEN = 0.9), where chlorine's greater electronegativity pulls electron density away from hydrogen. When ΔEN is large (typically > 1.7), the electron transfer is so lopsided that the bond is effectively **ionic** — as in NaCl (ΔEN = 2.1), where sodium essentially surrenders its electron to chlorine entirely.

These boundaries are guidelines, not sharp cutoffs — bond polarity exists on a continuous spectrum from purely covalent to purely ionic. What matters practically is that bond polarity determines much of a molecule's chemical behavior. Polar bonds create sites of partial charge that attract other polar molecules, influence reaction mechanisms by making certain atoms more susceptible to attack, and ultimately determine whether a molecule as a whole is polar — which you will explore when you study molecular polarity. The simple act of looking up two electronegativity values and taking their difference gives you predictive power over a molecule's bonding character, solubility behavior, and reactivity patterns.
