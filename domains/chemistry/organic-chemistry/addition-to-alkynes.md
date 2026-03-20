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
stage: advanced
status: draft
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

## Explainer

If you understand electrophilic addition to alkenes, you already know the basic playbook: an electron-rich pi bond attacks an electrophile, forming a new sigma bond and a carbocation intermediate, which is then captured by a nucleophile. Alkynes follow the same logic but with a twist — they have **two pi bonds** available for reaction instead of one. This means every addition reaction you learned for alkenes can happen twice on an alkyne, and the real skill is controlling whether you stop at one addition or go all the way to two.

Consider **hydrohalogenation** with HBr. One equivalent of HBr adds across the triple bond following Markovnikov's rule, giving a **vinyl halide** — an alkene with a halogen attached. If you add a second equivalent, it adds across the remaining double bond, again following Markovnikov's rule, placing both halogens on the same carbon (a geminal dihalide). The first addition is actually slower than you might expect, because the intermediate **vinyl cation** is less stable than a typical secondary or tertiary carbocation — the positive charge sits on an sp-hybridized carbon, which holds its electrons more tightly. This counterintuitive slowness means that under carefully controlled conditions, you can often stop at the monoaddition product.

**Hydration** of alkynes reveals a beautifully useful consequence of addition chemistry. Markovnikov addition of water to a terminal alkyne (using HgSO₄ as catalyst in dilute H₂SO₄) places the OH group on the internal carbon, producing an **enol** — a vinyl alcohol. But enols are unstable and spontaneously undergo **tautomerization** to the more stable keto form, giving you a methyl ketone. Anti-Markovnikov hydration via hydroboration-oxidation places the OH on the terminal carbon, and its tautomerization gives an **aldehyde** instead. So the regiochemistry of water addition determines whether you get a ketone or an aldehyde — a powerful synthetic tool.

The most elegant control comes from **partial hydrogenation**. A standard catalyst like Pd or Pt will reduce an alkyne all the way to an alkane, adding two equivalents of H₂. But the **Lindlar catalyst** — palladium deposited on calcium carbonate and deactivated with lead acetate and quinoline — is just active enough to reduce the triple bond to a double bond and then stops. Because both hydrogens add to the same face of the triple bond (syn addition on the catalyst surface), the product is exclusively the **cis-alkene**. If you want the **trans-alkene** instead, you use dissolving-metal reduction (Na in liquid NH₃), which proceeds through a radical anion mechanism that delivers hydrogens from opposite faces. Having both stereochemical options available from the same alkyne starting material makes alkynes extraordinarily versatile in synthesis.
