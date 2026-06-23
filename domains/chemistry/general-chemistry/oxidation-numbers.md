---
id: oxidation-numbers
title: Oxidation Numbers
domain: chemistry
course: general-chemistry
prerequisites:
- id: periodic-table-overview
  type: hard
- id: oxidation-reduction-basics
  type: soft
builds-toward:
  - electrochemistry-basics
tags:
- oxidation-state
- oxidation-number-rules
- electron-bookkeeping
- formal-charge-vs-oxidation-number
stage: formal-systems
status: validated
---
# Oxidation Numbers

## Core Idea
Oxidation numbers (oxidation states) are a bookkeeping tool that tracks the hypothetical charge an atom would have if all bonds were fully ionic. A set of rules governs assignment: free elements are 0, monatomic ions equal their charge, oxygen is usually −2 (except in peroxides), hydrogen is usually +1 (except in metal hydrides), and the sum of oxidation numbers in a neutral compound is 0 (or equals the ion charge for polyatomic ions). Changes in oxidation number across a reaction identify which atoms are oxidized (increase) and which are reduced (decrease).

## How It's Best Learned
Memorize the priority rules in order, then practice assigning oxidation numbers to atoms in progressively complex molecules and polyatomic ions. Compare oxidation numbers before and after a reaction to confirm redox has occurred and to identify the number of electrons transferred.

## Common Misconceptions
- Oxidation numbers are not actual charges on atoms — they are a formal bookkeeping device. In covalent molecules, electrons are shared, not fully transferred.
- Fluorine is always −1 (the most electronegative element), but other halogens can have positive oxidation numbers when bonded to oxygen or a more electronegative halogen.

## Questions

```yaml
- question: "In H₂O₂ (hydrogen peroxide), oxygen has an oxidation number of −1 rather than the usual −2. Which explanation is correct?"
  type: multiple-choice
  options:
    - "Hydrogen is more electronegative than oxygen in peroxides, pulling electron density away from oxygen"
    - "Each oxygen is bonded to another oxygen of equal electronegativity, so neither can claim both electrons from that bond — leaving each oxygen with only one extra electron instead of two"
    - "The oxidation number rules do not apply to compounds with oxygen-oxygen bonds"
    - "Oxygen alternates between −1 and −2 depending on temperature and pressure"
  answer: 1
  explanation: "Oxidation numbers are assigned by giving all shared electrons to the more electronegative atom. In the O–O bond of H₂O₂, both oxygens are equally electronegative, so they split the bonding electrons equally — neither gets to claim both. This reduces each oxygen's 'extra' electrons from 2 (the usual −2) to 1 (hence −1). This is a principled application of the bookkeeping logic, not an exception to the rules."

- question: "In the reaction 2Fe₂O₃ + 3C → 4Fe + 3CO₂, iron goes from +3 to 0 and carbon goes from 0 to +4. Which of the following correctly identifies what happened?"
  type: multiple-choice
  options:
    - "Iron was oxidized; carbon was the oxidizing agent"
    - "Iron was reduced; carbon was the oxidizing agent"
    - "Iron was reduced; carbon was the reducing agent"
    - "Iron was oxidized; carbon was the reducing agent"
  answer: 2
  explanation: "Iron goes from +3 to 0 — its oxidation number decreases, meaning it gained electrons — so iron was reduced. Carbon goes from 0 to +4 — its oxidation number increases, meaning it lost electrons — so carbon was oxidized. The reducing agent is the species that gets oxidized (loses electrons) and causes reduction in another species: that's carbon. The oxidizing agent is the species that gets reduced (gains electrons): that's the iron in Fe₂O₃. Confusing 'oxidizing agent' with 'the thing that gets oxidized' is the classic error here."

- question: "Oxidation numbers represent the actual electrical charges on atoms in a compound."
  type: true-false
  answer: false
  explanation: "Oxidation numbers are a formal bookkeeping device — they represent the hypothetical charge an atom would have if all bonds were fully ionic and all electrons were assigned to the more electronegative atom. In covalent compounds like CO₂, electrons are shared, not fully transferred; carbon does not carry an actual +4 charge. Oxidation numbers are a useful fiction that enables tracking electron flow in redox reactions without requiring full quantum mechanical analysis of each bond."

- question: "In NaH (sodium hydride), hydrogen has an oxidation number of −1, even though hydrogen is typically +1 in compounds with nonmetals."
  type: true-false
  answer: true
  explanation: "The assignment rule for hydrogen is context-dependent: hydrogen is +1 when bonded to nonmetals (which are more electronegative, so hydrogen 'loses' its electron), but −1 when bonded to metals in hydrides. Sodium is less electronegative than hydrogen, so in NaH the electrons are assigned to hydrogen, giving it −1. Sodium is +1. This is one of the key priority-rule exceptions students must apply correctly."

- question: "An atom's oxidation number increases from +2 to +5 during a chemical reaction. Was this atom oxidized or reduced? What does this change tell you about electron movement, and what role does this atom play in the overall redox reaction?"
  type: short-answer
  answer: "The atom was oxidized. An increase in oxidation number means the atom has (formally) lost electrons — in the bookkeeping system, it ends up with fewer electrons assigned to it. This atom is therefore the reducing agent: it donates electrons to another species, enabling that other species to be reduced. The magnitude of the change (+3 oxidation states) indicates that 3 electrons were transferred per atom of this species."
  explanation: "The mnemonic OIL RIG (Oxidation Is Loss, Reduction Is Gain) captures the directionality. Higher oxidation number = fewer electrons assigned = oxidized = reducing agent. Students often confuse the agent with the process: the reducing agent is the one that gets oxidized (it reduces others by donating electrons to them). The change in oxidation number also provides the stoichiometry of electron transfer, which is essential for balancing redox reactions using the half-reaction method."
```

