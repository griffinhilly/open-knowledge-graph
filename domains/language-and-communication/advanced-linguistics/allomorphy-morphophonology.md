---
id: allomorphy-morphophonology
title: Allomorphy and Morphophonological Processes
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: morpheme-types
  type: hard
- id: phonological-systems
  type: hard
tags:
- morphology
- allomorphy
- phonology
stage: expert
status: validated
---

# Allomorphy and Morphophonological Processes

## Core Idea
Allomorphy occurs when a single morpheme has multiple phonological realizations conditioned by phonological, morphological, or lexical context, as in English plurals (/s/, /z/, /əz/) or past-tense -ed. Understanding allomorphy integrates phonological rules, morphological structure, and lexical exceptions.

## How It's Best Learned
Catalog allomorphs in a language and determine conditioning factors (environment, morpheme class, lexical listing); distinguish regular rule-governed allomorphy from suppletive forms.

## Common Misconceptions
Allomorphy is not disorder but systematic variation; even exceptions often follow phonological principles and are learned as indexed to specific morphological contexts.

## Questions

```yaml
- question: "The English words 'cats,' 'dogs,' and 'buses' end with the sounds /s/, /z/, and /əz/ respectively. From the perspective of morphological analysis, these three sounds are best described as..."
  type: multiple-choice
  options:
    - "Three different plural morphemes, each assigned to different noun classes"
    - "Three allomorphs of a single plural morpheme, conditioned by the phonological context of the stem"
    - "Free variation — English speakers choose arbitrarily among /s/, /z/, and /əz/"
    - "Two distinct morphemes: a regular plural and a sibilant-harmony plural"
  answer: 1
  explanation: "All three are realizations of the same underlying plural morpheme. The distribution is fully predictable: /əz/ follows sibilants (to avoid two adjacent sibilants), /s/ follows other voiceless consonants (voicing assimilation), and /z/ follows voiced sounds and vowels (the default voiced form). Because the allomorph choice is determined by phonological context, these are phonologically conditioned allomorphs of a single morpheme — not separate morphemes or free variants."

- question: "A student notices that the past tense of 'go' is 'went,' sharing no phonological material with the base form. This is an example of which morphological phenomenon?"
  type: multiple-choice
  options:
    - "Phonologically conditioned allomorphy, because the verb class determines the ending"
    - "Regular morphological alternation triggered by a following vowel"
    - "Suppletive allomorphy, where the allomorphs share no phonological relationship and must be stored in the lexicon"
    - "Zero morphology, because no suffix is added to create the past tense"
  answer: 2
  explanation: "Suppletion is the term for paradigm alternations where forms share no phonological resemblance — the relationship is purely lexical and must be memorized. 'Went' shares nothing phonological with 'go'; compare this with phonologically conditioned allomorphy (like plural /s/ vs. /z/), where the rule is derivable from the phonological context. High-frequency forms in natural languages frequently develop suppletive paradigms because they get memorized as whole-form entries rather than computed rule-by-rule."

- question: "Allomorphy is phonological disorder — different forms of the same morpheme vary unpredictably depending on dialect or speaker preference."
  type: true-false
  answer: false
  explanation: "Allomorphy is systematic, not disordered. Phonologically conditioned allomorphy is fully predictable from the phonological environment and applies consistently across all speakers of a language. Even morphologically or lexically conditioned allomorphy (like English strong verbs) follows class-level patterns — the sing/sang/sung pattern applies to a whole set of verbs (ring/rang/rung, swim/swam/swum). Only suppletive forms are idiosyncratic, but even these are uniformly shared across speakers."

- question: "The allomorph selected for a phonologically conditioned morpheme is determined by properties of the adjacent sounds, not by arbitrary lexical indexing."
  type: true-false
  answer: true
  explanation: "Phonological conditioning means the allomorph distribution follows a sound-based rule: /s/ vs. /z/ in English plurals is determined by the voicing of the stem's final consonant, and /əz/ is triggered by sibilant consonants. These rules operate on phonological features (voiced/voiceless, sibilant/non-sibilant), not on memorized word-by-word lists. This is what distinguishes phonological conditioning from lexical conditioning, where the choice must be remembered per-lexeme (as with irregular plurals like 'ox/oxen')."

- question: "Why must suppletive allomorphs be stored individually in the lexicon rather than derived by phonological rule, and what does this reveal about the organization of linguistic knowledge?"
  type: short-answer
  answer: "Suppletive allomorphs (e.g., go/went, good/better) share no phonological material, so no rule could derive one from the other. A phonological rule maps one sound sequence to another predictably; suppletion has no predictable input-output mapping. Linguists conclude these forms are stored as separate lexical entries linked by paradigmatic relationships, not computed at the time of use. This reveals that linguistic knowledge includes both rule-governed productivity (applied online) and stored exceptions (indexed to specific items)."
  explanation: "The concentration of suppletion in high-frequency items is a cross-linguistic universal: frequent forms get memorized directly because retrieval is more efficient than rule application for items accessed thousands of times. The distinction between 'rule' and 'list' is central to generative morphological theory and reflects the dual architecture of language processing."
```

## Explainer

From your study of morpheme types, you know that morphemes are the minimal units of meaning or grammatical function — roots like *dog*, prefixes like *un-*, suffixes like *-ed*. From phonological systems, you know that sounds are organized into abstract categories (phonemes) that have predictable realizations depending on their sound environment. **Allomorphy** is where morphology and phonology collide: a single underlying morpheme can surface with different phonological shapes depending on context, and understanding those shapes requires both kinds of knowledge at once.

The English plural morpheme is the canonical example. We write it consistently as *-s*, but listen carefully: *cats* ends in /s/, *dogs* ends in /z/, and *buses* ends in /əz/. These are three distinct phonological forms — **allomorphs** — of the same morpheme. The conditioning is phonological: /s/ follows voiceless consonants (/t/ in *cat*), /z/ follows voiced sounds (/g/ in *dog* and all vowels), and /əz/ follows sibilant sounds (/s/, /z/, /ʃ/, /ʒ/, /tʃ/, /dʒ/) because two sibilants cannot be adjacent without a buffer vowel. This is **phonologically conditioned allomorphy**: the same distributional logic applies to the third-person singular -*s* (*walks/runs/pushes*) and the possessive -*'s*. Once you see the rule, three "different" endings collapse into one underlying morpheme with predictable surface shapes.

Not all allomorphy is this tidy. **Suppletive allomorphy** is the linguist's term for cases where the allomorphs share no phonological resemblance at all — they are simply learned as exceptions. *Go/went* is the English past tense with maximum suppletivity: nothing in the form of *went* is derivable from *go* by phonological rule. Similarly, *good/better/best* and *bad/worse/worst* show suppletive comparison. These forms must be stored in the lexicon as irregular paradigm entries, not derived by rule. Suppletive allomorphy is common cross-linguistically in high-frequency items, which fits with what we know about memory: frequent forms get memorized directly rather than computed.

Between rule-governed allomorphy and full suppletion lies a middle ground of **morphologically or lexically conditioned** variation. The English past tense -*ed* surfaces as /t/, /d/, or /əd/ (the same voicing logic as the plural), but some verbs take "strong" or irregular pasts (*sing/sang*, *drive/drove*) indexed to specific lexical classes inherited from Germanic. The theoretical debate is whether to capture these with abstract morphophonological rules (treating vowel alternations as triggered by an underlying abstract morpheme) or to list them as stored alternations. Modern approaches generally use **Optimality Theory** or similar constraint-based frameworks to handle the interaction between phonological well-formedness and morphological faithfulness, weighting constraints differently across languages to generate the observed patterns.

