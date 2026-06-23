---
id: polyprotic-acids
title: Polyprotic Acids
domain: chemistry
course: general-chemistry
prerequisites:
- id: weak-acid-ionization
  type: hard
tags:
- diprotic
- triprotic
- Ka1
- Ka2
- Ka3
- sequential-ionization
- phosphoric-acid
- sulfuric-acid
stage: formal-systems
status: validated
---
# Polyprotic Acids

## Core Idea
Polyprotic acids can donate more than one proton per molecule, ionizing in sequential steps. Each successive ionization has a smaller Ka (Ka₁ >> Ka₂ >> Ka₃) because removing a proton from an increasingly negative species requires more energy. For most polyprotic acids, the pH is determined almost entirely by the first ionization — the second and third contribute negligibly to [H⁺]. Sulfuric acid is a notable exception: its first ionization is strong (complete), so Ka₂ must be used for the second proton. Intermediate species (like HCO₃⁻ or H₂PO₄⁻) are amphoteric — they can act as either acid or base.

## How It's Best Learned
Solve the first ionization as a standard weak acid ICE table, then verify that the second ionization's contribution to [H⁺] is negligible (typically [H⁺] from Ka₂ ≈ Ka₂ itself when Ka₁ >> Ka₂). For the pH of an amphoteric intermediate, use the formula pH ≈ ½(pKa₁ + pKa₂).

## Common Misconceptions
- Students often try to solve all ionizations simultaneously. Because Ka₁ >> Ka₂, the ionizations can be treated as independent sequential equilibria — the first is solved, and its result becomes the initial condition for the second.
- The concentration of the doubly-deprotonated species is approximately equal to Ka₂ (not dependent on initial concentration), a counterintuitive result that follows directly from the algebra of sequential equilibria.

## Questions

```yaml
- question: "You dissolve 0.10 M H₃PO₄ in water. A student sets up three simultaneous equilibrium expressions — one for each ionization — and solves them together to find the exact pH. What is the conceptual problem with this approach?"
  type: multiple-choice
  options:
    - "There is no problem; solving all three simultaneously gives the most accurate result"
    - "The student should use the Henderson-Hasselbalch equation instead of Ka expressions for polyprotic acids"
    - "Because Ka₁ >> Ka₂ >> Ka₃, the ionizations can be treated as sequential and independent; solving only Ka₁ with an ICE table gives pH accurate enough that subsequent ionizations contribute negligible H⁺"
    - "Only Ka₃ matters because it governs the final equilibrium state of the system"
  answer: 2
  explanation: "The enormous difference between successive Ka values (roughly 10⁵-fold for H₃PO₄) means each ionization essentially completes before the next begins. The H⁺ produced by the first step suppresses subsequent ionizations via Le Chatelier's principle, and Ka₂ and Ka₃ are already tiny. Treating all three as simultaneous creates a needlessly complex system; sequential treatment gives essentially the same answer. The simplification is justified by the physics, not just mathematical convenience."

- question: "For a solution of H₂CO₃ (Ka₁ = 4.3 × 10⁻⁷, Ka₂ = 4.7 × 10⁻¹¹), which statement best describes the concentration of CO₃²⁻ at equilibrium?"
  type: multiple-choice
  options:
    - "[CO₃²⁻] ≈ √(Ka₁ × C), where C is the initial H₂CO₃ concentration"
    - "[CO₃²⁻] ≈ Ka₁, because the first ionization dominates the equilibrium"
    - "[CO₃²⁻] ≈ Ka₂ ≈ 4.7 × 10⁻¹¹ M, nearly independent of the initial acid concentration"
    - "[CO₃²⁻] cannot be estimated without solving all equilibria simultaneously"
  answer: 2
  explanation: "This counterintuitive result follows directly from the algebra of sequential equilibria. After solving Ka₁, [H⁺] ≈ [HCO₃⁻]. Substituting into the Ka₂ expression: Ka₂ = [H⁺][CO₃²⁻]/[HCO₃⁻] ≈ [H⁺][CO₃²⁻]/[H⁺] = [CO₃²⁻]. So [CO₃²⁻] ≈ Ka₂, regardless of the initial concentration. This elegant simplification is a direct consequence of Ka₁ >> Ka₂."

- question: "For most diprotic and triprotic weak acids, the pH of the solution is determined almost entirely by the first ionization because Ka₁ >> Ka₂."
  type: true-false
  answer: true
  explanation: "When Ka₁ >> Ka₂, the H⁺ already present from the first ionization suppresses the second ionization (Le Chatelier's principle), and Ka₂ itself is so small that even if it proceeded fully, its H⁺ contribution would be negligible. Solving the Ka₁ ICE table and verifying that Ka₂'s contribution is small (often ≈ Ka₂ itself) is the standard procedure, and the approximation holds well for most polyprotic acids."

- question: "Sulfuric acid can be treated like other diprotic acids — solve Ka₁ first, then check if Ka₂ contributes negligibly to the final pH."
  type: true-false
  answer: false
  explanation: "H₂SO₄ is a special case because its first ionization is strong (complete dissociation), not weak. Ka₁ is effectively infinite, so the first proton fully dissociates. The second proton has Ka₂ = 1.2 × 10⁻², which is not negligible — especially in dilute solutions where the bisulfate ion's additional dissociation significantly affects [H⁺]. You must explicitly account for Ka₂ in H₂SO₄ calculations, unlike with H₃PO₄ or H₂CO₃."

- question: "Why is the concentration of the doubly-deprotonated species in a polyprotic acid solution approximately equal to Ka₂, and why is this result independent of the initial acid concentration?"
  type: short-answer
  answer: "After solving the first ionization, [H⁺] ≈ [HA⁻]. Substituting these into the Ka₂ expression — Ka₂ = [H⁺][A²⁻]/[HA⁻] — gives Ka₂ ≈ [H⁺][A²⁻]/[H⁺] = [A²⁻]. Since the initial concentration cancels out of the ratio, [A²⁻] ≈ Ka₂ regardless of how concentrated the original acid was."
  explanation: "This result is one of the most useful shortcuts in polyprotic acid chemistry. It holds because the first ionization sets [H⁺] ≈ [HA⁻], creating a 1:1 ratio in the denominator of Ka₂ that exactly cancels [H⁺] from the numerator. The independence from initial concentration is counterintuitive but follows cleanly from the algebra — the concentration terms divide out."
```

