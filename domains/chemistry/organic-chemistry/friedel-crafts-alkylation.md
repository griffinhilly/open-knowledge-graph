---
id: friedel-crafts-alkylation
title: Friedel-Crafts Alkylation and Limitations
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-aromatic-substitution
  type: hard
builds-toward:
- friedel-crafts-acylation
tags:
- friedel-crafts
- alkylation
- carbocation
- rearrangement
- polyalkylation
stage: advanced
status: draft
---

# Friedel-Crafts Alkylation and Limitations

## Core Idea
Friedel-Crafts alkylation uses an alkyl halide and Lewis acid catalyst (AlCl₃) to alkylate aromatic rings, forming C-C bonds. The mechanism involves carbocation formation; consequently, rearrangement occurs with primary halides, and the resulting alkyl group activates the ring toward further alkylation (polyalkylation problem). Friedel-Crafts alkylation fails on strongly deactivated rings and benzene rings with certain electron-withdrawing groups.

## Explainer

From electrophilic aromatic substitution (EAS), you know the general pattern: an electrophile attacks the π-electron cloud of benzene, forming an arenium ion intermediate (a carbocation delocalized across the ring), followed by loss of a proton to restore aromaticity. Friedel-Crafts alkylation fits this template exactly — the electrophile is a **carbocation** generated from an alkyl halide and a Lewis acid catalyst, typically **aluminum chloride (AlCl₃)**. The Lewis acid abstracts the halide to form a reactive carbocation (or a highly polarized complex that behaves like one), which then attacks the aromatic ring in the standard EAS mechanism.

The involvement of a carbocation intermediate explains the reaction's two major limitations. First, **carbocation rearrangement**: if you attempt to add a primary alkyl group using a primary alkyl halide, the initially formed primary carbocation (or incipient carbocation in the AlCl₃ complex) can undergo a 1,2-hydride or methyl shift to produce a more stable secondary or tertiary carbocation. The product you isolate then has a branched alkyl group rather than the straight chain you intended. For example, reacting benzene with 1-chloropropane and AlCl₃ often yields isopropylbenzene (from rearrangement to a secondary carbocation) rather than n-propylbenzene. If you need a straight-chain alkyl group on a ring, you must use Friedel-Crafts acylation followed by reduction instead.

Second, **polyalkylation**: once one alkyl group is on the ring, it donates electron density through hyperconjugation and induction, making the ring more nucleophilic than the starting benzene. The monoalkylated product reacts faster than benzene itself, so a second (and third) alkylation occurs readily. Controlling the reaction to give just one substitution requires using a large excess of benzene relative to the alkyl halide so that statistically, most electrophilic attacks hit unreacted benzene rather than the already-alkylated product.

Finally, Friedel-Crafts alkylation **fails entirely on deactivated rings** — those bearing strong electron-withdrawing groups such as –NO₂, –CN, or –SO₃H. These groups pull electron density out of the ring so aggressively that the ring is too electron-poor to attack the carbocation electrophile. The reaction also fails with amines because the nitrogen lone pair coordinates to the Lewis acid catalyst, destroying its catalytic activity. Recognizing these limitations is essential: when you see a target molecule with an alkyl group on a deactivated ring, you know Friedel-Crafts was not the route — the alkyl group must have been installed before the deactivating group, or a different strategy was used entirely.
