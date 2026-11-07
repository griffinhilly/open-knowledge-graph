---
id: nonaqueous-solvents-and-leveling-effect
title: Nonaqueous Solvents, the Leveling Effect, and Superacids
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: acid-base-definitions
  type: hard
- id: acid-base-strength-ka-kb-calculations
  type: hard
- id: hsab-theory
  type: soft
- id: polar-protic-aprotic-solvents
  type: soft
- id: acidity-organic-compounds-pka
  type: soft
builds-toward: []
tags:
- leveling effect
- differentiating solvent
- liquid ammonia
- solvent system
- superacids
- autoionization
stage: advanced
status: validated
---

# Nonaqueous Solvents, the Leveling Effect, and Superacids

## Core Idea
The solvent sets the limits of acid-base chemistry. In water, every acid stronger than H₃O⁺ ionizes completely, so HCl, HBr and HClO₄ all look equally strong; this is the leveling effect. Less basic solvents such as glacial acetic acid can tell these acids apart, and more basic solvents such as liquid ammonia level even weak acids. Superacids, which are more acidic than 100% sulfuric acid, extend the scale far beyond what water allows.

## How It's Best Learned
Begin with water's autoionization and ask what the strongest acid and strongest base are that can survive in it. Repeat the exercise for liquid ammonia (NH₄⁺ and NH₂⁻) and for acetic acid. Place several acids on one pKa line and mark each solvent's "window" to see which acids are leveled and which are differentiated.

## Common Misconceptions
- HCl and HClO₄ are equally strong acids. (They only appear so in water, which levels both to H₃O⁺; in acetic acid, perchloric acid is measurably stronger.)
- Acid strength is a property of the acid alone. (Ionization is a proton transfer to the solvent, so the solvent's basicity decides how far it goes.)
- pH and Ka values carry over unchanged from water to any solvent. (Each solvent has its own autoionization constant and its own acidity scale.)

## Questions

```yaml
- question: "Why do HCl and HClO₄ show the same acid strength in dilute aqueous solution?"
  type: multiple-choice
  options: ["They have identical Ka values in every solvent", "Water is basic enough to ionize both completely, so both are leveled to H₃O⁺", "Both are diprotic acids", "Their conjugate bases have the same size"]
  answer: 1
  explanation: "Any acid stronger than H₃O⁺ transfers its proton to water essentially completely. The acid that actually remains in solution is H₃O⁺ in both cases, so their intrinsic difference is hidden."
- question: "Acetic acid, a weak acid in water, behaves as a strong acid in liquid ammonia."
  type: true-false
  answer: true
  explanation: "Ammonia is a much stronger base than water. It accepts protons from acetic acid essentially completely, so acetic acid is leveled to NH₄⁺, the strongest acid that can exist in liquid ammonia."
- question: "In liquid ammonia, which species is the strongest base that can exist in the solvent?"
  type: multiple-choice
  options: ["OH⁻", "NH₄⁺", "NH₂⁻", "NH₃"]
  answer: 2
  explanation: "Liquid ammonia autoionizes as 2NH₃ ⇌ NH₄⁺ + NH₂⁻. Any base stronger than the amide ion would deprotonate ammonia and be leveled to NH₂⁻."
- question: "What is a superacid, and why are superacids useful to chemists?"
  type: short-answer
  answer: "A superacid is a medium more acidic than 100% sulfuric acid, such as HSO₃F–SbF₅ (magic acid) or HF–SbF₅. They can protonate very weak bases, including hydrocarbons, and keep carbocations long-lived enough to study."
  explanation: "George Olah used superacid media to observe carbocations directly by NMR, work recognized with the 1994 Nobel Prize in Chemistry. Such media lie far beyond the acidity window of water."
```

## Explainer

When an acid dissolves, it hands a proton to the solvent. The extent of that transfer depends on two things: how readily the acid gives up the proton and how strongly the solvent accepts it. Water accepts protons well enough that any acid stronger than H₃O⁺ ionizes completely. As a result, H₃O⁺ is the strongest acid that can exist in water in appreciable amounts, and OH⁻ is the strongest base. Hydrochloric, hydrobromic, hydroiodic, nitric and perchloric acids all reduce to the same species, H₃O⁺. This is the leveling effect, and water is called a leveling solvent for these acids.

To rank such acids, use a solvent that is a weaker base. Glacial acetic acid accepts protons reluctantly, so strong acids ionize only partly in it, and their differences show up. In acetic acid, perchloric acid is clearly stronger than hydrochloric acid. A solvent that reveals these differences is called a differentiating solvent.

The reverse happens in a strongly basic solvent. Liquid ammonia, which boils at about −33 °C, autoionizes as 2NH₃ ⇌ NH₄⁺ + NH₂⁻. In it, NH₄⁺ plays the role of H₃O⁺ and the amide ion NH₂⁻ plays the role of OH⁻. Because ammonia is far more basic than water, even acetic acid ionizes completely. The solvent-system definition generalizes this: an acid is a solute that raises the concentration of the solvent's own cation, and a base raises the concentration of its anion. Liquid ammonia also dissolves alkali metals to give blue solutions that contain solvated electrons, a strong reducing medium used in organic synthesis.

Going in the acidic direction leads to superacids, defined as media more acidic than 100% sulfuric acid. Mixing a strong Brønsted acid with a strong Lewis acid gives the most extreme examples. Fluorosulfuric acid combined with antimony pentafluoride is called magic acid, and HF with SbF₅ forms fluoroantimonic acid. Because pH does not apply to such media, acidity is measured with the Hammett acidity function, H₀; pure sulfuric acid has H₀ near −12, and superacids lie well below that. These media can protonate alkanes and hold carbocations long enough to record their NMR spectra, the work for which George Olah received the 1994 Nobel Prize in Chemistry.

The general lesson is that every solvent defines a window of usable acidity. Choosing the solvent is a way to choose which acid-base reactions are possible.
