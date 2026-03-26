---
id: sn2-mechanism-kinetics-and-factors
title: SN2 Mechanism, Kinetics, and Factors Affecting Reactivity
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: walden-inversion-sn2
  type: hard
- id: haloalkane-structure-nomenclature
  type: hard
- id: walden-inversion-stereochemistry
  type: soft
builds-toward:
- competing-substitution-and-elimination
- williamson-ether-synthesis-sn2
tags:
- sn2
- bimolecular
- mechanism
- kinetics
- inversion
- primary
stage: formal-systems
status: validated
---
# SN2 Mechanism, Kinetics, and Factors Affecting Reactivity

## Core Idea
The SN2 reaction is a one-step bimolecular nucleophilic substitution occurring via a single transition state with inversion of stereochemistry. Second-order kinetics depend on both substrate and nucleophile concentrations. Factors favoring SN2 include primary carbon centers, polar aprotic solvents, strong nucleophiles, and good leaving groups.

## Questions

```yaml
- question: "Two substitution reactions are run in parallel. In Reaction A, doubling the nucleophile concentration doubles the rate. In Reaction B, doubling the nucleophile concentration has no effect on the rate. What is the most likely mechanistic explanation?"
  type: multiple-choice
  options:
    - "Reaction A is SN2 (rate = k[substrate][nucleophile]); Reaction B is SN1 (rate = k[substrate] only)"
    - "Reaction A is SN1 and Reaction B is SN2, because SN1 requires excess nucleophile"
    - "Both are SN2, but Reaction B uses a polar protic solvent that cancels the concentration effect"
    - "Reaction B has a better leaving group, which offsets the nucleophile concentration effect"
  answer: 0
  explanation: "The rate law is the definitive diagnostic. SN2: rate = k[substrate][nucleophile] — both species are present in the single bimolecular transition state, so doubling either doubles the rate. SN1: rate = k[substrate] — the rate-determining step is unimolecular ionization to a carbocation, which occurs before the nucleophile attacks. Doubling nucleophile concentration has zero effect on an SN1 rate. This kinetic test directly distinguishes the mechanisms without needing to know anything about the substrate's structure."

- question: "Why is a tertiary alkyl halide essentially unreactive in SN2 reactions, while a methyl halide reacts fastest?"
  type: multiple-choice
  options:
    - "Tertiary carbons are more electronegative, making the carbon less susceptible to nucleophilic attack"
    - "Three bulky substituents around the tertiary carbon block the back-side approach that SN2 requires, creating prohibitive steric hindrance"
    - "The tertiary C–X bond is inherently stronger than a primary C–X bond, requiring more activation energy"
    - "Tertiary substrates have a lower LUMO energy that disfavors nucleophilic approach"
  answer: 1
  explanation: "SN2 requires the nucleophile to attack from directly behind the leaving group (180°). At a methyl carbon, only three small hydrogen atoms flank the reactive center — virtually no steric barrier. At a tertiary carbon, three carbon-containing groups create a wall that physically prevents the nucleophile from reaching the carbon close enough for orbital overlap in the transition state. This is steric, not electronic. Option A is wrong: tertiary carbons are not more electronegative. The steric explanation also clarifies why even neopentyl (a formally primary carbon flanked by a bulky t-Bu group) is slow for SN2."

- question: "Switching from methanol (polar protic) to DMSO (polar aprotic) as solvent can increase SN2 reaction rates by factors of a million or more."
  type: true-false
  answer: true
  explanation: "Polar protic solvents form hydrogen bonds with nucleophilic anions (Br⁻, CN⁻, N₃⁻), surrounding them in a solvent cage that ties up their electron pairs and dramatically reduces nucleophilicity. Polar aprotic solvents cannot hydrogen-bond with anions (no O–H or N–H bonds), leaving the nucleophile's electrons fully available for back-side attack. The million-fold rate enhancement observed for some reactions makes solvent choice one of the most powerful variables in SN2 chemistry."

- question: "A stronger base is generally a better nucleophile in SN2 reactions, because both properties measure the ability to donate an electron pair."
  type: true-false
  answer: false
  explanation: "Nucleophilicity (a kinetic property — how fast an electron pair attacks carbon) and basicity (a thermodynamic property — how strongly an electron pair bonds to a proton) frequently diverge. In protic solvents, large polarizable atoms like I⁻ and RS⁻ are excellent nucleophiles because their diffuse electron clouds are less tightly solvated, even though they are weaker bases than F⁻ or RO⁻. Fluoride is a strong base but a poor SN2 nucleophile in protic media. The two properties track together in aprotic solvents more closely, but the universal equation of basicity with nucleophilicity fails."

- question: "Explain why methyl and primary substrates favor SN2 reactions while tertiary substrates do not, using the concept of back-side attack."
  type: short-answer
  answer: "SN2 proceeds through a single concerted transition state in which the nucleophile attacks the electrophilic carbon from directly behind the leaving group (180°). At a methyl carbon, only three small hydrogen atoms surround the reactive carbon, leaving the back lobe of the C–LG antibonding orbital fully accessible. At a primary carbon, one alkyl group partially obstructs the back side but the reaction remains viable. At a secondary carbon, two alkyl groups create significant steric compression. At a tertiary carbon, three bulky groups make the required transition-state geometry prohibitively high in energy — the nucleophile cannot approach close enough for productive orbital overlap."
  explanation: "This structural sensitivity is one of the key diagnostic criteria for the SN2 mechanism. If a substrate is tertiary and substitution still occurs, it must proceed by SN1 (through a carbocation intermediate, which is stabilized by three alkyl groups). The steric argument also explains why SN2 and SN1 are complementary: the same substitution pattern (primary vs. tertiary) that disfavors SN2 favors SN1 and vice versa."
```

