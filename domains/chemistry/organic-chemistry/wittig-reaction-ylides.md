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

## Explainer

From your study of nucleophilic addition to carbonyls, you know that nucleophiles attack the electrophilic carbonyl carbon to form new C–C bonds — Grignard reagents do this to give alcohols. The **Wittig reaction** takes this idea one step further: instead of stopping at an alcohol, it replaces the entire C=O with a C=C, converting a carbonyl directly into an alkene. This makes the Wittig reaction one of the most powerful tools in synthetic chemistry because you know exactly where the double bond will end up — right where the carbonyl used to be.

The reagent that makes this possible is a **phosphonium ylide**, a species with a negatively charged carbon bonded to a positively charged phosphorus: R₃P⁺–C⁻R'. The ylide is prepared in two steps. First, triphenylphosphine (Ph₃P) attacks an alkyl halide in an SN2 reaction to form a phosphonium salt. Then, a strong base (like n-butyllithium) removes a proton from the carbon adjacent to phosphorus, generating the ylide. The carbon in the ylide is both nucleophilic (it carries a formal negative charge) and carbene-like, which is what allows it to attack the carbonyl.

When the ylide meets the carbonyl, the nucleophilic carbon of the ylide attacks the electrophilic carbonyl carbon, forming a four-membered ring intermediate called an **oxaphosphetane** — a ring containing carbon, oxygen, and phosphorus. This intermediate then undergoes a concerted [2+2] cycloreversion: the ring breaks apart to release the alkene and triphenylphosphine oxide (Ph₃P=O). The formation of the very strong P=O bond (bond energy ~540 kJ/mol) is the thermodynamic driving force that makes the entire reaction irreversible and highly favorable.

The stereochemistry of the product alkene depends on the ylide type. **Unstabilized ylides** (no electron-withdrawing groups on the carbanion carbon) react quickly and kinetically, producing predominantly the **Z-alkene** (cis). **Stabilized ylides** (bearing groups like esters or nitriles) react more slowly and under thermodynamic control, favoring the **E-alkene** (trans). This stereoselectivity, combined with the positional specificity of double bond placement, makes the Wittig reaction a cornerstone of retrosynthetic analysis: whenever you see an alkene in a target molecule, you can mentally "disconnect" it back to a carbonyl and an ylide.
