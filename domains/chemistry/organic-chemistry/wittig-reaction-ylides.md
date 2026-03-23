---
id: wittig-reaction-ylides
title: 'The Wittig Reaction: Ylides and Alkene Synthesis'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: nucleophilic-addition-to-carbonyls
  type: hard
- id: grignard-reagent
  type: soft
tags:
- wittig
- ylide
- phosphorus
- alkene-synthesis
- stereospecific
stage: formal-systems
status: draft
---

# The Wittig Reaction: Ylides and Alkene Synthesis

## Core Idea
The Wittig reaction converts carbonyls (aldehydes, ketones) to alkenes using phosphonium ylides (R₃P⁺=C⁻R'), generated from triphenylphosphine and alkyl halides via carbanionic intermediates. The ylide attacks the carbonyl carbon; the resulting intermediate (oxaphosphetane) decomposes to release an alkene and triphenylphosphine oxide. Stabilized ylides (bearing electron-withdrawing groups) give Z-alkenes (thermodynamic); unstabilized ylides give E-alkenes (kinetic).

## Questions

```yaml
- question: "You need to synthesize a Z-alkene (cis double bond) via a Wittig reaction. Which ylide type should you choose?"
  type: multiple-choice
  options:
    - "A stabilized ylide bearing an ester group — the electron-withdrawing group slows reaction and provides thermodynamic control"
    - "An unstabilized ylide with no electron-withdrawing groups — kinetic control of the oxaphosphetane intermediate favors the Z product"
    - "Either type — Z vs. E selectivity is determined by the carbonyl substrate, not the ylide"
    - "A stabilized ylide — stronger carbanion character makes it more selective toward cis attack"
  answer: 1
  explanation: "Ylide stability is the key variable controlling stereoselectivity. Unstabilized ylides react rapidly under kinetic control and give predominantly Z-alkene (cis). Stabilized ylides (with ester, nitrile, or other EWG on the carbanion carbon) react more slowly under thermodynamic control and give predominantly E-alkene (trans). The carbonyl substrate does not control this — it is determined by the ylide."

- question: "What is the thermodynamic driving force that makes the Wittig reaction essentially irreversible once the oxaphosphetane forms?"
  type: multiple-choice
  options:
    - "Release of CO₂ gas as a byproduct, which drives the equilibrium toward products"
    - "Formation of the very strong P=O bond in triphenylphosphine oxide (bond energy ~540 kJ/mol)"
    - "The high stability of the four-membered oxaphosphetane ring intermediate"
    - "Loss of water during elimination of the phosphorus-containing group"
  answer: 1
  explanation: "The P=O bond in triphenylphosphine oxide is extraordinarily strong (~540 kJ/mol), making its formation highly exothermic. The oxaphosphetane ring cycloreversion releases this driving force, making the overall reaction thermodynamically irreversible. This is why the Wittig reaction is so synthetically reliable — once the reaction starts, equilibrium strongly favors the alkene and Ph₃P=O products."

- question: "The Wittig reaction gives complete regiochemical control over double bond placement: the new C=C appears exactly where the C=O existed in the starting carbonyl compound."
  type: true-false
  answer: true
  explanation: "This is the most synthetically powerful feature of the Wittig reaction. The ylide's nucleophilic carbon attacks the carbonyl carbon, and the subsequent oxaphosphetane decomposition places the double bond precisely where the carbonyl was. No other alkene-forming reaction offers this level of regiochemical certainty. It is why retrosynthetic analysis of alkene targets almost always considers the Wittig disconnection: mentally replace C=C with C=O to identify the precursors."

- question: "The oxaphosphetane intermediate in the Wittig reaction is a stable, isolable compound under standard synthetic conditions."
  type: true-false
  answer: false
  explanation: "The oxaphosphetane is a strained four-membered ring containing C–C–O–P. It is a transient intermediate, not a stable isolable compound under typical Wittig conditions. The ring undergoes rapid concerted [2+2] cycloreversion to give the alkene and triphenylphosphine oxide. Under special low-temperature conditions, oxaphosphetanes have been observed spectroscopically, but in a standard Wittig synthesis you cannot stop at this stage."

- question: "Explain why the Wittig reaction is particularly valuable in retrosynthetic analysis when designing a synthesis for a target molecule containing a specific alkene."
  type: short-answer
  answer: "The Wittig reaction installs a C=C bond with known regiochemistry (exactly where the carbonyl was) and predictable stereochemistry (Z with unstabilized ylide, E with stabilized ylide). In retrosynthesis, any alkene in the target can be disconnected back to a carbonyl compound plus a phosphonium ylide precursor. This gives the synthetic planner two readily adjustable fragments: the carbonyl (from a known aldehyde or ketone) and the ylide (from triphenylphosphine plus the appropriate alkyl halide)."
  explanation: "Contrast the Wittig reaction with acid-catalyzed dehydration or elimination reactions, which often give mixtures of regioisomers and stereoisomers. The Wittig reaction's specificity eliminates ambiguity in retrosynthetic planning. For complex natural product synthesis, knowing exactly where a double bond will appear — and being able to set its geometry — is essential for efficient route design."
```

## Explainer

From your study of nucleophilic addition to carbonyls, you know that nucleophiles attack the electrophilic carbonyl carbon to form new C–C bonds — Grignard reagents do this to give alcohols. The **Wittig reaction** takes this idea one step further: instead of stopping at an alcohol, it replaces the entire C=O with a C=C, converting a carbonyl directly into an alkene. This makes the Wittig reaction one of the most powerful tools in synthetic chemistry because you know exactly where the double bond will end up — right where the carbonyl used to be.

The reagent that makes this possible is a **phosphonium ylide**, a species with a negatively charged carbon bonded to a positively charged phosphorus: R₃P⁺–C⁻R'. The ylide is prepared in two steps. First, triphenylphosphine (Ph₃P) attacks an alkyl halide in an SN2 reaction to form a phosphonium salt. Then, a strong base (like n-butyllithium) removes a proton from the carbon adjacent to phosphorus, generating the ylide. The carbon in the ylide is both nucleophilic (it carries a formal negative charge) and carbene-like, which is what allows it to attack the carbonyl.

When the ylide meets the carbonyl, the nucleophilic carbon of the ylide attacks the electrophilic carbonyl carbon, forming a four-membered ring intermediate called an **oxaphosphetane** — a ring containing carbon, oxygen, and phosphorus. This intermediate then undergoes a concerted [2+2] cycloreversion: the ring breaks apart to release the alkene and triphenylphosphine oxide (Ph₃P=O). The formation of the very strong P=O bond (bond energy ~540 kJ/mol) is the thermodynamic driving force that makes the entire reaction irreversible and highly favorable.

The stereochemistry of the product alkene depends on the ylide type. **Unstabilized ylides** (no electron-withdrawing groups on the carbanion carbon) react quickly and kinetically, producing predominantly the **Z-alkene** (cis). **Stabilized ylides** (bearing groups like esters or nitriles) react more slowly and under thermodynamic control, favoring the **E-alkene** (trans). This stereoselectivity, combined with the positional specificity of double bond placement, makes the Wittig reaction a cornerstone of retrosynthetic analysis: whenever you see an alkene in a target molecule, you can mentally "disconnect" it back to a carbonyl and an ylide.
