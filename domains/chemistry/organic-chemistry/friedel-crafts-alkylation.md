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
stage: formal-systems
status: validated
---

# Friedel-Crafts Alkylation and Limitations

## Core Idea
Friedel-Crafts alkylation uses an alkyl halide and Lewis acid catalyst (AlCl₃) to alkylate aromatic rings, forming C-C bonds. The mechanism involves carbocation formation; consequently, rearrangement occurs with primary halides, and the resulting alkyl group activates the ring toward further alkylation (polyalkylation problem). Friedel-Crafts alkylation fails on strongly deactivated rings and benzene rings with certain electron-withdrawing groups.

## Questions

```yaml
- question: "A chemist attempts to synthesize n-propylbenzene by reacting benzene with 1-chloropropane and AlCl₃. What is the major product actually formed?"
  type: multiple-choice
  options:
    - "n-propylbenzene — the intended straight-chain product"
    - "isopropylbenzene — the rearranged product via a more stable secondary carbocation"
    - "allylbenzene — formed by elimination before ring attack"
    - "No reaction — primary alkyl halides cannot form carbocations with AlCl₃"
  answer: 1
  explanation: "The AlCl₃ generates an incipient primary carbocation from 1-chloropropane, which rapidly rearranges via a 1,2-hydride shift to the more stable secondary carbocation. That secondary carbocation is the actual electrophile that attacks benzene, giving isopropylbenzene. Primary carbocations are too unstable to persist, so rearrangement is essentially unavoidable with primary alkyl halides."

- question: "Why does polyalkylation occur in Friedel-Crafts alkylation, even when benzene is the sole starting material?"
  type: multiple-choice
  options:
    - "Each alkyl group added makes the AlCl₃ catalyst progressively more active"
    - "The installed alkyl group donates electron density to the ring, making it more nucleophilic than unreacted benzene"
    - "The carbocation electrophile preferentially attacks the more substituted product"
    - "Polyalkylation is a side reaction caused by moisture contaminating the AlCl₃"
  answer: 1
  explanation: "Alkyl groups are electron-donating via hyperconjugation and inductive effects, activating the ring toward electrophilic substitution. A monoalkylated product is therefore a better nucleophile than benzene itself — it reacts faster with the carbocation electrophile. The practical fix is using a large excess of benzene so most carbocations statistically encounter unreacted benzene rather than the already-alkylated product."

- question: "Friedel-Crafts alkylation can be performed successfully on nitrobenzene if excess AlCl₃ is used to overcome the deactivating effect of the nitro group."
  type: true-false
  answer: false
  explanation: "No amount of excess AlCl₃ rescues Friedel-Crafts alkylation on strongly deactivated rings. A nitro group withdraws electron density so aggressively that the ring is too electron-poor to attack the carbocation electrophile — the reaction simply fails. This is a fundamental mechanistic limitation, not a kinetic problem that can be overcome by increasing catalyst loading."

- question: "Polyalkylation in Friedel-Crafts reactions occurs because each successive alkyl substitution deactivates the ring, so subsequent reactions occur at a different position on the ring rather than attacking the same molecule again."
  type: true-false
  answer: false
  explanation: "This inverts the correct logic. Each alkyl group activates the ring, making the monosubstituted product MORE reactive than benzene — not less. Polyalkylation is not about regioselectivity on one ring; it is about the already-alkylated molecule being a faster-reacting species than the starting benzene in solution."

- question: "Why must Friedel-Crafts acylation (followed by reduction) be used instead of direct alkylation when a straight-chain alkyl group is needed on an aromatic ring?"
  type: short-answer
  answer: "Friedel-Crafts alkylation generates a carbocation intermediate that rearranges: primary carbocations shift to secondary or tertiary before attacking the ring, yielding branched products. Acylation produces a resonance-stabilized acylium ion that cannot rearrange because any shift would generate a less stable species. The resulting ketone retains the correct straight-chain carbon skeleton, which is then reduced (Clemmensen or Wolff-Kishner) to the desired alkyl group."
  explanation: "The deeper point is that this limitation is mechanistic, not a matter of conditions. Because the electrophile in alkylation is a carbocation, rearrangement is inherent whenever a primary (or certain secondary) alkyl halide is used. Acylation sidesteps this by using a fundamentally different electrophile that preserves the carbon skeleton."
```

## Explainer

From electrophilic aromatic substitution (EAS), you know the general pattern: an electrophile attacks the π-electron cloud of benzene, forming an arenium ion intermediate (a carbocation delocalized across the ring), followed by loss of a proton to restore aromaticity. Friedel-Crafts alkylation fits this template exactly — the electrophile is a **carbocation** generated from an alkyl halide and a Lewis acid catalyst, typically **aluminum chloride (AlCl₃)**. The Lewis acid abstracts the halide to form a reactive carbocation (or a highly polarized complex that behaves like one), which then attacks the aromatic ring in the standard EAS mechanism.

The involvement of a carbocation intermediate explains the reaction's two major limitations. First, **carbocation rearrangement**: if you attempt to add a primary alkyl group using a primary alkyl halide, the initially formed primary carbocation (or incipient carbocation in the AlCl₃ complex) can undergo a 1,2-hydride or methyl shift to produce a more stable secondary or tertiary carbocation. The product you isolate then has a branched alkyl group rather than the straight chain you intended. For example, reacting benzene with 1-chloropropane and AlCl₃ often yields isopropylbenzene (from rearrangement to a secondary carbocation) rather than n-propylbenzene. If you need a straight-chain alkyl group on a ring, you must use Friedel-Crafts acylation followed by reduction instead.

Second, **polyalkylation**: once one alkyl group is on the ring, it donates electron density through hyperconjugation and induction, making the ring more nucleophilic than the starting benzene. The monoalkylated product reacts faster than benzene itself, so a second (and third) alkylation occurs readily. Controlling the reaction to give just one substitution requires using a large excess of benzene relative to the alkyl halide so that statistically, most electrophilic attacks hit unreacted benzene rather than the already-alkylated product.

Finally, Friedel-Crafts alkylation **fails entirely on deactivated rings** — those bearing strong electron-withdrawing groups such as –NO₂, –CN, or –SO₃H. These groups pull electron density out of the ring so aggressively that the ring is too electron-poor to attack the carbocation electrophile. The reaction also fails with amines because the nitrogen lone pair coordinates to the Lewis acid catalyst, destroying its catalytic activity. Recognizing these limitations is essential: when you see a target molecule with an alkyl group on a deactivated ring, you know Friedel-Crafts was not the route — the alkyl group must have been installed before the deactivating group, or a different strategy was used entirely.
