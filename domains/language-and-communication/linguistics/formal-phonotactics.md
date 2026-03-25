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
- id: morpheme-structure-constraints
  type: soft
builds-toward:
- constraint-based-phonology-formal
tags:
- phonology
- constraints
- formalism
stage: advanced
status: validated
---
# Formal Phonotactics: Constraints on Sound Sequences

## Core Idea
Phonotactic constraints formally specify which sound sequences are permissible in a language (e.g., onset clusters must satisfy sonority sequencing). These constraints can be expressed as formal rules, forbidden structures, or ranked preferences (in Optimality Theory).

## Questions

```yaml
- question: "Standard German devoices obstruents in coda position (e.g., /d/ → [t] in word-final position), while English does not. How does Optimality Theory account for this cross-linguistic difference?"
  type: multiple-choice
  options:
    - "German has a phonotactic rule banning voiced codas that English simply lacks; the two languages have different rule inventories"
    - "Both languages have the same universal constraints — *VOICED-CODA and IDENT-VOICE — but German ranks *VOICED-CODA above IDENT-VOICE, while English ranks IDENT-VOICE above *VOICED-CODA"
    - "German acquired this pattern through historical sound change; OT explains synchronic patterns but not diachronic ones"
    - "The difference is phonetic rather than phonological — German speakers physically cannot produce voiced coda consonants"
  answer: 1
  explanation: "This is the core explanatory power of Optimality Theory. Rather than stipulating a language-specific rule for German ('delete voicing in coda'), OT proposes that both *VOICED-CODA (a markedness constraint against voiced coda obstruents) and IDENT-VOICE (a faithfulness constraint preserving underlying voicing) are part of the universal constraint set. In German, *VOICED-CODA outranks IDENT-VOICE, so the grammar tolerates a surface change to satisfy the higher-ranked constraint. In English, IDENT-VOICE outranks *VOICED-CODA, so underlying voicing is preserved. Same constraints, different rankings — same architecture generates different language-specific patterns."

- question: "The onset cluster /lp-/ (as in a hypothetical word beginning with /lpa.../) is unattested as a native-language onset in most languages. What does the Sonority Sequencing Principle predict about this cluster, and why?"
  type: multiple-choice
  options:
    - "It is well-formed because both /l/ and /p/ are consonants — SSP only restricts vowel-consonant sequences"
    - "It violates SSP because sonority decreases from /l/ (high sonority lateral) to /p/ (low sonority stop); SSP requires sonority to rise toward the nucleus"
    - "It is acceptable under SSP but banned by a separate constraint on place of articulation"
    - "SSP predicts it should be well-formed in languages with complex onsets, like English"
  answer: 1
  explanation: "The Sonority Sequencing Principle requires that sonority increase as you move from the onset periphery toward the syllable nucleus. /l/ has higher sonority than /p/ — laterals are more open and louder than stops. An onset /lp-/ starts high-sonority and moves to low-sonority, violating SSP. The reverse cluster /pl-/ (stop → lateral → vowel) is well-formed because sonority rises toward the nucleus. This constraint is formalizable over feature matrices: any segment sequence in an onset where sonority decreases toward the nucleus is ruled out, capturing a near-universal pattern without stipulating it language by language."

- question: "In Optimality Theory, the constraint *VOICED-CODA (no voiced obstruents in coda position) is a universal constraint — it exists in the grammar of every language, including English."
  type: true-false
  answer: true
  explanation: "OT's key claim is that the constraint set is universal: every constraint exists in every language's grammar. What differs between languages is the *ranking* of those constraints, not their presence or absence. In English, the faithfulness constraint IDENT-VOICE outranks *VOICED-CODA, so voiced codas are tolerated. But *VOICED-CODA is still in the English grammar — it is simply outranked. When constraints are equally ranked or when there is no conflicting faithfulness constraint, even low-ranked markedness constraints can influence outputs. This universality is the theoretically distinctive claim of OT and allows it to capture implicational universals across languages."

- question: "The Sonority Sequencing Principle is a language-specific rule that each language may choose to apply, modify, or ignore."
  type: true-false
  answer: false
  explanation: "The SSP is proposed as a *phonological universal* — a constraint that appears in all languages' grammars and reflects a universal auditory or articulatory preference for sonority profiles that rise toward the nucleus. Individual languages may have additional constraints (permitting or banning specific clusters), and some specific cluster types (like the /s/ + stop onset in English, which violates strict SSP) are attested exceptions. But the SSP is not a language-particular stipulation — it is a universal constraint that individual grammars instantiate with varying strictness. In OT terms, it is in every grammar; what varies is how it interacts with other constraints."

- question: "How does Optimality Theory explain cross-linguistic variation in phonotactics without writing a different rule set for each language?"
  type: short-answer
  answer: "OT proposes a universal set of constraints shared by all languages — both markedness constraints (e.g., *VOICED-CODA, *COMPLEX-ONSET) and faithfulness constraints (e.g., IDENT-VOICE, MAX-IO). Cross-linguistic variation arises entirely from different rankings of these shared constraints. A language that bans voiced codas ranks *VOICED-CODA above IDENT-VOICE; a language that allows them ranks IDENT-VOICE higher. The grammar evaluates candidate output forms by comparing their violation profiles against the ranked constraints, selecting the candidate that best satisfies the highest-ranked constraints. Because the same universal constraints generate different patterns under different rankings, OT can account for typological variation with a single architecture — no language-specific rules required."
  explanation: "The explanatory power comes from the claim that what varies cross-linguistically is ranking, not inventory. This makes typological predictions: if language X bans structure A, it should also ban all structures that violate any constraint ranked above the one banning A. OT thus generates implicational universals — patterns across languages that follow from the constraint ranking logic — rather than treating each language as an arbitrary stipulation."
```

