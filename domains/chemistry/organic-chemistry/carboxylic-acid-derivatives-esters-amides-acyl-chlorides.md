---
id: carboxylic-acid-derivatives-esters-amides-acyl-chlorides
title: 'Carboxylic Acid Derivatives: Esters, Amides, and Acyl Chlorides'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carboxylic-acids-and-derivatives
  type: hard
- id: iupac-nomenclature-alkanes
  type: hard
builds-toward:
- nucleophilic-acyl-substitution
- amide-formation-and-properties
- relative-reactivity-carboxylic-acid-derivatives
tags:
- esters
- amides
- acyl-chlorides
- anhydrides
- carboxylic-acid-derivatives
stage: advanced
status: draft
---

# Carboxylic Acid Derivatives: Esters, Amides, and Acyl Chlorides

## Core Idea
Carboxylic acid derivatives share the acyl group (RCO-) and undergo nucleophilic acyl substitution. Acyl chlorides are highly reactive; anhydrides and esters are moderately reactive; amides are least reactive. IUPAC nomenclature specifies the type (e.g., ethanoate for an ester, ethanamide for an amide). Understanding the reactivity trends and functional group structures is essential for synthesis planning.

## Questions

```yaml
- question: "A chemist wants to synthesize an amide from a carboxylic acid and an amine. She tries mixing them directly but gets mostly unreacted starting materials. She should instead first convert the carboxylic acid to which intermediate?"
  type: multiple-choice
  options:
    - "An ester, then react with the amine"
    - "An acyl chloride, then react with the amine"
    - "An anhydride, then react with the amine — both are equally valid"
    - "No conversion is needed; heating the mixture suffices"
  answer: 1
  explanation: "Direct combination of a carboxylic acid and amine leads to an acid-base neutralization (forming a salt) rather than amide bond formation. The solution is to activate the acid by converting it to a more reactive derivative — the acyl chloride — which reacts readily with the amine to form the amide. Option A (via ester) is technically possible but slower and less clean. The key principle is that synthesis flows downhill: acyl chloride → ester/anhydride → amide, never uphill."

- question: "Why are amides the least reactive of the carboxylic acid derivatives toward nucleophilic acyl substitution?"
  type: multiple-choice
  options:
    - "Amides have the largest molecular weight, making diffusion to the reaction site slower"
    - "The nitrogen lone pair donates strongly into the carbonyl via resonance, reducing electrophilicity at the carbonyl carbon"
    - "The C–N bond is weaker than the C–O bond in esters, making amides unstable"
    - "Amides are less soluble in common solvents, so reagents cannot access the carbonyl"
  answer: 1
  explanation: "Reactivity in nucleophilic acyl substitution is determined by how electrophilic the carbonyl carbon is. Nitrogen is a stronger resonance donor than oxygen — its lone pair delocalizes more extensively into the carbonyl π system, reducing the partial positive charge on carbon and making it less attractive to nucleophiles. This is not a physical/solubility effect but an electronic one rooted in nitrogen's better lone-pair overlap with the carbonyl. Acyl chlorides are most reactive because chlorine's 3p orbitals overlap poorly with the 2p carbonyl, leaving the carbon highly electrophilic."

- question: "An acyl chloride is more reactive than an ester because chlorine donates more electron density into the carbonyl through resonance than oxygen does."
  type: true-false
  answer: false
  explanation: "This reverses the explanation. Acyl chlorides are MORE reactive than esters precisely because chlorine donates LESS electron density into the carbonyl than oxygen does. Chlorine's 3p orbital overlaps poorly with the 2p orbital on carbon, so the carbonyl carbon remains highly electrophilic. In esters, the alkoxy oxygen's lone pair delocalizes readily into the carbonyl, reducing electrophilicity and decreasing reactivity. Greater resonance donation = less reactive, not more."

- question: "You can convert an ester into an acyl chloride simply by treating it with a suitable chlorinating reagent under mild conditions."
  type: true-false
  answer: false
  explanation: "Interconversion among carboxylic acid derivatives flows only downhill — from more reactive to less reactive (acyl chloride → anhydride → ester → amide). You cannot convert a less reactive derivative into a more reactive one without first reverting to the free carboxylic acid and then re-activating it. To go from an ester to an acyl chloride, you must first hydrolyze the ester back to the carboxylic acid, then treat the acid with a reagent like SOCl₂ or PCl₃. This 'downhill-only' principle is a core organizing concept in acyl substitution chemistry."

- question: "Explain the reactivity trend among acyl chlorides, esters, and amides in nucleophilic acyl substitution. What structural feature drives the differences?"
  type: short-answer
  answer: "Reactivity follows acyl chloride > ester > amide. The key driver is how much the leaving group donates electron density back into the carbonyl carbon through resonance. Chlorine donates the least (poor 3p–2p orbital overlap), leaving the carbonyl carbon highly electrophilic and reactive. Oxygen in esters donates more, reducing electrophilicity. Nitrogen in amides donates the most, making the carbonyl carbon least electrophilic and amides the most resistant to nucleophilic attack."
  explanation: "Understanding this trend is essential for synthesis: you always activate toward a more reactive form before converting to a less reactive one. The driving force is not bond strength or leaving group size — it is resonance donation from the atom directly bonded to the carbonyl. Better donation → less electrophilic carbonyl → lower reactivity. This is why amides are the thermodynamic 'sink' in acyl substitution chemistry."
```

