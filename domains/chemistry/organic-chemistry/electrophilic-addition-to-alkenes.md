---
id: electrophilic-addition-to-alkenes
title: Electrophilic Addition to Alkenes
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alkene-structure-and-nomenclature
  type: hard
- id: reaction-mechanisms-overview
  type: hard
- id: iupac-nomenclature-alkenes
  type: soft
- id: nucleophile-electrophile-definitions
  type: hard
builds-toward:
- aromatic-compounds-intro
tags:
- addition
- electrophilic
- Markovnikov
- hydrohalogenation
- halogenation
- hydration
- hydroboration
stage: formal-systems
status: validated
---

# Electrophilic Addition to Alkenes

## Core Idea
Alkenes react with electrophiles through electrophilic addition, where the pi electrons attack an electrophile to form a carbocation intermediate (or cyclic halonium/bromonium ion), which is then trapped by a nucleophile. Markovnikov's rule — the proton adds to the carbon bearing more hydrogens — is a consequence of forming the more stable (more substituted) carbocation. Halogenation (X₂) proceeds through a cyclic bromonium ion, giving anti addition of both halogens. Hydroboration–oxidation gives syn, anti-Markovnikov addition, with no carbocation intermediate.

## How It's Best Learned
For each reagent (HX, X₂, H₂SO₄/H₂O, BH₃/H₂O₂), predict regiochemistry (which carbon receives which group) and stereochemistry (syn vs anti) before checking. Draw the mechanism for each, identifying the key intermediate.

## Common Misconceptions
- Markovnikov's rule is not arbitrary: it follows from the stability of the intermediate carbocation.
- Anti addition means the two groups add to opposite faces of the pi bond, not to opposite ends of the molecule.
- Hydroboration gives anti-Markovnikov alcohol via concerted syn addition — no carbocation forms, so no rearrangements occur.

## Questions

```yaml
- question: "When HBr adds to propene (CH3CH=CH2), the major product is 2-bromopropane. Which mechanistic explanation is correct?"
  type: multiple-choice
  options: ["Bromine is larger and prefers the less hindered primary carbon", "The proton adds to the carbon bearing fewer hydrogens, placing Br on the primary carbon", "The proton adds to the carbon bearing more hydrogens, generating a more stable secondary carbocation at the internal carbon, which bromide then attacks", "HBr always adds anti-Markovnikov when the alkene is unsymmetrical"]
  answer: 2
  explanation: "Markovnikov's rule follows from carbocation stability, not from a rule about atom size. H+ adds to the terminal carbon (more H's), generating a secondary carbocation at C2 — more stable than a primary carbocation at C1 because adjacent alkyl groups stabilize positive charge through hyperconjugation and inductive donation. Bromide then attacks the secondary carbocation, giving 2-bromopropane as the major product."

- question: "Hydroboration–oxidation of 1-methylcyclohexene gives the same alcohol product as acid-catalyzed hydration (H2SO4/H2O) of the same alkene."
  type: true-false
  answer: false
  explanation: "Acid-catalyzed hydration follows Markovnikov's rule and places OH on the more substituted carbon (the tertiary carbon of 1-methylcyclohexene), giving 1-methylcyclohexanol. Hydroboration–oxidation delivers OH to the less substituted carbon (anti-Markovnikov), giving the secondary alcohol at C2. The two methods are complementary precisely because they give constitutional isomers — choosing the right reagent determines which alcohol you make."

- question: "Why does halogenation of an alkene with Br2 give exclusively anti (trans) addition rather than a mixture of syn and anti products?"
  type: short-answer
  answer: "Br2 reacts with the pi bond to form a cyclic bromonium ion that bridges both carbons and blocks one face of the former double bond. The second bromide ion must attack from the opposite face (backside, SN2-like), forcing anti addition and giving the trans dibromo product."
  explanation: "If addition proceeded through an open secondary carbocation, bromide could attack from either face, producing a mixture of stereoisomers. The bromonium ion locks the geometry by making both carbons part of a three-membered ring — the bridging Br+ shields the top face, so attack is restricted to the bottom. This anti-addition stereochemistry is diagnostic for a halonium ion mechanism and is one of the key pieces of experimental evidence that bromonium ions exist."
```

## Explainer

From the alkene structure topic, you know that the pi bond is an electron-rich region perpendicular to the molecular plane — a nucleophilic cloud that sits above and below the double bond. Electrophilic addition begins when an electrophile (an electron-poor species) is drawn toward that cloud. The pi electrons attack the electrophile, breaking the pi bond and forming a new bond to one of the alkene carbons. This leaves the other carbon electron-deficient — a carbocation — which is then captured by a nucleophile. That two-step sequence, electrophile attack then nucleophile capture, defines all ionic addition reactions to alkenes.

Markovnikov's rule — proton adds to the carbon bearing more hydrogens — is not a memorization fact but a consequence of carbocation stability. When H+ adds to propene, two possible carbocations could form: a primary one at C1 or a secondary one at C2. The secondary carbocation is more stable because adjacent alkyl groups donate electron density toward the positive charge through hyperconjugation and inductive effects. The reaction proceeds through the lower-energy intermediate, which determines which carbon ends up bearing the halide in the product. Understanding *why* Markovnikov's rule holds lets you predict regiochemistry for any alkene without memorizing a rule: always ask which carbocation is more stable.

Halogenation with Br2 adds a stereochemical layer. The two bromine atoms do not add to the same face (syn); they add to opposite faces (anti). This happens because Br2 does not simply fall apart into Br+ and Br- and hand over a carbocation. Instead, the pi electrons push one bromine off the other, forming a cyclic bromonium ion — a three-membered ring in which Br+ bridges both carbons simultaneously. This ring shields one face of the double bond entirely. The bromide ion released in the first step can only attack from the opposite face (backside attack, like an SN2 reaction). The result is anti addition of the two halogens, producing the trans dibromide as the stereochemical product.

Hydroboration–oxidation is mechanistically the most different from the others. Borane (BH3) is an electrophile (empty p orbital on B), but addition is concerted: both the B-H bond adds across the alkene in a single four-centered transition state, with B going to the less substituted carbon and H going to the more substituted carbon. There is no carbocation intermediate at any point. The consequences are significant: the regiochemistry is anti-Markovnikov (OH ends up on the less substituted carbon after oxidation of the C-B bond), the stereochemistry is syn (B and H add to the same face), and no carbocation rearrangements can occur. If a substrate would give a rearranged product via the carbocation route, hydroboration gives the unrearranged, anti-Markovnikov alcohol cleanly.

Mastering electrophilic addition means tracking three things for each reagent: (1) *which* carbon receives which group (regiochemistry, governed by carbocation stability or boron's preference for less substituted carbons), (2) *which face* each group adds to (stereochemistry: syn or anti, governed by the mechanism's key intermediate), and (3) whether a carbocation intermediate exists (if yes, rearrangements are possible; if no, the product is determined by the concerted geometry). Laying out those three questions systematically for HX, X2, H2O/H+, and BH3/H2O2 covers the core of alkene reactivity.