## Explainer

From feature matrices, you have a formal vocabulary for characterizing individual sounds — each phoneme is a bundle of binary features like [±voice], [±nasal], [±sonorant]. Formal phonotactics lifts this analysis to the level of *sequences*: given a set of segment feature specifications, which sequences are well-formed and which are prohibited? The answer varies by language, and capturing that variation formally is the central problem of phonotactic theory.

The **Sonority Sequencing Principle** (SSP) is the most studied phonotactic universal. Sonority — a scalar property roughly tracking loudness and openness — rises toward the syllable nucleus and falls away from it. In the onset cluster /spl-/ (as in "splash"), sonority increases: /s/ is a fricative (low sonority), /p/ is a stop (slightly lower, actually violating strict SSP — the /s/ + stop cluster is an attested exception cross-linguistically), /l/ is a lateral (high sonority), and the vowel is highest. The formal statement of SSP can be expressed as a rule over sonority indices or, equivalently, as a constraint on feature matrices. Any onset cluster where sonority decreases rather than increases (e.g., *[lp-]) is ruled out. This constraint is not stipulated arbitrarily for each language — it is a formal universal that individual grammars refine or occasionally violate.

**Forbidden structure rules** state phonotactic restrictions in negative terms: no onset cluster of the form [+sonorant][−sonorant], no coda of the form [+voice], and so on. These can be written as constraints over feature matrices using the formalism you already know. A rule that bans voiced obstruents in coda position (a real restriction in Standard German) is expressed as: *C[−sonorant, +voice] in coda. Every surface form of the language is checked against this constraint; any form that violates it is either blocked or repaired.

**Optimality Theory** (OT) reframes this logic. Rather than stating inviolable rules, OT posits a universal set of ranked constraints. The candidate output that best satisfies the highest-ranked constraints (incurring fewest violations of the most important ones) is the winner. A language that allows voiced coda obstruents simply ranks the IDENT-VOICE faithfulness constraint above *VOICED-CODA; a language that devoices them ranks the markedness constraint higher. This allows formal phonotactics to capture cross-linguistic variation without writing different rule sets for each language — the architecture is universal, and language-specific orderings generate language-specific patterns. Your transition to constraint-based phonology formalism will generalize this ranking logic to broader phenomena beyond the syllable.
