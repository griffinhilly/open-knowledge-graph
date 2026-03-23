---
id: hydroboration-oxidation-alkenes
title: 'Hydroboration-Oxidation: Anti-Markovnikov Hydration'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: markovnikov-rule-regioselectivity
  type: hard
builds-toward:
- alcohol-oxidation-to-carbonyls
tags:
- addition
- hydroboration
- alcohol-synthesis
- non-markovnikov
stage: formal-systems
status: validated
---

# Hydroboration-Oxidation: Anti-Markovnikov Hydration

## Core Idea
Hydroboration-oxidation converts alkenes to primary alcohols (or secondary from internal alkenes) with anti-Markovnikov regiochemistry and syn stereochemistry. Borane (BH₃) adds to the alkene such that hydride goes to the more substituted carbon and boron to the less substituted carbon; oxidation with H₂O₂/OH⁻ replaces B with OH while inverting the stereochemistry of that position.

## How It's Best Learned
Draw the borane addition, hydride migration, and oxidation steps. Compare the overall regiochemistry and stereochemistry to standard HX addition and understand why hydroboration is synthetically valuable for anti-Markovnikov products.

## Common Misconceptions
- Confusing which carbon receives B vs. H; boron attaches to the less substituted carbon (opposite of H in Markovnikov additions).
- Forgetting the inverting nature of the oxidation step after the initial syn addition of borane.

## Questions

```yaml
- question: "A student treats 1-methylcyclohexene with BH₃·THF, then H₂O₂/NaOH. Which product is formed?"
  type: multiple-choice
  options:
    - "1-methylcyclohexan-1-ol — Markovnikov addition places OH on the more substituted carbon"
    - "cis-2-methylcyclohexan-1-ol — anti-Markovnikov regiochemistry with syn addition"
    - "trans-2-methylcyclohexan-1-ol — anti-Markovnikov regiochemistry with anti addition"
    - "A racemic mixture of 1-methylcyclohexan-1-ol via a planar carbocation intermediate"
  answer: 1
  explanation: "Hydroboration places boron on the less substituted carbon (C2, next to the methyl-bearing C1) via a concerted syn addition — both B and H add to the same face. Oxidation then replaces B with OH with retention of configuration at that carbon. The net result is anti-Markovnikov regiochemistry (OH on C2, not C1) and syn stereochemistry — hence cis-2-methylcyclohexan-1-ol. Option A is the acid-catalyzed hydration product. Option C would require anti addition, which does not occur here. Option D describes the carbocation pathway that hydroboration specifically avoids."

- question: "Why does boron end up on the less substituted carbon during hydroboration?"
  type: multiple-choice
  options:
    - "The less substituted carbon has more hydrogens available to stabilize the developing negative charge on boron"
    - "Steric factors direct the bulkier boron to the less hindered carbon, and the transition state places partial positive charge on the more substituted carbon, which better stabilizes it"
    - "Boron is nucleophilic and attacks the terminal carbon of the double bond in all cases"
    - "Markovnikov's rule applies to boron just as it does to hydrogen — the less electronegative atom goes to the less substituted carbon"
  answer: 1
  explanation: "Two factors conspire to place boron on the less substituted carbon. First, steric: boron is a large atom that preferentially occupies the less hindered position. Second, electronic: in the four-centered transition state, there is partial positive charge on the carbon receiving the hydride — the more substituted carbon better stabilizes this partial positive charge through hyperconjugation and inductive effects. Note that option D states 'Markovnikov's rule applies to boron' — this is precisely backwards; hydroboration is the anti-Markovnikov reaction."

- question: "The oxidation step (H₂O₂/NaOH) in hydroboration-oxidation inverts the configuration at the carbon that bore the boron substituent."
  type: true-false
  answer: false
  explanation: "This is a common misconception. The 1,2-alkyl migration from boron to oxygen in the oxidation mechanism proceeds with retention of configuration at the migrating carbon. Since boron was placed by syn addition in the hydroboration step, and oxidation retains that configuration, OH ends up on the same face where boron was — no inversion occurs. The overall reaction delivers syn stereochemistry because both new bonds (C–B then C–OH) form on the same face."

- question: "Hydroboration-oxidation and acid-catalyzed hydration of an unsymmetrical alkene give the same regiochemical product but differ in stereochemical outcome."
  type: true-false
  answer: false
  explanation: "The two reactions give opposite regiochemistry, not just different stereochemistry. Acid-catalyzed hydration follows Markovnikov's rule — OH ends up on the more substituted carbon via a carbocation intermediate. Hydroboration-oxidation places OH on the less substituted carbon (anti-Markovnikov). For an unsymmetrical alkene like propene, acid hydration gives 2-propanol while hydroboration-oxidation gives 1-propanol. This complementary regiochemistry is precisely why both reactions are taught together."

- question: "Explain why hydroboration-oxidation is described as giving 'syn' addition overall, even though it involves two chemically distinct reaction steps."
  type: short-answer
  answer: "In the hydroboration step, borane adds in a concerted, four-centered transition state where both the B–C and H–C bonds form simultaneously on the same face of the double bond. This locks in syn stereochemistry — boron and hydrogen are delivered to the same face. In the oxidation step, the carbon that migrates to oxygen does so with retention of configuration. So the oxygen inherits the same facial position that boron occupied. Because boron was on the same face as the hydrogen (from the syn addition), and oxygen replaces boron with retention, the final product has OH and H on the same face — syn addition overall."
  explanation: "The key insight is that syn selectivity is established in the first step (the concerted borane addition) and preserved by the retention mechanism of the second step (oxidation). There is no inversion anywhere in the pathway. This contrasts with reactions that go through carbocations (no stereocontrol) or those where addition occurs from opposite faces (anti addition)."
```

