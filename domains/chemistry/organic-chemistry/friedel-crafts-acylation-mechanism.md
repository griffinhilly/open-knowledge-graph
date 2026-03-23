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
stage: formal-systems
status: validated
---

# Friedel-Crafts Acylation Mechanism

## Core Idea
Friedel-Crafts acylation adds an acyl group (RCO-) to benzene via an acylium ion (RCO⁺) intermediate, generated from an acyl chloride or anhydride with a Lewis acid catalyst. Unlike alkylation, acylation does not undergo rearrangement and readily forms aromatic ketones. The reaction is more reliable for synthesizing aromatic ketones from acyl chlorides.

## Questions

```yaml
- question: "A chemist wants to synthesize n-propylbenzene (benzene with a straight-chain propyl group attached). Why should they use Friedel-Crafts acylation followed by reduction rather than direct Friedel-Crafts alkylation with n-propyl chloride?"
  type: multiple-choice
  options:
    - "Direct alkylation would give a product with an electron-withdrawing group that deactivates the ring, stopping the reaction before completion"
    - "Direct alkylation would produce rearrangement products (e.g., isopropylbenzene) because the n-propyl carbocation can rearrange to a more stable secondary cation; acylation gives a non-rearranging acylium ion, and the ketone can be reduced to the straight-chain product"
    - "Acylation requires only a catalytic amount of Lewis acid while alkylation requires stoichiometric amounts, making acylation cheaper"
    - "Direct alkylation cannot add more than one carbon to the ring, so a three-carbon chain would require three separate reactions"
  answer: 1
  explanation: "The n-propyl carbocation (a primary cation) readily rearranges via hydride shift to form the more stable isopropyl (secondary) carbocation, giving the unwanted branched product. The acylium ion (CH₃CH₂CO⁺) is stabilized by resonance with the oxygen and does not rearrange. The straight-chain propanoyl group is installed cleanly, and subsequent Clemmensen or Wolff-Kishner reduction gives n-propylbenzene. Note that option C is backwards — it's acylation that requires stoichiometric Lewis acid."

- question: "Why must Friedel-Crafts acylation use a full equivalent of AlCl₃, even though Lewis acids are traditionally described as catalysts in Friedel-Crafts reactions?"
  type: multiple-choice
  options:
    - "The acylium ion is so reactive that it consumes the AlCl₃ before the ring can react, requiring excess to drive the reaction forward"
    - "The carbonyl oxygen of the aromatic ketone product coordinates strongly to AlCl₃, forming a stable product-Lewis acid complex that sequesters the catalyst; one full equivalent of AlCl₃ is therefore consumed per mole of product"
    - "AlCl₃ is catalytic in acylation, but practical reactions use excess because some AlCl₃ is destroyed by moisture during workup"
    - "Multiple equivalents of acylium ion attack the ring before the product deactivates it, requiring excess Lewis acid to generate each electrophile"
  answer: 1
  explanation: "The carbonyl oxygen of the ketone product is a Lewis base that coordinates strongly to AlCl₃, forming a stable [ketone–AlCl₃] complex. This complex is thermodynamically downhill and essentially irreversible under the reaction conditions, which means the Lewis acid is no longer free to catalyze further reactions. The AlCl₃ must be stoichiometric (one equivalent per product molecule) and is only released — along with the free ketone — during aqueous workup. This is a key practical difference from other Lewis acid-catalyzed reactions where the catalyst is truly regenerated."

- question: "Friedel-Crafts acylation is self-limiting: the reaction cleanly stops after a single substitution because the acyl product deactivates the ring toward further electrophilic attack."
  type: true-false
  answer: true
  explanation: "The acyl group (RCO–) is an electron-withdrawing group through both inductive effects (the electronegative oxygen withdraws electron density through the sigma bond) and resonance effects (the carbonyl pi system draws electrons out of the ring). This deactivation raises the energy of the arenium ion intermediate for any subsequent electrophilic attack, effectively shutting down further substitution. This is one of acylation's practical advantages over alkylation: the product is inherently resistant to overreaction, giving the mono-substituted ketone in high selectivity."

- question: "The acylium ion (RCO⁺) is an unstable intermediate that readily undergoes rearrangement to form a more stable carbocation, just like the carbocation intermediates in Friedel-Crafts alkylation."
  type: true-false
  answer: false
  explanation: "This is the key mechanistic distinction that makes acylation more reliable than alkylation. The acylium ion is stabilized by resonance: the positive charge is delocalized between carbon (R–C⁺=O) and oxygen (R–C≡O⁺). This resonance stabilization means the acylium ion does not need to rearrange to find a lower-energy structure — it already is lower energy. In alkylation, an unstabilized carbocation intermediate (e.g., primary → secondary rearrangement) drives unwanted skeletal rearrangement. The resonance-stabilized acylium ion delivers the expected acyl group without rearrangement, making the reaction synthetically predictable."

- question: "Why does Friedel-Crafts acylation produce a single monosubstituted product reliably, while Friedel-Crafts alkylation often gives a mixture of mono- and polysubstituted products?"
  type: short-answer
  answer: "Acylation installs an electron-withdrawing acyl group that deactivates the ring toward further electrophilic attack — once one acyl group is added, the ring is less reactive than unsubstituted benzene, so polysubstitution does not occur. Alkylation installs an electron-donating alkyl group that activates the ring toward further substitution — the monoalkyl product is more reactive than the starting benzene, making a second (and third) substitution energetically favorable. This means alkylation tends to give mixtures, while acylation cleanly stops at mono-substitution."
  explanation: "The contrast stems from the electronic effects of the two groups. Alkyl groups donate electrons to the ring through hyperconjugation and induction, raising the ring's nucleophilicity and accelerating further EAS. The product is therefore more reactive than the starting material, leading to overalkylation. The carbonyl group does the opposite: it withdraws electron density via resonance and induction, deactivating the ring. The product is less reactive than benzene, and the reaction stops naturally. This built-in selectivity is why acylation is so synthetically useful — it delivers a pure monosubstituted product without requiring careful control of stoichiometry."
```

