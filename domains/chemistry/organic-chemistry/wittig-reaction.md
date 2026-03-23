---
id: wittig-reaction
title: 'Wittig Reaction: Phosphorus Ylides and Alkene Synthesis'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: aldehyde-and-ketone-structure-and-nomenclature
  type: hard
- id: nucleophilic-addition-to-carbonyls
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- wittig-reaction
- ylide
- phosphorus
- alkene-synthesis
- carbonyl-olefination
stage: formal-systems
status: validated
---

# Wittig Reaction: Phosphorus Ylides and Alkene Synthesis

## Core Idea
The Wittig reaction converts aldehydes or ketones to alkenes via a phosphonium ylide nucleophile, which attacks the carbonyl to form a betaine intermediate that collapses to an oxaphosphetane and then to the alkene and phosphine oxide. This reaction is stereoselective, with stabilized ylides favoring E-alkenes and unstabilized ylides favoring Z-alkenes, making it invaluable for precise alkene synthesis.

## Questions

```yaml
- question: "A chemist wants to synthesize (Z)-3-heptene (a cis-alkene) using a Wittig reaction. Which type of ylide should they use?"
  type: multiple-choice
  options:
    - "A stabilized ylide (with an adjacent ester group), because it reacts faster and produces predominantly Z-alkene"
    - "An unstabilized ylide (no electron-withdrawing groups on the carbanion), because it reacts quickly and irreversibly, favoring Z-alkene formation"
    - "A stabilized ylide, because the extra stability slows the reaction and allows kinetic control toward the Z-isomer"
    - "Either type — the geometric outcome is determined by the carbonyl compound, not the ylide"
  answer: 1
  explanation: "Unstabilized ylides (no electron-withdrawing groups on the carbanion carbon) react quickly and irreversibly via a kinetically controlled pathway that preferentially produces the Z (cis) alkene. Stabilized ylides (with EWGs like esters or nitriles) react more slowly and reversibly, allowing equilibration to the thermodynamically more stable E (trans) product. Option A is wrong on both counts — stabilized ylides are slower, not faster, and they favor E-alkenes. Option D is wrong — it is the ylide type, not the carbonyl, that determines stereoselectivity."

- question: "What is the primary thermodynamic driving force that makes the Wittig reaction proceed to completion?"
  type: multiple-choice
  options:
    - "The stability of the new alkene π bond formed in the product"
    - "The formation of triphenylphosphine oxide (Ph₃P=O), which contains an exceptionally strong P=O bond (~540 kJ/mol)"
    - "The release of strain from the four-membered oxaphosphetane ring"
    - "The restoration of aromaticity in the triphenylphosphine leaving group"
  answer: 1
  explanation: "The extraordinary thermodynamic driving force is the formation of the P=O bond in triphenylphosphine oxide. At ~540 kJ/mol, this is one of the strongest bonds in organic chemistry and makes the overall reaction highly exothermic and essentially irreversible. While oxaphosphetane ring strain (option C) does contribute to the [2+2] cycloreversion step, it is the exceptional strength of the P=O bond that makes the overall equilibrium so strongly product-favored. The alkene π bond (option A) forms but is not the primary driver."

- question: "A stabilized Wittig ylide (one with an electron-withdrawing group adjacent to the carbanion) predominantly produces the E-alkene because it reacts slowly enough to allow thermodynamic equilibration."
  type: true-false
  answer: true
  explanation: "Stabilized ylides have the carbanion's charge delocalized by adjacent electron-withdrawing groups, making them less reactive. They react more slowly with carbonyl compounds, and the intermediate steps (including oxaphosphetane formation) are reversible, allowing the system to equilibrate. Since the E (trans) alkene is typically more thermodynamically stable than the Z (cis) alkene, equilibration produces E-alkene as the major product. This contrasts with unstabilized ylides, which react irreversibly under kinetic control and give Z-alkene."

- question: "The Wittig reaction works with aldehydes but cannot be used with ketones, because the additional alkyl group makes the carbonyl too hindered for ylide attack."
  type: true-false
  answer: false
  explanation: "The Wittig reaction works with both aldehydes and ketones. Ketones are less reactive than aldehydes due to greater steric hindrance and electron donation from two alkyl groups, but the reaction still proceeds — sometimes requiring more forcing conditions or more reactive unstabilized ylides. The Core Idea explicitly states the reaction 'converts aldehydes or ketones to alkenes.' Using the Wittig reaction on ketones is routine in synthesis, particularly for making trisubstituted alkenes."

- question: "Why is the formation of the oxaphosphetane ring a key intermediate step, and how does its decomposition give rise to stereocontrol in the Wittig reaction?"
  type: short-answer
  answer: "The oxaphosphetane is a strained four-membered ring formed when the oxygen of the original carbonyl attacks the phosphorus after the initial C-C bond-forming step. This ring undergoes a concerted [2+2] cycloreversion, releasing the alkene and triphenylphosphine oxide. The stereochemistry of the alkene is set when the oxaphosphetane ring forms: with unstabilized ylides, ring formation is fast and irreversible, favoring a syn arrangement of substituents that leads to Z-alkene upon ring opening. With stabilized ylides, ring formation is reversible, and the more stable anti arrangement accumulates, leading to E-alkene. The oxaphosphetane acts as a stereochemical relay — the geometry established in ring formation is preserved in the alkene product."
  explanation: "Stereocontrol in the Wittig reaction is mechanistic, not imposed after the fact. The ylide type controls the reversibility of the ring-forming step, which controls the geometry of the ring, which determines the E/Z outcome. Understanding this mechanism is what distinguishes conceptual mastery from mere memorization of 'unstabilized = Z, stabilized = E.'"
```

