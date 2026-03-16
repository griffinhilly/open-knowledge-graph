---
id: constraint-ranking-optimality-theory
title: Constraint Interaction and Ranking in Optimality Theory
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: optimality-theory-introduction
  type: hard
- id: faithfulness-constraints-phonology
  type: soft
- id: markedness-constraints-phonology
  type: soft
tags:
- constraint-ranking
- optimality-theory
- phonology
stage: advanced
status: draft
---

# Constraint Interaction and Ranking in Optimality Theory

## Core Idea
Constraint ranking determines the output of phonological systems: higher-ranked constraints must be satisfied; lower-ranked constraints are violated if necessary. Languages differ in ranking, so the same constraints produce different phonological systems. Constraint ranking explains why languages with the same constraints exhibit different processes—ranking determines priority. Winner-take-all evaluation (the candidate with the fewest top-ranked constraint violations wins) makes the theory both simple and explanatory.

## How It's Best Learned
Construct OT tableaux for sets of candidate outputs, ranking constraints to select the correct surface form. Vary rankings to show how different orderings produce different phonological systems.

## Common Misconceptions
- Constraint ranking is not fixed across a language; some constraints may be unranked or probabilistically ranked.
- Not all differences between languages require different constraint inventories; ranking differences suffice.

## Explainer

Constraint ranking is the engine that makes Optimality Theory (OT) work. Recall from your introduction to OT: the framework proposes that phonological systems are governed by universal **constraints** — requirements like ONSET (syllables should have onsets), NOCODA (syllables should not have codas), and MAX-IO (don't delete input segments). The key insight of constraint ranking is that these constraints are never all satisfied simultaneously in real languages; they conflict, and how they're ranked determines which conflicts get resolved which way.

Think of constraints as a priority list. If NOCODA outranks MAX-IO in some hypothetical language, the grammar will prefer to delete a coda consonant rather than leave it in place. If MAX-IO outranks NOCODA, the grammar will preserve the coda even though NOCODA is violated. Same two constraints, opposite ranking, opposite output — this is the core mechanism. Constraint ranking explains why different languages produce different surface forms from the same underlying representations: they're running the same constraint set with different priority orderings.

The evaluation procedure uses **tableaux** to make this explicit. A tableau lists the input form on the left, the competing output candidates across the rows, and the ranked constraints across the columns. For each candidate, violations of each constraint are marked with asterisks. The winner is the candidate that loses no direct competition — that is, the candidate with no higher-ranked constraint violated more than an alternative candidate. The tableau is essentially a visual tournament: candidates are eliminated one by one as higher-ranked constraints knock them out, until only the winner remains. Constructing tableaux is the primary analytical skill of OT: you must determine which ranking correctly selects the attested output over all the losing candidates.

The explanatory power of constraint ranking becomes clear when you compare languages. Consider syllabification: English tolerates complex onsets like /str-/ in "string" but forbids certain coda clusters; Japanese strongly prefers CV syllables and inserts epenthetic vowels to break up consonant clusters. In OT terms, English and Japanese aren't following different rules — they have different rankings of the same constraints. Japanese ranks NOCODA and ONSET very high; English ranks them lower relative to MAX-IO (faithfulness to the input). This **factorial typology** claim — that the set of possible human languages corresponds to the set of possible rankings of a universal constraint inventory — is OT's boldest prediction, and generating typologies through permutation of rankings is one of the theory's primary research methodologies.

One important subtlety: ranking is not always total (every constraint strictly above every other). Some constraints may be **unranked** with respect to each other, allowing ties and producing optionality or dialectal variation. More recent OT variants, like Stochastic OT and Maximum Entropy grammars, assign numerical weights rather than strict orderings, allowing graded probabilities of surface forms. These refinements preserve the core ranking logic while extending it to phenomena that strict ranking cannot capture — gradient grammaticality, free variation, and the gradual phonological shifts that characterize language acquisition and change.