## Explainer

From your study of electrophilic aromatic substitution (EAS), you know the general pattern: an electrophile attacks the pi electron cloud of benzene, forming a resonance-stabilized carbocation intermediate (the arenium ion or sigma complex), and then a proton is lost to restore aromaticity. Friedel-Crafts acylation follows this same template, but with an **acylium ion** (RCO⁺) serving as the electrophile — and this particular electrophile solves several problems that plague Friedel-Crafts alkylation.

The mechanism begins with generation of the electrophile. An **acyl chloride** (RCOCl) reacts with a Lewis acid catalyst, typically AlCl₃, which coordinates to the chlorine and pulls it away, generating the **acylium ion** (R–C≡O⁺). This ion is resonance-stabilized: one resonance structure shows the positive charge on carbon, while the other places it on oxygen with a triple bond between C and O. This stabilization is the key advantage over alkylation — because the acylium ion is resonance-stabilized, it does *not* rearrange. In Friedel-Crafts alkylation, the carbocation intermediate can undergo hydride or methyl shifts to form a more stable cation, giving unexpected products. The acylium ion's built-in stability eliminates this problem entirely.

Once formed, the acylium ion attacks the benzene ring in the standard EAS fashion. The pi electrons of benzene attack the electrophilic carbon of R–C≡O⁺, forming the arenium ion intermediate. Deprotonation by AlCl₄⁻ (the conjugate base generated in the first step) restores aromaticity and yields the **aromatic ketone** product. However, there is an important stoichiometric detail: the carbonyl oxygen of the product coordinates strongly to AlCl₃, forming a stable complex. This means a full equivalent of Lewis acid is consumed, not just a catalytic amount. The product-Lewis acid complex is broken apart during aqueous workup.

Friedel-Crafts acylation has a built-in self-limiting feature that makes it particularly useful. The acyl group placed on the ring is an **electron-withdrawing group** (through both inductive and resonance effects of the carbonyl). This deactivates the ring toward further electrophilic attack, so the reaction stops cleanly after one substitution — you get the monosubstituted ketone without worrying about polysubstitution. This stands in contrast to Friedel-Crafts alkylation, where the alkyl group activates the ring and can lead to multiple substitutions. For this reason, acylation followed by reduction (Clemmensen or Wolff-Kishner) is often the preferred route to alkylbenzenes, avoiding the rearrangement and overreaction problems of direct alkylation.
