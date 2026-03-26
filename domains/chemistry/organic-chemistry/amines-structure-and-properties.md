---
id: amines-structure-and-properties
title: 'Amines: Structure, Basicity, and Reactions'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: functional-groups-overview
  type: hard
- id: acid-base-chemistry
  type: hard
- id: electrophilic-aromatic-substitution
  type: soft
- id: carboxylic-acids-and-derivatives
  type: soft
- id: nucleophilic-acyl-substitution
  type: soft
tags:
- amines
- basicity
- nucleophilicity
- primary
- secondary
- tertiary
- amine
- arylamines
- pKa
stage: formal-systems
status: validated
---
# Amines: Structure, Basicity, and Reactions

## Core Idea
Amines are organic derivatives of ammonia bearing one to three carbon substituents on nitrogen. Nitrogen's lone pair makes amines both basic and nucleophilic. Alkylamines (conjugate acid pKa ≈ 10–11) are more basic than arylamines (pKa ≈ 4–5) because the aromatic ring delocalizes the nitrogen lone pair into the pi system, reducing its availability for protonation. Amines react as nucleophiles with carbonyl compounds, acyl chlorides, and alkyl halides. Amide nitrogens are significantly less basic and nucleophilic than amine nitrogens because their lone pair is delocalized into the adjacent carbonyl.

## How It's Best Learned
Compare basicity of the series: NH₃, methylamine, dimethylamine, aniline, pyridine, and the nitrogen of acetamide. For each, draw resonance structures or identify inductive effects explaining the trend. Then predict the product when each reacts with an acyl chloride.

## Common Misconceptions
- More alkyl substitution generally increases basicity in the gas phase but in water, solvation effects complicate the trend for secondary vs tertiary amines.
- Amide nitrogens are drastically less basic than amine nitrogens — protonation of an amide occurs on oxygen, not nitrogen, because the N lone pair is delocalized.
- Quaternary ammonium salts (R₄N⁺) carry a permanent positive charge and cannot act as bases or nucleophiles.

## Questions

```yaml
- question: "A student predicts that aniline (C₆H₅NH₂) should be a stronger base than methylamine (CH₃NH₂), reasoning that the benzene ring is electron-rich and should push electron density toward nitrogen. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — aniline is indeed a stronger base because the aromatic ring donates electrons to nitrogen via induction"
    - "The benzene ring withdraws electrons from nitrogen inductively through the C–N bond, which reduces basicity but not through resonance"
    - "The benzene ring delocalizes the nitrogen lone pair into the π system via resonance, reducing its availability for protonation and making aniline far less basic"
    - "Aniline cannot be protonated at all because the lone pair is fully committed to maintaining aromaticity"
  answer: 2
  explanation: "This is the central misconception about arylamine basicity. The benzene ring does contain high electron density, but it interacts with the nitrogen lone pair through resonance — the lone pair donates into the aromatic π system, delocalizing it across the ring. This resonance reduces the availability of the lone pair for accepting a proton. Aniline's conjugate acid pKa ≈ 4–5 vs. methylamine's ≈ 10–11 — aniline is roughly a million times weaker as a base. The student's error is confusing overall ring electron density with lone-pair availability: resonance delocalization into the ring stabilizes aniline but simultaneously makes protonation much less favorable."

- question: "Why are amide nitrogens (as in acetamide, CH₃CONH₂) far less basic than amine nitrogens?"
  type: multiple-choice
  options:
    - "The carbonyl oxygen withdraws electrons from nitrogen purely through induction along the C–N bond"
    - "The nitrogen lone pair is delocalized into the adjacent carbonyl π system via resonance, leaving it much less available for protonation"
    - "Amide nitrogen is bonded to more substituents, which sterically block approach of a proton"
    - "The carbonyl group formally converts the amide nitrogen into a quaternary center with no lone pair"
  answer: 1
  explanation: "In amides, the nitrogen lone pair participates in resonance with the adjacent carbonyl — this is why amide C–N bonds have partial double-bond character and why amide bonds are rigid and planar. The lone pair is delocalized into the carbonyl π* orbital. As a result, protonation of an amide occurs preferentially on oxygen (giving a more resonance-stabilized cation), not on nitrogen. The dramatic loss of lone pair availability makes amide nitrogens barely basic, with conjugate acid pKa values near 0, compared to ~10–11 for simple alkylamines. Understanding this delocalization is essential for predicting reactivity in peptide chemistry."

- question: "An amine that is less basic than another will generally also be a weaker nucleophile toward a sterically accessible electrophilic carbon center."
  type: true-false
  answer: true
  explanation: "Basicity (toward H⁺) and nucleophilicity (toward carbon electrophiles) both depend on the availability of the nitrogen lone pair. An amine with a more available, less delocalized lone pair is both more willing to donate to H⁺ (more basic) and more willing to attack an electrophilic carbon (more nucleophilic). This is why arylamines like aniline are both weaker bases AND weaker nucleophiles than alkylamines — the resonance delocalization that reduces basicity also reduces nucleophilicity toward carbon electrophiles. The important caveat is steric effects: a bulky tertiary amine like triethylamine is a good base but a poor nucleophile because the alkyl groups block approach to carbon centers."

- question: "Adding more alkyl groups to an amine generally increases its basicity in aqueous solution."
  type: true-false
  answer: false
  explanation: "In the gas phase, basicity increases monotonically with alkylation (Me₃N > Me₂NH > MeNH₂ > NH₃) because each alkyl group donates electrons inductively to nitrogen. In aqueous solution, the trend breaks down: secondary amines are typically more basic than tertiary amines because solvation matters. A protonated tertiary amine (R₃NH⁺) is less effectively stabilized by hydrogen bonding with water than a protonated secondary amine (R₂NH₂⁺), which has more N–H bonds available for hydrogen bonding. The solvation penalty partially offsets the inductive benefit, so the aqueous trend is non-monotonic. This is a classic case where gas-phase logic must be qualified for solution-phase conditions."

- question: "Explain why aniline (C₆H₅NH₂) is a far weaker base than cyclohexylamine (C₆H₁₁NH₂), even though both have a nitrogen atom with a lone pair."
  type: short-answer
  answer: "Cyclohexylamine has an sp³ carbon substituent on nitrogen; the cyclohexyl ring donates electrons inductively, leaving the nitrogen lone pair localized in an sp³ orbital and more available for protonation. Aniline has an aryl group on nitrogen; draw the resonance structures and you see the nitrogen lone pair delocalizing into the ortho and para positions of the benzene ring, generating partial negative charge on the ring and partial positive charge on nitrogen. This resonance stabilizes aniline itself, but destabilizes protonation because accepting a proton would require the lone pair to localize — eliminating the resonance benefit. The net result: aniline's conjugate acid pKa ≈ 4.6 vs. cyclohexylamine's ≈ 10.6, a difference of ~10⁶ in Kₐ."
  explanation: "The key insight is that resonance delocalization of the lone pair stabilizes the free base but makes protonation thermodynamically costly. When aniline is protonated, nitrogen rehybridizes toward sp³, the N–aromatic π interaction is disrupted, and the resonance stabilization is lost. The conjugate acid of aniline is therefore poorly stabilized relative to the free base, making protonation unfavorable. For cyclohexylamine, no such resonance stabilization exists in the free base, so there is no analogous penalty upon protonation."
```