## Explainer

You already know from the basic SN2 reaction and Walden inversion that the nucleophile attacks the electrophilic carbon from the back side, pushing out the leaving group in a single concerted step with complete inversion of stereochemistry. This topic zooms in on why the reaction behaves this way kinetically and what structural factors make it faster or slower.

The **rate law** is the defining fingerprint: rate = k[substrate][nucleophile]. Both species appear in the rate expression because both are present in the single transition state — that is what "bimolecular" means. Double the nucleophile concentration and the rate doubles. Double the substrate concentration and the rate doubles again. This second-order kinetics distinguishes SN2 from SN1, where only the substrate appears in the rate law. The practical consequence is immediate: if you want a faster SN2 reaction, increasing nucleophile concentration works, whereas it would have no effect on an SN1 reaction.

**Substrate structure** is the most powerful factor. The nucleophile must physically reach the electrophilic carbon, so anything that blocks the back side slows the reaction dramatically. Methyl substrates (CH₃-LG) are fastest because there are only hydrogen atoms flanking the carbon — essentially no steric obstruction. Primary substrates are nearly as good. Secondary substrates are much slower because two carbon-containing groups partially block approach. Tertiary substrates are essentially unreactive by SN2 — three bulky groups create a wall the nucleophile cannot penetrate. Think of it like trying to thread a needle: methyl is an open doorway, primary is a normal door, secondary is a narrow gap, and tertiary is a locked wall.

The remaining three factors fine-tune reactivity. A **strong nucleophile** (one with high nucleophilicity — recall that this is a kinetic property distinct from basicity) accelerates the reaction because it appears in the rate law. A **good leaving group** stabilizes the developing negative charge in the transition state; the better it departs, the lower the activation energy. And **solvent choice** matters enormously: polar aprotic solvents like DMSO and acetone do not solvate anions through hydrogen bonding, leaving the nucleophile's electron pair fully available for back-side attack. Switching from a protic solvent like methanol to an aprotic solvent like DMSO can increase SN2 rates by factors of a million. These four factors — substrate, nucleophile, leaving group, and solvent — form a checklist for predicting when an SN2 pathway will dominate over competing mechanisms.
