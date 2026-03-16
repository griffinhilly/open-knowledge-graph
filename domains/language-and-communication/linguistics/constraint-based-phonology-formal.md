---
id: constraint-based-phonology-formal
title: 'Constraint-Based Phonology: Formal Foundations'
domain: language-and-communication
course: linguistics
prerequisites:
- id: formal-phonotactics
  type: hard
- id: optimality-theory-introduction
  type: soft
tags:
- phonology
- constraints
- OT
stage: formal-systems
status: draft
---

# Constraint-Based Phonology: Formal Foundations

## Core Idea
Constraint-based phonology, especially Optimality Theory, formalizes phonology as the interaction of violable constraints ranked by language. Outputs are optimal (minimal-cost) structures satisfying the ranking; this replaces ordered rules with ranked principles.

## Explainer

From your study of formal phonotactics, you know that every language permits some sound sequences and prohibits others — English allows *str-* onsets but not *tl-*, for example. Rule-based phonology explained these patterns through ordered derivational rules: the underlying form is the input, rules apply in a specified sequence, and the surface form is the output. This works, but it has a significant limitation: when languages differ, you must posit different rules for each one, and explaining why certain patterns cluster together across unrelated languages requires separate stipulation for each case. **Optimality Theory (OT)** offers a different architecture that addresses this directly.

In OT, the grammar has three components. **GEN** generates a large (in principle infinite) set of candidate output forms from any given input — every conceivable way of pronouncing the underlying representation. **CON** is a universal set of constraints, shared across all human languages. **EVAL** applies the ranked constraint hierarchy to filter the candidates, selecting the one that best satisfies the ranking as the grammatical output. The key insight is that constraints are **violable**: the winning candidate is not the one that violates no constraints, but the one that violates the fewest highly ranked ones. Every candidate violates something; the optimal one violates only lower-ranked constraints.

The constraints in CON fall into two fundamental families. **Markedness constraints** penalize phonologically marked structures — complex onsets, closed syllables, nasal vowels, voiced obstruents in coda position, and so on. These constraints push outputs toward simple, typologically common forms. **Faithfulness constraints** require outputs to match the input — preserve the input's segments, maintain their features, keep their order. These constraints resist the simplifying pressure of markedness. The grammar of any language is essentially a ranking of these two families against each other: when markedness outranks faithfulness, the language sacrifices input fidelity to produce simpler structures; when faithfulness outranks markedness, the language preserves input contrasts even at the cost of phonological complexity.

Cross-linguistic variation falls out naturally from ranking differences. Consider syllable-final consonant clusters: a language that ranks *NoCoda* (no coda consonants) above *Max-IO* (don't delete input segments) will delete coda consonants — the output is simpler, at the cost of faithfulness. A language with the opposite ranking will preserve coda clusters. The same two constraints, different ranking, different typological outcome. This is OT's central theoretical achievement: universal constraints plus language-specific rankings generates the space of possible human language grammars, explaining why languages differ in constrained, predictable ways rather than arbitrarily. Where your earlier work in phonotactics described which sequences are legal, OT explains *why* — as the result of constraint interaction rather than stipulated rules.
