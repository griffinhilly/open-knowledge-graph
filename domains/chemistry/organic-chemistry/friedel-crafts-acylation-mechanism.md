---
id: friedel-crafts-acylation-mechanism
title: Friedel-Crafts Acylation Mechanism
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-aromatic-substitution
  type: hard
- id: aromatic-compounds-intro
  type: hard
- id: carbonyl-chemistry-intro
  type: hard
builds-toward:
- directed-electrophilic-aromatic-substitution
tags:
- friedel-crafts-acylation
- fc-acylation
- acylium-ion
- aromatic-ketones
stage: advanced
status: draft
---

# Friedel-Crafts Acylation Mechanism

## Core Idea
Friedel-Crafts acylation adds an acyl group (RCO-) to benzene via an acylium ion (RCO⁺) intermediate, generated from an acyl chloride or anhydride with a Lewis acid catalyst. Unlike alkylation, acylation does not undergo rearrangement and readily forms aromatic ketones. The reaction is more reliable for synthesizing aromatic ketones from acyl chlorides.

## Explainer

From your study of electrophilic aromatic substitution (EAS), you know the general pattern: an electrophile attacks the pi electron cloud of benzene, forming a resonance-stabilized carbocation intermediate (the arenium ion or sigma complex), and then a proton is lost to restore aromaticity. Friedel-Crafts acylation follows this same template, but with an **acylium ion** (RCO⁺) serving as the electrophile — and this particular electrophile solves several problems that plague Friedel-Crafts alkylation.

The mechanism begins with generation of the electrophile. An **acyl chloride** (RCOCl) reacts with a Lewis acid catalyst, typically AlCl₃, which coordinates to the chlorine and pulls it away, generating the **acylium ion** (R–C≡O⁺). This ion is resonance-stabilized: one resonance structure shows the positive charge on carbon, while the other places it on oxygen with a triple bond between C and O. This stabilization is the key advantage over alkylation — because the acylium ion is resonance-stabilized, it does *not* rearrange. In Friedel-Crafts alkylation, the carbocation intermediate can undergo hydride or methyl shifts to form a more stable cation, giving unexpected products. The acylium ion's built-in stability eliminates this problem entirely.

Once formed, the acylium ion attacks the benzene ring in the standard EAS fashion. The pi electrons of benzene attack the electrophilic carbon of R–C≡O⁺, forming the arenium ion intermediate. Deprotonation by AlCl₄⁻ (the conjugate base generated in the first step) restores aromaticity and yields the **aromatic ketone** product. However, there is an important stoichiometric detail: the carbonyl oxygen of the product coordinates strongly to AlCl₃, forming a stable complex. This means a full equivalent of Lewis acid is consumed, not just a catalytic amount. The product-Lewis acid complex is broken apart during aqueous workup.

Friedel-Crafts acylation has a built-in self-limiting feature that makes it particularly useful. The acyl group placed on the ring is an **electron-withdrawing group** (through both inductive and resonance effects of the carbonyl). This deactivates the ring toward further electrophilic attack, so the reaction stops cleanly after one substitution — you get the monosubstituted ketone without worrying about polysubstitution. This stands in contrast to Friedel-Crafts alkylation, where the alkyl group activates the ring and can lead to multiple substitutions. For this reason, acylation followed by reduction (Clemmensen or Wolff-Kishner) is often the preferred route to alkylbenzenes, avoiding the rearrangement and overreaction problems of direct alkylation.