## Explainer

From the periodic table, you know that atoms have characteristic tendencies to gain or lose electrons based on their position — metals tend to lose, nonmetals tend to gain. **Oxidation numbers** extend this idea into a universal bookkeeping system that tracks where electrons "belong" in any compound, even covalent ones where electrons are actually shared. The trick is to pretend that every bond is fully ionic: assign all shared electrons to the more electronegative atom, then count up the hypothetical charge on each atom. The resulting number is the oxidation state.

A set of priority rules makes assignment systematic. **Free elements** (like O₂, Fe, or S₈) have an oxidation number of 0 — atoms bonded only to identical atoms have no reason to shift electrons. **Monatomic ions** have oxidation numbers equal to their charge (Na⁺ is +1, Cl⁻ is −1). **Fluorine** is always −1 because it is the most electronegative element — nothing pulls electrons away from it. **Oxygen** is almost always −2 (except in peroxides like H₂O₂, where it is −1, because each oxygen shares electrons equally with the other oxygen). **Hydrogen** is +1 when bonded to nonmetals and −1 in metal hydrides like NaH. And crucially, the oxidation numbers in any neutral compound must sum to zero, while in a polyatomic ion they must sum to the ion's charge. This last rule is your algebraic handle: when you know the oxidation numbers of all atoms but one, you can solve for the unknown.

Consider the permanganate ion, MnO₄⁻. Oxygen is −2, and there are four oxygens: 4(−2) = −8. The overall charge is −1. So manganese must be +7, because +7 + (−8) = −1. In Cr₂O₇²⁻, the seven oxygens contribute −14, the ion charge is −2, so two chromiums share +12, making each Cr +6. This algebraic approach works for any compound or ion, no matter how complex.

The real power of oxidation numbers appears when you compare them across a reaction. If an atom's oxidation number **increases** from reactant to product, that atom has been **oxidized** — it has lost electrons (or behaves as if it did). If the number **decreases**, the atom has been **reduced** — it has gained electrons. This is how you identify redox reactions and figure out which species is the oxidizing agent (contains the atom being reduced) and which is the reducing agent (contains the atom being oxidized). For example, in the reaction 2Fe₂O₃ + 3C → 4Fe + 3CO₂, iron goes from +3 to 0 (reduced) and carbon goes from 0 to +4 (oxidized). The number of electrons lost must equal the number gained, which is the principle you will use when you begin writing and balancing half-reactions.
