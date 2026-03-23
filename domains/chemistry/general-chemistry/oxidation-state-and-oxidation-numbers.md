---
id: oxidation-state-and-oxidation-numbers
title: Assigning Oxidation Numbers and Identifying Redox
domain: chemistry
course: general-chemistry
prerequisites:
- id: oxidation-numbers
  type: hard
- id: chemical-equations-balancing
  type: hard
builds-toward:
- half-reactions-and-balancing
- balancing-redox-equations
tags:
- oxidation numbers
- redox identification
- oxidation state rules
stage: formal-systems
status: validated
---

# Assigning Oxidation Numbers and Identifying Redox

## Core Idea
Oxidation numbers track electron transfer. Rules for assigning them include: elements in their standard state = 0, monatomic ions = their charge, O = −2 (except in peroxides), H = +1 (except in metal hydrides).

## How It's Best Learned
Practice assigning oxidation numbers to all atoms in a compound, then identify what is oxidized and reduced.

## Common Misconceptions
Forgetting exceptions to oxidation number rules (peroxides, metal hydrides).

## Questions

```yaml
- question: "In H₂O₂ (hydrogen peroxide), what is the oxidation state of oxygen, and why does the standard rule not apply?"
  type: multiple-choice
  options:
    - "−2, because oxygen is always −2 in any compound"
    - "−1, because each oxygen is bonded to another oxygen of equal electronegativity, so neither atom wins the shared electrons outright"
    - "0, because the molecule is electrically neutral"
    - "+1, because hydrogen contributes +1 to balance each oxygen"
  answer: 1
  explanation: "The standard rule (O = −2) assumes oxygen bonds to a less electronegative element and claims all shared electrons. In peroxides, each oxygen is bonded to another oxygen — identical electronegativity means the electrons are split equally, giving each oxygen −1 instead of −2. This is the classic peroxide exception. Students who memorize 'oxygen is always −2' without understanding the electronegativity basis will assign the wrong value here."

- question: "In the reaction Zn + H₂SO₄ → ZnSO₄ + H₂, which species is reduced, and how do you know?"
  type: multiple-choice
  options:
    - "Zinc, because it forms a compound and gains a positive charge"
    - "Sulfur, because it is present on both sides as sulfate"
    - "Hydrogen, because it goes from +1 in H₂SO₄ to 0 in H₂ — a decrease in oxidation number"
    - "Oxygen, because it ends up in the sulfate product on both sides"
  answer: 2
  explanation: "Reduction means a decrease in oxidation number (gain of electron density — the 'R' in 'OIL RIG'). Hydrogen starts at +1 in H₂SO₄ and becomes 0 in elemental H₂ — a decrease, so hydrogen is reduced. Zinc goes from 0 to +2 (oxidized). Sulfur stays at +6 throughout; oxygen stays at −2 throughout. Neither undergoes a change, so neither participates in the electron transfer."

- question: "Oxidation states represent the actual electrical charges that atoms carry within a compound."
  type: true-false
  answer: false
  explanation: "Oxidation states are a bookkeeping fiction, not a physical measurement. They are assigned by pretending all bonds are fully ionic — giving all shared electrons to the more electronegative atom — even in covalent molecules where electrons are only partially shifted. For example, carbon in CO₂ is assigned +4, but it does not carry a genuine +4 charge. The real charge distribution is determined by partial electronegativities, bond polarity, and electron delocalization. Oxidation states are useful for tracking electron transfers in redox reactions, not for describing actual charge."

- question: "If no atom's oxidation number changes on either side of a chemical equation, the reaction is not a redox reaction."
  type: true-false
  answer: true
  explanation: "Redox reactions are defined by electron transfer, and oxidation numbers track electron ownership. If every atom has the same oxidation number on both sides of the equation, no electrons have changed hands — there has been no oxidation or reduction. The reaction might be a precipitation, an acid-base neutralization, or a complex-forming reaction, but it is not a redox reaction. Changing oxidation numbers are both necessary and sufficient to classify a reaction as redox."

- question: "Explain why hydrogen has an oxidation state of +1 in water (H₂O) but −1 in sodium hydride (NaH), and what principle underlies this difference."
  type: short-answer
  answer: "In H₂O, oxygen is more electronegative than hydrogen, so oxygen 'wins' the shared electrons in the O–H bond. Hydrogen is assigned +1 because it is the electron-donor in the bond. In NaH, sodium is more electropositive (less electronegative) than hydrogen, so hydrogen 'wins' the shared electrons in the Na–H bond. Hydrogen is now the electron-acceptor, giving it an oxidation state of −1. The underlying principle is electronegativity: in the oxidation number system, the more electronegative atom in a bond is assigned all the shared electrons. When hydrogen bonds to an element more electropositive than itself (metals), hydrogen becomes the winner and takes on a negative oxidation state."
  explanation: "The peroxide and metal hydride exceptions both stem from the same principle: the standard rules (O = −2, H = +1) hold only when the usual electronegativity ordering applies. When oxygen bonds to oxygen, or hydrogen bonds to a metal more electropositive than itself, the usual hierarchy breaks down and the exceptions apply. Understanding the electronegativity basis means you can always derive the correct assignment rather than memorizing a list of exceptions."
```

## Explainer

From your work with oxidation numbers and balancing chemical equations, you already know the basic concept: atoms in compounds are assigned numbers that reflect how electrons are distributed. **Oxidation states** are a bookkeeping device — they track where electrons "belong" by assuming that all bonds are fully ionic, even when they are covalent. This artificial assignment lets you see at a glance which atoms have gained electron density and which have lost it, making it possible to identify **redox reactions** (reactions involving electron transfer) from the equation alone.

The rules for assigning oxidation numbers follow a clear hierarchy. Any element in its elemental form — O₂, Fe, N₂, S₈ — has an oxidation state of **0**, because identical atoms share electrons equally. Monatomic ions take their charge as their oxidation state: Na⁺ is +1, Cl⁻ is −1, Ca²⁺ is +2. For compounds, fluorine is always −1 (it is the most electronegative element and always "wins" the electrons). Oxygen is −2 in most compounds, with the key exception of **peroxides** (like H₂O₂) where it is −1, because each oxygen shares a bond with the other. Hydrogen is +1 when bonded to nonmetals and −1 in **metal hydrides** (like NaH), where the metal is more electropositive and "gives" its electron to hydrogen. The sum of all oxidation numbers in a neutral compound must equal zero; in a polyatomic ion, it must equal the ion's charge.

To identify a redox reaction, assign oxidation numbers to every atom on both sides of the equation and look for changes. If an atom's oxidation number increases, it has been **oxidized** — it lost electron density. If it decreases, it has been **reduced** — it gained electron density. The mnemonic "OIL RIG" (Oxidation Is Loss, Reduction Is Gain) captures this. For example, in the reaction 2Fe + 3Cl₂ → 2FeCl₃, iron goes from 0 to +3 (oxidized) and chlorine goes from 0 to −1 (reduced). If no oxidation numbers change, the reaction is not a redox reaction — it might be an acid-base, precipitation, or other type.

This ability to identify what is oxidized and reduced is the gateway to writing **half-reactions**, which separate the oxidation and reduction processes and make it possible to balance complex redox equations systematically. The oxidation number rules may feel like arbitrary conventions, but they encode a real physical insight: electronegativity determines which atom in a bond controls the shared electrons, and the oxidation state reflects that assignment. Mastering these rules now pays off immediately in electrochemistry, corrosion chemistry, and metabolic biochemistry, where tracking electron flow is central to understanding how reactions work.
