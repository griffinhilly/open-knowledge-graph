---
id: carbocation-rearrangement-1-2-shifts
title: 'Carbocation Rearrangement: 1,2-Hydride and 1,2-Alkyl Shifts'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbocation-stability-rearrangement
  type: soft
- id: e1-elimination
  type: soft
- id: addition-to-alkynes
  type: soft
builds-toward:
- oxymercuration-mechanism
tags:
- mechanism
- rearrangement
- carbocation
- hydride-shift
- alkyl-shift
stage: formal-systems
status: validated
---

# Carbocation Rearrangement: 1,2-Hydride and 1,2-Alkyl Shifts

## Core Idea
Carbocations can undergo 1,2-hydride or 1,2-alkyl shifts from an adjacent carbon to form more stable carbocations. These rearrangements occur when a secondary carbocation can rearrange to a tertiary (more stable) one. The migrating group moves with its bonding electrons toward the carbocation center.

## How It's Best Learned
Identify secondary vs. tertiary carbocations and predict which rearrangements increase stability. Draw electron flow diagrams for hydride and alkyl shifts.

## Common Misconceptions
- Assuming all carbocations rearrange; rearrangement only occurs if it leads to a more stable carbocation.
- Misunderstanding the electron flow; the migrating group's bonding electrons move toward the positive charge, not away.

## Questions

```yaml
- question: "Treating 3-methyl-2-butanol with concentrated H₂SO₄ gives 2-methylbut-2-ene as the major product rather than 3-methylbut-1-ene. What best explains this observation?"
  type: multiple-choice
  options:
    - "The initially formed secondary carbocation at C2 undergoes a 1,2-hydride shift to a more stable tertiary carbocation at C3, and elimination from this rearranged intermediate gives the observed alkene"
    - "Dehydration follows Zaitsev's rule, which always produces the more substituted alkene without any carbocation rearrangement"
    - "The reaction proceeds via a concerted E2 mechanism that bypasses carbocation intermediates and directly forms the more stable alkene"
    - "A 1,2-methyl shift converts the secondary carbocation at C2 to a primary carbocation at C1, which is then stabilized by resonance"
  answer: 0
  explanation: "The 2° carbocation initially formed at C2 is adjacent to C3, a tertiary carbon (bearing three alkyl substituents). A 1,2-hydride shift from C3 to C2 produces a more stable 3° carbocation at C3. Elimination from this rearranged cation gives the methylbutene products. Option B is the classic misconception — it invokes Zaitsev's rule without rearrangement, but Zaitsev alone cannot explain why the product carbon skeleton differs from what simple elimination would predict. Rearrangements must be identified before applying regiochemistry rules."

- question: "In a 1,2-hydride shift, which arrow correctly represents the electron flow?"
  type: multiple-choice
  options:
    - "A curved arrow from the C–H bond on the adjacent carbon toward the empty p orbital of the carbocation"
    - "A curved arrow from the empty p orbital of the carbocation toward the C–H bond on the adjacent carbon"
    - "A curved arrow from the positively charged carbon toward a lone pair on the migrating hydrogen"
    - "Two curved arrows: one showing H⁺ departure and one showing proton capture by the cation"
  answer: 0
  explanation: "Electron flow always runs from electron-rich to electron-poor — from the C–H bonding pair toward the empty p orbital. The hydrogen migrates as a hydride (H:⁻, with both bonding electrons), not as a proton. Option B reverses the arrow direction, which would imply electron flow from an empty orbital — physically impossible. Option D describes a proton transfer mechanism, which is a different type of reaction and would not shift carbon connectivity."

- question: "A secondary carbocation adjacent to a tertiary carbon will generally rearrange to a tertiary carbocation before reacting with a nucleophile."
  type: true-false
  answer: true
  explanation: "The 1,2-hydride shift from the adjacent C–H bond into the empty p orbital has a very low energy barrier — just the orbital overlap requirement — and is thermodynamically favorable because it generates a more stable carbocation. This rearrangement typically occurs faster than nucleophilic capture of the less stable secondary cation. As a practical rule: whenever a carbocation is adjacent to a carbon bearing a hydrogen that would generate a more substituted cation upon migration, assume rearrangement occurs and draw the new intermediate before predicting the product."

- question: "A 1,2-alkyl shift typically involves a methyl group, since smaller groups migrate more readily than larger alkyl substituents."
  type: true-false
  answer: false
  explanation: "Any alkyl group on the adjacent carbon can undergo a 1,2-shift — methyl, ethyl, isopropyl, or more complex groups. The driving force is thermodynamic stability gain, not the size of the migrating group. 'Methyl shift' refers specifically to migration of a –CH₃ group, but '1,2-alkyl shift' encompasses any carbon group. Larger alkyl groups actually tend to stabilize the resulting carbocation more effectively through hyperconjugation and inductive effects, providing additional driving force."

- question: "Why is it essential to check for possible carbocation rearrangements before predicting the final product of a reaction that proceeds through a carbocation intermediate?"
  type: short-answer
  answer: "If the initial carbocation rearranges to a more stable one, the final product forms from the rearranged intermediate — not from the original carbocation. The regiochemistry of addition, substitution, or elimination depends entirely on which carbocation undergoes the final step. Failing to account for rearrangement leads to predicting the wrong constitutional isomer as the major product."
  explanation: "Rearrangement is driven by thermodynamics: the more stable carbocation is the 'sink' that the mechanism flows toward. Once rearrangement occurs, the new carbocation dictates the product's carbon skeleton — which may differ entirely from what the starting material's connectivity suggests. This is why predicting correct products in multi-step synthesis requires checking: does the initially formed cation have a neighboring carbon that could donate a hydride or alkyl group to form a more substituted cation? If yes, draw the rearranged intermediate first."
```

