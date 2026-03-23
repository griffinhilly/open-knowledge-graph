---
id: chemical-equations-and-balancing
title: 'Chemical Equations: Writing and Balancing Reactions'
domain: chemistry
course: general-chemistry
prerequisites:
- id: matter-classification-and-properties
  type: hard
- id: writing-ionic-formulas
  type: soft
builds-toward:
- stoichiometry-calculations
- oxidation-reduction-reactions
tags:
- chemical equations
- balancing
- coefficients
- mass conservation
stage: formal-systems
status: draft
---

# Chemical Equations: Writing and Balancing Reactions

## Core Idea
Chemical equations show reactants (left side) converting to products (right side) through breaking and forming bonds. Balancing equations ensures mass is conserved: the same number of each element's atoms appears on both sides. Coefficients (not subscripts) are adjusted to balance. Equation type (synthesis, combustion, etc.) indicates the reaction type.

## Questions

```yaml
- question: "A student needs to balance the equation: H₂ + O₂ → H₂O. They write: H₂ + O₂ → H₂O₂. What is the critical error?"
  type: multiple-choice
  options:
    - "The student added the wrong number of oxygen atoms to the right side"
    - "The student changed a subscript, converting water into hydrogen peroxide — a different compound"
    - "The student should have added a coefficient of 2 in front of O₂ instead"
    - "The equation does not need balancing because both sides already have 2 hydrogen atoms"
  answer: 1
  explanation: "Changing H₂O to H₂O₂ changes the subscript, which changes the identity of the substance — H₂O is water; H₂O₂ is hydrogen peroxide, a completely different compound with different properties. The rule is absolute: subscripts define what the substance is and must never be changed to balance an equation. The correct balanced form is 2H₂ + O₂ → 2H₂O, using coefficients only."

- question: "What is the correct coefficient for O₂ in the balanced combustion equation for propane: C₃H₈ + _O₂ → 3CO₂ + 4H₂O?"
  type: multiple-choice
  options:
    - "3"
    - "4"
    - "5"
    - "8"
  answer: 2
  explanation: "Count oxygen atoms on the right: 3 CO₂ contributes 6 oxygen atoms; 4 H₂O contributes 4 more = 10 total. Each O₂ molecule supplies 2 oxygen atoms, so you need 10 ÷ 2 = 5 O₂. The fully balanced equation is C₃H₈ + 5O₂ → 3CO₂ + 4H₂O, which conserves 3 carbons, 8 hydrogens, and 10 oxygens on each side."

- question: "To balance a chemical equation, you may change the subscripts in a formula if the coefficients alone cannot produce equal atom counts on both sides."
  type: true-false
  answer: false
  explanation: "Subscripts are never changed to balance an equation. A subscript defines the chemical identity of a substance — H₂O and H₂O₂ are fundamentally different compounds. Changing a subscript does not balance the equation; it changes what the equation describes. Only coefficients (the numbers in front of complete formulas) are adjusted. If atom counts cannot be balanced without changing subscripts, the equation itself is incorrectly written."

- question: "In a complete combustion reaction of any hydrocarbon (compound containing only carbon and hydrogen), the products are always carbon dioxide and water."
  type: true-false
  answer: true
  explanation: "Complete combustion of a hydrocarbon by definition means fully oxidizing all carbon to CO₂ and all hydrogen to H₂O. The pattern holds regardless of the hydrocarbon's size or structure: CH₄ → CO₂ + H₂O; C₈H₁₈ → CO₂ + H₂O; C₃H₈ → CO₂ + H₂O. Recognizing this reaction type lets you predict products before balancing, which is one of the practical payoffs of learning reaction classifications."

- question: "Why is it incorrect to change subscripts when balancing a chemical equation, even if doing so would make the atom counts equal?"
  type: short-answer
  answer: "Subscripts define the molecular formula — they specify the exact ratio of atoms bonded together in that compound. Changing a subscript creates a different chemical substance with different properties, bonds, and behavior. Balancing requires accounting for the same substances on both sides; substituting a different compound violates this requirement and misrepresents the chemistry. Coefficients, by contrast, simply state how many formula units participate — they scale quantities without altering identities."
  explanation: "A classic example: changing H₂O to H₂O₂ might seem to 'fix' the oxygen count, but it converts water to hydrogen peroxide — which has a peroxide bond, different reactivity, and different density. The resulting equation no longer describes the reaction that actually occurs. Conservation of mass requires the same substances before and after, just in different proportions — which is exactly what coefficients (not subscript changes) accomplish."
```

## Explainer

A chemical equation is the sentence structure of chemistry — it tells you what reacts, what forms, and in what proportions. The reactants go on the left side of an arrow, the products on the right, and the arrow itself means "yields" or "produces." From your earlier study of matter classification, you know that atoms are neither created nor destroyed in ordinary chemical reactions. This is the **law of conservation of mass**, and it imposes a rigid constraint: every atom that appears on the left must also appear on the right. A balanced equation satisfies this constraint.

The key tool for balancing is the **coefficient** — the number placed in front of a formula. Coefficients multiply every atom in that formula. For example, placing a 2 in front of H₂O means two water molecules: 4 hydrogen atoms and 2 oxygen atoms total. Critically, you never change **subscripts** to balance an equation, because subscripts define what the substance *is*. Changing H₂O to H₂O₂ does not balance water — it turns it into hydrogen peroxide, a completely different compound.

A practical strategy for balancing works in most cases: start by balancing elements that appear in only one compound on each side, save hydrogen and oxygen for last (since they often appear in multiple compounds), and balance polyatomic ions as a unit when they pass through unchanged. Consider the combustion of propane: C₃H₈ + O₂ → CO₂ + H₂O. Carbon appears in one reactant and one product, so balance it first: you need 3 CO₂. Hydrogen appears in one reactant and one product: 8 hydrogens require 4 H₂O. Now count oxygen on the right: 3(2) + 4(1) = 10 oxygen atoms, requiring 5 O₂ on the left. The balanced equation C₃H₈ + 5O₂ → 3CO₂ + 4H₂O now conserves every atom.

Beyond simple balancing, learning to recognize **reaction types** accelerates your ability to predict products. In a **synthesis** (combination) reaction, two or more substances merge into one (A + B → AB). In a **decomposition**, one substance breaks apart (AB → A + B). **Single replacement** reactions swap one element for another in a compound (A + BC → AC + B), while **double replacement** reactions exchange partners between two compounds (AB + CD → AD + CB). **Combustion** of hydrocarbons always produces CO₂ and H₂O. Recognizing the pattern tells you what products to expect before you even start balancing — and balanced equations are the foundation for every stoichiometric calculation that follows.
