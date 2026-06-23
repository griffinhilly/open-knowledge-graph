---
id: percent-yield-calculations
title: Percent Yield and Reaction Efficiency
domain: chemistry
course: general-chemistry
prerequisites:
- id: limiting-reagent-determination
  type: hard
- id: proportions
  type: soft
- id: percent-yield-and-limiting-reagent-analysis
  type: soft
tags:
- percent yield
- actual yield
- efficiency
stage: formal-systems
status: validated
---
# Percent Yield and Reaction Efficiency

## Core Idea
Percent yield compares actual yield (obtained experimentally) to theoretical yield (calculated from stoichiometry): % yield = (actual/theoretical) × 100%. A percent yield of 100% is ideal; real reactions often give less due to incomplete reactions, side reactions, or product loss. Percent yield measures reaction efficiency.

## Questions

```yaml
- question: "A student runs a reaction and calculates 112% yield. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The reaction was unusually efficient and produced more product than the stoichiometric limit"
    - "The student used the wrong limiting reagent in the theoretical yield calculation"
    - "The isolated product contains impurities — residual solvent, unreacted starting material, or byproducts — that added mass"
    - "Conservation of mass was violated under the reaction conditions"
  answer: 2
  explanation: "A percent yield above 100% is not physically possible — the theoretical yield is an absolute ceiling set by stoichiometry and conservation of mass. A value over 100% signals an error: the 'product' mass includes something extra, most commonly residual solvent that wasn't fully dried, unreacted starting material that wasn't washed away, or byproducts. The student should re-dry and re-weigh. Option B could cause an incorrect theoretical yield calculation, but that would give an unexpectedly high or low percent, not specifically >100%."

- question: "A five-step synthesis has each individual step running at 85% yield. What is the overall percent yield of the complete synthesis?"
  type: multiple-choice
  options:
    - "85% — yield is determined by the lowest single step"
    - "17% — losses add across five steps"
    - "44% — losses multiply across five steps (0.85⁵ ≈ 0.444)"
    - "75% — the average yield across steps"
  answer: 2
  explanation: "Yields compound multiplicatively, not additively. Each step retains only 85% of the material from the previous step: 0.85 × 0.85 × 0.85 × 0.85 × 0.85 = 0.85⁵ ≈ 0.444, or about 44%. This is why organic chemists obsess over yield optimization even for 'good' yields — a 5-step synthesis at 90% per step gives only 59% overall, and at 80% per step gives only 33%."

- question: "A percent yield of 100% is achievable with sufficiently careful laboratory technique."
  type: true-false
  answer: false
  explanation: "100% yield is virtually unattainable in practice. Mechanical losses are unavoidable: some product always clings to glassware walls, is lost in transfers, remains dissolved in wash solvents, or is destroyed by side reactions. Conservation of mass still holds — the 'missing' product is physically somewhere — but it cannot all be recovered. Experienced chemists consider yields above 90% excellent for most reaction types. A reported yield of exactly 100% should itself raise suspicion that the product is not fully pure."

- question: "A reversible reaction that reaches equilibrium before all reactants are consumed will produce a percent yield less than 100% even if no product is physically lost."
  type: true-false
  answer: true
  explanation: "Incomplete reaction is one of the main reasons real yields fall short. If a reaction is reversible, it reaches an equilibrium state where both reactants and products are present simultaneously. The theoretical yield assumes complete conversion of the limiting reagent, but equilibrium stops the reaction before that point. Le Chatelier's principle can be used to push the equilibrium toward products (e.g., removing product as it forms), but some shortfall is inherent in reversible systems."

- question: "A student obtains 110% yield and declares the experiment a success. What does this result actually indicate, and what should the student do next?"
  type: short-answer
  answer: "A 110% yield is impossible — conservation of mass prevents producing more product than the stoichiometric maximum. The result indicates the isolated 'product' contains impurities that added mass. The student should re-dry the product completely (to remove residual solvent), confirm purity by melting point, TLC, or spectroscopy, wash away unreacted starting material if present, and recalculate yield from the pure product mass."
  explanation: "The theoretical yield is a hard ceiling derived from stoichiometry. Anything above it means the measured mass includes something that is not the desired product. Common culprits are residual solvent (not dried long enough), starting material that co-crystallized with the product, or inorganic salt byproducts not washed away. Reporting >100% without investigating is an error in laboratory practice."
```

## Explainer

From your work with limiting reagents, you know how to calculate the maximum amount of product a reaction can theoretically produce — that calculation assumes every molecule of the limiting reagent converts perfectly into product. This calculated maximum is the **theoretical yield**. In an actual laboratory or industrial setting, you weigh or measure the product you actually isolate after the reaction is complete, and this is the **actual yield**. Percent yield compares the two: % yield = (actual yield / theoretical yield) × 100%.

A simple example makes the calculation concrete. Suppose you react 10.0 g of hydrogen gas with excess oxygen to form water. Stoichiometry tells you the theoretical yield is 89.4 g of water. But after collecting and measuring, you recover only 75.0 g. Your percent yield is (75.0 / 89.4) × 100% = 83.9%. The "missing" 14.4 g did not vanish — conservation of mass still holds. It was lost to practical realities: some water vapor escaped before you could collect it, some remained as droplets on the walls of the apparatus, or a small side reaction consumed some of the hydrogen.

Understanding *why* yields fall below 100% is as important as calculating the number. **Incomplete reactions** stop short of full conversion, especially reversible reactions that reach equilibrium with both reactants and products still present. **Side reactions** divert some starting material into unwanted byproducts — for instance, organic reactions frequently produce isomers or oxidation products alongside the intended product. **Mechanical losses** occur during transfers between containers, filtration, or purification steps; every time you pour, filter, or recrystallize, a small amount of product stays behind. In multi-step synthesis, these losses compound — if each step has 90% yield, a five-step synthesis yields only 0.9⁵ = 59% overall.

Percent yield is a practical metric that guides decisions in both the lab and industry. A research chemist seeing consistently low yields might change reaction conditions — temperature, solvent, catalyst, or concentration — to improve efficiency. In manufacturing, even a few percentage points of yield improvement can translate into significant cost savings. Note that percent yields above 100% are not physically meaningful — they signal an error, typically that the product is impure (contaminated with solvent, unreacted starting material, or byproducts that add mass) or that a measurement was inaccurate. A yield of 100% itself is virtually unattainable in practice; experienced chemists consider yields above 90% excellent for most reaction types.
