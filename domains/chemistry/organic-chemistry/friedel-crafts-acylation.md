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

## Questions

```yaml
- question: "A chemist needs to attach a straight-chain propyl group to benzene without any rearrangement. Which approach reliably achieves this?"
  type: multiple-choice
  options:
    - "React benzene with 1-chloropropane and AlCl₃ (direct Friedel-Crafts alkylation)"
    - "React benzene with propanoyl chloride and AlCl₃, then reduce the ketone to a methylene group"
    - "React benzene with 2-chloropropane and AlCl₃ to get the secondary carbocation, then quench"
    - "React benzene with propionic acid and AlCl₃ directly"
  answer: 1
  explanation: "Direct alkylation with 1-chloropropane would generate a primary carbocation that readily rearranges to a secondary carbocation, yielding isopropylbenzene instead of propylbenzene. Acylation with propanoyl chloride generates a resonance-stabilized acylium ion (no rearrangement possible), installs the correct three-carbon skeleton as a ketone, and the ketone is then cleanly reduced (Clemmensen or Wolff-Kishner) to the desired propyl group. Options C and D are either rearrangement-prone or chemically incorrect — carboxylic acids do not react under standard Friedel-Crafts conditions."

- question: "Why does Friedel-Crafts acylation stop after one acyl group is installed, whereas Friedel-Crafts alkylation often gives polysubstituted products?"
  type: multiple-choice
  options:
    - "The acylium ion is too bulky to attack a substituted ring a second time"
    - "AlCl₃ is consumed in the first reaction and unavailable for a second substitution"
    - "The ketone product is electron-withdrawing and deactivates the ring toward further electrophilic attack"
    - "The acylation product is insoluble and precipitates, removing it from reaction"
  answer: 2
  explanation: "The ketone product contains a carbonyl group directly attached to the ring — a strong electron-withdrawing group that pulls electron density away from the aromatic π system. This deactivation makes the ring far less reactive toward electrophilic aromatic substitution, so a second acylation does not occur under normal conditions. By contrast, an alkyl group is electron-donating, activating the ring and making the first substitution product even more reactive than benzene, leading to polysubstitution. Option B is partially true (AlCl₃ does complex with the product), but this is not the correct reason for selectivity — the electronic deactivation is."

- question: "The acylium ion (RCO⁺) undergoes rearrangement to a more stable carbocation before attacking the aromatic ring."
  type: true-false
  answer: false
  explanation: "This is false. The acylium ion is resonance-stabilized: the positive charge is delocalized between carbon and oxygen (R–C≡O⁺ ↔ R–C=O⁺), making it already stabilized without needing to rearrange. Simple carbocations (primary, secondary, tertiary) can rearrange via hydride or methyl shifts to reach a lower-energy structure, but the acylium ion's resonance stabilization removes the thermodynamic incentive to rearrange. This is precisely why Friedel-Crafts acylation gives predictable carbon skeletons while alkylation often does not."

- question: "Friedel-Crafts acylation requires a full stoichiometric equivalent of AlCl₃, not merely a catalytic amount."
  type: true-false
  answer: true
  explanation: "True. Unlike in some Lewis acid-catalyzed reactions, the AlCl₃ is not truly regenerated in Friedel-Crafts acylation. After the reaction, AlCl₃ forms a stable 1:1 complex with the ketone product (via the lone pair on the carbonyl oxygen). This complex must be destroyed in the aqueous workup to liberate the ketone and AlCl₃. Because one equivalent of AlCl₃ is sequestered per equivalent of product, a full stoichiometric amount is required — making the reaction more wasteful and costly than a catalytic process."

- question: "Explain why the acylium ion does not undergo carbocation rearrangement, whereas a simple primary carbocation does."
  type: short-answer
  answer: "The acylium ion is resonance-stabilized: the positive charge is shared between carbon and oxygen through the π bond of the carbonyl (R–C≡O⁺ ↔ R–C=O). This delocalization makes the acylium ion thermodynamically stable without rearranging. A simple primary carbocation has no such stabilization — it is a localized, high-energy species with a strong thermodynamic driving force to rearrange (via hydride or methyl migration) to reach a lower-energy secondary or tertiary carbocation. The acylium ion's resonance removes that driving force entirely."
  explanation: "The mechanism of carbocation rearrangement is driven by enthalpy: a primary carbocation rearranges because the product secondary or tertiary carbocation is significantly more stable. The acylium ion avoids this by achieving stability through a different mechanism — resonance delocalization of the positive charge onto electronegative oxygen. With no lower-energy structure available via rearrangement, the acylium ion attacks the aromatic ring with its original carbon skeleton intact, guaranteeing the expected product."
```

## Explainer

You know from Friedel-Crafts alkylation that a Lewis acid catalyst (typically AlCl₃) activates an electrophile to attack an aromatic ring. Acylation follows the same logic but uses an **acyl chloride** (RCOCl) instead of an alkyl halide. AlCl₃ coordinates with the chlorine of the acyl chloride, generating a resonance-stabilized **acylium ion** (RC≡O⁺). This electrophile then attacks the π system of the aromatic ring through the standard electrophilic aromatic substitution mechanism: the acylium ion forms a sigma complex (arenium ion), and loss of a proton restores aromaticity, yielding an aryl ketone.

The acylium ion is the reason Friedel-Crafts acylation solves two major problems that plague alkylation. First, **no carbocation rearrangement occurs**. In alkylation, primary carbocations can undergo hydride or methyl shifts to form more stable secondary or tertiary carbocations, leading to unexpected products. The acylium ion avoids this entirely because it is already stabilized by resonance — the positive charge is shared between carbon and oxygen (R–C≡O⁺ ↔ R–C=O). There is no energetic incentive to rearrange. Second, **polysubstitution does not occur**. The ketone product is an electron-withdrawing group that deactivates the ring toward further electrophilic attack, so the reaction stops cleanly after one acyl group is installed. Contrast this with alkylation, where the alkyl group activates the ring, inviting additional substitutions.

These advantages make acylation a cornerstone of aromatic synthesis. A common strategy exploits both: to attach a straight-chain alkyl group to a ring without rearrangement, you first acylate (installing the correct carbon skeleton as a ketone) and then reduce the carbonyl to a methylene group using Clemmensen reduction (Zn/Hg, HCl) or Wolff-Kishner reduction (hydrazine, KOH, heat). This two-step sequence — acylation followed by reduction — reliably delivers the product that direct alkylation would scramble.

One important limitation to remember: Friedel-Crafts reactions (both alkylation and acylation) do not work on rings that are strongly deactivated by electron-withdrawing groups (nitrobenzene, for example) or on rings bearing amino groups (which coordinate the Lewis acid catalyst instead of activating the ring). The ring must be at least moderately electron-rich for the electrophilic substitution to proceed. Also note that acylation requires a full stoichiometric equivalent of AlCl₃, not just a catalytic amount, because the Lewis acid complexes with the ketone product and must be destroyed in the aqueous workup.
