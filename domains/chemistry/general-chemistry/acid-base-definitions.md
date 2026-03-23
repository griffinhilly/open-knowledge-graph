---
id: acid-base-definitions
title: Acid-Base Definitions
domain: chemistry
course: general-chemistry
prerequisites:
- id: covalent-bonding
  type: hard
- id: ionic-bonding
  type: soft
builds-toward:
- acid-base-chemistry
tags:
- Arrhenius
- Bronsted-Lowry
- Lewis-acid-base
- conjugate-acid
- conjugate-base
- proton-donor
- electron-pair-acceptor
stage: formal-systems
status: draft
---
# Acid-Base Definitions

## Core Idea
Three progressively broader definitions classify acids and bases. The Arrhenius definition (narrowest): acids produce H⁺ in water, bases produce OH⁻. The Brønsted-Lowry definition: acids are proton (H⁺) donors, bases are proton acceptors — this works in any solvent and introduces conjugate acid-base pairs (an acid donates a proton to become its conjugate base, and vice versa). The Lewis definition (broadest): acids are electron-pair acceptors, bases are electron-pair donors — encompassing reactions with no proton transfer at all, such as BF₃ accepting a lone pair from NH₃. Each broader definition includes all reactions classified by the narrower one.

## How It's Best Learned
Classify the same reaction under all three definitions where possible, then find examples that work under Lewis but not Brønsted-Lowry (e.g., metal-ligand coordination). Practice identifying conjugate pairs: every Brønsted-Lowry reaction has exactly two conjugate pairs.

## Common Misconceptions
- Not all Lewis acid-base reactions involve protons. Students who learn Brønsted-Lowry first often assume every acid-base reaction is a proton transfer, but metal ion hydration (M²⁺ + 6H₂O) is a Lewis acid-base reaction with no proton exchange.
- A substance can be an acid by one definition and a base by another depending on the reaction context. Water, for example, is amphoteric — acting as either acid or base.

## Questions

```yaml
- question: "Boron trifluoride (BF₃) reacts with ammonia (NH₃) to form BF₃·NH₃. BF₃ has no proton to donate and no OH⁻ to release. Under which acid-base framework(s) can BF₃ be classified as an acid?"
  type: multiple-choice
  options:
    - "Arrhenius only — BF₃ is an acid because it dissolves in water"
    - "Brønsted-Lowry only — BF₃ accepts a proton from NH₃"
    - "Lewis only — BF₃ accepts an electron pair from NH₃'s lone pair"
    - "None — BF₃ cannot be an acid because it doesn't donate protons or produce H⁺"
  answer: 2
  explanation: "BF₃ is a Lewis acid: boron has an empty orbital and accepts the lone pair on nitrogen, forming a coordinate covalent bond. There is no proton transfer (eliminating Brønsted-Lowry) and no H⁺ or OH⁻ production in water (eliminating Arrhenius). Option D represents the exact misconception the Lewis definition was designed to correct — not every acid-base reaction involves protons. The Lewis definition is broader precisely because it captures electron-pair interactions independent of proton transfer."

- question: "Which pair of definitions correctly classifies HF donating a proton to F⁻ to give HF₂⁻?"
  type: multiple-choice
  options:
    - "Arrhenius acid-base only — HF produces H⁺ in water"
    - "Brønsted-Lowry and Lewis — HF donates a proton (Brønsted-Lowry acid), and F⁻ donates a lone pair to the proton (Lewis base)"
    - "Lewis only — the reaction involves electron pair donation, not proton transfer"
    - "Arrhenius and Brønsted-Lowry, but not Lewis — Lewis requires no proton transfer"
  answer: 1
  explanation: "HF donating H⁺ to F⁻ is a Brønsted-Lowry acid-base reaction (proton transfer). It is also a Lewis reaction: F⁻ donates a lone pair to the proton (H⁺ is the Lewis acid, F⁻ is the Lewis base). Every Brønsted-Lowry reaction is simultaneously a Lewis reaction — proton transfer is always also an electron-pair donation to the proton. Option D gets the nesting backwards: Lewis is the broadest definition, not the narrowest."

- question: "The Lewis definition of acids and bases competes with the Brønsted-Lowry definition — chemists must choose which framework to use because they are incompatible."
  type: true-false
  answer: false
  explanation: "The three definitions are nested like concentric circles, not competing alternatives. Every Arrhenius acid-base reaction is also a Brønsted-Lowry one; every Brønsted-Lowry reaction is also a Lewis acid-base reaction. They are not incompatible — they are progressively broader ways of classifying the same phenomenon. Chemists choose based on what they are analyzing: Brønsted-Lowry for most aqueous and protic chemistry, Lewis when electron-pair transfer is occurring without proton involvement (coordination chemistry, organometallics, many organic mechanisms)."

- question: "Water is amphoteric, meaning it can act as either an acid or a base depending on what it reacts with."
  type: true-false
  answer: true
  explanation: "Water is the classic example of an amphoteric substance. When water reacts with a stronger acid like HCl, water accepts a proton (H₂O is the Brønsted-Lowry base: HCl → H₃O⁺ + Cl⁻). When water reacts with a stronger base like NH₃, water donates a proton (H₂O is the Brønsted-Lowry acid: H₂O + NH₃ → OH⁻ + NH₄⁺). This also illustrates that acid/base identity is context-dependent — a molecule is not inherently an acid or base, but acts as one relative to its reaction partner."

- question: "Why is the Lewis acid-base definition considered the broadest of the three definitions? What category of reactions does it capture that Brønsted-Lowry cannot?"
  type: short-answer
  answer: "The Lewis definition is broadest because it defines acids as electron-pair acceptors and bases as electron-pair donors, requiring no proton transfer at all. It captures reactions like metal ion coordination (M²⁺ accepting lone pairs from water or ligands), BF₃ accepting a lone pair from NH₃, and many organometallic reactions — none of which involve H⁺. Brønsted-Lowry requires a proton donor and acceptor, so it excludes all reactions where electron pairs are transferred without proton movement. The Lewis definition subsumes Brønsted-Lowry: a proton transfer is always also an electron-pair donation to H⁺ (which is the Lewis acid), but not every electron-pair transfer involves a proton."
  explanation: "The nesting relationship — Lewis ⊃ Brønsted-Lowry ⊃ Arrhenius — is the key conceptual structure. Understanding this prevents the common error of assuming every acid-base reaction is a proton transfer. Coordination chemistry and Lewis acid catalysis (critical in organic synthesis and industrial chemistry) are entirely explained by the electron-pair framework."
```

