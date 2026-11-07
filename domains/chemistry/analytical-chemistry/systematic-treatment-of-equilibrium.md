---
id: systematic-treatment-of-equilibrium
title: Systematic Treatment of Equilibrium (Charge and Mass Balance)
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: weak-acid-ionization
  type: hard
- id: polyprotic-acids
  type: soft
- id: ph-and-acid-base-calculations
  type: soft
- id: activity-coefficients-ionic-strength
  type: soft
builds-toward: []
tags:
- charge balance
- mass balance
- simultaneous equilibria
- equilibrium calculations
- approximations
stage: advanced
status: validated
---

# Systematic Treatment of Equilibrium (Charge and Mass Balance)

## Core Idea
When several equilibria act at once, ICE tables and guesses about which reaction dominates can fail. The systematic treatment writes down every relevant reaction and then two kinds of bookkeeping equations: a charge balance, stating that the solution is electrically neutral, and mass balances, stating that atoms added to the solution are conserved among all their forms. Together with the equilibrium-constant expressions, these give as many equations as unknowns, so the problem can be solved exactly or with clearly stated approximations.

## How It's Best Learned
Follow a fixed recipe on small problems: list reactions, write the charge balance, write mass balances, write the K expressions, count equations and unknowns, then solve. Start with a case where the shortcut fails, such as 1.0 × 10⁻⁸ M HCl, to see why the method is worth learning. Then apply it to a polyprotic acid and to a slightly soluble salt whose anion is basic.

## Common Misconceptions
- A charge balance sets the total concentration of cations equal to the total concentration of anions. (Each concentration must be multiplied by the magnitude of its charge, so [SO₄²⁻] enters as 2[SO₄²⁻].)
- The pH of a very dilute strong acid is just −log of its concentration. (At 1.0 × 10⁻⁸ M HCl, that would give a basic pH of 8; including water's autoionization through the charge balance gives about 6.98.)
- Mass balances and charge balances are the same equation. (A mass balance tracks one element or group across its chemical forms; the charge balance tracks electrical neutrality across all ions.)

## Questions

```yaml
- question: "Which is the correct charge balance for an aqueous solution of phosphoric acid, H₃PO₄?"
  type: multiple-choice
  options: ["[H⁺] = [H₂PO₄⁻] + [HPO₄²⁻] + [PO₄³⁻] + [OH⁻]", "[H⁺] = [H₂PO₄⁻] + 2[HPO₄²⁻] + 3[PO₄³⁻] + [OH⁻]", "3[H⁺] = [PO₄³⁻] + [OH⁻]", "[H₃PO₄] = [H₂PO₄⁻] + [HPO₄²⁻] + [PO₄³⁻]"]
  answer: 1
  explanation: "Positive charge comes only from H⁺. Each anion contributes its concentration times its charge, so HPO₄²⁻ counts twice and PO₄³⁻ three times. The last option is a mistaken mass balance, not a charge balance."
- question: "In a charge balance, the concentration of a 2− ion is multiplied by 2."
  type: true-false
  answer: true
  explanation: "One mole of a 2− ion carries two moles of negative charge. Neutrality requires the total positive charge to equal the total negative charge, so each concentration is weighted by the size of its charge."
- question: "A solution is made with 0.050 mol of acetic acid per liter. Which mass balance is correct?"
  type: multiple-choice
  options: ["0.050 = [CH₃COOH]", "0.050 = [CH₃COO⁻]", "0.050 = [CH₃COOH] + [CH₃COO⁻]", "0.050 = [H⁺] + [CH₃COO⁻]"]
  answer: 2
  explanation: "All the acetate groups added must be present as either the undissociated acid or the acetate ion. The mass balance adds every form of the same group."
- question: "Use the charge balance and Kw = 1.0 × 10⁻¹⁴ to find the pH of 1.0 × 10⁻⁸ M HCl."
  type: short-answer
  answer: "About 6.98"
  explanation: "Charge balance: [H⁺] = [Cl⁻] + [OH⁻] = 1.0 × 10⁻⁸ + Kw/[H⁺]. Solving [H⁺]² − (1.0 × 10⁻⁸)[H⁺] − 1.0 × 10⁻¹⁴ = 0 gives [H⁺] ≈ 1.05 × 10⁻⁷ M, so pH ≈ 6.98. Water's own H⁺ dominates."
```

## Explainer

Most equilibrium problems in general chemistry are solved with one reaction and an ICE table. That works when one equilibrium clearly dominates. Real solutions often contain several equilibria at once: an acid dissociating, water autoionizing, a salt dissolving, a metal ion binding a ligand. Guessing which one matters can go wrong. The systematic treatment avoids guessing by writing everything down.

The method has six steps. First, write every relevant chemical reaction. Second, write the charge balance. Third, write the mass balances. Fourth, write the equilibrium-constant expression for each reaction. Fifth, count unknowns and equations; you need as many equations as unknown concentrations. Sixth, solve, making approximations only where you can check them afterward.

The charge balance expresses electrical neutrality. The total positive charge equals the total negative charge, and each concentration is multiplied by the size of its ion's charge. For phosphoric acid in water:

[H⁺] = [H₂PO₄⁻] + 2[HPO₄²⁻] + 3[PO₄³⁻] + [OH⁻]

A mass balance expresses conservation of atoms. Whatever you put in must be found in some form. If you add 0.050 mol of acetic acid per liter, then 0.050 M = [CH₃COOH] + [CH₃COO⁻]. A solution can have several mass balances, one for each element or group you track.

A classic example shows why this matters. What is the pH of 1.0 × 10⁻⁸ M HCl? The shortcut gives pH 8, which would make an acid solution basic. The charge balance is [H⁺] = [Cl⁻] + [OH⁻]. Substitute [Cl⁻] = 1.0 × 10⁻⁸ M and [OH⁻] = Kw/[H⁺], and you get a quadratic in [H⁺]. Its positive root is about 1.05 × 10⁻⁷ M, so the pH is about 6.98. Water's autoionization supplies most of the H⁺, and the shortcut missed it.

For larger problems the algebra can become heavy, and spreadsheets or solvers are used. The approach stays the same. For high accuracy, activities replace concentrations in the K expressions, while the charge and mass balances always use concentrations.
