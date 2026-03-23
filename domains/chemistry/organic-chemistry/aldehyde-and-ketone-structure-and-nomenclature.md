---
id: aldehyde-and-ketone-structure-and-nomenclature
title: Aldehyde and Ketone Structure and Nomenclature
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
- id: functional-groups-overview
  type: hard
- id: iupac-nomenclature-alkanes
  type: hard
builds-toward:
- nucleophilic-addition-to-carbonyls
- keto-enol-tautomerism-mechanism
- enamine-chemistry-mechanism-and-reactions
tags:
- aldehyde
- ketone
- carbonyl
- nomenclature
- structure
stage: formal-systems
status: validated
---

# Aldehyde and Ketone Structure and Nomenclature

## Core Idea
Aldehydes contain a carbonyl group (C=O) bonded to a hydrogen and an alkyl group; ketones have the carbonyl bonded to two alkyl groups. Both are classified under the carbonyl functional group. Aldehydes are named using the suffix -al; ketones use -one. The carbonyl carbon is always the highest priority in the parent chain, making aldehydes more oxidized and generally more reactive in nucleophilic addition.

## Questions

```yaml
- question: "Why are aldehydes generally more reactive than ketones in nucleophilic addition reactions?"
  type: multiple-choice
  options:
    - "Aldehydes have higher molecular weight, giving them more kinetic energy"
    - "Ketones contain a hydrogen on the carbonyl, making them more sterically hindered"
    - "Aldehydes have only one alkyl group on the carbonyl carbon — less steric crowding and less electron donation than ketones with two alkyl groups"
    - "Aldehydes are less oxidized, so the carbonyl carbon carries less electrophilic character"
  answer: 2
  explanation: "Two factors make the aldehyde carbonyl carbon more electrophilic and more accessible to nucleophiles. First, less steric bulk: only one alkyl group flanks the carbonyl (versus two in ketones), so incoming nucleophiles face less obstruction. Second, less electron donation: alkyl groups push electron density toward the carbonyl carbon through induction, partially neutralizing its positive character. Two alkyl groups in a ketone donate more than one in an aldehyde, making the ketone less electrophilic. Option B reverses the structure — it is aldehydes, not ketones, that have a hydrogen on the carbonyl carbon."

- question: "A student needs to name the compound CH₃CH₂CH₂CHO using IUPAC rules. Which name is correct?"
  type: multiple-choice
  options:
    - "1-butanone"
    - "butanal"
    - "butan-1-one"
    - "4-oxobutane"
  answer: 1
  explanation: "The compound has a four-carbon chain with a carbonyl at one end bearing a hydrogen — an aldehyde. The IUPAC suffix -al replaces the terminal -e of the parent alkane name (butane → butanal). No position number is needed because -al always places the carbonyl at carbon 1; there is no other position possible. '1-butanone' and 'butan-1-one' would name a ketone, which requires the carbonyl to be bonded to two carbon groups — not a hydrogen. '4-oxobutane' is not standard IUPAC nomenclature for this compound."

- question: "Aldehydes can be oxidized to carboxylic acids under mild conditions, but ketones cannot be oxidized the same way."
  type: true-false
  answer: true
  explanation: "An aldehyde has a hydrogen on the carbonyl carbon; oxidation removes this hydrogen and adds a hydroxyl group, converting R-CHO to R-COOH (a carboxylic acid). A ketone has two alkyl groups on the carbonyl and no hydrogen to remove — oxidation to a higher state would require breaking a carbon-carbon bond, which demands harsh conditions and cleaves the molecule. This difference is exploited analytically: Tollens' reagent and Fehling's test distinguish aldehydes from ketones precisely because aldehydes are oxidized and ketones are not."

- question: "The compound propan-2-one (acetone) is a ketone because its carbonyl carbon is bonded to two hydrogen atoms."
  type: true-false
  answer: false
  explanation: "Acetone (propan-2-one) has the structure CH₃-CO-CH₃: the carbonyl carbon is bonded to two methyl groups, not two hydrogens. That is precisely what makes it a ketone — two alkyl (or aryl) groups on the carbonyl, with no hydrogen directly attached. If a hydrogen were on the carbonyl carbon, the compound would be an aldehyde. The confusion may arise from associating 'two groups' with hydrogens, but the defining groups for ketones are carbon-containing substituents."

- question: "Explain in your own words why the structural difference between aldehydes and ketones — one versus two alkyl groups on the carbonyl carbon — produces real differences in chemical reactivity."
  type: short-answer
  answer: "The aldehyde has a hydrogen on the carbonyl carbon; the ketone has two alkyl groups. This matters for two reasons: (1) Reactivity in nucleophilic addition — the aldehyde carbonyl has less steric shielding and less electron donation from substituents, making the carbonyl carbon a better electrophile and more accessible to nucleophilic attack. (2) Oxidation — the aldehyde hydrogen can be removed in oxidation, converting R-CHO to a carboxylic acid. Ketones lack this hydrogen and resist oxidation under ordinary conditions."
  explanation: "A seemingly small structural difference — one vs. two alkyl groups, presence vs. absence of a carbonyl hydrogen — propagates into two key chemical distinctions: susceptibility to nucleophilic addition and ability to be oxidized. Understanding these consequences is more important than memorizing the structural difference alone, because it predicts an entire network of reactions in carbonyl chemistry."
```