## Explainer

You already know functional groups and acid-base chemistry, so think of amines as ammonia (NH₃) with one, two, or three hydrogens replaced by carbon groups. A **primary amine** (RNH₂) has one carbon substituent, a **secondary amine** (R₂NH) has two, and a **tertiary amine** (R₃N) has three. In every case, nitrogen retains a lone pair of electrons in an sp³ orbital, giving amines their pyramidal geometry and — crucially — their dual chemical personality as both bases and nucleophiles.

**Basicity** is the defining property of amines and the key to predicting their behavior. When an amine accepts a proton, the lone pair on nitrogen forms a bond to H⁺, producing an ammonium ion. The strength of this tendency depends on how available that lone pair is. Alkyl groups are electron-donating (through induction), so **alkylamines** are more basic than ammonia — their conjugate acids have pKa values around 10–11. Now compare **arylamines** like aniline: the nitrogen lone pair overlaps with the aromatic π system, delocalizing electron density into the ring. This resonance stabilization makes the lone pair less available for protonation, dropping the conjugate acid pKa to about 4–5. The same logic explains why **amide** nitrogens (as in acetamide) are barely basic at all — the lone pair is heavily delocalized into the adjacent carbonyl, and protonation actually occurs preferentially on the oxygen rather than the nitrogen.

As **nucleophiles**, amines react with electrophilic carbon centers. They attack alkyl halides in SN2 reactions (though over-alkylation is a practical problem because the product amine is also nucleophilic), and they attack acyl chlorides and esters in nucleophilic acyl substitution to form amides. This nucleophilic reactivity follows the same electronic logic as basicity: the more available the lone pair, the better the nucleophile. Steric effects also matter — a bulky tertiary amine like triethylamine is a good base but a poor nucleophile because the carbon groups block approach to electrophilic centers.

The interplay between basicity and nucleophilicity is what makes amines so versatile in organic synthesis. A primary amine can serve as a nucleophile to open an epoxide, as a base to deprotonate an acid, or as a building block for forming amide bonds — the same linkage that connects amino acids in proteins. Understanding which role the amine plays in a given reaction comes down to the same question every time: how available is the nitrogen lone pair, and what electrophile or proton source is it encountering?
