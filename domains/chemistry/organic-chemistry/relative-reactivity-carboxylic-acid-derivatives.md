---
id: relative-reactivity-carboxylic-acid-derivatives
title: Relative Reactivity of Carboxylic Acid Derivatives
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carboxylic-acid-derivatives-esters-amides-acyl-chlorides
  type: hard
- id: nucleophilic-acyl-substitution
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- reactivity-trends
- acid-derivatives
- acyl-chloride
- ester
- amide
stage: advanced
status: draft
---

# Relative Reactivity of Carboxylic Acid Derivatives

## Core Idea
Carboxylic acid derivatives follow a reactivity hierarchy in nucleophilic acyl substitution: acyl chlorides > anhydrides > esters > amides (in order of decreasing reactivity). This trend reflects the stability of the tetrahedral intermediate and the quality of the leaving group. Amides are the least reactive because nitrogen's strong electron donation stabilizes the intermediate, while chlorine is the best leaving group.

## Questions

```yaml
- question: "You want to synthesize an ester from a carboxylic acid derivative and an alcohol under mild conditions. Which derivative would react most readily?"
  type: multiple-choice
  options:
    - "An amide — amines are excellent nucleophiles, suggesting high reactivity toward alcohol"
    - "A carboxylic acid — it is the parent compound and reacts directly"
    - "An acyl chloride — it has the best leaving group and the least resonance stabilization, making the carbonyl most electrophilic"
    - "An ester — the reaction is an exchange of one ester for another and proceeds readily"
  answer: 2
  explanation: "Acyl chlorides sit at the top of the reactivity ladder: Cl⁻ is an excellent leaving group (weak base, stable anion), and chlorine's 3p orbital overlaps poorly with carbon's 2p, so there is minimal resonance donation into the carbonyl. This leaves the carbonyl carbon highly electrophilic, making acyl chlorides react readily with alcohols to give esters. Option A confuses the nucleophile (amine) with the leaving group — in amide hydrolysis, the amine would have to leave as NH₂⁻, an extremely strong base and terrible leaving group."

- question: "A chemist attempts to convert an amide to an ester by stirring it with excess ethanol at room temperature. Why does this reaction fail?"
  type: multiple-choice
  options:
    - "Ethanol is not nucleophilic enough to attack the carbonyl carbon"
    - "The reaction fails because esters are thermodynamically less stable than amides and the equilibrium disfavors product formation — the reaction is just slow"
    - "Nitrogen's strong lone-pair donation into the carbonyl makes the carbon less electrophilic, and the amide ion (NH₂⁻) is too strong a base to serve as a leaving group — both factors oppose the reaction"
    - "Esters and amides cannot interconvert because they have different functional groups"
  answer: 2
  explanation: "Two reinforcing factors make amides the least reactive derivatives. First, nitrogen donates its lone pair strongly into the carbonyl π* orbital, giving the C–N bond roughly 40% double-bond character and making the carbonyl carbon far less electrophilic. Second, the leaving group would be NH₂⁻ (or NR₂⁻), an extremely strong base — strong bases resist departure. Converting an amide to an ester requires both overcoming this stabilization and forcing a terrible leaving group out, which demands harsh conditions or activating reagents. This reaction is strictly 'uphill' in the reactivity series."

- question: "In nucleophilic acyl substitution, reactions spontaneously convert more reactive derivatives to less reactive ones, but not the reverse."
  type: true-false
  answer: true
  explanation: "The reactivity hierarchy (acyl chlorides > anhydrides > esters > amides) reflects thermodynamic stability as well as kinetic reactivity. Converting an acyl chloride to an ester or amide releases the strain of the unstable starting material and produces a more stable, lower-energy product — thermodynamics and kinetics both favor the 'downhill' direction. Going 'uphill' (e.g., ester to acyl chloride) requires external activation (thionyl chloride, PCl₅) because the products are higher in energy than the starting materials."

- question: "Acyl chlorides are highly reactive primarily because chlorine's lone pairs donate strongly into the carbonyl, making it very electrophilic."
  type: true-false
  answer: false
  explanation: "This has the mechanism backwards. Chlorine's lone pairs are in 3p orbitals that overlap poorly with carbon's 2p orbital, so chlorine barely donates into the carbonyl. This is actually WHY acyl chlorides are reactive — the carbonyl remains highly electrophilic precisely because chlorine provides almost no resonance stabilization. By contrast, nitrogen in amides donates strongly into the carbonyl (both in 2p orbitals), which reduces carbonyl electrophilicity and makes amides unreactive."

- question: "Both nitrogen (in amides) and oxygen (in esters) have lone pairs adjacent to the carbonyl. Why does nitrogen's donation so dramatically reduce reactivity compared to oxygen's?"
  type: short-answer
  answer: "Nitrogen is a better electron donor than oxygen for two reasons: (1) nitrogen's lone pair is in a 2p orbital, matching carbon's 2p orbital for optimal overlap, giving amide C–N bonds substantial double-bond character (~40%); oxygen donates less effectively, partly due to its greater electronegativity withdrawing electron density. (2) If the reaction proceeds, nitrogen leaves as NH₂⁻ (pKa ~35), an extremely strong base and terrible leaving group, while oxygen leaves as RO⁻ (pKa ~16), a moderately strong base. Both factors — reduced electrophilicity AND worse leaving group — stack against amide reactivity."
  explanation: "The dual-factor analysis is the key insight: reactivity in nucleophilic acyl substitution depends on electrophilicity of the carbonyl carbon (controlled by heteroatom donation) AND leaving group quality (controlled by basicity of the departing anion). Amides score worst on both. This is not a coincidence — the same property (nitrogen's electron-donating ability) simultaneously reduces carbonyl electrophilicity and increases leaving-group basicity."
```

