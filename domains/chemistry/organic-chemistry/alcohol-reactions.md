---
id: alcohol-reactions
title: Reactions of Alcohols
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alcohols-and-ethers
  type: hard
- id: sn1-reaction
  type: hard
- id: e2-elimination
  type: soft
- id: e1-elimination
  type: soft
builds-toward:
- carbonyl-chemistry-intro
tags:
- alcohols
- oxidation
- dehydration
- tosylate
- SOCl2
- PBr3
- PCC
stage: advanced
status: validated
---

# Reactions of Alcohols

## Core Idea
Alcohols are versatile synthetic intermediates that undergo four major reaction types. Dehydration (acid catalyst, heat) converts them to alkenes via E1 (tertiary) or E2 (secondary) mechanisms, following Zaitsev's rule. Conversion to alkyl halides uses SOCl₂ (gives inversion via SN2 with chloride) or PBr₃. Oxidation with PCC (mild) converts primary alcohols to aldehydes and secondary to ketones; stronger oxidants (KMnO₄, CrO₃) carry primary alcohols through to carboxylic acids. Tertiary alcohols resist oxidation because no alpha C–H bond is present. Conversion to tosylates activates the –OH as a leaving group for subsequent SN2 reactions.

## How It's Best Learned
Organize reactions in a grid: substrate class (1°, 2°, 3°) on one axis, reagent on the other, product in each cell. Practice retrosynthetic thinking: given a target molecule, which alcohol starting material and which reaction would give it?

## Common Misconceptions
- PCC stops oxidation at the aldehyde because it is used in anhydrous conditions that prevent hydration to the gem-diol, which would be further oxidized.
- Tertiary alcohol dehydration proceeds by E1, not E2, because the carbocation is especially stable — a strong non-nucleophilic base is not needed.
- SOCl₂ with pyridine gives retention of configuration (via chlorosulfite intermediate attacked by Cl⁻ intramolecularly); without pyridine the result can differ.

## Questions

```yaml
- question: "You want to oxidize a primary alcohol to an aldehyde and stop there — you do not want the carboxylic acid. Which reagent should you use?"
  type: multiple-choice
  options:
    - "KMnO₄ in aqueous acid — a strong oxidant that ensures complete oxidation"
    - "Jones reagent (CrO₃/H₂SO₄) — reliable for primary alcohols"
    - "PCC in anhydrous CH₂Cl₂ — stops at the aldehyde because no water is present to allow further oxidation"
    - "SOCl₂ — converts the alcohol to an acid chloride in one step"
  answer: 2
  explanation: "PCC (pyridinium chlorochromate) in anhydrous dichloromethane is the standard reagent for stopping oxidation of a primary alcohol at the aldehyde stage. The mechanism requires water to hydrate the aldehyde to a gem-diol, which is what gets further oxidized to the carboxylic acid. Anhydrous conditions prevent this hydration, so the reaction stops at the aldehyde. Jones reagent and KMnO₄ (options A and B) are strong oxidants in aqueous conditions that carry the reaction all the way to the carboxylic acid. SOCl₂ (option D) does not oxidize — it converts an alcohol to an alkyl chloride by replacing OH with Cl."

- question: "Why do tertiary alcohols resist oxidation under conditions that oxidize primary and secondary alcohols?"
  type: multiple-choice
  options:
    - "Tertiary alcohols are more stable than primary or secondary alcohols, making them thermodynamically resistant to oxidation"
    - "Tertiary alcohols have a higher boiling point, so common oxidants do not reach them at standard temperatures"
    - "Oxidation of an alcohol requires removing a hydrogen from the carbon bearing the OH group; tertiary alcohols have no such hydrogen, so the oxidation cannot proceed"
    - "Tertiary alcohols form stable carbocations that resist further reaction"
  answer: 2
  explanation: "The oxidation of an alcohol to a carbonyl compound requires removing an α-hydrogen — the hydrogen attached to the carbon bearing the –OH. In a primary alcohol (R-CH₂-OH), there are two such hydrogens; in a secondary alcohol (R₂CH-OH), there is one. In a tertiary alcohol (R₃C-OH), the carbon bearing the hydroxyl has no hydrogens — it is bonded to three carbon substituents instead. There is nothing to remove, so the oxidation mechanism has no available pathway. This is a structural argument, not a thermodynamic or kinetic one: it's not that oxidation is slow or unfavorable for tertiary alcohols — it simply cannot proceed by the required mechanism."

- question: "When SOCl₂ converts an alcohol to an alkyl chloride, the product has inverted configuration at the carbon that bore the hydroxyl group."
  type: true-false
  answer: true
  explanation: "True. The mechanism proceeds through a chlorosulfite intermediate (R-O-SOCl), which activates the oxygen as a leaving group. Chloride ion then attacks the carbon in an SN2 backside attack, inverting the configuration at that carbon — the same Walden inversion seen in all SN2 reactions. This stereochemical outcome is one of the main reasons SOCl₂ is preferred over acid-catalyzed methods (using HCl): acid catalysis often proceeds through a carbocation intermediate (SN1-like), which gives a mixture of configurations. SOCl₂ provides a predictable, clean inversion, making it valuable in synthesis when stereochemical control is needed."

- question: "Acid-catalyzed dehydration of a tertiary alcohol proceeds by an E2 mechanism because the tertiary carbon is more hindered."
  type: true-false
  answer: false
  explanation: "False. Tertiary alcohol dehydration proceeds by E1, not E2. Acid protonates the –OH to give –OH₂⁺ (water as a leaving group). Water then departs to form a stable tertiary carbocation — the most stable type of carbocation — which subsequently loses a proton from an adjacent carbon to give the alkene. The stability of the tertiary carbocation drives the E1 pathway; a strong non-nucleophilic base is not required. E2 requires a strong base to remove the β-hydrogen simultaneously with leaving group departure, avoiding carbocation formation. The common misconception is that bulkier (more substituted) substrates 'favor' E2 because of steric arguments, but in acid-catalyzed reactions, the determining factor is mechanism, not bulk."

- question: "Every major reaction of alcohols is a strategy for solving the same fundamental problem. What is that problem, and how does acid-catalyzed dehydration solve it?"
  type: short-answer
  answer: "The fundamental problem is that –OH is a poor leaving group: hydroxide (HO⁻) is a strong base and will not spontaneously depart from a carbon in any of the standard substitution or elimination mechanisms. Acid-catalyzed dehydration solves this by protonating the –OH group (using H₂SO₄ or H₃PO₄) to convert it to –OH₂⁺ (water). Water is an excellent leaving group — it is a weak base and departs readily. For a tertiary alcohol, this allows a carbocation to form (E1), which then loses a proton to give the alkene. The same logic underlies all alcohol reactions: every reagent — SOCl₂, PBr₃, TsCl, or protonation — is a method for converting the poor –OH leaving group into something that will actually leave."
  explanation: "Understanding the leaving-group problem as the unifying concept makes alcohol chemistry coherent rather than a list of memorized reactions. Once a student sees that every reaction is answering 'how do we activate the OH?' the choice of reagent becomes logical rather than arbitrary: proton acid for elimination/SN1, SOCl₂ or PBr₃ for halide substitution with stereochemical control, TsCl for flexible activation before SN2 with any nucleophile. The reagents are different answers to the same question."
```