## Explainer

All carboxylic acid derivatives share a common structural core: the **acyl group** (R–C=O) bonded to a leaving group. What changes from one derivative to another is only the identity of that leaving group — chloride in acyl chlorides, a carboxylate in anhydrides, an alkoxy group (–OR') in esters, and an amine (–NR₂) in amides. This single substitution creates a family of compounds with the same fundamental reaction — nucleophilic acyl substitution — but with dramatically different reactivities.

The reactivity trend follows directly from leaving group ability and resonance donation. **Acyl chlorides** (R–COCl) are the most reactive because chloride is an excellent leaving group and donates relatively little electron density back into the carbonyl through resonance (chlorine's 3p orbitals overlap poorly with carbon's 2p). This leaves the carbonyl carbon highly electrophilic and eager to react with nucleophiles. **Anhydrides** (RCO–O–COR) are next: the leaving group is a carboxylate, which is reasonably stable, though the oxygen does donate some electron density via resonance. **Esters** (R–COOR') are less reactive still, because the alkoxy oxygen donates its lone pairs into the carbonyl through resonance, reducing the electrophilicity of the carbonyl carbon. **Amides** (R–CONR₂) sit at the bottom of the reactivity scale because nitrogen is a stronger resonance donor than oxygen — its lone pair delocalizes extensively into the carbonyl, making the carbonyl carbon the least electrophilic of all the derivatives.

Naming these compounds follows systematic IUPAC rules built on the parent carboxylic acid. For an ester, you name the alkyl group from the alcohol portion first, then change the "-ic acid" ending to "-ate" (ethanoic acid → methyl ethanoate). For an amide, replace "-ic acid" with "-amide" (ethanoic acid → ethanamide). Acyl chlorides use the "-yl chloride" suffix (ethanoyl chloride). Anhydrides name both acid components followed by "anhydride" (ethanoic anhydride). Recognizing these naming patterns lets you immediately identify the functional group and predict the compound's reactivity class.

The practical importance of this reactivity ladder is in synthesis. When you want to make an amide from a carboxylic acid, you do not attack the acid directly with an amine (the acid-base reaction gets in the way). Instead, you first convert the acid to a more reactive derivative — typically an acyl chloride — and then react that with the amine. The principle is general: you can always convert a more reactive derivative into a less reactive one (acyl chloride → anhydride → ester → amide), but not the reverse without special activation. This "downhill" flow of reactivity is the organizing logic behind acyl substitution chemistry.