## Explainer

You know from electrophilic addition that when HX adds to an unsymmetrical alkene, Markovnikov's rule places the hydrogen on the carbon with more hydrogens and the halide on the more substituted carbon. **Hydroboration-oxidation** is the essential complement to this reaction: it achieves the *opposite* regiochemistry, placing the hydroxyl group on the less substituted carbon to give an **anti-Markovnikov alcohol**. This makes it one of the most synthetically valuable reactions in the alkene toolkit — it gives you the product that acid-catalyzed hydration cannot.

The reaction proceeds in two distinct stages. In the **hydroboration step**, borane (BH₃, typically used as the THF complex) adds across the double bond in a single concerted step — no carbocation intermediate is formed. Boron is electrophilic (it has an empty p orbital) and the alkene's pi electrons attack it, while simultaneously a hydrogen transfers from boron to the adjacent carbon. Because both the B–C and H–C bonds form on the same face of the double bond in this four-centered transition state, the addition is **syn** (both groups add to the same side). Crucially, boron ends up on the **less substituted carbon** and hydrogen on the more substituted carbon. This regiochemistry arises because boron, the larger atom, preferentially goes to the less sterically hindered position, and because the transition state has partial negative charge on the carbon receiving boron — the more substituted carbon better stabilizes the partial positive charge on the other carbon.

Since BH₃ has three B–H bonds, it can add across three equivalents of alkene, producing a **trialkylborane** (R₃B). The second stage is **oxidation**: treating the trialkylborane with hydrogen peroxide (H₂O₂) in aqueous base (NaOH). This replaces each B–C bond with a HO–C bond. The mechanism involves nucleophilic attack of the hydroperoxide anion (HOO⁻) on boron, followed by a 1,2-alkyl migration from boron to oxygen — critically, this migration occurs with **retention of configuration** at the carbon that migrates. Since the boron was originally placed by syn addition, and the oxidation retains the configuration at that carbon, the net result is that OH replaces B in exactly the same position and on the same face.

The overall outcome — anti-Markovnikov regiochemistry and syn stereochemistry — is unique to hydroboration-oxidation. Contrast this with acid-catalyzed hydration (Markovnikov, no stereochemical control because of the planar carbocation) and oxymercuration (Markovnikov, anti addition). By choosing among these three methods, you can place a hydroxyl group on either carbon of an unsymmetrical alkene with predictable stereochemistry. This is the kind of reagent-controlled selectivity that makes retrosynthetic planning possible.