## Explainer

You already know that alcohols contain a hydroxyl group (–OH) bonded to an sp³ carbon, and you understand SN1, SN2, E1, and E2 mechanisms. The challenge with alcohols is that hydroxide (HO⁻) is a terrible leaving group — it is a strong base and simply will not depart on its own. Every major reaction class of alcohols is, at its core, a strategy for solving this leaving-group problem.

**Dehydration** is the elimination pathway. Adding a strong acid (H₂SO₄, H₃PO₄) protonates the –OH to give –OH₂⁺, converting it into water — an excellent leaving group. For tertiary alcohols, water departs first to form a carbocation (E1), which then loses a proton from the adjacent carbon to form the alkene. Zaitsev's rule predicts the more substituted alkene as the major product. Secondary alcohols can follow E1 or E2 depending on conditions, while primary alcohols typically require harsher conditions and may rearrange. The key mental model: protonate the oxygen, then apply the elimination mechanism appropriate to the substrate class.

**Conversion to alkyl halides** uses reagents that replace –OH with a halide while bypassing the poor leaving-group problem. SOCl₂ (thionyl chloride) converts alcohols to alkyl chlorides: it first forms a chlorosulfite ester intermediate, activating the oxygen as a leaving group, and then chloride attacks via SN2, giving inversion of configuration at the carbon. PBr₃ works analogously for bromides. These reagents are preferred over simply adding HBr or HCl because they give cleaner stereochemical outcomes and avoid the carbocation rearrangements that plague acid-catalyzed methods with secondary substrates. Converting the alcohol to a **tosylate** (by reacting with TsCl) is another activation strategy — the tosylate group is an outstanding leaving group that can then be displaced by any nucleophile via SN2.

**Oxidation** adjusts the oxidation state of the carbon bearing the –OH. Primary alcohols can be oxidized to aldehydes or all the way to carboxylic acids; secondary alcohols are oxidized to ketones; tertiary alcohols resist oxidation entirely because there is no hydrogen on the carbon bearing the hydroxyl to be removed. The reagent choice controls the outcome: **PCC** (pyridinium chlorochromate) in anhydrous CH₂Cl₂ stops at the aldehyde because without water, the aldehyde cannot hydrate to a gem-diol that would be further oxidized. Stronger oxidants like Jones reagent (CrO₃/H₂SO₄) or KMnO₄ push primary alcohols all the way to the carboxylic acid. The practical takeaway is a decision tree: identify the alcohol class, choose the reagent, predict the product.
