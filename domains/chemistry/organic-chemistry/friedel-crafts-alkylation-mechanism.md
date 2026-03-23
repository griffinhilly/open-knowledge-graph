---
id: friedel-crafts-alkylation-mechanism
title: Friedel-Crafts Alkylation Mechanism
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-aromatic-substitution
  type: hard
- id: aromatic-compounds-intro
  type: hard
- id: carbocation-stability-rearrangement
  type: hard
builds-toward:
- directed-electrophilic-aromatic-substitution
tags:
- friedel-crafts-alkylation
- fc-alkylation
- electrophile
- carbocation
stage: formal-systems
status: validated
---

# Friedel-Crafts Alkylation Mechanism

## Core Idea
Friedel-Crafts alkylation adds an alkyl group to a benzene ring via an alkyl carbocation intermediate, typically generated from an alkyl halide and a Lewis acid catalyst (AlCl₃). The reaction proceeds through electrophilic aromatic substitution with the benzene π-electrons attacking the carbocation. Rearrangement to more stable carbocations can occur, making primary alkyl halides problematic substrates.

## Questions

```yaml
- question: "You attempt to make n-propylbenzene by reacting benzene with 1-chloropropane and AlCl₃. What is the predominant product?"
  type: multiple-choice
  options:
    - "n-propylbenzene — the primary carbocation attacks directly before rearrangement"
    - "isopropylbenzene — the primary carbocation rearranges to a secondary carbocation via a 1,2-hydride shift"
    - "no reaction — AlCl₃ cannot ionize primary alkyl halides"
    - "a dialkylated benzene — polyalkylation occurs before any monosubstituted product forms"
  answer: 1
  explanation: "A primary carbocation is highly unstable and undergoes rapid 1,2-hydride shift to the more stable secondary carbocation before the benzene ring can attack. The secondary carbocation then reacts with benzene, giving isopropylbenzene. This rearrangement problem means Friedel-Crafts alkylation cannot reliably install straight-chain primary alkyl groups longer than ethyl."

- question: "Why does Friedel-Crafts alkylation tend to produce polyalkylated products even when a 1:1 ratio of alkyl halide to benzene is used?"
  type: multiple-choice
  options:
    - "AlCl₃ is regenerated after each reaction, so it can catalyze unlimited substitutions"
    - "The alkyl group installed on the ring is electron-donating, activating the ring toward further electrophilic attack"
    - "The carbocation intermediate attacks the product faster than benzene because of ring strain"
    - "Polyalkylation is a rearrangement artifact and only occurs with primary alkyl halides"
  answer: 1
  explanation: "Alkyl groups are electron-donating (via hyperconjugation and induction), which activates the ring and makes the monoalkylated product more reactive toward EAS than the starting benzene. The product therefore reacts faster than the starting material, making it hard to stop cleanly at monosubstitution. A large excess of benzene is used to dilute this effect."

- question: "Friedel-Crafts alkylation of benzene with 1-chloropropane and AlCl₃ gives predominantly n-propylbenzene."
  type: true-false
  answer: false
  explanation: "False. The primary carbocation formed from 1-chloropropane undergoes a 1,2-hydride shift to the more stable secondary carbocation before attacking benzene. The predominant product is isopropylbenzene (cumene), not n-propylbenzene. This rearrangement is unavoidable with primary alkyl halides longer than ethyl."

- question: "Friedel-Crafts alkylation fails on nitrobenzene because AlCl₃ is not a strong enough Lewis acid to ionize the alkyl halide in the presence of the nitro group."
  type: true-false
  answer: false
  explanation: "False. The reaction fails because the nitro group is a strong electron-withdrawing group that deactivates the benzene ring. The ring is no longer nucleophilic enough to attack the carbocation electrophile — not because the electrophile fails to form. Any strongly electron-withdrawing substituent (–NO₂, –CF₃, –COR) deactivates the ring to the point where EAS cannot proceed."

- question: "Why is Friedel-Crafts acylation often preferred over alkylation when the synthetic goal is to install a straight-chain alkyl group on a benzene ring?"
  type: short-answer
  answer: "Acylation generates a resonance-stabilized acylium cation (RC≡O⁺) that does not rearrange, giving a predictable product. The resulting ketone also deactivates the ring (the carbonyl is electron-withdrawing), preventing polyacylation. The ketone can then be reduced to the desired alkyl group. Alkylation suffers from both carbocation rearrangement and polyalkylation."
  explanation: "The acylium cation is stabilized by resonance with the oxygen lone pair, which distributes the positive charge and prevents 1,2-shifts. The carbonyl product deactivates the ring so cleanly that a second acylation rarely occurs. After Clemmensen or Wolff-Kishner reduction, you obtain the straight-chain alkyl group that alkylation could never deliver reliably."
```

## Explainer

You already know the general mechanism of **electrophilic aromatic substitution** (EAS): an electrophile attacks the pi electron cloud of benzene, forming a resonance-stabilized carbocation intermediate (the arenium ion or sigma complex), followed by loss of a proton to restore aromaticity. Friedel-Crafts alkylation is a specific instance of EAS where the electrophile is a **carbocation** derived from an alkyl halide, and the result is a new C–C bond between the ring and an alkyl group.

The reaction begins with generating the electrophile. Aluminum chloride (AlCl₃), a strong **Lewis acid**, coordinates to the halide of the alkyl halide (say, CH₃CH₂CH₂Cl), polarizing the C–Cl bond and either forming a tight ion pair or fully generating the free carbocation. The electron-rich benzene ring then attacks this electrophilic carbon, forming the arenium ion intermediate. Deprotonation by AlCl₄⁻ (the aluminum ate complex) restores the aromatic ring and regenerates the AlCl₃ catalyst. The overall transformation: a hydrogen on benzene has been replaced by an alkyl group.

The most important complication is **carbocation rearrangement**. From your study of carbocation stability, you know that secondary carbocations are more stable than primary, and tertiary more stable than secondary. If a primary alkyl halide like 1-chloropropane forms a primary carbocation, it will rapidly rearrange via a 1,2-hydride shift to the more stable secondary carbocation before the benzene ring attacks. This means that attempting Friedel-Crafts alkylation with n-propyl chloride gives predominantly isopropylbenzene, not n-propylbenzene. This rearrangement problem limits the synthetic utility of the reaction — you cannot reliably install primary alkyl groups longer than methyl or ethyl.

There is a second limitation: **polyalkylation**. The alkyl group you just attached to the ring is an electron-donating group (via hyperconjugation and induction), which activates the ring toward further electrophilic attack. This means the monoalkylated product reacts *faster* than the starting benzene, making it difficult to stop at a single substitution. Using a large excess of benzene relative to the alkyl halide helps, but the selectivity is imperfect. A third limitation is that the reaction fails entirely with rings bearing strong electron-withdrawing groups (–NO₂, –CF₃, –COR) because the deactivated ring is not nucleophilic enough to attack the carbocation. These limitations — rearrangement, polyalkylation, and sensitivity to ring electronics — are why Friedel-Crafts acylation (followed by reduction) is often preferred when you need to install a straight-chain alkyl group without rearrangement.
