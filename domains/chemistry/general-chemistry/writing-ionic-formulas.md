---
id: writing-ionic-formulas
title: Writing Chemical Formulas for Ionic Compounds
domain: chemistry
course: general-chemistry
prerequisites:
- id: ionic-bonding-formation
  type: hard
builds-toward:
- chemical-equations-and-balancing
tags:
- ionic formulas
- charge balance
- cations
- anions
stage: advanced
status: draft
---

# Writing Chemical Formulas for Ionic Compounds

## Core Idea
Ionic formulas are determined by balancing positive (cation) and negative (anion) charges. The formula shows the simplest whole-number ratio of ions, with no net charge. Polyatomic ions are written as units. The cation is named first, followed by the anion. Understanding charge and valence is essential for writing correct formulas.

## Questions

```yaml
- question: "What is the correct formula for calcium nitrate, formed from Ca²⁺ and NO₃⁻?"
  type: multiple-choice
  options:
    - "CaNO₃"
    - "Ca(NO₃)₂"
    - "CaN₂O₆"
    - "Ca₂NO₃"
  answer: 1
  explanation: "Ca²⁺ requires two NO₃⁻ ions to achieve charge neutrality (+2 and 2×−1). The entire nitrate unit must be enclosed in parentheses before adding the subscript: Ca(NO₃)₂. Writing CaNO₃ omits the second nitrate; writing CaN₂O₆ incorrectly expands the polyatomic ion instead of using parentheses. The parentheses are essential — the subscript applies to the whole NO₃⁻ group."

- question: "Applying the criss-cross method to Mg²⁺ and O²⁻ produces the preliminary formula Mg₂O₂. What is the correct final ionic formula?"
  type: multiple-choice
  options:
    - "Mg₂O₂, because ionic formulas preserve the subscripts from the criss-cross method exactly"
    - "MgO, because ionic formulas must be reduced to the simplest whole-number ratio"
    - "MgO₂, because the oxygen subscript is always kept when it exceeds 1"
    - "Mg₂O, because the cation subscript is retained and the anion subscript is dropped when equal"
  answer: 1
  explanation: "The criss-cross method gives a starting point, but you must always reduce the ratio to its simplest form. Mg₂O₂ has a 2:2 ion ratio, which simplifies to 1:1, giving MgO. A common error is treating the criss-cross result as final without checking for simplification."

- question: "The formula CaCl₂ represents a discrete molecule in which one calcium atom is covalently bonded to two chlorine atoms."
  type: true-false
  answer: false
  explanation: "Ionic formulas represent the simplest ratio of ions in an extended crystal lattice, not discrete covalently bonded molecules. In solid CaCl₂, each calcium ion is surrounded by multiple chloride ions and vice versa — there is no identifiable 'molecule.' The formula unit CaCl₂ simply expresses that the Ca²⁺ to Cl⁻ ratio in the lattice is 1:2."

- question: "When writing the formula for a compound that requires more than one polyatomic ion, the polyatomic ion must be enclosed in parentheses before adding the subscript."
  type: true-false
  answer: true
  explanation: "Parentheses are required because the subscript must apply to the entire polyatomic ion as a unit. For example, Ca(NO₃)₂ correctly indicates two complete NO₃⁻ groups. Without parentheses, CaNO₃₂ is ambiguous and chemically meaningless — it could be misread as a formula with 32 oxygen atoms or other errors."

- question: "Why must you reduce the ratio to its simplest whole numbers after applying the criss-cross method? Give an example where failing to do so would produce a wrong formula."
  type: short-answer
  answer: "Ionic formulas express the simplest whole-number ratio of ions — the empirical ratio in the crystal lattice. The criss-cross method ensures charge balance but can produce non-simplified ratios. For example, Mg²⁺ and O²⁻ criss-cross to Mg₂O₂, but the correct formula is MgO (ratio 1:1). Reporting Mg₂O₂ implies a different compound than MgO and would give incorrect molar masses and stoichiometric calculations."
  explanation: "Simplification is required because ionic formulas are empirical — they describe the fundamental ratio, not the absolute count of ions. Two formulas with the same ratio (MgO and Mg₂O₂) describe the same compound; only the simplified form is the accepted convention."
```

## Explainer

You already understand that ionic bonds form when a metal transfers electrons to a nonmetal, producing a positively charged **cation** and a negatively charged **anion**. Writing the formula for the resulting compound is essentially a charge-balancing exercise: the total positive charge must exactly cancel the total negative charge so that the compound is electrically neutral.

The procedure is straightforward. First, identify the charges on each ion. Sodium is Na⁺, chloride is Cl⁻ — one of each gives NaCl with zero net charge. But consider calcium (Ca²⁺) and chloride (Cl⁻): one calcium ion carries +2, so you need two chloride ions at −1 each to balance. The formula is CaCl₂. A useful shortcut is the **criss-cross method**: take the magnitude of each ion's charge and use it as the subscript for the other ion. For Al³⁺ and O²⁻, the 3 becomes oxygen's subscript and the 2 becomes aluminum's, giving Al₂O₃. Always reduce to the simplest whole-number ratio — Mg²⁺ and O²⁻ would criss-cross to Mg₂O₂, but that simplifies to MgO.

**Polyatomic ions** — groups like sulfate (SO₄²⁻), nitrate (NO₃⁻), or ammonium (NH₄⁺) — are treated as single units. When you need more than one of a polyatomic ion, enclose it in parentheses before adding the subscript. Calcium nitrate is Ca(NO₃)₂, not CaNO₃₂, because the subscript 2 applies to the entire NO₃⁻ unit. Forgetting the parentheses changes the meaning of the formula entirely.

Two conventions complete the picture. The cation is always written first in the formula, regardless of how the compound is named verbally — so it is Na₂SO₄, never SO₄Na₂. And ionic formulas represent the simplest ratio of ions in the crystal lattice, not a discrete molecule. NaCl does not mean one sodium atom is bonded to one chlorine atom in isolation; it means the ratio of sodium to chloride in the extended crystal is 1:1. This distinction between formula units and molecules matters when you move into stoichiometry and solution chemistry.
