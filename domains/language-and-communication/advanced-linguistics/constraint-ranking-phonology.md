---
id: constraint-ranking-phonology
title: Constraint Ranking and Typology in Optimality Theory
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: optimality-theory-introduction
  type: hard
tags:
- phonology
- typology
- constraints
stage: advanced
status: draft
---

# Constraint Ranking and Typology in Optimality Theory

## Core Idea
Different constraint rankings produce different phonological systems. If MAX (preserve input material) dominates DEP (avoid extra elements), the language preserves input; if DEP dominates MAX, deletion is preferred. By systematically considering all possible rankings, OT predicts the set of possible languages and explains why certain patterns are universal while others never occur, providing formal typological predictions.

## Explainer

Optimality Theory, which you've already studied, makes a radical claim: all languages use the same universal set of constraints, and what makes languages differ is the **ranking** of those constraints. This means that phonological typology — the study of which phonological systems are possible and which are not — becomes, in principle, computable. If you can enumerate all the constraints and all possible rankings, you can predict exactly which language types are possible.

The key idea is **strict domination**: when two constraints conflict, the higher-ranked constraint wins, regardless of how many lower-ranked constraints are violated. Consider two constraints: **MAX** (don't delete input material) and **DEP** (don't insert new material). If MAX >> DEP in a language, the language will preserve input consonants even at the cost of inserting vowels to satisfy other constraints. If DEP >> MAX, the language will delete input consonants rather than insert repair vowels. These two rankings produce genuinely different phonological behaviors — one language adds vowels, the other drops consonants — from a single difference in ranking.

**Factorial typology** is what you get when you consider all possible orderings of a set of constraints. With two constraints, there are two possible rankings; with three, there are six; with ten, there are 3.6 million. Not all of these produce distinct languages — some rankings make identical predictions — but OT uses this space to characterize the range of attested and possible systems. A pattern that occurs in no ranking of universal constraints is predicted to be impossible — unattested because ungenerable by any grammar, not merely accidentally absent from the sample. This is a strong typological prediction, and testing it against cross-linguistic data is a major ongoing research program.

The deepest payoff is explanatory: OT constraint ranking doesn't just describe individual languages but explains why certain properties cluster together across languages. If a language lacks codas, it will also lack complex onsets — because the same constraints that ban codas also penalize complex onsets when ranked high enough. These **harmonic typologies** — where certain properties always co-occur — follow automatically from the constraint interaction logic rather than from stipulated rules. This kind of unified explanation, derived from ranked universal constraints, is what makes OT a fundamentally different kind of phonological theory from its rule-based predecessors.