## Explainer

From your study of nucleophilic addition to carbonyls, you know that nucleophiles attack the electrophilic carbonyl carbon, forming a new C–C bond. The Wittig reaction uses this same carbonyl electrophilicity but replaces the typical nucleophile with a remarkable species: a **phosphorus ylide** (also called a Wittig reagent). An ylide is a molecule with adjacent positive and negative charges — in this case, a positively charged phosphorus bonded to a negatively charged, nucleophilic carbon. That carbanion character is what drives the initial attack on the carbonyl.

The ylide is prepared in two steps. First, a phosphine (usually triphenylphosphine, PPh₃) performs an SN2 reaction on an alkyl halide to form a **phosphonium salt**. Then a strong base (like n-butyllithium) deprotonates the carbon adjacent to phosphorus, generating the ylide. The key insight is that phosphorus happily bears a positive charge and stabilizes the adjacent carbanion through d-orbital overlap — something nitrogen or oxygen cannot do as effectively. This is why phosphorus is uniquely suited to this chemistry.

When the ylide encounters an aldehyde or ketone, its nucleophilic carbon attacks the carbonyl carbon in the familiar addition step. But instead of stopping at a simple alkoxide, the oxygen swings around to attack the phosphorus, forming a four-membered ring called an **oxaphosphetane**. This ring is unstable and undergoes a concerted [2+2] cycloreversion: the ring breaks apart to release the desired alkene and triphenylphosphine oxide (Ph₃P=O) as a byproduct. The thermodynamic driving force is the extraordinary strength of the P=O bond (~540 kJ/mol), which makes the overall reaction highly favorable.

The stereochemistry of the product alkene depends on the ylide type. **Unstabilized ylides** (where the carbanion has no additional stabilizing groups like esters or nitriles) react quickly and irreversibly, favoring the **Z-alkene** (cis) through a kinetically controlled pathway. **Stabilized ylides** (with electron-withdrawing groups adjacent to the carbanion) react more slowly and reversibly, allowing equilibration to the more thermodynamically stable **E-alkene** (trans). This predictable stereoselectivity is what makes the Wittig reaction so valuable in synthesis: you can place a double bond exactly where you want it in a carbon skeleton, with control over which geometric isomer forms, simply by choosing the right ylide. In retrosynthetic analysis, any alkene in a target molecule can be mentally "disconnected" back to a carbonyl plus an ylide — a powerful strategic simplification.
