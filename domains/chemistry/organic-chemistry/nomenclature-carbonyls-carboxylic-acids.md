---
id: nomenclature-carbonyls-carboxylic-acids
title: IUPAC Nomenclature of Carbonyls and Carboxylic Acids
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbonyl-chemistry-intro
  type: soft
- id: carboxylic-acids-and-derivatives
  type: soft
- id: iupac-nomenclature-alkanes
  type: hard
builds-toward:
- nucleophilic-acyl-substitution
- friedel-crafts-alkylation-acylation
tags:
- nomenclature
- aldehydes
- ketones
- carboxylic-acids
- iupac
stage: formal-systems
status: draft
---

# IUPAC Nomenclature of Carbonyls and Carboxylic Acids

## Core Idea
Aldehydes (C=O at the end of a chain) use the -al suffix; ketones use -one. Carboxylic acids use -oic acid and take priority in numbering. Esters, amides, and acid chlorides use suffixes -oate, -amide, and -oyl chloride, with the parent acid determining the base name.

## How It's Best Learned
Name increasingly complex structures with carbonyls and carboxylic acids, paying close attention to functional group priorities and ensuring correct suffix selection.

## Common Misconceptions
- Confusing the position and naming of aldehydes vs. ketones; aldehyde carbonyl is always at a chain terminus (position 1).
- Misremembering ester and amide suffix order or forgetting to reference the parent acid.

## Questions

```yaml
- question: "A 5-carbon molecule has a carboxylic acid group at one end and a ketone carbonyl at carbon 3. What is its correct IUPAC name?"
  type: multiple-choice
  options:
    - "3-oxopentanoic acid — carboxylic acid takes priority, ketone becomes an oxo- prefix"
    - "pentan-3-one-1-oic acid — both suffixes are listed simultaneously"
    - "3-ketopentanoic acid — 'keto-' is the standard prefix for a ketone in a chain with a carboxylic acid"
    - "5-oxopentanoic acid — the ketone is numbered from the opposite end"
  answer: 0
  explanation: "When a molecule contains both a ketone and a carboxylic acid, the carboxylic acid has higher naming priority and becomes the principal characteristic group, taking the -oic acid suffix. The carboxyl carbon is C1, so the chain is numbered from that end. The ketone, which cannot also take a suffix, is indicated with the prefix 'oxo-' at its position — here, C3. You cannot use two suffixes simultaneously (option B), 'keto-' is not standard IUPAC prefix notation (option C), and numbering from the wrong end gives 5-oxo incorrectly (option D)."

- question: "Which of the following is the correct IUPAC name for CH₃CH₂CHO?"
  type: multiple-choice
  options:
    - "propanal — a 3-carbon chain with an aldehyde terminal carbonyl"
    - "propan-1-one — a ketone suffix at position 1"
    - "1-propanaldehyde — a locant is needed to specify the aldehyde position"
    - "propanone — the suffix for any 3-carbon carbonyl compound"
  answer: 0
  explanation: "CH₃CH₂CHO is an aldehyde: the C=O is at the end of a 3-carbon chain. Aldehydes use the suffix -al, replacing the terminal -e of the parent alkane (propane → propanal). Because the carbonyl carbon in an aldehyde is ALWAYS at position 1, no locant is needed — so '1-propanaldehyde' (option C) is both incorrect in format and redundant. 'Propan-1-one' (option B) incorrectly uses the ketone suffix; 'propanone' (option D) also incorrectly uses the ketone suffix and would refer to a different structure."

- question: "In IUPAC nomenclature, the carbonyl carbon of an aldehyde is always carbon 1, so no position number is ever written as part of the -al suffix."
  type: true-false
  answer: true
  explanation: "This is correct. Aldehydes have the C=O at the end of the carbon chain by definition, making that carbon C1 automatically. Because the position is fixed, including a locant would be redundant and is not used in IUPAC nomenclature — you simply write 'propanal,' 'butanal,' etc. Compare this to ketones, where the carbonyl can be at different interior positions and a locant (e.g., 'pentan-3-one') is required."

- question: "In IUPAC nomenclature, the suffix '-oate' indicates an amide — a carbonyl group bonded to a nitrogen."
  type: true-false
  answer: false
  explanation: "'-Oate' is the suffix for an ester, not an amide. Esters are formed when a carboxylic acid reacts with an alcohol; the suffix replaces '-oic acid' with '-oate,' and the alkyl group from the alcohol is named first (e.g., methyl ethanoate). Amides — carbonyl groups bonded to nitrogen — use the suffix '-amide' (e.g., ethanamide). Confusing these two is one of the most common errors in carbonyl nomenclature."

- question: "How does IUPAC nomenclature handle a molecule that contains both a ketone and a carboxylic acid? Which group takes priority, and how is the lower-priority group indicated?"
  type: short-answer
  answer: "The carboxylic acid takes priority over the ketone. The carboxyl carbon becomes C1 and the compound takes the '-oic acid' suffix. The ketone cannot also take a suffix, so it is instead indicated with the prefix 'oxo-' at its position number. For example, a 5-carbon chain with COOH at one end and a C=O at C3 is named 3-oxopentanoic acid."
  explanation: "IUPAC nomenclature establishes a strict hierarchy among functional groups to ensure each compound has exactly one unambiguous name. Carboxylic acids rank above aldehydes and ketones, so when both are present, the acid suffix (-oic acid) is used and the ketone's presence is indicated with the prefix 'oxo-'. This hierarchy — carboxylic acid > aldehyde > ketone — is consistently tested because students often try to use two suffixes simultaneously, which is not permitted."
```

## Explainer

You already know how to name alkanes using IUPAC rules: find the longest chain, number from one end, and attach the right suffix. Naming carbonyls and carboxylic acids follows the same logic, but with one critical addition — **functional group priority** determines which suffix wins and which end of the chain gets position 1. The carbonyl group (C=O) is the defining feature of several functional groups, and each one has its own suffix that replaces the -e of the parent alkane name.

**Aldehydes** have the carbonyl at the end of a chain, so the carbonyl carbon is always carbon 1 — you never need to specify its position. Drop the -e from the parent name and add **-al**. Methanal (formaldehyde), ethanal (acetaldehyde), and propanal are the simplest examples. **Ketones** have the carbonyl between two carbons within the chain. Drop the -e and add **-one**, with a number indicating the carbonyl position: propan-2-one, pentan-3-one. The chain is numbered to give the carbonyl the lowest possible locant.

**Carboxylic acids** take the highest naming priority among these groups. The suffix is **-oic acid**, and the carboxyl carbon is always carbon 1. Ethanoic acid (acetic acid) and propanoic acid are straightforward examples. When a carboxylic acid is present alongside a ketone in the same molecule, the acid suffix takes priority and the ketone is indicated with an "oxo-" prefix instead of the -one suffix. This hierarchy — carboxylic acid > aldehyde > ketone — is one of the most frequently tested concepts in organic nomenclature.

The carboxylic acid derivatives follow a consistent pattern based on what replaces the -OH of the acid. **Esters** use the suffix **-oate** with the alkyl group from the alcohol named first as a separate word (e.g., methyl ethanoate). **Amides** replace -oic acid with **-amide** (ethanamide). **Acid chlorides** use **-oyl chloride** (ethanoyl chloride). In each case, the parent chain is named from the carbonyl carbon of the original acid. The key to mastering these names is recognizing that every derivative is named by reference to its parent acid — once you can name the acid, the derivative names follow by swapping suffixes.
