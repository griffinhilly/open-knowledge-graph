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

## Questions

```yaml
- question: "In Language X, stress always falls on the final syllable regardless of syllable weight. In Language Y, stress falls on a heavy penultimate syllable if one exists, otherwise on the final syllable. What is the key formal difference between these systems?"
  type: multiple-choice
  options:
    - "Language X uses iambic feet; Language Y uses trochaic feet"
    - "Language X is quantity-insensitive; Language Y is quantity-sensitive"
    - "Language X builds feet right-to-left; Language Y builds feet left-to-right"
    - "Language X lacks metrical grids; Language Y uses grid representations"
  answer: 1
  explanation: "Quantity sensitivity is the property by which syllable weight — whether a syllable has a long vowel or a coda consonant — affects stress placement. Language X ignores weight entirely (quantity-insensitive), applying a simple positional rule. Language Y uses weight to override the default positional rule when a heavy syllable is present (quantity-sensitive). This is independent of foot shape (trochaic vs. iambic) or directionality, which are separate parameters of the formal system."

- question: "English 'thirtéen' has stress on the second syllable in isolation. In the phrase 'thírteen mén,' the stress shifts to the first syllable of 'thirteen.' What principle explains this shift?"
  type: multiple-choice
  options:
    - "The word 'thirteen' has two stress placements and the speaker chooses based on conversational emphasis"
    - "The foot structure of 'thirteen' is permanently re-analyzed when it appears before monosyllabic words"
    - "The shift avoids a stress clash between two adjacent prominent syllables ('teen' and 'men')"
    - "Monosyllabic words always attract stress from preceding polysyllables"
  answer: 2
  explanation: "The Rhythmic Rule in metrical grid theory resolves stress clashes — two adjacent prominent syllables — by shifting one stress away. 'Thirtéen' + 'mén' would place heavy stress on 'teen' and 'men' in sequence; the grid operation moves 'teen's prominence leftward to 'thir,' creating the alternating rhythm 'thírteen mén.' This shows that stress is not a static property of individual words but is subject to phrasal adjustment governed by grid operations."

- question: "In formal metrical theory, specifying foot type (trochaic vs. iambic) and directionality (left-to-right vs. right-to-left) is sufficient to predict all stress patterns in any language."
  type: true-false
  answer: false
  explanation: "Many languages require a third parameter: quantity sensitivity. In a quantity-sensitive language, heavy syllables (those with long vowels or coda consonants) attract stress even when positional rules would place it elsewhere. Classical Latin and Arabic are examples. Without quantity sensitivity as a formal parameter, the analysis cannot account for stress patterns that respond to syllable weight. Foot type and directionality together describe the default rhythmic grouping, but they cannot capture weight effects."

- question: "Stress assignment rules in formal metrical phonology can predict where stress falls in words a speaker has never heard before, because the rules apply systematically to the phonological structure of the word."
  type: true-false
  answer: true
  explanation: "This is the key advantage of formal metrical analysis over purely memorized lexical stress. Because stress is derived from parameters (foot type, directionality, quantity sensitivity) applied to the syllable structure of any input, a native speaker's grammar can assign stress to novel words — as shown by experimental studies with nonsense words. The formal system is generative: it produces the correct stress assignment for any new phonological input that fits the language's syllable template."

- question: "What is quantity sensitivity in stress assignment, and why does it require syllable structure as a prerequisite concept?"
  type: short-answer
  answer: "Quantity sensitivity is the property of a stress system in which heavy syllables — those with a long vowel or a coda consonant — attract stress, sometimes overriding positional defaults. It requires syllable structure as a prerequisite because heaviness is determined by the internal organization of the syllable's rhyme: a syllable is heavy if its rhyme branches (contains a long vowel or closes with a consonant). Without knowing how to parse a word into syllables and identify their rhyme constituents, the analyst cannot determine which syllables are heavy and thus cannot apply the weight-sensitive stress rule."
  explanation: "The logic is that syllable weight is a structural property, not a surface feature. You cannot determine weight just from looking at phonemes in sequence — you must first parse them into syllables, then analyze the rhyme of each syllable. This is why syllable structure is listed as a prerequisite for formal stress models: the weight calculation that drives quantity-sensitive stress assignment takes syllable structure as its input."
```

## Explainer

From metrical phonology, you know that **stress** is not random — languages organize syllables into rhythmic groups, and certain syllables are prominent relative to others. From syllable structure, you know that syllables differ in their internal organization: some have **heavy** rhymes (a long vowel or a coda consonant), others are **light** (a short vowel with no coda). Formal models of stress take these intuitions and make them precise enough to predict, with considerable accuracy, where stress falls in any word — including words a speaker has never encountered before.

The core unit is the **foot**: a small rhythmic grouping, typically of two syllables, organized around a strong-weak or weak-strong contrast. English is primarily **trochaic**: feet are (strong-weak), so "HAPpy" is a single foot with stress on the first syllable, and "amAZing" parses as a weak syllable followed by a stressed foot [(a)(MAZ-ing)]. Languages differ in foot type — some are iambic (weak-strong), producing a different characteristic rhythm — and in **directionality**: does the language build feet left-to-right across the word, or right-to-left? The formal analysis specifies the foot inventory, foot-headedness (which syllable within the foot is strong), and directionality, and from these parameters it derives the stress pattern of any word in the language.

**Quantity sensitivity** adds a second dimension. In many languages, a heavy syllable — one with a long vowel or a coda consonant — attracts stress because it is intrinsically more prominent. Classical Arabic and Latin are quantity-sensitive: a penultimate syllable with a long vowel takes stress even when the default positional pattern would place it elsewhere. The formal analysis captures this with a weight condition requiring that feet be headed by heavy syllables when possible. This is why syllable structure is a prerequisite: the weight of a syllable is a function of its rhyme, and you cannot calculate weight without knowing internal syllable organization.

**Metrical grids** offer a complementary representation. A grid displays syllables as columns of marks, with taller columns indicating greater prominence: primary stress has the tallest column, secondary stress an intermediate one, unstressed syllables only one mark. Grid operations like the **Rhythmic Rule** shift stress to avoid **clashes** (two adjacent prominent syllables) or **lapses** (long stretches without prominence). In English, "thirtéen" has stress on the second syllable in isolation, but in "thírteen mén," it may shift to the first syllable to avoid a clash with the stressed "men." Together, feet and grids give phonologists a formal language for predicting and explaining stress patterns systematically — including the rhythmic adjustments that occur at the level of phrases and sentences, not just individual words.
