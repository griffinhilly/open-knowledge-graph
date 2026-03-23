---
id: distributed-morphology
title: Distributed Morphology
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: morphology-syntax-interface
  type: hard
- id: inflectional-morphology
  type: hard
tags:
- morphology
- distributed
- syntax
stage: expert
status: draft
---

# Distributed Morphology

## Core Idea
Distributed Morphology treats morphological and syntactic structure as unified. Syntax builds complex structures with abstract morphosyntactic features; at the phonological interface, features are replaced with phonological exponents (affix forms). This explains morphological idiosyncrasy and suppletion (go/went), where different stems appear for the same feature bundle due to competition among available exponents.

## Questions

```yaml
- question: "In a Distributed Morphology analysis, why does English use 'went' rather than '*goed' as the past tense of 'go'?"
  type: multiple-choice
  options:
    - "Because 'go' and 'went' are stored as a linked pair in the lexicon, with a stipulated exception to regular past tense formation"
    - "Because the Vocabulary Item [PAST, √GO] → 'went' outcompetes [PAST] → '-ed' due to the specificity principle: a more specific VI takes priority"
    - "Because DM treats suppletion as phonological reduction that obscures the regular past tense morpheme"
    - "Because syntax cannot attach the '-ed' morpheme to monosyllabic verb roots"
  answer: 1
  explanation: "DM explains suppletion through Vocabulary Insertion: competing Vocabulary Items apply to feature bundles, and the most specific match wins. The VI [PAST, √GO] → 'went' matches both features, beating the default [PAST] → '-ed', which matches only one. This is not a lexical quirk or stored exception — it is a principled competition predicted by the same mechanism that handles all morphology. Option A is the Lexicalist account that DM explicitly rejects."

- question: "What does 'Late Insertion' mean in Distributed Morphology, and what problem does it solve?"
  type: multiple-choice
  options:
    - "Morphological affixes are inserted late in the surface phonological string, after all syntactic movement"
    - "Phonological form is assigned to abstract morphosyntactic features only after syntactic computation is complete, not pre-stored in a traditional lexicon"
    - "Vocabulary Items are inserted after semantic interpretation, ensuring meaning is not affected by phonological form"
    - "Inflectional morphology is acquired later in language development than derivational morphology"
  answer: 1
  explanation: "Late Insertion is the architectural claim that syntax operates on abstract, phonologically unspecified features — phonological material is only assigned at the morphophonological interface, after syntactic operations are done. This solves the problem of explaining how the same abstract feature (e.g., [PAST]) can receive different phonological exponents in different contexts (regular '-ed' vs. suppletive 'went') without pre-listing these as separate lexical entries."

- question: "In Distributed Morphology, words are assembled in the mental lexicon before being inserted into syntactic structures."
  type: true-false
  answer: false
  explanation: "This is the Lexicalist view, which DM explicitly rejects. DM claims there is no pre-syntactic lexicon in the traditional sense. Instead, syntax builds structures from abstract morphosyntactic features, and phonological form is inserted only afterward (Late Insertion). The three-list architecture (syntactic features, Vocabulary, Encyclopedia) replaces the lexicon, with no pre-built words entering syntax."

- question: "Distributed Morphology predicts that syncretism — when one phonological form expresses multiple distinct feature bundles — results from under-specification in Vocabulary Items."
  type: true-false
  answer: true
  explanation: "Syncretism is a natural prediction of DM's architecture. A Vocabulary Item that is under-specified (matching multiple feature contexts) will insert in all those contexts, producing the same phonological form for what are structurally distinct feature bundles. For example, a VI matching [PAST] without specifying person or number would appear wherever those features are absent. This is a unified account of a phenomenon that Lexicalism treats as coincidental formal identity."

- question: "How does DM's three-list architecture differ from the Lexicalist model, and what specific architectural feature does 'Late Insertion' contribute?"
  type: short-answer
  answer: "Lexicalism stores fully formed words (with their phonological form and meaning) in a pre-syntactic lexicon that feeds syntax. DM replaces this with three separate lists: (1) abstract morphosyntactic features manipulated by syntax, (2) the Vocabulary (mappings from feature bundles to phonological forms), and (3) the Encyclopedia (idiosyncratic, non-compositional meanings). Late Insertion means phonological form is assigned only after syntactic computation — syntax never sees phonological content, only abstract features. This allows the same derivation to produce different phonological outputs depending on context (enabling suppletion, syncretism) without pre-specifying exceptions in the lexicon."
  explanation: "The key shift is from a word-based to a feature-based architecture. By separating phonological realization from syntactic computation, DM can account for morphological idiosyncrasy through principled competition mechanisms rather than stipulated exceptions, and makes the unified prediction that morphological and syntactic complexity reflect the same underlying hierarchical feature structures."
```

