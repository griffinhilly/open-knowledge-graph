---
id: addition-to-alkynes
title: Addition Reactions of Alkynes
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alkyne-structure-and-nomenclature
  type: hard
- id: electrophilic-addition-to-alkenes
  type: hard
- id: iupac-nomenclature-alkynes
  type: soft
builds-toward: []
tags:
- alkyne
- hydrohalogenation
- hydration
- Markovnikov
- anti-Markovnikov
- hydrogenation
- halogenation
- Lindlar catalyst
stage: formal-systems
status: validated
---
# Addition Reactions of Alkynes

## Core Idea
Alkynes undergo the same classes of addition reactions as alkenes — hydrohalogenation, hydration, halogenation, and hydrogenation — but with the added complexity of two pi bonds available for reaction. One equivalent of reagent converts an alkyne to a substituted alkene; two equivalents give the fully saturated product. Markovnikov hydration of alkynes (acid-catalyzed with HgSO4) produces enols that tautomerize to ketones, while anti-Markovnikov hydroboration-oxidation gives aldehydes from terminal alkynes. Selective partial hydrogenation using Lindlar catalyst (Pd/CaCO3, poisoned) yields cis-alkenes, whereas dissolving-metal reduction (Na/NH3) yields trans-alkenes.

## How It's Best Learned
Compare each alkyne reaction with its alkene analogue side by side to see what stays the same and what changes. For hydration, always draw the enol intermediate and show the tautomerization step explicitly. Practice stopping at one equivalent of reagent to predict the vinyl halide or vinyl borane intermediate before proceeding to the second addition.

## Common Misconceptions
- Markovnikov addition of water to an internal alkyne gives a ketone, not an aldehyde — the distinction between terminal and internal alkynes is critical for predicting the carbonyl product.
- Lindlar hydrogenation gives cis (syn addition), while Na/NH3 gives trans (anti addition); these are not interchangeable.
- Alkynes are slightly less reactive than alkenes toward electrophilic addition because the vinyl cation intermediate is less stable than a typical carbocation, despite alkynes being more electron-rich.

## Questions

```yaml
- question: "Acid-catalyzed hydration of 1-pentyne (using HgSO4/H2SO4) produces which carbonyl compound?"
  type: multiple-choice
  options:
    - "Pentan-1-al — water adds to the terminal carbon following Markovnikov's rule"
    - "Pentan-2-one — water adds to the internal carbon, forming an enol that tautomerizes to a ketone"
    - "Pentan-1-ol — the triple bond is fully reduced to a primary alcohol"
    - "Pentan-2-ol — Markovnikov addition gives a secondary alcohol directly"
  answer: 1
  explanation: "Markovnikov's rule places the OH on the more substituted (internal) carbon, giving a vinyl alcohol (enol) at C2. Enols are unstable and spontaneously tautomerize to the more stable keto form — a methyl ketone (pentan-2-one). Option A (aldehyde) is the most tempting wrong answer: it would require anti-Markovnikov addition (OH on C1), which requires hydroboration-oxidation, not acid catalysis."

- question: "A chemist adds exactly one equivalent of HBr to 2-butyne under Markovnikov conditions. What is the primary product?"
  type: multiple-choice
  options:
    - "2,2-dibromobutane — both bromines add to the same carbon"
    - "2-bromobutane — HBr adds across the triple bond giving an alkane product"
    - "2-bromo-2-butene — HBr adds once across the triple bond giving a vinyl halide"
    - "meso-2,3-dibromobutane — anti addition of two bromines occurs"
  answer: 2
  explanation: "One equivalent of HBr adds once across one of the two pi bonds, converting the alkyne to a vinyl halide (an alkene bearing a halogen). The triple bond has two pi bonds available; controlled addition of one equivalent stops at the alkene stage. Option A (geminal dihalide) would require two equivalents of HBr. Option D would require Br2, not HBr."

- question: "Lindlar catalyst and sodium in liquid ammonia (Na/NH3) both partially hydrogenate alkynes to alkenes and produce the same stereochemical outcome."
  type: true-false
  answer: false
  explanation: "These reagents produce opposite stereochemistry. Lindlar catalyst (poisoned Pd) delivers both hydrogen atoms to the same face of the triple bond (syn addition), giving the cis-alkene. Na/NH3 (dissolving-metal reduction) proceeds through a radical anion mechanism that delivers hydrogens from opposite faces (anti addition), giving the trans-alkene. Having both options available from the same alkyne is a powerful synthetic tool."

- question: "Alkynes are less reactive than alkenes toward electrophilic addition reactions, despite containing more pi electrons."
  type: true-false
  answer: true
  explanation: "This is counterintuitive but correct. The intermediate in electrophilic addition to an alkyne is a vinyl cation — a carbocation on an sp-hybridized carbon. sp carbons hold their electrons more tightly than sp2 carbons, making vinyl cations less stable than typical secondary or tertiary carbocations formed during alkene additions. The less stable intermediate raises the activation energy, slowing the reaction despite alkynes being formally more electron-rich."

- question: "Why does Markovnikov hydration of a terminal alkyne give a ketone, while anti-Markovnikov hydration (hydroboration-oxidation) of the same terminal alkyne gives an aldehyde?"
  type: short-answer
  answer: "Markovnikov addition places OH on the internal carbon (C2), producing an enol with the double bond between C1 and C2. This enol tautomerizes to a methyl ketone (carbonyl at C2). Anti-Markovnikov addition places OH on the terminal carbon (C1), producing an enol with the double bond between C1 and C2 but OH at C1. Tautomerization gives an aldehyde (carbonyl at C1). The regiochemistry of the initial water addition — which carbon gets the OH — determines the position of the carbonyl after tautomerization."
  explanation: "Both pathways proceed through an enol intermediate that tautomerizes to a carbonyl compound. The difference is purely regiochemical: the position of OH in the enol becomes the position of the C=O in the product. Markovnikov rules and hydroboration-oxidation are thus complementary tools that give the chemist complete control over whether the terminal alkyne becomes a methyl ketone or an aldehyde."
```

