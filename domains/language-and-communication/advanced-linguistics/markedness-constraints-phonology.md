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
- id: feature-geometry-phonology
  type: soft
- id: sound-change-mechanisms-diachronic
  type: soft
builds-toward:
- constraint-ranking-optimality-theory
tags:
- markedness
- optimality-theory
- phonology
stage: expert
status: validated
---
# Markedness Constraints in Phonology

## Core Idea
Markedness constraints penalize marked structures—those that are rare, complex, or violate universal phonological preferences. ONSET requires syllables to have onsets; NO-CODA disfavors codas. Markedness constraints interact with faithfulness: when markedness constraints are ranked high, languages exhibit processes (deletion, epenthesis) that create unmarked structures. Ranking of markedness constraints determines the phonotactic inventory and phonological processes of a language.

## How It's Best Learned
Identify which phonological processes in a language are driven by markedness (e.g., vowel epenthesis to satisfy ONSET), and construct constraint rankings that derive them. Compare across languages with different markedness priorities.

## Common Misconceptions
- Markedness is not universal immutability; marked structures can surface if high-ranked faithfulness constraints protect them.
- Marked does not mean rare in an absolute sense; it means marked relative to universal phonotactic preferences.

## Questions

```yaml
- question: "In Language X, a word-initial vowel always acquires a preceding /n/ in surface forms (e.g., /ata/ → [nata], /ima/ → [nima]). Which constraint ranking best explains this epenthesis process?"
  type: multiple-choice
  options:
    - "MAX >> ONSET (faithfulness dominates, so no epenthesis occurs)"
    - "ONSET >> DEP (markedness dominates faithfulness, forcing onset insertion)"
    - "NO-CODA >> MAX (coda avoidance forces deletion of the input vowel)"
    - "DEP >> ONSET (faithfulness prevents insertion, so syllables lack onsets)"
  answer: 1
  explanation: "ONSET is a markedness constraint requiring every syllable to have a consonant onset. DEP is a faithfulness constraint penalizing segments in the output that have no input correspondent (i.e., epenthesis). When ONSET outranks DEP, the grammar tolerates epenthesis (adding /n/) to satisfy the onset requirement — the cost of violating faithfulness is worth it to avoid a marked onsetless syllable. When DEP >> ONSET, faithfulness wins and vowel-initial syllables surface intact. This analysis shows how markedness-faithfulness ranking directly predicts phonological processes."

- question: "Language A freely allows word-final consonants; Language B never allows them, deleting any coda consonant in the input. What is the OT constraint ranking difference between these languages?"
  type: multiple-choice
  options:
    - "Language A: NO-CODA >> MAX; Language B: MAX >> NO-CODA"
    - "Language A: MAX >> NO-CODA; Language B: NO-CODA >> MAX"
    - "Language A: ONSET >> DEP; Language B: DEP >> ONSET"
    - "Both languages have the same ranking; they differ in their underlying representations"
  answer: 1
  explanation: "NO-CODA is the markedness constraint penalizing coda consonants; MAX is the faithfulness constraint penalizing deletion (input segments with no output correspondent). When MAX outranks NO-CODA (Language A), faithfulness wins and coda consonants are preserved even though they violate a markedness constraint. When NO-CODA outranks MAX (Language B), the grammar prefers to delete the coda rather than surface a marked structure. This exemplifies OT's core claim: languages differ not in which constraints they have, but in how they rank universal constraints."

- question: "A language can have complex coda clusters (a marked structure) if faithfulness constraints outrank the markedness constraints penalizing them."
  type: true-false
  answer: true
  explanation: "Markedness constraints are never 'turned off' in any language — they are always present and always assign violations. What varies is ranking. If a high-ranked faithfulness constraint (like MAX, penalizing deletion) outranks the markedness constraint against complex codas, then the grammar preserves the input consonant cluster even though it violates phonological preferences. This is why marked structures exist in languages at all: faithfulness is the counterweight that allows marked inputs to surface intact."

- question: "Markedness constraints predict that all languages should converge on the same phonological inventory, since the same universal constraints penalize the same structures everywhere."
  type: true-false
  answer: false
  explanation: "Markedness constraints are universal, but their interaction with faithfulness constraints — which vary in ranking across languages — produces cross-linguistic diversity. If markedness alone determined phonology, all languages would indeed have only CV syllables and unmarked sounds. But faithfulness constraints, ranked differently in different grammars, protect different sets of marked inputs from being repaired. The universality is in the constraint set; the diversity is in the ranking. OT predicts that no language invents completely novel processes — they all use the same constraints — but rankings produce different surface typologies."

- question: "Why do phonological changes in languages almost always move toward less marked structures rather than more marked ones?"
  type: short-answer
  answer: "In OT, the grammar is constantly pushing toward unmarked structures via markedness constraints. When sound change occurs, it typically reflects a weakening of a faithfulness constraint — the grammar stops protecting some marked input and instead repairs it toward the unmarked output. Since markedness constraints favor simpler, more universally preferred structures (CV syllables, voiceless codas, etc.), the output after faithfulness weakens is always a less marked form. Moving toward more marked structures would require a markedness constraint to be demoted below faithfulness, which is the direction of borrowing or exceptional forms, not regular change."
  explanation: "This directionality of change is a core empirical prediction of OT with markedness. Languages simplify toward CV syllables, lose complex clusters, devoice final obstruents — these are not random drifts but gradient pressures exerted by markedness constraints that faithfulness constraints were previously suppressing. The asymmetry explains why similar sound changes appear repeatedly across unrelated languages: they are all responding to the same universal markedness pressures."
```

