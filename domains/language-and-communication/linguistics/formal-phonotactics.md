---
id: formal-phonotactics
title: 'Formal Phonotactics: Constraints on Sound Sequences'
domain: language-and-communication
course: linguistics
prerequisites:
- id: feature-matrices-phonology
  type: hard
- id: syllable-structure-phonotactics
  type: soft
builds-toward:
- constraint-based-phonology-formal
tags:
- phonology
- constraints
- formalism
stage: advanced
status: draft
---

# Formal Phonotactics: Constraints on Sound Sequences

## Core Idea
Phonotactic constraints formally specify which sound sequences are permissible in a language (e.g., onset clusters must satisfy sonority sequencing). These constraints can be expressed as formal rules, forbidden structures, or ranked preferences (in Optimality Theory).

## Explainer

From feature matrices, you have a formal vocabulary for characterizing individual sounds — each phoneme is a bundle of binary features like [±voice], [±nasal], [±sonorant]. Formal phonotactics lifts this analysis to the level of *sequences*: given a set of segment feature specifications, which sequences are well-formed and which are prohibited? The answer varies by language, and capturing that variation formally is the central problem of phonotactic theory.

The **Sonority Sequencing Principle** (SSP) is the most studied phonotactic universal. Sonority — a scalar property roughly tracking loudness and openness — rises toward the syllable nucleus and falls away from it. In the onset cluster /spl-/ (as in "splash"), sonority increases: /s/ is a fricative (low sonority), /p/ is a stop (slightly lower, actually violating strict SSP — the /s/ + stop cluster is an attested exception cross-linguistically), /l/ is a lateral (high sonority), and the vowel is highest. The formal statement of SSP can be expressed as a rule over sonority indices or, equivalently, as a constraint on feature matrices. Any onset cluster where sonority decreases rather than increases (e.g., *[lp-]) is ruled out. This constraint is not stipulated arbitrarily for each language — it is a formal universal that individual grammars refine or occasionally violate.

**Forbidden structure rules** state phonotactic restrictions in negative terms: no onset cluster of the form [+sonorant][−sonorant], no coda of the form [+voice], and so on. These can be written as constraints over feature matrices using the formalism you already know. A rule that bans voiced obstruents in coda position (a real restriction in Standard German) is expressed as: *C[−sonorant, +voice] in coda. Every surface form of the language is checked against this constraint; any form that violates it is either blocked or repaired.

**Optimality Theory** (OT) reframes this logic. Rather than stating inviolable rules, OT posits a universal set of ranked constraints. The candidate output that best satisfies the highest-ranked constraints (incurring fewest violations of the most important ones) is the winner. A language that allows voiced coda obstruents simply ranks the IDENT-VOICE faithfulness constraint above *VOICED-CODA; a language that devoices them ranks the markedness constraint higher. This allows formal phonotactics to capture cross-linguistic variation without writing different rule sets for each language — the architecture is universal, and language-specific orderings generate language-specific patterns. Your transition to constraint-based phonology formalism will generalize this ranking logic to broader phenomena beyond the syllable.