## Explainer

If you understand electrophilic addition to alkenes, you already know the basic playbook: an electron-rich pi bond attacks an electrophile, forming a new sigma bond and a carbocation intermediate, which is then captured by a nucleophile. Alkynes follow the same logic but with a twist — they have **two pi bonds** available for reaction instead of one. This means every addition reaction you learned for alkenes can happen twice on an alkyne, and the real skill is controlling whether you stop at one addition or go all the way to two.

Consider **hydrohalogenation** with HBr. One equivalent of HBr adds across the triple bond following Markovnikov's rule, giving a **vinyl halide** — an alkene with a halogen attached. If you add a second equivalent, it adds across the remaining double bond, again following Markovnikov's rule, placing both halogens on the same carbon (a geminal dihalide). The first addition is actually slower than you might expect, because the intermediate **vinyl cation** is less stable than a typical secondary or tertiary carbocation — the positive charge sits on an sp-hybridized carbon, which holds its electrons more tightly. This counterintuitive slowness means that under carefully controlled conditions, you can often stop at the monoaddition product.

**Hydration** of alkynes reveals a beautifully useful consequence of addition chemistry. Markovnikov addition of water to a terminal alkyne (using HgSO₄ as catalyst in dilute H₂SO₄) places the OH group on the internal carbon, producing an **enol** — a vinyl alcohol. But enols are unstable and spontaneously undergo **tautomerization** to the more stable keto form, giving you a methyl ketone. Anti-Markovnikov hydration via hydroboration-oxidation places the OH on the terminal carbon, and its tautomerization gives an **aldehyde** instead. So the regiochemistry of water addition determines whether you get a ketone or an aldehyde — a powerful synthetic tool.

The most elegant control comes from **partial hydrogenation**. A standard catalyst like Pd or Pt will reduce an alkyne all the way to an alkane, adding two equivalents of H₂. But the **Lindlar catalyst** — palladium deposited on calcium carbonate and deactivated with lead acetate and quinoline — is just active enough to reduce the triple bond to a double bond and then stops. Because both hydrogens add to the same face of the triple bond (syn addition on the catalyst surface), the product is exclusively the **cis-alkene**. If you want the **trans-alkene** instead, you use dissolving-metal reduction (Na in liquid NH₃), which proceeds through a radical anion mechanism that delivers hydrogens from opposite faces. Having both stereochemical options available from the same alkyne starting material makes alkynes extraordinarily versatile in synthesis.