## Explainer

From your study of nucleophilic acyl substitution, you know the general mechanism: a nucleophile attacks the electrophilic carbonyl carbon, forming a tetrahedral intermediate, and then a leaving group departs to regenerate the carbonyl. The question this topic answers is: why do acyl chlorides react explosively with water while amides can sit in aqueous solution for days without hydrolyzing? The answer comes down to two reinforcing factors — leaving group ability and resonance stabilization of the starting material.

Consider the **leaving group trend** first. In acyl chlorides, the leaving group is Cl⁻ — a weak base and excellent leaving group, happy to depart with the bonding electrons. In anhydrides, the leaving group is a carboxylate (RCO₂⁻), still a reasonably stable anion. In esters, it is an alkoxide (RO⁻) — a stronger base and poorer leaving group. In amides, the leaving group would be an amide ion (NH₂⁻ or NR₂⁻) — an extremely strong base that resists departure. The better the leaving group, the faster the tetrahedral intermediate collapses to products.

Now consider **resonance stabilization** of the starting material. Every carboxylic acid derivative has a lone pair on the atom attached to the carbonyl (the heteroatom). This lone pair can donate into the carbonyl's pi system, stabilizing the ground state and reducing the electrophilicity of the carbonyl carbon. Nitrogen is the best electron donor of the group — its lone pair overlaps strongly with the carbonyl pi* orbital, giving amides substantial double-bond character in the C–N bond (roughly 40% pi character). This makes the amide carbonyl much less electrophilic than you might expect. Oxygen in esters donates less effectively, and chlorine in acyl chlorides barely donates at all because its 3p orbital overlaps poorly with carbon's 2p. So acyl chlorides have the most electrophilic carbonyl and the best leaving group — both factors drive high reactivity.

The practical consequence is that you can only convert derivatives **downhill** in the reactivity series without forcing conditions. An acyl chloride can be converted to an anhydride, ester, or amide simply by adding the appropriate nucleophile. But you cannot convert an amide to an ester just by adding an alcohol — the amide is too stable and NH₂⁻ is too poor a leaving group. To go "uphill" in reactivity, you need activating reagents or harsh conditions. This reactivity ladder is central to retrosynthetic planning: when you see an amide target, you know you can build it from an acyl chloride or ester, but not the reverse without special chemistry.
