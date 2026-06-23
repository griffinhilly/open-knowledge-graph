---
id: bond-energy-and-enthaly
title: Bond Energy and Enthalpy Change
domain: chemistry
course: general-chemistry
prerequisites:
- id: covalent-bonding
  type: hard
- id: thermochemistry-enthalpy
  type: hard
- id: endothermic-and-exothermic-reactions
  type: soft
builds-toward:
- hess-law-of-enthalpy
- reaction-coordinate-diagrams
tags:
- bond energy
- bond breaking
- bond formation
stage: formal-systems
status: validated
---

# Bond Energy and Enthalpy Change

## Core Idea
Bond energy is the energy required to break a bond. ΔH for a reaction equals energy required to break bonds minus energy released when forming new bonds.

## How It's Best Learned
Use bond energy tables to calculate ΔH; compare with other methods like Hess's Law.

## Questions

```yaml
- question: "A reaction breaks 1 mole of H–H bonds (436 kJ/mol) and 1 mole of F–F bonds (157 kJ/mol), then forms 2 moles of H–F bonds (565 kJ/mol each). What is the estimated ΔH, and is the reaction endothermic or exothermic?"
  type: multiple-choice
  options:
    - "−537 kJ/mol (exothermic) — more energy is released forming H–F bonds than consumed breaking H–H and F–F bonds"
    - "+537 kJ/mol (endothermic) — breaking bonds always requires energy, so reactions are always endothermic overall"
    - "−593 kJ/mol (exothermic) — the total energy of bonds broken is released as heat"
    - "+1130 kJ/mol (endothermic) — the energy of bonds formed must be added to the bond-breaking cost"
  answer: 0
  explanation: "ΔH ≈ Σ(bonds broken) − Σ(bonds formed) = (436 + 157) − 2(565) = 593 − 1130 = −537 kJ/mol. The negative value confirms the reaction is exothermic: the two H–F bonds formed are collectively much stronger than the H–H and F–F bonds broken, so more energy is released than consumed. Option B is the most common error — conflating 'bond breaking requires energy' with 'the whole reaction requires energy.' The reaction is a net balance; what matters is whether bonds formed release more energy than bonds broken absorb."

- question: "Why do bond energy calculations give estimates of ΔH rather than exact values?"
  type: multiple-choice
  options:
    - "Because bond energies are measured at non-standard conditions and must be corrected"
    - "Because bond energies are averages across many different molecular environments, and the actual strength of a given bond depends on its surroundings"
    - "Because the calculation ignores kinetic barriers and only measures thermodynamic potential"
    - "Because some bonds are formed and broken simultaneously, making the sequential bookkeeping inaccurate"
  answer: 1
  explanation: "Bond energy values in tables are averages. The C–H bond energy of 413 kJ/mol is the mean across many molecules — methane, ethanol, chloroform, etc. — even though the actual C–H bond strength varies because surrounding atoms influence the electron distribution. A C–H bond alpha to a carbonyl is weaker than one in a pure alkane. Bond energy calculations give useful estimates for ΔH, but for precise thermochemistry you would use standard enthalpies of formation and Hess's Law, which account for the actual molecular context."

- question: "In the bond energy method, ΔH ≈ Σ(bond energies formed) − Σ(bond energies broken)."
  type: true-false
  answer: false
  explanation: "The formula is reversed: ΔH ≈ Σ(bond energies broken) − Σ(bond energies formed). Breaking bonds requires energy input (positive contribution to ΔH), and forming bonds releases energy (negative contribution). The reaction is exothermic (ΔH < 0) when the bonds formed are stronger — release more energy — than the bonds broken. Reversing the formula gives the wrong sign and would predict that reactions favoring strong new bonds are endothermic, which contradicts basic thermochemistry."

- question: "A reaction that forms stronger bonds than it breaks is generally predicted to be exothermic."
  type: true-false
  answer: true
  explanation: "Stronger bonds have higher bond energies — they release more energy when formed. If the bonds formed in products are stronger (higher kJ/mol) than the bonds broken in reactants, then Σ(formed) > Σ(broken), and ΔH = Σ(broken) − Σ(formed) < 0 (exothermic). This is the intuitive rule: exothermic reactions tend to produce more stable (stronger-bonded) products. Combustion exemplifies this — breaking C–H and O=O bonds (moderate strength) and forming C=O and O–H bonds (very strong) releases substantial heat."

- question: "Explain why breaking a bond always requires energy input and forming a bond always releases energy. How does this principle determine whether a reaction is endothermic or exothermic?"
  type: short-answer
  answer: "Bonds form because the bonded state is lower in energy than the separated atoms — electrons are stabilized by being shared between nuclei. Breaking a bond requires supplying energy to separate the atoms back to their higher-energy isolated state. Forming a bond releases that energy as the atoms reach their lower-energy bonded state. In a reaction, ΔH is the net energy balance: energy in (breaking reactant bonds) minus energy out (forming product bonds). If more energy is released making products' bonds than was consumed breaking reactants' bonds, ΔH is negative and the reaction is exothermic. If the reverse, ΔH is positive and the reaction is endothermic."
  explanation: "This bookkeeping principle is physically grounded in potential energy: bonding lowers the potential energy of electrons and nuclei relative to the separated-atom reference state. Bond energy quantifies exactly how much lower. Since chemical reactions are just rearrangements of these bonds, ΔH reduces to counting the net change in total bond energy — a powerful conceptual simplification that connects molecular structure to macroscopic heat flow."
```

## Explainer

You already know that covalent bonds form when atoms share electrons, and from thermochemistry you know that enthalpy change (ΔH) measures the heat absorbed or released during a reaction at constant pressure. Bond energy connects these two ideas: it tells you exactly how much energy is stored in each bond, which lets you estimate ΔH for any reaction directly from its structural formula.

**Bond energy** (also called bond dissociation energy) is the energy required to break one mole of a particular bond in the gas phase, producing separated atoms. For example, breaking one mole of H–H bonds requires 436 kJ — that's the bond energy of H–H. Breaking bonds always requires energy input (endothermic), while forming bonds always releases energy (exothermic). This is the fundamental bookkeeping principle: a chemical reaction is essentially a process of breaking old bonds and forming new ones, and ΔH is the net energy balance.

The calculation follows a simple formula: **ΔH ≈ Σ(bond energies broken) − Σ(bond energies formed)**. Consider the combustion of methane: CH₄ + 2O₂ → CO₂ + 2H₂O. You break four C–H bonds and two O=O bonds (energy input), then form two C=O bonds and four O–H bonds (energy output). Plugging in table values: breaking costs 4(413) + 2(498) = 2648 kJ; forming releases 2(799) + 4(463) = 3450 kJ. The difference is 2648 − 3450 = −802 kJ/mol — negative because more energy is released forming bonds than consumed breaking them, confirming that combustion is exothermic, which matches your everyday experience of fire producing heat.

One important caveat: bond energies are averages across many different molecules. The C–H bond energy of 413 kJ/mol is an average — the actual C–H bond strength in methane differs slightly from that in ethanol or chloroform because the surrounding atoms influence electron distribution. This means bond energy calculations give estimates of ΔH, not exact values. For precise thermodynamic calculations, you would use Hess's Law with standard enthalpies of formation. But bond energies are powerful for quick predictions and for building intuition about why some reactions are energetically favorable: reactions tend to be exothermic when they form stronger bonds than they break.
