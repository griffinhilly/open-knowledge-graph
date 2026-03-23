---
id: nomenclature-oxygenated-compounds
title: IUPAC Nomenclature of Alcohols, Ethers, and Thiols
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alcohols-and-ethers
  type: soft
- id: iupac-nomenclature-alkanes
  type: hard
builds-toward:
- alcohol-oxidation-to-carbonyls
- nucleophile-electrophile-definitions
tags:
- nomenclature
- alcohols
- ethers
- thiols
- functional-groups
stage: formal-systems
status: draft
---

# IUPAC Nomenclature of Alcohols, Ethers, and Thiols

## Core Idea
Alcohols and thiols use the -ol and -thiol suffixes, with the OH or SH carbon included in the main chain and numbered to give the functional group the lowest position. Ethers are named either as alkoxyalkanes or as ether-functional-group compounds, depending on which functional group is principal.

## How It's Best Learned
Name alcohols and thiols, ensuring the OH/SH carbon is part of the main chain count and gets the lowest number. Compare naming of ethers as alkoxy-substituted alkanes versus as principal ethers.

## Common Misconceptions
- Omitting the OH or SH carbon from the main chain count.
- Incorrectly assigning the ether as the principal functional group when another functional group (alcohol, aldehyde) should be principal.

## Questions

```yaml
- question: "A molecule contains both a hydroxyl group (–OH) and an ether linkage (–O–). How should it be named under IUPAC rules?"
  type: multiple-choice
  options:
    - "As an ether with a hydroxy substituent, because the ether oxygen bridges two carbons"
    - "As an alcohol with an alkoxy substituent, because the hydroxyl group outranks the ether in the functional group hierarchy"
    - "The choice depends on which functional group is attached to the longer carbon chain"
    - "As an alkoxyalcohol, treating both groups as co-principal functional groups"
  answer: 1
  explanation: "IUPAC rules rank functional groups in a strict priority hierarchy: alcohols outrank ethers. Only the highest-priority group earns the suffix; everything else becomes a prefix or substituent. So the molecule is named as an alcohol (suffix -ol) with the ether oxygen treated as an alkoxy- substituent. Option A reverses the hierarchy — ethers are always substituents when a higher-priority group is present."

- question: "When naming the compound CH₃–CH(OH)–CH₂–CH₃, why is the carbon bearing the –OH numbered as carbon 2 rather than carbon 3?"
  type: multiple-choice
  options:
    - "IUPAC rules require numbering from the end closest to the most branches"
    - "IUPAC rules require the principal functional group to receive the lowest possible locant"
    - "The numbering starts from the end with the most substituents, regardless of functional group"
    - "Both numbering directions give the same name for this molecule"
  answer: 1
  explanation: "For alcohols (and all oxygenated compounds), the chain is numbered so that the functional group carbon gets the lowest possible locant. Numbering from the left gives –OH on C2 (butan-2-ol); numbering from the right gives –OH on C3 (butan-3-ol). IUPAC chooses C2 because 2 < 3. This is a direct extension of the lowest-locant rule you already know for substituents on alkanes, now applied to the principal functional group."

- question: "Thiols are named using the same rules as alcohols, substituting the suffix -thiol for -ol, and the sulfur-bearing carbon must be included in and numbered within the parent chain."
  type: true-false
  answer: true
  explanation: "Correct. Thiols (R–SH) follow the same naming logic as alcohols (R–OH): the -e of the parent alkane is replaced by -thiol, the SH carbon must be part of the main chain count, and the chain is numbered to give the SH carbon the lowest possible locant. For example, CH₃CH₂SH is ethanethiol, parallel to ethanol."

- question: "In IUPAC nomenclature, an ether can serve as the principal functional group (receiving the -oxy suffix) even when a hydroxyl group is present in the same molecule."
  type: true-false
  answer: false
  explanation: "Ethers rank below alcohols, aldehydes, ketones, and carboxylic acids in IUPAC's functional group priority hierarchy. When a higher-priority group is present, the ether oxygen is always treated as an alkoxy substituent (prefix), not as the principal group. The suffix is reserved for the highest-priority functional group only."

- question: "Why does the IUPAC functional group priority hierarchy require that only one group receive the suffix when multiple oxygenated groups are present?"
  type: short-answer
  answer: "Because giving multiple groups suffix status would create ambiguous or contradictory names — the suffix encodes the primary chemical reactivity and class of the compound. The hierarchy ensures a unique, unambiguous name: the most reactive or highest-priority group determines the compound's class (suffix), while all others are described as substituents (prefixes). This lets a chemist immediately identify the compound's principal reactivity from the name alone."
  explanation: "The suffix communicates the compound's functional class and guides chemical reactivity predictions. If both –OH and an ether could each claim the suffix, two different valid names would exist for the same compound, violating IUPAC's goal of one compound → one name. The strict hierarchy resolves every tie by rank, producing a unique name regardless of molecular complexity."
```

## Explainer

You already know how to name alkanes using IUPAC rules — find the longest chain, number it, and attach substituent prefixes. Naming oxygenated compounds follows the same logic, but now the oxygen-containing functional group takes priority and determines the suffix. Think of it as adding a new rule on top of the naming system you already have: the functional group gets the lowest possible locant, and the suffix changes to reflect what kind of oxygen is present.

For **alcohols** (R–OH), replace the final -e of the parent alkane with **-ol**. The hydroxyl group must be part of the longest chain, and you number the chain so the –OH carbon gets the lowest possible number. For example, butan-2-ol tells you the parent chain is four carbons long and the hydroxyl is on carbon 2. If there are multiple hydroxyl groups, use -diol, -triol, and so on (ethane-1,2-diol for ethylene glycol). **Thiols** (R–SH) follow the same pattern but use the suffix **-thiol** instead — ethanethiol is the sulfur analog of ethanol.

**Ethers** (R–O–R') are handled differently because the oxygen bridges two carbon groups rather than terminating the chain. The IUPAC approach names the smaller group as an **alkoxy substituent** on the larger parent chain. For instance, methoxyethane describes a methyl group connected through oxygen to an ethane chain. This "alkoxy-as-substituent" method works cleanly when the ether is the only functional group. When a higher-priority group is present — say a hydroxyl or a carbonyl — the ether oxygen is always named as the alkoxy substituent, never as the principal suffix.

The critical skill is recognizing **functional group priority**. IUPAC rules rank functional groups in a strict hierarchy: carboxylic acids outrank aldehydes, which outrank ketones, which outrank alcohols, which outrank ethers. Only the highest-priority group gets the suffix; everything else becomes a prefix or substituent. A molecule with both an –OH and an ether linkage is named as an alcohol with an alkoxy substituent, not the other way around. Practicing this hierarchy with molecules that contain multiple oxygen-based groups is the fastest way to build reliable naming fluency.
