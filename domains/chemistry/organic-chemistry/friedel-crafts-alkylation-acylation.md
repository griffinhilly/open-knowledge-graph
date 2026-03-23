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
stage: formal-systems
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

## Questions

```yaml
- question: "A chemist reacts benzene with 1-chloropropane and AlCl₃. What is the major product?"
  type: multiple-choice
  options:
    - "n-propylbenzene, from direct attachment of the n-propyl group"
    - "Isopropylbenzene (cumene), from rearrangement of the primary carbocation to a secondary one"
    - "No reaction — primary alkyl halides cannot generate carbocations"
    - "Dipropylbenzene, due to over-alkylation"
  answer: 1
  explanation: "1-Chloropropane + AlCl₃ generates a primary carbocation, which rapidly rearranges via a 1,2-hydride shift to the more stable secondary carbocation (isopropyl cation). This rearranged electrophile then attacks benzene, giving isopropylbenzene as the major product — not the n-propyl product the reagent structure might suggest. This is the central practical limitation of Friedel-Crafts alkylation with primary alkyl halides."

- question: "A chemist needs to add an n-butyl group to benzene without rearrangement. Which strategy is best?"
  type: multiple-choice
  options:
    - "Use 1-chlorobutane with excess AlCl₃ to drive the reaction before rearrangement occurs"
    - "Use butanoyl chloride with AlCl₃ (acylation), then reduce the ketone to a methylene group"
    - "Use 2-chlorobutane instead, since secondary carbocations are more stable and won't rearrange further"
    - "Perform the alkylation at low temperature to suppress rearrangement"
  answer: 1
  explanation: "Acylation with butanoyl chloride generates the resonance-stabilized acylium ion, which does not rearrange, giving a phenyl ketone with the correct four-carbon chain. The ketone is then reduced to a CH₂ group using Clemmensen or Wolff-Kishner reduction, yielding the straight-chain n-butylbenzene. This two-step acylation-reduction sequence is the standard workaround for the carbocation rearrangement problem in alkylation."

- question: "In Friedel-Crafts acylation, the acylium ion does not rearrange because it is resonance-stabilized across the carbon-oxygen bond."
  type: true-false
  answer: true
  explanation: "The acylium ion R–C≡O⁺ is stabilized by resonance: the positive charge is delocalized between the carbonyl carbon and the oxygen. This stability means the ion has no thermodynamic driving force to rearrange to a different structure. In contrast, a primary carbocation in alkylation has no comparable stabilization and rapidly shifts toward a more stable secondary or tertiary ion via hydride or methyl migration."

- question: "If only one equivalent of alkyl halide is used in a Friedel-Crafts alkylation, over-alkylation is not a concern because stoichiometry limits the reaction to one substitution."
  type: true-false
  answer: false
  explanation: "Stoichiometry does not prevent over-alkylation. The alkyl group attached in the first substitution is electron-donating, making the monoalkylated ring more reactive toward electrophilic attack than the original benzene. The product is therefore a better substrate for the second alkylation than the starting material, and it will react preferentially even when alkyl halide is limiting. To get primarily monoalkylation, excess benzene (as solvent) is typically used to dilute the more reactive product — not a stoichiometric limit on the reagent."

- question: "Why does Friedel-Crafts reaction fail on strongly deactivated aromatic rings such as nitrobenzene, even with excess Lewis acid catalyst?"
  type: short-answer
  answer: "Strongly deactivating groups like –NO₂ withdraw electron density from the ring, making it electron-poor. Electrophilic aromatic substitution requires the ring to act as a nucleophile and attack the electrophile. When the ring lacks sufficient electron density, it cannot effectively attack the carbocation or acylium ion, so no substitution occurs. The ring simply is not nucleophilic enough to form the required σ-complex intermediate."
  explanation: "This reflects a general rule: EAS requires an electron-rich aromatic ring. Deactivating meta-directors withdraw electron density through induction and resonance, lowering the ring's HOMO energy and reducing its reactivity. Friedel-Crafts reactions are among the most sensitive to deactivation because the carbocation/acylium electrophiles require significant nucleophilic attack to form the sigma complex. Amino-substituted rings fail for a different reason — the amine coordinates to AlCl₃, poisoning the catalyst."
```

## Explainer

Friedel-Crafts reactions are the primary way to attach carbon groups directly to a benzene ring, and they follow the general electrophilic aromatic substitution mechanism you already know: generate an electrophile, let the electron-rich aromatic ring attack it to form a σ-complex, then lose a proton to restore aromaticity. What distinguishes the two Friedel-Crafts variants is how the electrophile is generated and the practical complications that follow.

In **Friedel-Crafts alkylation**, an alkyl halide (R–X) reacts with a Lewis acid catalyst, typically AlCl₃. The Lewis acid coordinates to the halide's lone pair, polarizing the C–X bond and generating either a full carbocation (R⁺) or a highly polarized complex that behaves like one. This carbocation is the electrophile that the benzene ring attacks. The problem is that carbocations rearrange — a primary carbocation will undergo hydride or methyl shifts to become more stable (secondary or tertiary), just as you learned in carbocation chemistry. So if you try to put a straight-chain propyl group on benzene using 1-chloropropane, you do not get n-propylbenzene; you get isopropylbenzene, because the primary cation rearranges to a more stable secondary one. A second problem is **polyalkylation**: the alkyl group you just attached is electron-donating, making the product ring more reactive than the starting benzene, so a second alkylation occurs faster than the first.

**Friedel-Crafts acylation** solves both problems elegantly. An acid chloride (R–COCl) reacts with AlCl₃ to generate the **acylium ion** (R–C≡O⁺), a resonance-stabilized electrophile in which the positive charge is shared between carbon and oxygen. Because the acylium ion is already stabilized, it does not rearrange — you get exactly the carbon skeleton you intended. Furthermore, the product is an aryl ketone, and the carbonyl group is electron-withdrawing, deactivating the ring and preventing polyacylation. If you ultimately want an alkyl group on the ring without rearrangement, the standard strategy is to perform acylation first (no rearrangement, no polysubstitution) and then reduce the ketone to a methylene group using Clemmensen reduction (Zn/Hg, HCl) or Wolff-Kishner reduction (hydrazine, KOH, heat).

There are important limitations to know. Friedel-Crafts reactions fail on strongly deactivated rings — if the benzene already bears a meta-directing, deactivating group like –NO₂, the ring is too electron-poor to attack the electrophile. They also fail with aryl and vinyl halides, because these cannot form stable carbocations. And amine-substituted rings cause problems because the amine's lone pair coordinates to AlCl₃, poisoning the catalyst. Recognizing when Friedel-Crafts will and will not work is essential for planning multi-step aromatic syntheses.