## Explainer

Your prerequisites give you two foundations: an understanding of morphological structure (how words are built from morphemes) and a grasp of the morphology-syntax interface (whether morphology and syntax are the same or different systems). Traditional **Lexicalist** theories — the dominant view before Distributed Morphology — held that complex words are assembled in the **lexicon** (a mental dictionary), and these pre-built words are then inserted whole into syntactic structures. Syntax manipulates phrases; morphology builds words; the two are separate modules. **Distributed Morphology** (DM), developed by Halle and Marantz in 1993, attacks this separation directly. Its central claim: there is no lexicon in the traditional sense. Morphological structure is not built before syntax — it *is* syntax, applying the same hierarchical feature-combining operations to smaller units.

DM replaces the traditional lexicon with three distinct lists that operate at different stages of derivation. The **Syntactic features** (roots plus functional features like [PAST], [PLURAL], [NOMINATIVE]) are abstract, phonologically unspecified building blocks that syntax manipulates. The **Vocabulary** is a list of **Vocabulary Items (VIs)** — mappings from feature bundles to phonological forms (e.g., [PAST] → *-ed*). The **Encyclopedia** stores idiosyncratic, non-compositional meanings (e.g., *kick the bucket* means 'die', not 'kick a bucket'). The key architectural claim, called **Late Insertion**, is that phonological material is inserted *after* syntactic computation. Syntax works with abstract features; only at the morphophonological interface do those features receive phonological form. This is the inversion of the Lexicalist picture.

The power of DM becomes clearest in its account of morphological idiosyncrasy. Consider *go*: its past tense is *went*, not *goed*. A Lexicalist theory treats this as a lexical quirk — *go* and *went* are stored as separate entries linked by stipulation. DM provides a principled account. The syntactic derivation generates a structure with features [PAST, √GO]. At Vocabulary Insertion, rules apply in a **specificity hierarchy**: a Vocabulary Item matching more features takes priority over a less specific one. *went* is a VI that matches exactly [PAST, √GO], so it outcompetes the default past tense *-ed*, which matches [PAST] but not [√GO]. **Suppletion** is thus not a lexical quirk but a competition among Vocabulary Items, predicted by the same mechanism that handles regular morphology. The same logic explains irregular plurals (*mice*, not *mouses*) and irregular comparatives (*better*, not *gooder*).

DM makes strong empirical predictions beyond suppletion. It predicts **syncretism** — when one phonological form expresses multiple distinct feature bundles — as resulting from under-specification in Vocabulary Items (a single VI that matches multiple contexts). It predicts that morphological complexity reflects underlying syntactic structure. It also predicts that operations like **head movement** — roots moving to adjoin to functional heads — are syntactic movement, not morphological operations, unifying the two domains under one theory. Critics challenge whether DM's architecture is genuinely simpler than Lexicalist alternatives, or simply re-describes the same facts in different vocabulary. But as a research program, DM has been enormously productive, generating unified accounts of phenomena that Lexicalism treated as unrelated exceptions across dozens of typologically diverse languages.
