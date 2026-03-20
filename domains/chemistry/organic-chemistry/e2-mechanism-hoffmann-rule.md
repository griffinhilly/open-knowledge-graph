---
id: e2-mechanism-hoffmann-rule
title: E2 Elimination Mechanism and Hoffmann's Rule
domain: chemistry
course: organic-chemistry
prerequisites:
- id: e2-elimination
  type: hard
- id: alkene-structure-and-nomenclature
  type: hard
- id: haloalkane-structure-nomenclature
  type: hard
builds-toward:
- competing-substitution-and-elimination
tags:
- e2
- elimination
- bimolecular
- hoffmann
- anti-periplanar
stage: advanced
status: draft
---

# E2 Elimination Mechanism and Hoffmann's Rule

## Core Idea
E2 is a bimolecular elimination occurring in a single step via an anti-periplanar transition state. Hoffmann's rule states that when Zaitsev's rule is expected to give a minor product (due to steric hindrance), the less substituted alkene becomes the major product. E2 is favored by primary and secondary substrates, strong bases, and low temperatures.

## Explainer

You already know that E2 elimination removes a proton and a leaving group in a single concerted step, requiring them to be **anti-periplanar** — positioned 180° apart when viewed along the C–C bond axis. This geometric requirement is the key to understanding why the E2 mechanism sometimes defies the usual Zaitsev selectivity and instead follows **Hoffmann's rule**, producing the less substituted alkene as the major product.

Under normal E2 conditions with a moderately sized base like ethoxide (EtO⁻), Zaitsev's rule predicts the more substituted alkene — the thermodynamically more stable product. But when the base is **sterically bulky** — think potassium tert-butoxide ((CH₃)₃CO⁻ K⁺) — the base cannot easily reach the more hindered internal hydrogen. It is physically blocked by the surrounding methyl groups. Instead, it abstracts the more accessible hydrogen on the less substituted side, producing the **Hoffmann product** (the less substituted alkene). The reaction is still E2 in mechanism — concerted, bimolecular, anti-periplanar — but the steric environment of the base shifts the regiochemistry.

Consider 2-bromobutane as a concrete example. With NaOEt (a small base), the major product is 2-butene (Zaitsev: more substituted). With KOtBu (a bulky base), the major product is 1-butene (Hoffmann: less substituted). The substrate is identical in both cases; only the base changes. This demonstrates that regioselectivity in E2 is not purely a property of the substrate but depends on the steric interplay between base and substrate.

Hoffmann selectivity is also observed when the substrate itself is heavily branched. Quaternary ammonium salts undergoing Hofmann elimination (a different but related context) preferentially lose the least hindered proton for the same steric reasons. The practical takeaway is a decision rule: use a small, strong base (NaOEt, NaOH) when you want the Zaitsev (more substituted) alkene, and use a bulky, strong base (KOtBu) when you want the Hoffmann (less substituted) alkene. The anti-periplanar requirement remains non-negotiable in either case — always check that the desired β-hydrogen can achieve the correct geometry before predicting the product.