## Explainer

From weak acid ionization, you know how to set up an ICE table for a monoprotic acid like acetic acid: it partially ionizes, and Ka tells you the equilibrium ratio of products to reactant. A **polyprotic acid** is simply an acid with more than one ionizable proton — **diprotic** acids like H₂SO₄ and H₂CO₃ can donate two protons, and **triprotic** acids like H₃PO₄ can donate three. The essential new idea is that these protons come off **one at a time**, in sequential equilibria, each with its own Ka.

The reason for sequential ionization is electrostatic: after the first proton leaves, the remaining species carries a negative charge. Removing a second proton from a negatively charged ion is harder — you are pulling a positive charge away from something that is already pulling it inward. This is why Ka₁ is always much larger than Ka₂, which is much larger than Ka₃. For phosphoric acid, the ratios are dramatic: Ka₁ = 7.5 × 10⁻³, Ka₂ = 6.2 × 10⁻⁸, Ka₃ = 4.2 × 10⁻¹³. Each successive ionization is roughly 100,000 times weaker than the one before it.

This enormous drop in Ka values leads to a practical simplification: **the first ionization dominates the pH calculation**. When you dissolve H₃PO₄ in water, the first ionization produces H⁺ and H₂PO₄⁻. You solve this exactly as you would for a monoprotic weak acid using Ka₁ and an ICE table. The H⁺ produced by the first step suppresses the second ionization (Le Chatelier's principle), and since Ka₂ is already tiny, the second ionization contributes a negligible amount of additional H⁺. You can verify this: after solving the first equilibrium, plug the results into the Ka₂ expression and confirm that the additional [H⁺] is insignificant. A useful shortcut emerges from this algebra — the concentration of the doubly-deprotonated species (like HPO₄²⁻) is approximately equal to Ka₂ regardless of the initial acid concentration.

**Sulfuric acid** is the important exception. Its first ionization is strong (complete dissociation: H₂SO₄ → H⁺ + HSO₄⁻), so Ka₁ is effectively infinite. This means you cannot ignore the second ionization the way you normally would — you must use Ka₂ (1.2 × 10⁻²) to calculate how much additional H⁺ the bisulfate ion contributes, especially in dilute solutions where it matters most. The intermediate species of polyprotic acids — HSO₄⁻, HCO₃⁻, H₂PO₄⁻ — are **amphoteric**: they can donate a proton (acting as an acid) or accept one (acting as a base). To find the pH of a solution of an amphoteric intermediate, a clean approximation is pH ≈ ½(pKa₁ + pKa₂), which averages the two equilibria that the species participates in.
