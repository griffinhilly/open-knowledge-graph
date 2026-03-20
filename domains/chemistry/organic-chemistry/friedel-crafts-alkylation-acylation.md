---
id: friedel-crafts-alkylation-acylation
title: Friedel-Crafts Alkylation and Acylation
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-aromatic-substitution
  type: soft
- id: nucleophile-electrophile-definitions
  type: hard
builds-toward:
- electrophilic-aromatic-substitution-directors
tags:
- friedel-crafts
- alkylation
- acylation
- aromatic
- substitution
stage: advanced
status: draft
---

# Friedel-Crafts Alkylation and Acylation

## Core Idea
Friedel-Crafts alkylation and acylation are electrophilic aromatic substitutions. Alkylation uses an alkyl halide with Lewis acid (AlCl₃) to generate a carbocation; acylation uses an acid chloride to form an acylium ion (R-C≡O⁺). The electrophile attacks the benzene ring, displacing hydride. Alkylation suffers from carbocation rearrangement and over-alkylation; acylation is generally cleaner because the acylium ion is resonance-stabilized and does not rearrange.

## How It's Best Learned
Draw the carbocation and acylium ion formation, then the attack on the benzene ring. Understand why alkylation with primary alkyl halides fails (rearrangement) and why over-alkylation is a problem.

## Common Misconceptions
- Assuming Friedel-Crafts alkylation with primary alkyl halides gives the primary substitution product; rearrangement to more stable carbocations occurs.
- Forgetting that the initial FC product (with an alkyl or acyl group) is more activated toward further substitution, leading to over-alkylation unless controlled carefully.

## Explainer

Friedel-Crafts reactions are the primary way to attach carbon groups directly to a benzene ring, and they follow the general electrophilic aromatic substitution mechanism you already know: generate an electrophile, let the electron-rich aromatic ring attack it to form a σ-complex, then lose a proton to restore aromaticity. What distinguishes the two Friedel-Crafts variants is how the electrophile is generated and the practical complications that follow.

In **Friedel-Crafts alkylation**, an alkyl halide (R–X) reacts with a Lewis acid catalyst, typically AlCl₃. The Lewis acid coordinates to the halide's lone pair, polarizing the C–X bond and generating either a full carbocation (R⁺) or a highly polarized complex that behaves like one. This carbocation is the electrophile that the benzene ring attacks. The problem is that carbocations rearrange — a primary carbocation will undergo hydride or methyl shifts to become more stable (secondary or tertiary), just as you learned in carbocation chemistry. So if you try to put a straight-chain propyl group on benzene using 1-chloropropane, you do not get n-propylbenzene; you get isopropylbenzene, because the primary cation rearranges to a more stable secondary one. A second problem is **polyalkylation**: the alkyl group you just attached is electron-donating, making the product ring more reactive than the starting benzene, so a second alkylation occurs faster than the first.

**Friedel-Crafts acylation** solves both problems elegantly. An acid chloride (R–COCl) reacts with AlCl₃ to generate the **acylium ion** (R–C≡O⁺), a resonance-stabilized electrophile in which the positive charge is shared between carbon and oxygen. Because the acylium ion is already stabilized, it does not rearrange — you get exactly the carbon skeleton you intended. Furthermore, the product is an aryl ketone, and the carbonyl group is electron-withdrawing, deactivating the ring and preventing polyacylation. If you ultimately want an alkyl group on the ring without rearrangement, the standard strategy is to perform acylation first (no rearrangement, no polysubstitution) and then reduce the ketone to a methylene group using Clemmensen reduction (Zn/Hg, HCl) or Wolff-Kishner reduction (hydrazine, KOH, heat).

There are important limitations to know. Friedel-Crafts reactions fail on strongly deactivated rings — if the benzene already bears a meta-directing, deactivating group like –NO₂, the ring is too electron-poor to attack the electrophile. They also fail with aryl and vinyl halides, because these cannot form stable carbocations. And amine-substituted rings cause problems because the amine's lone pair coordinates to AlCl₃, poisoning the catalyst. Recognizing when Friedel-Crafts will and will not work is essential for planning multi-step aromatic syntheses.
