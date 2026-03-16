---
id: autosegmental-phonology
title: Autosegmental Phonology
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: phonological-features
  type: hard
- id: suprasegmental-phonology
  type: hard
tags:
- phonology
- autosegmental
- features
stage: advanced
status: draft
---

# Autosegmental Phonology

## Core Idea
Autosegmental phonology represents segments as bundles of features organized on parallel, independent tiers, allowing features to behave independently of segment boundaries. This framework elegantly explains tone spreading, vowel harmony, and geminate consonants that resist linear representation.

## How It's Best Learned
Draw autosegmental representations for tone and harmony systems in African and Finno-Ugric languages; test how features spread across segment boundaries.

## Common Misconceptions
Autosegmental tiers are not psychologically real; they are analytical abstractions that capture generalizations about feature behavior.

## Explainer

From your study of phonological features, you know that segments are not atomic units but bundles of distinctive features — [+voice], [-nasal], [+high], and so on. From suprasegmental phonology, you know that properties like tone, stress, and length operate over domains larger than individual segments. Autosegmental phonology is the theoretical framework that unifies these observations and resolves a fundamental problem with standard linear representations: why do some phonological properties behave as if they belong to the segment, while others spread, jump, or persist independently of what happens to individual segments?

The core problem that motivated autosegmental theory — developed by John Goldsmith in the mid-1970s — is **tone spreading** in African languages. In many Bantu languages, a high tone on one vowel spreads to neighboring vowels even when consonants (which are not toned) intervene. In a purely linear representation, each segment has its own tone specification, so spreading requires elaborate copying rules. More troubling: when a vowel is deleted, its tone often "survives" on the adjacent vowel — a ghost of the deleted segment. A linear model has no natural way to represent a tone that persists after its segment is gone. The autosegmental solution is simple and elegant: **tones are represented on a separate tier**, connected to segments by **association lines**, and the two tiers are governed by their own independent well-formedness conditions.

The key innovation is the **multi-tiered representation**. Instead of a single linear string of feature bundles, autosegmental phonology posits parallel tiers — a segmental tier, a tonal tier, a laryngeal tier, a place tier, and so on — each tier governed by its own constraints, connected to others through association lines. A single tonal specification can associate with multiple segments (producing tone spreading), or a single segment can associate with multiple tonal specifications (producing contour tones). The **Obligatory Contour Principle (OCP)** — the constraint that identical adjacent elements on any tier must be represented as a single unit — explains why the same tone rarely occurs twice in a row on the tonal tier: they merge into a single specification with dual association. This accounts for a surprising range of morphological and phonological patterns across languages.

**Vowel harmony** is the other phenomenon where autosegmental analysis earns its keep. In Finnish or Turkish, all vowels in a word must share the same value for a feature like [back] or [round] — back vowels trigger back vowels, front vowels trigger front vowels, across the whole word. Linearly, this requires a copying operation that must skip consonants and apply repeatedly. Autosegmentally, a single [+back] or [-back] specification on the vocalic tier simply associates with all vowels in the word — the harmony is just a single feature with a wide domain of association. **Geminate** consonants — doubly long segments that in many languages resist certain processes — are similarly handled as a single segment specification associated with two timing slots, explaining why processes that delete "one consonant" often leave a geminate intact.

What makes autosegmental phonology powerful is that it recasts phonological rules as operations on tiers and association lines, governed by universal constraints like the OCP and the prohibition on crossing association lines. This moves phonology from a set of language-particular rules to a constrained space of possible grammars. It was a major step toward the modular, constraint-based approach that later crystallized in Optimality Theory. The representations may be abstractions rather than cognitive reality, but they capture genuine generalizations about what phonological processes look like across the world's languages.