## Explainer

You already know, from phonological features and Optimality Theory, that sounds are not atoms — they have internal structure, and some structures are preferred over others cross-linguistically. **Markedness** is the theoretical framework that formalizes this observation: some phonological structures are **marked** (complex, rare, or avoided) and others are **unmarked** (simple, common, preferred). Markedness constraints are OT constraints that penalize marked structures — they push grammars toward simpler, more universally common phonological patterns.

The most intuitive markedness constraints are phonotactic: **ONSET** requires every syllable to begin with a consonant; **NO-CODA** disfavors syllables that end in a consonant. These constraints capture genuine cross-linguistic tendencies — CV (consonant-vowel) syllables are the most universally preferred syllable type, found in every language, while CVC syllables and especially complex codas are restricted in many. But markedness isn't limited to syllable structure. There are markedness constraints against voiced obstruents in coda position (many languages devoice final consonants), against nasal vowels, against particular consonant clusters, against tones in certain positions. Each constraint represents a preference that human phonological grammars lean toward when not overridden by competing constraints.

The crucial interaction is with **faithfulness constraints** like MAX and DEP. Markedness constraints want to eliminate complex structures; faithfulness constraints want to preserve the input. When markedness dominates faithfulness, the language uses phonological processes to repair marked structures: vowel epenthesis to satisfy ONSET (inserting a vowel so that a word-initial vowel acquires a preceding consonant), final consonant deletion to satisfy NO-CODA, cluster simplification to satisfy onset complexity constraints. When faithfulness dominates markedness, marked structures surface intact — the input is preserved even though it violates phonological preferences. This is why marked structures exist in languages at all: they are licensed by high-ranked faithfulness.

What markedness theory explains that earlier rule-based accounts could not is the cross-linguistic asymmetry in phonological processes. Languages systematically simplify toward unmarked structures — they rarely introduce more complex structures through phonological processes. When a language undergoes sound change, the change almost always moves toward less marked structures when faithfulness constraints weaken, almost never toward more marked ones. This **directionality** of phonological change and variation is predicted by the architecture of OT with markedness constraints: the grammar is always pushing toward unmarked structures, and faithfulness is the only counterweight holding marked structures in place.
