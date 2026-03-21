---
id: alkyne-structure-and-nomenclature
title: Alkyne Structure and Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alkene-structure-and-nomenclature
  type: hard
tags:
- alkynes
- triple bond
- sp hybridization
- terminal alkyne
- acidity
- reduction
stage: advanced
status: validated
---

# Alkyne Structure and Reactions

## Core Idea
Alkynes contain a C≡C triple bond — one sigma and two mutually perpendicular pi bonds — with sp-hybridized carbons and linear geometry (180°). Terminal alkynes (R–C≡C–H) are weakly acidic (pKa ≈ 25) because the sp carbon's high s-character keeps bonding electrons close to the nucleus, stabilizing the conjugate base alkynide anion. Alkynes undergo electrophilic addition similar to alkenes but can add two equivalents of reagent. Selective partial reduction to cis-alkenes uses Lindlar's catalyst; dissolving metal (Na/NH₃) reduction gives the trans-alkene.

## How It's Best Learned
Compare acidity: water (pKa 16) > terminal alkyne (25) > alkene vinyl H (44) > alkane (50) and explain each trend. Practice predicting the product of one vs two equivalents of HBr addition to a terminal alkyne, applying Markovnikov's rule at each step.

## Common Misconceptions
- Terminal alkyne protons are not strongly acidic — deprotonation requires bases like NaNH₂ or n-BuLi, not NaOH.
- Partial reduction selectivity (cis vs trans) is determined entirely by the choice of reducing agent, not by any property of the alkyne.
- Alkyne addition of two equivalents does not give the same stereochemistry as two sequential alkene additions.

## Questions

```yaml
- question: "A chemist wants to deprotonate a terminal alkyne to generate a nucleophilic alkynide anion for a carbon-carbon bond forming reaction. Which reagent is appropriate?"
  type: multiple-choice
  options:
    - "NaOH in aqueous solution (conjugate acid pKa ≈ 16)"
    - "NaHCO₃ in aqueous solution (conjugate acid pKa ≈ 10)"
    - "NaNH₂ in THF (conjugate acid pKa ≈ 38)"
    - "Acetic acid (pKa ≈ 5)"
  answer: 2
  explanation: "To deprotonate a terminal alkyne (pKa ≈ 25), the base must have a conjugate acid with a pKa *higher* than 25 — the base's conjugate acid must be weaker than the terminal alkyne's conjugate acid. NaNH₂ has a conjugate acid (NH₃) with pKa ≈ 38, making it sufficiently basic. NaOH (conjugate acid pKa ≈ 16) and NaHCO₃ (pKa ≈ 10) are far too weak. Acetic acid is an acid, not a base. This is a classic misconception: terminal alkynes feel 'relatively acidic' compared to alkanes, but pKa 25 still requires strong bases like NaNH₂ or n-BuLi — not aqueous hydroxide."

- question: "Why is the C–H bond on a terminal alkyne (pKa ≈ 25) more acidic than a vinyl C–H bond on an alkene (pKa ≈ 44)?"
  type: multiple-choice
  options:
    - "The triple bond withdraws electron density through resonance, weakening the C–H bond inductively"
    - "The sp carbon of the alkyne has 50% s-character, stabilizing the negative charge on the alkynide anion better than the 33% s-character of an sp² carbon"
    - "The linear geometry of the alkyne reduces steric hindrance around the acidic proton"
    - "The two pi bonds in the triple bond donate electron density to the sigma framework, polarizing the C–H bond"
  answer: 1
  explanation: "The key is hybridization and s-character. An sp orbital has 50% s-character; sp² has 33%; sp³ has 25%. S orbitals hold electrons closer to the nucleus at lower energy. The greater the s-character of the orbital holding the lone pair on the carbanion (alkynide anion), the better it stabilizes the negative charge. Therefore, sp (50%) > sp² (33%) > sp³ (25%) in carbanion stability, giving the acidity order: terminal alkyne > vinyl C–H > alkane C–H. This is a hybridization effect, not resonance."

- question: "Treating an internal alkyne with sodium metal dissolved in liquid ammonia (dissolving metal reduction) gives the trans-alkene as the major product."
  type: true-false
  answer: true
  explanation: "True. Dissolving metal reduction proceeds via a radical anion mechanism: an electron from Na is added to the alkyne to give a vinyl radical anion, which is protonated by NH₃ to give a vinyl radical; then a second electron gives a vinyl carbanion, which is protonated again. The most stable vinyl radical and carbanion intermediates have the two substituents *trans* (anti) to minimize steric strain. This mechanism delivers hydrogens to *opposite* faces, producing the *trans* (E) alkene exclusively. In contrast, Lindlar's catalyst delivers both hydrogens from the same catalyst surface, giving the *cis* (Z) alkene."

- question: "Terminal alkynes are strongly acidic and can be readily deprotonated by common bases like aqueous sodium hydroxide solution."
  type: true-false
  answer: false
  explanation: "False. Terminal alkynes have pKa ≈ 25 — more acidic than alkenes (~44) or alkanes (~50), but very weakly acidic by ordinary standards. Water has pKa 16, meaning NaOH (conjugate acid pKa ≈ 16) is not strong enough to deprotonate a terminal alkyne. Strong bases like NaNH₂ (conjugate acid pKa ~38) or n-BuLi (~50) are required. The relative acidity of terminal alkynes is important for synthetic utility but should not be overstated — an alkyne proton is roughly 10 billion times less acidic than an acetic acid proton."

- question: "Explain, using hybridization and s-character, why terminal alkynes are more acidic than vinyl C–H bonds, which are in turn more acidic than alkane C–H bonds."
  type: short-answer
  answer: "Acidity reflects the stability of the conjugate base (carbanion). In each case, the negative charge resides in a hybrid orbital on carbon: sp for alkynide (50% s-character), sp² for vinyl carbanion (33%), sp³ for alkyl carbanion (25%). S-orbital electrons experience greater nuclear attraction and are held at lower energy. The greater the s-character, the more the negative charge is stabilized, and the more acidic the corresponding C–H bond. This gives the order: terminal alkyne (pKa ~25) > vinyl C–H (pKa ~44) > alkane C–H (pKa ~50), mirroring s-character: 50% > 33% > 25%."
  explanation: "This is purely a hybridization argument — not resonance or inductive effects. The same reasoning explains why sp-hybridized carbanions are *more* stable (higher s-character stabilizes negative charge) while sp-hybridized carbocations would be *less* stable (pulling positive charge toward the nucleus destabilizes it). This is one of the cleaner structure-reactivity relationships in organic chemistry: the s-character numbers map directly and predictably to the observed acidity trend."
```

