---
id: stress-assignment-rules
title: Formal Models of Stress and Accent
domain: language-and-communication
course: linguistics
prerequisites:
- id: metrical-phonology-stress
  type: hard
- id: syllable-structure-prosody
  type: soft
builds-toward:
- intonational-phonology
tags:
- prosody
- stress
- metrical-theory
- accent
stage: advanced
status: draft
---

# Formal Models of Stress and Accent

## Core Idea
Metrical phonology formalizes stress assignment through hierarchically organized feet—binary-branching units of strong and weak syllables. Some languages assign stress by fixed position (always the final or penultimate syllable), while others by weight (heavy syllables attract stress) or syllable count. Metrical grids and trees predict primary and secondary stress locations.

## Explainer

From metrical phonology, you know that **stress** is not random — languages organize syllables into rhythmic groups, and certain syllables are prominent relative to others. From syllable structure, you know that syllables differ in their internal organization: some have **heavy** rhymes (a long vowel or a coda consonant), others are **light** (a short vowel with no coda). Formal models of stress take these intuitions and make them precise enough to predict, with considerable accuracy, where stress falls in any word — including words a speaker has never encountered before.

The core unit is the **foot**: a small rhythmic grouping, typically of two syllables, organized around a strong-weak or weak-strong contrast. English is primarily **trochaic**: feet are (strong-weak), so "HAPpy" is a single foot with stress on the first syllable, and "amAZing" parses as a weak syllable followed by a stressed foot [(a)(MAZ-ing)]. Languages differ in foot type — some are iambic (weak-strong), producing a different characteristic rhythm — and in **directionality**: does the language build feet left-to-right across the word, or right-to-left? The formal analysis specifies the foot inventory, foot-headedness (which syllable within the foot is strong), and directionality, and from these parameters it derives the stress pattern of any word in the language.

**Quantity sensitivity** adds a second dimension. In many languages, a heavy syllable — one with a long vowel or a coda consonant — attracts stress because it is intrinsically more prominent. Classical Arabic and Latin are quantity-sensitive: a penultimate syllable with a long vowel takes stress even when the default positional pattern would place it elsewhere. The formal analysis captures this with a weight condition requiring that feet be headed by heavy syllables when possible. This is why syllable structure is a prerequisite: the weight of a syllable is a function of its rhyme, and you cannot calculate weight without knowing internal syllable organization.

**Metrical grids** offer a complementary representation. A grid displays syllables as columns of marks, with taller columns indicating greater prominence: primary stress has the tallest column, secondary stress an intermediate one, unstressed syllables only one mark. Grid operations like the **Rhythmic Rule** shift stress to avoid **clashes** (two adjacent prominent syllables) or **lapses** (long stretches without prominence). In English, "thirtéen" has stress on the second syllable in isolation, but in "thírteen mén," it may shift to the first syllable to avoid a clash with the stressed "men." Together, feet and grids give phonologists a formal language for predicting and explaining stress patterns systematically — including the rhythmic adjustments that occur at the level of phrases and sentences, not just individual words.