## Explainer

You already know from functional groups that the **carbonyl group** — a carbon double-bonded to oxygen (C=O) — is one of the most important structural motifs in organic chemistry. Aldehydes and ketones are the two simplest carbonyl-containing families, differing only in what is attached to the carbonyl carbon. In an **aldehyde**, the carbonyl carbon is bonded to at least one hydrogen (and one alkyl group or a second hydrogen in formaldehyde). In a **ketone**, the carbonyl carbon is bonded to two alkyl or aryl groups — no hydrogen directly on the carbonyl. This seemingly small structural difference has real chemical consequences: the hydrogen in aldehydes makes the carbonyl carbon more accessible to incoming nucleophiles and also means aldehydes can be further oxidized (to carboxylic acids), while ketones generally cannot.

Naming these compounds follows the IUPAC system you learned for alkanes, with modifications. For aldehydes, find the longest carbon chain that includes the carbonyl carbon, replace the -e ending of the parent alkane with **-al**, and number the chain so that the carbonyl carbon is always carbon 1 (no number is needed in the name since -al always means position 1). Methanal (formaldehyde), ethanal (acetaldehyde), and propanal are the simplest examples. For ketones, replace the -e ending with **-one** and number the chain to give the carbonyl carbon the lowest possible number. So pentan-2-one has a five-carbon chain with the carbonyl at position 2. When both an aldehyde and a ketone are present in the same molecule, the aldehyde takes naming priority because -al outranks -one in IUPAC conventions.

The carbonyl group's geometry and electronics set the stage for everything that follows in carbonyl chemistry. The carbon is sp² hybridized — trigonal planar with bond angles near 120°. Oxygen is more electronegative than carbon, so the C=O bond is strongly polarized: the oxygen carries a partial negative charge (δ⁻) and the carbon carries a partial positive charge (δ⁺). This makes the carbonyl carbon electrophilic — an inviting target for nucleophiles. In aldehydes, only one alkyl group flanks this electrophilic carbon, so there is less steric crowding and less electron donation compared to ketones, where two alkyl groups partially stabilize the positive character through induction. This is why aldehydes are generally more reactive toward nucleophilic addition than ketones.

Many important aldehydes and ketones also have widely used common names that predate IUPAC nomenclature. Formaldehyde (methanal), acetaldehyde (ethanal), acetone (propan-2-one), and benzaldehyde are names you will encounter constantly. Learning both naming systems is practical: IUPAC names are systematic and unambiguous, but common names dominate in laboratory conversation, reagent bottles, and biological chemistry. Recognizing the carbonyl group in either naming system is your entry point to the rich reaction chemistry of these compounds.