## Explainer

You already know that alkenes feature a C=C double bond with sp² hybridization and trigonal planar geometry. Alkynes take this one step further: a **C≡C triple bond** consists of one sigma bond and two pi bonds, with the two pi bonds oriented perpendicular to each other. The carbon atoms are **sp-hybridized**, meaning each uses two hybrid orbitals (one for the sigma bond to the other triple-bond carbon, one for the bond to the substituent) and two unhybridized p orbitals for the pi bonds. This gives alkynes a distinctive **linear geometry** with 180° bond angles — the region around the triple bond is a rod, not a plane.

This linear geometry has a surprising chemical consequence: **terminal alkynes are weakly acidic**. The C–H bond on a terminal alkyne (R–C≡C–H) has a pKa of about 25, which is dramatically more acidic than an alkene vinyl C–H (~44) or an alkane C–H (~50). The explanation connects directly to hybridization. An sp orbital has 50% s-character, compared to 33% for sp² and 25% for sp³. Since s orbitals hold electrons closer to the nucleus, the sp orbital stabilizes the negative charge on the resulting **alkynide anion** (R–C≡C⁻) more effectively. This acidity is synthetically powerful: bases like NaNH₂ can deprotonate terminal alkynes to generate nucleophilic alkynide ions, which then react with electrophiles to form new carbon-carbon bonds.

Alkynes undergo **electrophilic addition** reactions similar to alkenes, but with a key difference: since there are two pi bonds available, alkynes can react with one *or* two equivalents of reagent. Adding one equivalent of HBr to a terminal alkyne follows Markovnikov's rule, placing the bromine on the more substituted carbon to give a vinyl halide. Adding a second equivalent yields a geminal dihalide. Controlling the stoichiometry — stopping at one equivalent — is an important synthetic skill.

Perhaps the most useful alkyne reaction is **partial reduction** to an alkene, where the choice of reagent controls stereochemistry completely. **Lindlar's catalyst** (a poisoned palladium catalyst) delivers hydrogen to the same face of the triple bond, producing the **cis-alkene** exclusively. **Dissolving metal reduction** (sodium in liquid ammonia) proceeds through a radical anion mechanism that delivers hydrogen to opposite faces, giving the **trans-alkene**. This stereochemical control makes alkynes valuable synthetic intermediates: you can build a triple bond, then selectively reduce it to whichever alkene geometry you need.
