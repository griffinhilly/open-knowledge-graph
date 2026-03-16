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
status: draft
---

# Wittig Reaction: Phosphorus Ylides and Alkene Synthesis

## Core Idea
The Wittig reaction converts aldehydes or ketones to alkenes via a phosphonium ylide nucleophile, which attacks the carbonyl to form a betaine intermediate that collapses to an oxaphosphetane and then to the alkene and phosphine oxide. This reaction is stereoselective, with stabilized ylides favoring E-alkenes and unstabilized ylides favoring Z-alkenes, making it invaluable for precise alkene synthesis.

## Explainer

From your study of nucleophilic addition to carbonyls, you know that nucleophiles attack the electrophilic carbonyl carbon, forming a new C–C bond. The Wittig reaction uses this same carbonyl electrophilicity but replaces the typical nucleophile with a remarkable species: a **phosphorus ylide** (also called a Wittig reagent). An ylide is a molecule with adjacent positive and negative charges — in this case, a positively charged phosphorus bonded to a negatively charged, nucleophilic carbon. That carbanion character is what drives the initial attack on the carbonyl.

The ylide is prepared in two steps. First, a phosphine (usually triphenylphosphine, PPh₃) performs an SN2 reaction on an alkyl halide to form a **phosphonium salt**. Then a strong base (like n-butyllithium) deprotonates the carbon adjacent to phosphorus, generating the ylide. The key insight is that phosphorus happily bears a positive charge and stabilizes the adjacent carbanion through d-orbital overlap — something nitrogen or oxygen cannot do as effectively. This is why phosphorus is uniquely suited to this chemistry.

When the ylide encounters an aldehyde or ketone, its nucleophilic carbon attacks the carbonyl carbon in the familiar addition step. But instead of stopping at a simple alkoxide, the oxygen swings around to attack the phosphorus, forming a four-membered ring called an **oxaphosphetane**. This ring is unstable and undergoes a concerted [2+2] cycloreversion: the ring breaks apart to release the desired alkene and triphenylphosphine oxide (Ph₃P=O) as a byproduct. The thermodynamic driving force is the extraordinary strength of the P=O bond (~540 kJ/mol), which makes the overall reaction highly favorable.

The stereochemistry of the product alkene depends on the ylide type. **Unstabilized ylides** (where the carbanion has no additional stabilizing groups like esters or nitriles) react quickly and irreversibly, favoring the **Z-alkene** (cis) through a kinetically controlled pathway. **Stabilized ylides** (with electron-withdrawing groups adjacent to the carbanion) react more slowly and reversibly, allowing equilibration to the more thermodynamically stable **E-alkene** (trans). This predictable stereoselectivity is what makes the Wittig reaction so valuable in synthesis: you can place a double bond exactly where you want it in a carbon skeleton, with control over which geometric isomer forms, simply by choosing the right ylide. In retrosynthetic analysis, any alkene in a target molecule can be mentally "disconnected" back to a carbonyl plus an ylide — a powerful strategic simplification.
