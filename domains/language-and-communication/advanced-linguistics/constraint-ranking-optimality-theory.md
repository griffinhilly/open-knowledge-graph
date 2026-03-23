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
stage: expert
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

## Questions

```yaml
- question: "Language A always deletes word-final consonants; Language B always preserves them. An OT analyst claims both languages possess the same constraints NOCODA and MAX-IO. How can opposite outputs arise from the same two constraints?"
  type: multiple-choice
  options:
    - "Language A has NOCODA but lacks MAX-IO; Language B has MAX-IO but lacks NOCODA"
    - "In Language A, NOCODA outranks MAX-IO, so coda deletion is preferred; in Language B, MAX-IO outranks NOCODA, so consonants are preserved even at the cost of a coda violation"
    - "Language A applies NOCODA only in word-final position as a phonological rule; Language B's rule is different"
    - "The constraints are the same but Language B applies them only to stressed syllables"
  answer: 1
  explanation: "This is the central explanatory mechanism of OT: the same universal constraint inventory produces different phonological systems through different rankings. NOCODA (prefer no coda consonants) and MAX-IO (preserve input segments) conflict when an input has a coda. Which constraint wins depends on ranking. Language A prioritizes surface syllable well-formedness over faithfulness to the input; Language B does the opposite. No language-specific rules are needed — only a language-specific ranking order."

- question: "In an OT tableau, how is the winning candidate selected from a set of competitors?"
  type: multiple-choice
  options:
    - "The candidate with the fewest total constraint violations across all constraints wins"
    - "The candidate with no higher-ranked constraint violated more than any competing candidate wins — a single fatal violation of a top-ranked constraint eliminates a candidate regardless of how few lower-ranked violations it has"
    - "Candidates are scored on a weighted sum of violations; the highest score wins"
    - "All constraints must be satisfied; if no candidate satisfies all constraints, the input is ungrammatical"
  answer: 1
  explanation: "OT uses winner-take-all evaluation at each constraint level, not a sum of violations. Higher-ranked constraints take absolute priority. If candidate A violates a constraint ranked above any constraint that candidate B violates, B wins — even if A has fewer total violations overall. This is why the tableau procedure works column by column from left (highest ranked) to right: a candidate can be eliminated by a single fatal violation at the top, regardless of its performance on lower-ranked constraints."

- question: "Two languages can exhibit entirely different phonological processes while sharing an identical inventory of universal constraints, if their constraint rankings differ."
  type: true-false
  answer: true
  explanation: "This is OT's core prediction about cross-linguistic variation. English and Japanese have dramatically different syllable structures — English tolerates complex onsets and codas; Japanese strongly prefers open CV syllables and inserts epenthetic vowels. In OT terms, they share the same constraints (ONSET, NOCODA, MAX-IO, DEP-IO, etc.) but rank them differently. Japanese ranks syllable-structure markedness constraints very high; English ranks faithfulness constraints higher. The factorial typology claim holds that all possible human phonological systems are predicted by the set of possible rankings of a universal constraint set."

- question: "In Optimality Theory, a language that deletes consonants has a 'delete' rule that a language preserving those consonants lacks."
  type: true-false
  answer: false
  explanation: "OT replaces language-specific rules with language-specific constraint rankings. Both languages possess the same constraints — including MAX-IO (don't delete) and whatever markedness constraint motivates deletion. The language that deletes has simply ranked the markedness constraint above MAX-IO; the language that preserves has the reverse ranking. No language-specific deletion rule is required or posited. This is what makes OT a theory of linguistic typology: variation comes from ranking differences, not from different grammars being built from different primitive operations."

- question: "Why does OT predict that the set of possible human phonological systems corresponds to the set of possible rankings of a universal constraint inventory, rather than requiring separate rule inventories for each language?"
  type: short-answer
  answer: "Because the same finite set of constraints, ranked in different orders, generates different outputs from the same inputs without language-specific rules. Each ranking is a grammar; each possible ranking of n constraints is a possible human language. This means OT's typological predictions are generated mathematically — by permuting rankings — rather than by stipulating different rules for each language. The theory explains why cross-linguistic variation is bounded (only outputs achievable by some ranking of the universal set are possible) and why languages differ systematically rather than arbitrarily."
  explanation: "This is OT's boldest theoretical claim, called factorial typology. If there are n constraints, there are n! possible total rankings, each predicting a different phonological system. Researchers test the theory by checking whether observed cross-linguistic patterns are a subset of the predicted typological space. Languages outside the predicted set would falsify OT. This makes the theory empirically testable in a way that language-specific rule systems are not."
```

## Explainer

Constraint ranking is the engine that makes Optimality Theory (OT) work. Recall from your introduction to OT: the framework proposes that phonological systems are governed by universal **constraints** — requirements like ONSET (syllables should have onsets), NOCODA (syllables should not have codas), and MAX-IO (don't delete input segments). The key insight of constraint ranking is that these constraints are never all satisfied simultaneously in real languages; they conflict, and how they're ranked determines which conflicts get resolved which way.

Think of constraints as a priority list. If NOCODA outranks MAX-IO in some hypothetical language, the grammar will prefer to delete a coda consonant rather than leave it in place. If MAX-IO outranks NOCODA, the grammar will preserve the coda even though NOCODA is violated. Same two constraints, opposite ranking, opposite output — this is the core mechanism. Constraint ranking explains why different languages produce different surface forms from the same underlying representations: they're running the same constraint set with different priority orderings.

The evaluation procedure uses **tableaux** to make this explicit. A tableau lists the input form on the left, the competing output candidates across the rows, and the ranked constraints across the columns. For each candidate, violations of each constraint are marked with asterisks. The winner is the candidate that loses no direct competition — that is, the candidate with no higher-ranked constraint violated more than an alternative candidate. The tableau is essentially a visual tournament: candidates are eliminated one by one as higher-ranked constraints knock them out, until only the winner remains. Constructing tableaux is the primary analytical skill of OT: you must determine which ranking correctly selects the attested output over all the losing candidates.

The explanatory power of constraint ranking becomes clear when you compare languages. Consider syllabification: English tolerates complex onsets like /str-/ in "string" but forbids certain coda clusters; Japanese strongly prefers CV syllables and inserts epenthetic vowels to break up consonant clusters. In OT terms, English and Japanese aren't following different rules — they have different rankings of the same constraints. Japanese ranks NOCODA and ONSET very high; English ranks them lower relative to MAX-IO (faithfulness to the input). This **factorial typology** claim — that the set of possible human languages corresponds to the set of possible rankings of a universal constraint inventory — is OT's boldest prediction, and generating typologies through permutation of rankings is one of the theory's primary research methodologies.

One important subtlety: ranking is not always total (every constraint strictly above every other). Some constraints may be **unranked** with respect to each other, allowing ties and producing optionality or dialectal variation. More recent OT variants, like Stochastic OT and Maximum Entropy grammars, assign numerical weights rather than strict orderings, allowing graded probabilities of surface forms. These refinements preserve the core ranking logic while extending it to phenomena that strict ranking cannot capture — gradient grammaticality, free variation, and the gradual phonological shifts that characterize language acquisition and change.