## Explainer

You already know that carbocations are classified by substitution — primary, secondary, tertiary — and that more substituted carbocations are more stable due to hyperconjugation and inductive effects. **Carbocation rearrangement** is the direct consequence of this stability hierarchy: if a reaction generates a less stable carbocation and a more stable one is just one bond-shift away, the rearrangement will happen, often faster than any competing reaction. This is not an optional side reaction — it is a thermodynamic imperative that the mechanism follows automatically.

A **1,2-hydride shift** is the most common rearrangement. Imagine a secondary carbocation on carbon-2 of a chain, with a tertiary carbon adjacent at carbon-3 bearing a hydrogen. The hydrogen on carbon-3 migrates *with its bonding electrons* to the positively charged carbon-2. The result: the positive charge has moved from carbon-2 (secondary) to carbon-3 (now tertiary, because the hydrogen left). Crucially, what migrates is not a bare proton (H⁺) — it is a hydride (H:⁻), carrying the bonding pair. The electron flow arrow points from the C–H bond toward the empty p orbital of the carbocation. This is why the shift is drawn as a curved arrow from the adjacent C–H bond to the cation center.

A **1,2-alkyl shift** (also called a 1,2-methyl shift when the migrating group is –CH₃) works identically, except an entire alkyl group migrates with its bonding electrons instead of a hydrogen. This occurs when no hydride shift can improve stability, but moving an alkyl group can. For example, a secondary carbocation adjacent to a quaternary carbon (which has no hydrogen to shift) can rearrange via methyl migration to form a tertiary carbocation. The principle is the same: the group moves toward the positive charge, carrying its electrons with it.

Not every carbocation rearranges. The shift only occurs if it leads to a *more stable* carbocation — secondary to tertiary, or secondary to a resonance-stabilized cation. A tertiary carbocation adjacent to another tertiary carbon has no driving force to rearrange and will proceed directly to product. When predicting products, always check: does the initially formed carbocation have a neighboring carbon that could donate a hydride or alkyl group to produce a more substituted cation? If yes, draw the rearranged intermediate *before* predicting the final product. Failing to check for rearrangement is one of the most common mistakes in organic mechanism problems, leading to incorrect regiochemistry in addition, substitution, and elimination products.
