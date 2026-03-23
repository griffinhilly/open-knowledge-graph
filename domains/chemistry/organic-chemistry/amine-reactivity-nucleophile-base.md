---
id: amine-reactivity-nucleophile-base
title: 'Amine Reactivity: Nucleophilicity and Basicity'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: amines-structure-and-properties
  type: hard
- id: acid-base-chemistry
  type: hard
builds-toward:
- amine-alkylation-quaternary-ammonium
- amide-formation-and-properties
tags:
- amine-basicity
- nucleophilicity
- pka
- lone-pair
stage: formal-systems
status: draft
---

# Amine Reactivity: Nucleophilicity and Basicity

## Core Idea
Amines are nucleophiles and bases due to their lone pair on nitrogen. Basicity (measured by pKb or conjugate acid pKa) reflects the availability of the lone pair for protonation; nucleophilicity reflects the lone pair's tendency to attack an electrophilic carbon. Aliphatic amines are better nucleophiles than anilines due to electron delocalization in the aromatic ring, while basicity and nucleophilicity trends are not always parallel.

## Questions

```yaml
- question: "Diisopropylamine (conjugate acid pKₐ ≈ 11) reacts far more slowly with methyl iodide than methylamine (conjugate acid pKₐ ≈ 10.6), despite being a slightly stronger base. What best explains this?"
  type: multiple-choice
  options:
    - "The electron-withdrawing isopropyl groups reduce the electron density on nitrogen, making it less nucleophilic"
    - "The bulky isopropyl groups sterically shield the nitrogen lone pair, reducing its nucleophilicity toward carbon electrophiles even though basicity (proton affinity) remains high"
    - "Methylamine is a stronger nucleophile precisely because it is a weaker base — basicity and nucleophilicity always trade off"
    - "The reaction with methyl iodide proceeds through a proton-transfer mechanism, which favors weaker bases"
  answer: 1
  explanation: "Steric bulk around nitrogen impedes approach to an electrophilic carbon (an SN2 transition state) without significantly affecting basicity, which only requires approach to a tiny proton. Diisopropylamine's two isopropyl groups shield nitrogen from carbon electrophiles while leaving it capable of deprotonating acidic protons. This is the key divergence between nucleophilicity (kinetic, depends on geometry) and basicity (equilibrium, depends on electron availability)."

- question: "Aniline (PhNH₂, conjugate acid pKₐ ≈ 4.6) is a far weaker base than cyclohexylamine (conjugate acid pKₐ ≈ 10.7) primarily because:"
  type: multiple-choice
  options:
    - "The aromatic ring withdraws electrons inductively through σ bonds, reducing nitrogen's electron density"
    - "Nitrogen in aniline is sp² hybridized and geometrically unable to accept a proton"
    - "The nitrogen lone pair in aniline is delocalized into the π system of the aromatic ring, making it less available for protonation"
    - "Aniline's conjugate acid (anilinium) is destabilized by electrostatic repulsion from the aromatic ring"
  answer: 2
  explanation: "In aniline, nitrogen's lone pair overlaps with the aromatic π system — resonance structures show electron density donated from N into the ring. This delocalization reduces the availability of the lone pair for protonation (basicity) and also for carbon attack (nucleophilicity). Cyclohexylamine has no such delocalization; its lone pair is fully localized in an sp³ orbital and available for both proton and carbon attack."

- question: "A bulky amine like diisopropylamine can be a stronger base than a smaller amine while simultaneously being a weaker nucleophile toward carbon electrophiles, because steric effects impact reaction kinetics more than they impact equilibrium proton affinity."
  type: true-false
  answer: true
  explanation: "Protonation requires only a small proton to approach nitrogen — steric bulk barely obstructs it. Carbon electrophile attack (SN2) requires a larger carbon center to approach nitrogen and form a transition state — here steric bulk is decisive. This explains why LDA (lithium diisopropylamide), with pKₐ of conjugate acid ≈ 36, is used as a strong, non-nucleophilic base: it deprotonates readily but doesn't add to carbonyls."

- question: "Because basicity and nucleophilicity both depend on the nitrogen lone pair, a stronger amine base will always be a better nucleophile toward carbon electrophiles."
  type: true-false
  answer: false
  explanation: "Basicity and nucleophilicity are distinct: basicity is an equilibrium property (thermodynamic) reflecting affinity for protons; nucleophilicity is a kinetic property reflecting rate of attack on carbon. They often correlate, but steric effects, polarizability, and solvent all cause divergence. A bulky base like LDA is a weaker nucleophile than its basicity predicts. In protic solvents, large, polarizable species (e.g., iodide) can be strong nucleophiles despite being weak bases."

- question: "A chemist wants to deprotonate the α-carbon of a ketone to form an enolate without any addition to the carbonyl group. Why would they choose LDA (lithium diisopropylamide) rather than a small primary amine like n-propylamine?"
  type: short-answer
  answer: "LDA is a very strong base (conjugate acid pKₐ ≈ 36, far exceeding the α-carbon pKₐ of ~20) but a very poor nucleophile due to the steric bulk of its two isopropyl groups. This makes it ideal for clean deprotonation (base role) without nucleophilic addition to the carbonyl carbon. N-propylamine is a much weaker base (pKₐ ≈ 10.7) — too weak to deprotonate the α-carbon efficiently — and is also a good nucleophile, making it prone to 1,2-addition to the carbonyl rather than deprotonation."
  explanation: "The choice between acting as a base vs. a nucleophile is the central design decision in amine chemistry. When you need a base without nucleophilic side reactions, you choose sterically hindered amines. When you need nucleophilic attack on carbon, you choose small, unhindered amines with localized lone pairs."
```

## Explainer

From acid-base chemistry, you know that a base is a species that donates an electron pair to a proton. From your study of amine structure, you know that nitrogen in an amine carries a lone pair of electrons in an sp³ orbital. That lone pair is the source of all amine reactivity — but it can do two fundamentally different things: grab a proton (acting as a **base**) or attack an electrophilic carbon (acting as a **nucleophile**). Understanding when an amine does which — and how structural features bias the balance — is the key to predicting amine behavior in reactions.

**Basicity** is an equilibrium property: how much does the amine want to hold onto a proton once it has one? We measure this by the pKₐ of the conjugate acid (the ammonium ion, RNH₃⁺). A higher conjugate acid pKₐ means the amine is a stronger base. Aliphatic amines like methylamine (conjugate acid pKₐ ≈ 10.6) are moderately strong bases because the nitrogen lone pair is localized and electron-donating alkyl groups stabilize the positive charge on the ammonium ion. Aniline (conjugate acid pKₐ ≈ 4.6) is a far weaker base because its lone pair is delocalized into the aromatic ring — the electrons are partially "borrowed" by the π system and less available for protonation.

**Nucleophilicity** is a kinetic property: how fast does the lone pair attack an electrophilic carbon? It correlates with basicity in many cases, but not always. Steric bulk around nitrogen reduces nucleophilicity without necessarily reducing basicity much — a bulky base like diisopropylamine is still a strong base (its conjugate acid pKₐ ≈ 11) but a poor nucleophile because the nitrogen is shielded. Conversely, polarizability and solvent effects can make a species a better nucleophile than its basicity would predict. The practical rule is: basicity predicts proton affinity; nucleophilicity predicts carbon-attack rate. When designing a reaction, you choose your amine based on which role you need it to play — a hindered amine like LDA when you want deprotonation without substitution, or a small unhindered amine like n-butylamine when you want nucleophilic attack on a carbonyl or alkyl halide.
