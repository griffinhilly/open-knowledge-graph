---
id: nucleophilic-addition-to-carbonyls
title: Nucleophilic Addition to Aldehydes and Ketones
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbonyl-chemistry-intro
  type: hard
- id: reaction-mechanisms-overview
  type: hard
builds-toward:
- enols-and-enolate-chemistry
- carboxylic-acids-and-derivatives
tags:
- nucleophilic addition
- hemiacetal
- acetal
- imine
- enamine
- cyanohydrin
- Grignard
- reversibility
stage: formal-systems
status: validated
---

# Nucleophilic Addition to Aldehydes and Ketones

## Core Idea
Nucleophilic addition to aldehydes and ketones involves attack of a nucleophile at the electrophilic carbonyl carbon, converting the sp2 carbon to sp3, followed by protonation of the resulting alkoxide. The reaction is fundamentally reversible; equilibrium favors addition for aldehydes more than ketones due to sterics. Key reactions include: hydrate formation (H₂O), hemiacetal and acetal formation (ROH, acid catalysis), imine formation with primary amines, enamine formation with secondary amines, cyanohydrin synthesis (HCN), and Grignard addition (RMgX) to give secondary or tertiary alcohols.

## How It's Best Learned
Draw the complete mechanism including all proton-transfer steps for hemiacetal and acetal formation. Practice predicting whether addition equilibrium favors product based on substrate structure. Compare what product forms when a primary vs secondary amine reacts with an aldehyde.

## Common Misconceptions
- Acetal formation requires acid catalyst throughout and is inhibited by base — reversibility is crucial and pH control is essential.
- Hydrates (gem-diols) are usually unstable in equilibrium with the carbonyl form, with notable exceptions (chloral, formaldehyde).
- Imine (Schiff base) forms with primary amines (R–NH₂); enamine forms with secondary amines (R₂NH) — the products are structurally and reactively distinct.

## Questions

```yaml
- question: "Cyclohexanone reacts with diethylamine (a secondary amine, Et₂NH) under acid catalysis with removal of water. What is the primary organic product?"
  type: multiple-choice
  options: ["An imine (C=N–Et)", "An enamine (C=C–N)", "A hemiacetal", "A cyanohydrin"]
  answer: 1
  explanation: "Secondary amines (R₂NH) cannot form imines because they have no N–H bond left after the initial addition — they cannot lose a proton to form a C=N double bond. Instead, the reaction proceeds by eliminating the adjacent C–H (an α-hydrogen) to give a C=C–N enamine. Primary amines (R–NH₂) retain an N–H and so can form imines."

- question: "Aldehydes undergo nucleophilic addition more readily than ketones under equivalent conditions."
  type: true-false
  answer: true
  explanation: "Two factors favor aldehydes. First, ketones bear two alkyl groups on the carbonyl carbon, which creates more steric hindrance that slows nucleophilic attack. Second, alkyl groups are electron-donating, which slightly reduces the electrophilicity of the carbonyl carbon in ketones. Both effects make aldehydes more reactive toward nucleophiles than ketones."

- question: "Why does acetal formation from an aldehyde and an alcohol require acid catalysis, and why is base catalysis ineffective for this reaction?"
  type: short-answer
  answer: "Acid protonates the carbonyl oxygen, activating it toward nucleophilic attack, and later protonates the hemiacetal hydroxyl to make it a good leaving group. Base would deprotonate the alcohol to give an alkoxide, but alkoxides are poor nucleophiles toward neutral carbonyls and base cannot activate the hydroxyl leaving group — the critical protonation steps simply don't occur under basic conditions."
  explanation: "The mechanism proceeds through protonation of C=O, nucleophilic addition of ROH, protonation of the resulting alkoxide, loss of water to form an oxocarbenium ion, and final addition of a second ROH. Every protonation step requires acid. Base-catalyzed addition of alkoxide to the carbonyl can occur but produces a hemiacetal alkoxide that cannot be further converted to acetal without acid."
```

## Explainer

The carbonyl group (C=O) is electrophilic at carbon because oxygen strongly pulls electron density away through the C=O π bond, leaving the carbon partially positive. When a nucleophile — anything with a lone pair or negative charge — approaches this carbon, it donates electrons into the empty π* orbital, breaking the π bond and converting the sp2 carbon to sp3. This produces an alkoxide intermediate that is immediately protonated (by water or the conjugate acid of a catalyst) to give the addition product. This two-step sequence — nucleophilic attack, then protonation — is the core mechanism of every reaction in this topic.

Whether the addition is reversible matters enormously. Water adds to aldehydes and ketones to form gem-diols (hydrates), but the equilibrium usually strongly favors the carbonyl form because forming two C–O single bonds at the expense of a C=O π bond is energetically unfavorable for most substrates. Formaldehyde and chloral are exceptions: electron-withdrawing substituents or lack of steric bulk shift the equilibrium toward the hydrate. This same logic explains why aldehydes are more reactive than ketones — the two bulky alkyl groups on ketones both hinder approach of the nucleophile and donate electrons into the carbonyl, reducing its electrophilicity.

Acetal formation extends the hemiacetal mechanism by one more step. In acid, the hemiacetal –OH is protonated and leaves as water, generating a highly electrophilic oxocarbenium ion (R–CH=O⁺R) that is immediately trapped by a second equivalent of alcohol. The entire sequence is reversible, and acetals are stable only in neutral or basic conditions — reintroducing acid with water regenerates the original carbonyl. This pH-dependent reversibility is the basis for using acetals as carbonyl protecting groups in multi-step synthesis.

Nitrogen nucleophiles follow a different path. Primary amines (R–NH₂) add to the carbonyl in the same initial step, but the hemiaminal intermediate can undergo an additional elimination: the nitrogen lone pair expels the adjacent OH as water to form an imine (C=N–R), also called a Schiff base. Secondary amines (R₂NH) cannot form imines because after addition there is no N–H bond remaining. Instead, they lose an α-hydrogen — a proton from the carbon adjacent to the carbonyl — to form an enamine (C=C–N). Imines and enamines are both important intermediates in biological chemistry and synthetic methodology, but their structure and reactivity differ substantially.

Grignard reagents (RMgX) are among the most powerful nucleophiles in this family because the R group attacks as an organometallic carbanion equivalent with no reversibility under the reaction conditions. Addition to an aldehyde gives a secondary alcohol; addition to a ketone gives a tertiary alcohol; addition to formaldehyde gives a primary alcohol. The irreversibility of Grignard addition contrasts with the equilibria seen in hemiacetal and imine chemistry, making it a reliable method for building C–C bonds.
