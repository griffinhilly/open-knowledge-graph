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
stage: advanced
status: draft
---

# Nucleophilicity, Basicity, and Leaving Group Ability

## Core Idea
Nucleophilicity measures the rate at which a species attacks an electrophilic center; basicity measures the extent of proton acceptance. These are not the same—basicity is a thermodynamic property (Kb, pKa), while nucleophilicity is kinetic. Factors affecting nucleophilicity include charge, atom size, orbital overlap, and solvent. Good leaving groups are weak bases that stabilize negative charge (Cl⁻, Br⁻, TsO⁻); poor leaving groups are strong bases (OH⁻, H⁻, NH₂⁻).

## How It's Best Learned
Rank nucleophiles by both basicity and nucleophilicity in different solvents. Predict leaving group ability from pKa of conjugate acid. Compare reactivity of charged vs neutral nucleophiles.

## Common Misconceptions
Strong bases are always good nucleophiles—false, e.g., t-BuO⁻ is a strong base but weak nucleophile due to steric hindrance. Nucleophilicity and basicity always correlate—they diverge significantly in aprotic solvents. Charge always increases nucleophilicity—only if the charge is directly involved in bonding.

## Explainer

You already know from acid-base chemistry that some species donate electrons to protons — that is basicity. **Nucleophilicity** asks a different question: how fast does a species donate electrons to a carbon (or other electrophilic atom)? Both involve electron donation, but basicity is about equilibrium (how much product forms at the end) while nucleophilicity is about rate (how quickly the attack happens). This kinetic-versus-thermodynamic distinction is the single most important idea in this topic, because it means the best base is not always the best nucleophile.

Several factors control nucleophilicity independently of basicity. **Polarizability** is the big one: larger atoms like sulfur and iodide have diffuse electron clouds that can begin overlapping with the electrophilic carbon at longer distances, making them excellent nucleophiles even though they are weak bases. Compare iodide (great nucleophile, terrible base) with fluoride (decent base, sluggish nucleophile in protic solvents). **Steric bulk** also splits the two properties apart. Potassium tert-butoxide is a strong base because protons are tiny and accessible, but it is a poor nucleophile because carbon electrophilic centers are buried behind other atoms — the bulky tert-butyl group simply cannot reach them.

Solvent plays a decisive role. In **protic solvents** (water, alcohols), small anions like fluoride get tightly solvated by hydrogen bonds, which stabilizes them but buries their electron density — nucleophilicity drops even though basicity stays high. Larger anions like iodide are poorly solvated, leaving their electrons available for attack. This is why nucleophilicity in protic solvents follows the trend I⁻ > Br⁻ > Cl⁻ > F⁻, the reverse of basicity. Switch to a **polar aprotic solvent** (DMSO, acetone, DMF) and the hydrogen-bond cage disappears. Now nucleophilicity tracks basicity more closely: F⁻ > Cl⁻ > Br⁻ > I⁻.

On the other side of the reaction, **leaving group ability** is essentially basicity in reverse. A good leaving group is a species that is stable after departure — meaning it is a weak base that does not want to re-donate its electrons. The conjugate bases of strong acids make the best leaving groups: tosylate (TsO⁻), iodide, bromide, and chloride all have low pKa conjugate acids and depart readily. Poor leaving groups — hydroxide, alkoxide, amide — are strong bases that cling to the carbon. This is why alcohols do not undergo substitution directly; the OH⁻ leaving group is too basic. Protonating the alcohol first converts it to water, an excellent leaving group. Recognizing that leaving group ability mirrors conjugate acid strength gives you a single organizing principle: look up the pKa of the leaving group's conjugate acid, and the lower it is, the better the leaving group.
