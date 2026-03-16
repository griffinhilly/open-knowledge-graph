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
stage: advanced
status: draft
---

# Distributed Morphology

## Core Idea
Distributed Morphology treats morphological and syntactic structure as unified. Syntax builds complex structures with abstract morphosyntactic features; at the phonological interface, features are replaced with phonological exponents (affix forms). This explains morphological idiosyncrasy and suppletion (go/went), where different stems appear for the same feature bundle due to competition among available exponents.

## Explainer

Your prerequisites give you two foundations: an understanding of morphological structure (how words are built from morphemes) and a grasp of the morphology-syntax interface (whether morphology and syntax are the same or different systems). Traditional **Lexicalist** theories — the dominant view before Distributed Morphology — held that complex words are assembled in the **lexicon** (a mental dictionary), and these pre-built words are then inserted whole into syntactic structures. Syntax manipulates phrases; morphology builds words; the two are separate modules. **Distributed Morphology** (DM), developed by Halle and Marantz in 1993, attacks this separation directly. Its central claim: there is no lexicon in the traditional sense. Morphological structure is not built before syntax — it *is* syntax, applying the same hierarchical feature-combining operations to smaller units.

DM replaces the traditional lexicon with three distinct lists that operate at different stages of derivation. The **Syntactic features** (roots plus functional features like [PAST], [PLURAL], [NOMINATIVE]) are abstract, phonologically unspecified building blocks that syntax manipulates. The **Vocabulary** is a list of **Vocabulary Items (VIs)** — mappings from feature bundles to phonological forms (e.g., [PAST] → *-ed*). The **Encyclopedia** stores idiosyncratic, non-compositional meanings (e.g., *kick the bucket* means 'die', not 'kick a bucket'). The key architectural claim, called **Late Insertion**, is that phonological material is inserted *after* syntactic computation. Syntax works with abstract features; only at the morphophonological interface do those features receive phonological form. This is the inversion of the Lexicalist picture.

The power of DM becomes clearest in its account of morphological idiosyncrasy. Consider *go*: its past tense is *went*, not *goed*. A Lexicalist theory treats this as a lexical quirk — *go* and *went* are stored as separate entries linked by stipulation. DM provides a principled account. The syntactic derivation generates a structure with features [PAST, √GO]. At Vocabulary Insertion, rules apply in a **specificity hierarchy**: a Vocabulary Item matching more features takes priority over a less specific one. *went* is a VI that matches exactly [PAST, √GO], so it outcompetes the default past tense *-ed*, which matches [PAST] but not [√GO]. **Suppletion** is thus not a lexical quirk but a competition among Vocabulary Items, predicted by the same mechanism that handles regular morphology. The same logic explains irregular plurals (*mice*, not *mouses*) and irregular comparatives (*better*, not *gooder*).

DM makes strong empirical predictions beyond suppletion. It predicts **syncretism** — when one phonological form expresses multiple distinct feature bundles — as resulting from under-specification in Vocabulary Items (a single VI that matches multiple contexts). It predicts that morphological complexity reflects underlying syntactic structure. It also predicts that operations like **head movement** — roots moving to adjoin to functional heads — are syntactic movement, not morphological operations, unifying the two domains under one theory. Critics challenge whether DM's architecture is genuinely simpler than Lexicalist alternatives, or simply re-describes the same facts in different vocabulary. But as a research program, DM has been enormously productive, generating unified accounts of phenomena that Lexicalism treated as unrelated exceptions across dozens of typologically diverse languages.
