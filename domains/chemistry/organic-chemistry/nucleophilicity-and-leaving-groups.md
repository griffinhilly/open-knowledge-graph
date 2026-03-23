---
id: nucleophilicity-and-leaving-groups
title: Nucleophilicity, Basicity, and Leaving Group Ability
domain: chemistry
course: organic-chemistry
prerequisites:
- id: heteroatom-nucleophiles
  type: hard
- id: acid-base-definitions
  type: hard
builds-toward:
- sn1-sn2-reaction-selectivity-factors
- zaitsevs-rule-hofmann-elimination
tags:
- nucleophilicity
- basicity
- leaving-group
- solvent-effects
stage: formal-systems
status: draft
---

# Nucleophilicity, Basicity, and Leaving Group Ability

## Core Idea
Nucleophilicity measures the rate at which a species attacks an electrophilic center; basicity measures the extent of proton acceptance. These are not the same—basicity is a thermodynamic property (Kb, pKa), while nucleophilicity is kinetic. Factors affecting nucleophilicity include charge, atom size, orbital overlap, and solvent. Good leaving groups are weak bases that stabilize negative charge (Cl⁻, Br⁻, TsO⁻); poor leaving groups are strong bases (OH⁻, H⁻, NH₂⁻).

## How It's Best Learned
Rank nucleophiles by both basicity and nucleophilicity in different solvents. Predict leaving group ability from pKa of conjugate acid. Compare reactivity of charged vs neutral nucleophiles.

## Common Misconceptions
Strong bases are always good nucleophiles—false, e.g., t-BuO⁻ is a strong base but weak nucleophile due to steric hindrance. Nucleophilicity and basicity always correlate—they diverge significantly in aprotic solvents. Charge always increases nucleophilicity—only if the charge is directly involved in bonding.

## Questions

```yaml
- question: "In a protic solvent like water, you need to perform an SN2 reaction. You have two candidate nucleophiles: fluoride (F⁻) and iodide (I⁻). Which is the better nucleophile, and why?"
  type: multiple-choice
  options:
    - "Fluoride, because it is the stronger base and basicity always determines nucleophilicity"
    - "Iodide, because it is larger and less tightly solvated, leaving its electrons more available for attack"
    - "Fluoride, because higher charge density means stronger electron donation to carbon"
    - "They are equally reactive; both carry a −1 charge, which is the only relevant factor"
  answer: 1
  explanation: "In protic solvents, small anions like F⁻ are tightly surrounded by hydrogen bonds that bury their electron density — nucleophilicity drops even though basicity is high. Larger I⁻ is only weakly solvated, so its diffuse electron cloud remains available for attack at carbon. This is the classic divergence between basicity (thermodynamic) and nucleophilicity (kinetic): F⁻ is the stronger base but I⁻ is the stronger nucleophile in water. The trend in protic solvents is I⁻ > Br⁻ > Cl⁻ > F⁻ — the reverse of basicity order."

- question: "An alcohol (R-OH) reacts very slowly in SN2 reactions until a strong acid is added to protonate it first. The rate acceleration occurs because:"
  type: multiple-choice
  options:
    - "Protonation increases the nucleophilicity of the attacking nucleophile by raising the solution pH"
    - "Protonation converts OH⁻ (a strong base, poor leaving group) into H₂O (a weak base, excellent leaving group)"
    - "Protonation increases the electrophilicity of the carbon center by withdrawing electron density inductively"
    - "Protonation changes the hybridization of the α-carbon from sp³ to sp²"
  answer: 1
  explanation: "Leaving group ability mirrors conjugate acid weakness: the lower the pKa of the leaving group's conjugate acid, the better the leaving group. H₂O (pKa of H₃O⁺ ≈ −1.7) is a far weaker base than OH⁻ (pKa of H₂O ≈ 15.7), so water departs readily while hydroxide clings to carbon. Protonating the alcohol converts the poor leaving group (OH⁻) into an excellent one (H₂O). This is the key role of acid catalysis in substitution and elimination reactions — it activates the leaving group, not the nucleophile."

- question: "In polar aprotic solvents (e.g., DMSO or DMF), fluoride is a better nucleophile than iodide."
  type: true-false
  answer: true
  explanation: "In polar aprotic solvents there are no hydrogen-bond donors to solvate anions, so the hydrogen-bond cage that buries F⁻'s electron density in water is absent. Without solvation, nucleophilicity tracks basicity more closely, and fluoride — the smallest, most electronegative halide with highest charge density — is the strongest nucleophile among the halides. The nucleophilicity order in aprotic solvents (F⁻ > Cl⁻ > Br⁻ > I⁻) is essentially the reverse of the protic-solvent order, illustrating how powerfully solvent can invert reactivity trends."

- question: "Potassium tert-butoxide (t-BuO⁻ K⁺) is both a strong base and a strong nucleophile because it carries a full negative charge on oxygen."
  type: true-false
  answer: false
  explanation: "t-BuO⁻ is indeed a strong base — protons are tiny and easily approached by the oxygen lone pairs. However, it is a poor nucleophile toward carbon electrophiles because the three methyl groups surrounding the oxygen create severe steric hindrance. Carbon electrophilic centers in alkyl halides are far more sterically demanding than a bare proton. This is the steric argument for basicity-nucleophilicity divergence: bulky bases can grab protons but cannot reach into crowded carbon centers. In reactions with secondary or tertiary alkyl halides, t-BuO⁻ favors E2 elimination over SN2 substitution precisely because it is a better base than nucleophile."

- question: "Explain why basicity and nucleophilicity are related but distinct properties. Identify one factor that causes them to diverge and explain the mechanism of that divergence."
  type: short-answer
  answer: "Basicity is a thermodynamic property measuring the equilibrium extent to which a species accepts a proton (quantified by pKa of the conjugate acid). Nucleophilicity is a kinetic property measuring the rate at which a species attacks an electrophilic carbon center. Both involve electron donation, but the reaction partner, geometry, and conditions differ. A key divergence factor is solvent: in protic solvents, small, highly basic anions like F⁻ are tightly hydrogen-bonded, burying their electron density and slowing carbon attack. Large, polarizable anions like I⁻ are weakly solvated, so their electrons remain kinetically available — making them excellent nucleophiles despite being weak bases."
  explanation: "Steric bulk is another divergence factor: t-BuO⁻ is a strong base but poor nucleophile because bulky methyl groups block approach to sp³ carbon. Polarizability also matters: large atoms have diffuse electron clouds that begin overlapping with an electrophilic center at longer range, increasing nucleophilicity beyond what basicity predicts. The fundamental distinction is that basicity describes equilibrium with a tiny proton, while nucleophilicity describes a bimolecular rate constant toward a much larger, more sterically demanding carbon center."
```

