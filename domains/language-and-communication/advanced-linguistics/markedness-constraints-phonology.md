---
id: markedness-constraints-phonology
title: Markedness Constraints in Phonology
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: optimality-theory-introduction
  type: hard
- id: phonological-features
  type: hard
builds-toward:
- constraint-ranking-optimality-theory
tags:
- markedness
- optimality-theory
- phonology
stage: advanced
status: draft
---

# Markedness Constraints in Phonology

## Core Idea
Markedness constraints penalize marked structures—those that are rare, complex, or violate universal phonological preferences. ONSET requires syllables to have onsets; NO-CODA disfavors codas. Markedness constraints interact with faithfulness: when markedness constraints are ranked high, languages exhibit processes (deletion, epenthesis) that create unmarked structures. Ranking of markedness constraints determines the phonotactic inventory and phonological processes of a language.

## How It's Best Learned
Identify which phonological processes in a language are driven by markedness (e.g., vowel epenthesis to satisfy ONSET), and construct constraint rankings that derive them. Compare across languages with different markedness priorities.

## Common Misconceptions
- Markedness is not universal immutability; marked structures can surface if high-ranked faithfulness constraints protect them.
- Marked does not mean rare in an absolute sense; it means marked relative to universal phonotactic preferences.

## Explainer

You already know, from phonological features and Optimality Theory, that sounds are not atoms — they have internal structure, and some structures are preferred over others cross-linguistically. **Markedness** is the theoretical framework that formalizes this observation: some phonological structures are **marked** (complex, rare, or avoided) and others are **unmarked** (simple, common, preferred). Markedness constraints are OT constraints that penalize marked structures — they push grammars toward simpler, more universally common phonological patterns.

The most intuitive markedness constraints are phonotactic: **ONSET** requires every syllable to begin with a consonant; **NO-CODA** disfavors syllables that end in a consonant. These constraints capture genuine cross-linguistic tendencies — CV (consonant-vowel) syllables are the most universally preferred syllable type, found in every language, while CVC syllables and especially complex codas are restricted in many. But markedness isn't limited to syllable structure. There are markedness constraints against voiced obstruents in coda position (many languages devoice final consonants), against nasal vowels, against particular consonant clusters, against tones in certain positions. Each constraint represents a preference that human phonological grammars lean toward when not overridden by competing constraints.

The crucial interaction is with **faithfulness constraints** like MAX and DEP. Markedness constraints want to eliminate complex structures; faithfulness constraints want to preserve the input. When markedness dominates faithfulness, the language uses phonological processes to repair marked structures: vowel epenthesis to satisfy ONSET (inserting a vowel so that a word-initial vowel acquires a preceding consonant), final consonant deletion to satisfy NO-CODA, cluster simplification to satisfy onset complexity constraints. When faithfulness dominates markedness, marked structures surface intact — the input is preserved even though it violates phonological preferences. This is why marked structures exist in languages at all: they are licensed by high-ranked faithfulness.

What markedness theory explains that earlier rule-based accounts could not is the cross-linguistic asymmetry in phonological processes. Languages systematically simplify toward unmarked structures — they rarely introduce more complex structures through phonological processes. When a language undergoes sound change, the change almost always moves toward less marked structures when faithfulness constraints weaken, almost never toward more marked ones. This **directionality** of phonological change and variation is predicted by the architecture of OT with markedness constraints: the grammar is always pushing toward unmarked structures, and faithfulness is the only counterweight holding marked structures in place.