## Explainer

The simplest way to think about acids and bases starts with water. The **Arrhenius definition** says an acid is any substance that produces H⁺ ions when dissolved in water, and a base produces OH⁻ ions. HCl dissolves and releases H⁺; NaOH dissolves and releases OH⁻. This works well for straightforward aqueous reactions, but it immediately runs into limits. What about ammonia, NH₃, which makes solutions basic without containing any OH⁻ in its formula? And what about reactions that happen in solvents other than water, or with no solvent at all? You need a broader framework.

The **Brønsted-Lowry definition** solves this by focusing on proton transfer rather than what dissolves in water. An acid is a proton (H⁺) donor; a base is a proton acceptor. When HCl reacts with NH₃, HCl donates a proton to NH₃ — HCl is the acid, NH₃ is the base. This definition introduces a powerful concept: **conjugate pairs**. After HCl donates its proton, it becomes Cl⁻, which is HCl's conjugate base. After NH₃ accepts the proton, it becomes NH₄⁺, which is NH₃'s conjugate acid. Every Brønsted-Lowry reaction produces exactly two conjugate pairs. From your understanding of covalent bonding, you can see why this works — the proton transfer involves breaking one covalent bond (H–Cl) and forming another (N–H). The strength of these bonds determines how readily the transfer occurs.

The **Lewis definition** takes one more step outward. Instead of tracking protons, it tracks electron pairs. A Lewis acid accepts an electron pair; a Lewis base donates one. This is the broadest definition because it captures reactions with no proton involved at all. When BF₃ reacts with NH₃, boron has an empty orbital that accepts the lone pair on nitrogen — BF₃ is the Lewis acid, NH₃ is the Lewis base, and a new coordinate covalent bond forms. Metal ions in solution act as Lewis acids when water molecules donate lone pairs to them during hydration. None of these involve proton transfer, yet they follow the same underlying logic of electron-pair sharing that you learned in covalent bonding.

The three definitions are nested like concentric circles: every Arrhenius acid-base reaction is also a Brønsted-Lowry reaction, and every Brønsted-Lowry reaction is also a Lewis reaction — but not the reverse. In practice, chemists default to Brønsted-Lowry for most aqueous chemistry and reach for the Lewis definition when dealing with coordination chemistry, organic reaction mechanisms, or any scenario where protons are not the central players. The key insight is that these are not competing theories but progressively wider lenses for the same fundamental phenomenon: the movement of electron density between species.
