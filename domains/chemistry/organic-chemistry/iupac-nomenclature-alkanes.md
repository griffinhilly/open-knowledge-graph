---
id: iupac-nomenclature-alkanes
title: IUPAC Nomenclature of Alkanes
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
builds-toward:
- alkane-structure-and-properties
- alkene-structure-and-nomenclature
- functional-groups-overview
tags:
- nomenclature
- IUPAC
- alkanes
- naming
- substituents
stage: formal-systems
status: validated
---

# IUPAC Nomenclature of Alkanes

## Core Idea
IUPAC nomenclature provides a systematic method for naming organic compounds so that each name unambiguously encodes one structure. For alkanes, the rules involve identifying the longest carbon chain (the parent), numbering it to give substituents the lowest possible locants, naming branches as alkyl groups with numerical prefixes, and listing substituents alphabetically. Mastering IUPAC naming for alkanes establishes the logical pattern applied to all other functional classes.

## How It's Best Learned
Practice converting names to structures and structures to names in both directions. Start with straight-chain alkanes, add one branch at a time, then introduce multiple and identical substituents. Use name→structure exercises as a self-check on understanding.

## Common Misconceptions
- The longest chain is not always drawn horizontally; it must be found by counting carbons regardless of drawing orientation.
- Numbering always starts from the end closer to the first substituent — not automatically from the left or right.
- Substituents are cited alphabetically (ignoring multiplying prefixes di-, tri-) before the parent chain name.

## Questions

```yaml
- question: "A compound has a 5-carbon parent chain with a methyl group on C2 and an ethyl group on C4. What is its correct IUPAC name?"
  type: multiple-choice
  options:
    - "2-methyl-4-ethylpentane"
    - "4-ethyl-2-methylpentane"
    - "2-ethyl-4-methylpentane"
    - "4-methyl-2-ethylpentane"
  answer: 1
  explanation: "Substituents are cited alphabetically, ignoring multiplying prefixes. 'Ethyl' (E) precedes 'methyl' (M) alphabetically, so ethyl is listed first: 4-ethyl-2-methylpentane. The locants 2 and 4 are correct because numbering from the end closer to the first substituent gives 2 (for the methyl end) vs. numbering from the other end, which would give a higher set. Option A lists substituents in reverse alphabetical order."

- question: "In naming 2,5-dimethylheptane, the prefix 'di' is considered when alphabetizing substituents alongside other substituents."
  type: true-false
  answer: false
  explanation: "Multiplying prefixes (di-, tri-, tetra-, etc.) are ignored when alphabetizing substituents in IUPAC nomenclature. If this compound also had an ethyl group, the order would be 'ethyl' before 'methyl' (E before M), regardless of the 'di' prefix on the methyls. The same rule applies to sec- and tert- prefixes, which are also ignored for alphabetizing, while 'iso-' and 'cyclo-' are included."

- question: "A student draws a structural formula and, looking at the drawing, identifies the longest horizontal chain as 6 carbons, naming the compound 3-methylhexane. What error might the student be making, and how should they correct it?"
  type: short-answer
  answer: "The student may be picking the longest horizontal path in the drawing rather than the longest actual carbon chain. Structural drawings are arbitrary in orientation — what appears as a branch might be part of a longer continuous chain. The student should trace every possible continuous carbon path and count carbons in each, choosing the longest regardless of drawing orientation."
  explanation: "IUPAC naming requires finding the longest continuous carbon chain in the molecule, not the longest horizontal segment in a particular drawing. A substituent drawn as a vertical branch might actually be connected to more carbons that, when followed through the drawing, form a longer chain than the horizontal one. Systematically tracing all paths is the only reliable method."
```

## Explainer

IUPAC nomenclature is a systematic language for organic chemistry: given a name, you can reconstruct an exact structure; given a structure, you can derive its unique name. For alkanes — hydrocarbons with only single bonds — the naming logic follows four steps, and mastering them builds the foundation for naming every other functional class.

The first task is finding the longest continuous carbon chain in the molecule. This is the parent chain, and its length gives the base name: meth- (1C), eth- (2C), prop- (3C), but- (4C), pent- (5C), hex- (6C), hept- (7C), oct- (8C), non- (9C), dec- (10C). The trap here is that structural drawings are 2D representations: a "branch" drawn vertically might actually extend the longest chain if you follow the carbons through the drawing. You must trace every possible continuous path, counting all carbons, before deciding on the parent chain.

Once the parent chain is identified, number it from the end that gives the first substituent the lowest possible position number. If a methyl group hangs off C2 from one end and C4 from the other, number from the end that gives 2, not 4. If there are multiple substituents, apply the lowest-set-of-locants rule: compare the full sets of locants and choose the numbering that minimizes them at the first point of difference.

Substituents on the parent chain are named as alkyl groups: -CH₃ is methyl, -CH₂CH₃ is ethyl, -CH(CH₃)₂ is isopropyl, and so on. When writing the name, list substituents alphabetically before the parent chain name. Alphabetize by the base name of the substituent, ignoring multiplying prefixes (di-, tri-, sec-, tert-). So a compound with both ethyl and dimethyl groups would list ethyl first (E before M), then dimethyl. Each substituent gets a locant, and identical substituents take a multiplying prefix: 2,3-dimethyl, not methyl-methyl.

The completed name reads locant(s)-substituent...locant(s)-substituent...parent chain, all as one word. For example: 4-ethyl-2-methylheptane describes a 7-carbon chain (heptane) with a methyl group at C2 and an ethyl group at C4, with ethyl listed before methyl alphabetically. Practicing conversion in both directions — name → structure and structure → name — is the fastest way to build fluency, because errors in one direction usually reveal a misunderstanding that would appear in the other.
