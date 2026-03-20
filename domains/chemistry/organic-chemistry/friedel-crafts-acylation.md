---
id: friedel-crafts-acylation
title: Friedel-Crafts Acylation and Aromatic Ketones
domain: chemistry
course: organic-chemistry
prerequisites:
- id: friedel-crafts-alkylation
  type: hard
- id: nucleophilic-acyl-substitution
  type: soft
builds-toward:
- directed-ortho-para-effects
tags:
- friedel-crafts
- acylation
- acylium
- ketone
- electrophilic-aromatic-substitution
stage: advanced
status: draft
---

# Friedel-Crafts Acylation and Aromatic Ketones

## Core Idea
Friedel-Crafts acylation uses an acyl chloride (RCOCl) and Lewis acid to introduce a ketone (RCOR') to an aromatic ring. The mechanism proceeds via an acylium ion (RCO⁺) that attacks the aromatic ring. Unlike alkylation, acylation does NOT suffer from rearrangement (no secondary carbocation), and the ketone product is deactivating, preventing polyacylation. The acyl group is meta-directing, guiding subsequent electrophilic aromatic substitution.

## Explainer

You know from Friedel-Crafts alkylation that a Lewis acid catalyst (typically AlCl₃) activates an electrophile to attack an aromatic ring. Acylation follows the same logic but uses an **acyl chloride** (RCOCl) instead of an alkyl halide. AlCl₃ coordinates with the chlorine of the acyl chloride, generating a resonance-stabilized **acylium ion** (RC≡O⁺). This electrophile then attacks the π system of the aromatic ring through the standard electrophilic aromatic substitution mechanism: the acylium ion forms a sigma complex (arenium ion), and loss of a proton restores aromaticity, yielding an aryl ketone.

The acylium ion is the reason Friedel-Crafts acylation solves two major problems that plague alkylation. First, **no carbocation rearrangement occurs**. In alkylation, primary carbocations can undergo hydride or methyl shifts to form more stable secondary or tertiary carbocations, leading to unexpected products. The acylium ion avoids this entirely because it is already stabilized by resonance — the positive charge is shared between carbon and oxygen (R–C≡O⁺ ↔ R–C=O). There is no energetic incentive to rearrange. Second, **polysubstitution does not occur**. The ketone product is an electron-withdrawing group that deactivates the ring toward further electrophilic attack, so the reaction stops cleanly after one acyl group is installed. Contrast this with alkylation, where the alkyl group activates the ring, inviting additional substitutions.

These advantages make acylation a cornerstone of aromatic synthesis. A common strategy exploits both: to attach a straight-chain alkyl group to a ring without rearrangement, you first acylate (installing the correct carbon skeleton as a ketone) and then reduce the carbonyl to a methylene group using Clemmensen reduction (Zn/Hg, HCl) or Wolff-Kishner reduction (hydrazine, KOH, heat). This two-step sequence — acylation followed by reduction — reliably delivers the product that direct alkylation would scramble.

One important limitation to remember: Friedel-Crafts reactions (both alkylation and acylation) do not work on rings that are strongly deactivated by electron-withdrawing groups (nitrobenzene, for example) or on rings bearing amino groups (which coordinate the Lewis acid catalyst instead of activating the ring). The ring must be at least moderately electron-rich for the electrophilic substitution to proceed. Also note that acylation requires a full stoichiometric equivalent of AlCl₃, not just a catalytic amount, because the Lewis acid complexes with the ketone product and must be destroyed in the aqueous workup.