## Explainer

You already know from acid-base chemistry that some species donate electrons to protons — that is basicity. **Nucleophilicity** asks a different question: how fast does a species donate electrons to a carbon (or other electrophilic atom)? Both involve electron donation, but basicity is about equilibrium (how much product forms at the end) while nucleophilicity is about rate (how quickly the attack happens). This kinetic-versus-thermodynamic distinction is the single most important idea in this topic, because it means the best base is not always the best nucleophile.

Several factors control nucleophilicity independently of basicity. **Polarizability** is the big one: larger atoms like sulfur and iodide have diffuse electron clouds that can begin overlapping with the electrophilic carbon at longer distances, making them excellent nucleophiles even though they are weak bases. Compare iodide (great nucleophile, terrible base) with fluoride (decent base, sluggish nucleophile in protic solvents). **Steric bulk** also splits the two properties apart. Potassium tert-butoxide is a strong base because protons are tiny and accessible, but it is a poor nucleophile because carbon electrophilic centers are buried behind other atoms — the bulky tert-butyl group simply cannot reach them.

Solvent plays a decisive role. In **protic solvents** (water, alcohols), small anions like fluoride get tightly solvated by hydrogen bonds, which stabilizes them but buries their electron density — nucleophilicity drops even though basicity stays high. Larger anions like iodide are poorly solvated, leaving their electrons available for attack. This is why nucleophilicity in protic solvents follows the trend I⁻ > Br⁻ > Cl⁻ > F⁻, the reverse of basicity. Switch to a **polar aprotic solvent** (DMSO, acetone, DMF) and the hydrogen-bond cage disappears. Now nucleophilicity tracks basicity more closely: F⁻ > Cl⁻ > Br⁻ > I⁻.

On the other side of the reaction, **leaving group ability** is essentially basicity in reverse. A good leaving group is a species that is stable after departure — meaning it is a weak base that does not want to re-donate its electrons. The conjugate bases of strong acids make the best leaving groups: tosylate (TsO⁻), iodide, bromide, and chloride all have low pKa conjugate acids and depart readily. Poor leaving groups — hydroxide, alkoxide, amide — are strong bases that cling to the carbon. This is why alcohols do not undergo substitution directly; the OH⁻ leaving group is too basic. Protonating the alcohol first converts it to water, an excellent leaving group. Recognizing that leaving group ability mirrors conjugate acid strength gives you a single organizing principle: look up the pKa of the leaving group's conjugate acid, and the lower it is, the better the leaving group.
