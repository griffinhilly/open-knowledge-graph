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
status: draft
---

# Friedel-Crafts Alkylation Mechanism

## Core Idea
Friedel-Crafts alkylation adds an alkyl group to a benzene ring via an alkyl carbocation intermediate, typically generated from an alkyl halide and a Lewis acid catalyst (AlCl₃). The reaction proceeds through electrophilic aromatic substitution with the benzene π-electrons attacking the carbocation. Rearrangement to more stable carbocations can occur, making primary alkyl halides problematic substrates.

## Explainer

You already know the general mechanism of **electrophilic aromatic substitution** (EAS): an electrophile attacks the pi electron cloud of benzene, forming a resonance-stabilized carbocation intermediate (the arenium ion or sigma complex), followed by loss of a proton to restore aromaticity. Friedel-Crafts alkylation is a specific instance of EAS where the electrophile is a **carbocation** derived from an alkyl halide, and the result is a new C–C bond between the ring and an alkyl group.

The reaction begins with generating the electrophile. Aluminum chloride (AlCl₃), a strong **Lewis acid**, coordinates to the halide of the alkyl halide (say, CH₃CH₂CH₂Cl), polarizing the C–Cl bond and either forming a tight ion pair or fully generating the free carbocation. The electron-rich benzene ring then attacks this electrophilic carbon, forming the arenium ion intermediate. Deprotonation by AlCl₄⁻ (the aluminum ate complex) restores the aromatic ring and regenerates the AlCl₃ catalyst. The overall transformation: a hydrogen on benzene has been replaced by an alkyl group.

The most important complication is **carbocation rearrangement**. From your study of carbocation stability, you know that secondary carbocations are more stable than primary, and tertiary more stable than secondary. If a primary alkyl halide like 1-chloropropane forms a primary carbocation, it will rapidly rearrange via a 1,2-hydride shift to the more stable secondary carbocation before the benzene ring attacks. This means that attempting Friedel-Crafts alkylation with n-propyl chloride gives predominantly isopropylbenzene, not n-propylbenzene. This rearrangement problem limits the synthetic utility of the reaction — you cannot reliably install primary alkyl groups longer than methyl or ethyl.

There is a second limitation: **polyalkylation**. The alkyl group you just attached to the ring is an electron-donating group (via hyperconjugation and induction), which activates the ring toward further electrophilic attack. This means the monoalkylated product reacts *faster* than the starting benzene, making it difficult to stop at a single substitution. Using a large excess of benzene relative to the alkyl halide helps, but the selectivity is imperfect. A third limitation is that the reaction fails entirely with rings bearing strong electron-withdrawing groups (–NO₂, –CF₃, –COR) because the deactivated ring is not nucleophilic enough to attack the carbocation. These limitations — rearrangement, polyalkylation, and sensitivity to ring electronics — are why Friedel-Crafts acylation (followed by reduction) is often preferred when you need to install a straight-chain alkyl group without rearrangement.
