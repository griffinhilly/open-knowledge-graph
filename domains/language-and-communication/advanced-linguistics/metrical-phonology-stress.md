---
id: metrical-phonology-stress
title: Metrical Phonology and Stress Systems
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: suprasegmental-phonology
  type: hard
- id: constraint-ranking-phonology
  type: hard
tags:
- phonology
- stress
- metrical
stage: expert
status: validated
---

# Metrical Phonology and Stress Systems

## Core Idea
Metrical phonology models stress via hierarchical tree structures where syllables are grouped into metrical feet, and feet are grouped into prosodic words. Stress falls on metrically strong positions; variation in foot type (iambic vs. trochaic) and directionality (left vs. right) accounts for cross-linguistic stress patterns.

## How It's Best Learned
Map stress patterns in languages with fixed (Finnish, French) and bounded-variable (English, Spanish) stress rules; construct metrical trees and test predictions against exceptions.

## Common Misconceptions
Stress is not purely acoustic prominence; metrically weak syllables can be acoustically prominent if carrying other prosodic features (tone, duration).

## Questions

```yaml
- question: "English 'above' carries stress on the second syllable (a-BOVE). Which metrical foot type and directionality best accounts for this pattern?"
  type: multiple-choice
  options:
    - "A trochee (strong-weak) built from the left edge of the word"
    - "An iamb (weak-strong) built from the left edge of the word"
    - "A trochee built from the right edge of the word"
    - "Fixed stress assigned to the initial syllable regardless of foot structure"
  answer: 1
  explanation: "An iamb groups syllables as weak-strong, producing stress on the second element. Building it from the left gives the pattern (σ-STRESS) that places stress on 'BOVE.' A trochee from the left would yield (STRESS-σ), predicting stress on 'a-,' which is wrong. Finnish exemplifies that left-anchored trochee pattern (always first syllable). The foot type parameter — iambic vs. trochaic — is what distinguishes languages like English from languages like Finnish."

- question: "A language places primary stress on the first syllable of every word, regardless of syllable weight or word length. Which metrical characterization fits this pattern?"
  type: multiple-choice
  options:
    - "An iambic foot with right-to-left directionality"
    - "A trochaic foot with left-to-right directionality"
    - "A quantity-sensitive system that always promotes the heaviest syllable"
    - "An unbounded stress system with no consistent foot type"
  answer: 1
  explanation: "Building a trochee (strong-weak) starting from the left edge of the word always produces a foot whose strong node is the leftmost syllable — exactly what this language does. This is the Finnish pattern. Iambs from the right would predict final stress. Quantity-sensitive systems produce variable stress depending on syllable weight. The power of metrical parameters is that two choices — foot type and directionality — jointly predict which syllable bears stress across a huge range of languages."

- question: "In metrical phonology, a syllable occupying a metrically weak position within a foot can seldom be acoustically prominent."
  type: true-false
  answer: false
  explanation: "This is the key misconception flagged in the topic: metrical strength and acoustic prominence are not the same thing. A syllable in a weak metrical position can carry a lexical tone, be lengthened, or bear contrastive stress — all of which make it acoustically salient — without being the head of its foot. Metrical structure determines prominence *within the stress system*, but other prosodic features (tone, duration, emphasis) can render a weak syllable acoustically striking. The two dimensions are real but dissociable."

- question: "Stress placement in English depends partly on whether syllables are heavy (containing long vowels or codas) or light, making English a quantity-sensitive stress system."
  type: true-false
  answer: true
  explanation: "Unlike Finnish (fixed initial stress regardless of syllable content), English stress is sensitive to syllable weight. Heavy syllables tend to attract stress — compare 'aróma' (heavy penultimate) with 'édit' (light penultimate). The quantity-sensitivity parameter means you cannot predict English stress from position alone; you also need to know the weight profile of each syllable. This is why English stress seems irregular compared to languages with pure positional stress, and why metrical theory needs both the foot-type parameter and the quantity-sensitivity parameter to handle it."

- question: "Why do metrical phonologists argue that stress 'emerges from hierarchical structure' rather than being directly assigned to syllables?"
  type: short-answer
  answer: "Stress is relational: a syllable is stressed because it is the strong node of its foot, and the foot's head is the strong node of the prosodic word. This hierarchical account explains why words have primary stress, secondary stress, and unstressed syllables — they reflect distinct levels in the nested structure (syllable → foot → prosodic word → phonological phrase), not three separate kinds of marking applied independently. It also captures cross-linguistic variation economically: two parameters (foot type: trochee vs. iamb; directionality: left vs. right) predict a large portion of the world's stress patterns without needing language-specific rules for each language."
  explanation: "The hierarchical view has explanatory advantages over direct assignment. If stress were simply listed for each syllable independently, you would need separate stipulations for primary vs. secondary stress and could not explain why their relationship is systematic. The tree structure makes the relationships formal and predictable: primary stress is always the prosodic word's head, secondary stress marks subsidiary foot heads, and unstressed syllables are weak nodes at the foot level. This architecture also connects naturally to Optimality Theory, where ranked ALIGN and PARSE constraints determine which hierarchical structure wins."
```

## Explainer

From your work on suprasegmental phonology you know that stress is a property of syllables — a marking of relative prominence within a prosodic domain — and that it interacts with tone, length, and rhythm. From constraint ranking (OT) you know that phonological patterns can be analyzed as the optimal satisfaction of competing constraints. Metrical phonology adds a crucial structural layer: stress is not just assigned to individual syllables arbitrarily, but emerges from **grouping syllables into hierarchical constituents** called feet.

The basic unit is the **metrical foot**: a grouping of two (or sometimes three) syllables into a strong-weak or weak-strong pattern. A **trochee** is strong-weak (English *butter*, *doctor*); an **iamb** is weak-strong (English *above*, *begin*). Languages differ in which foot type they predominantly use — this is the **foot typology parameter**. They also differ in whether footing begins from the left edge or the right edge of the word — this is **directionality**. Finnish stress is fixed on the first syllable (leftmost trochee wins); French stress is fixed on the final syllable (rightmost foot wins); English stress is bounded and quantity-sensitive — the position of stress depends on whether syllables are heavy (containing long vowels or codas) or light, with heavy syllables attracting stress. These parameters together generate a surprisingly large proportion of the stress patterns attested cross-linguistically.

The hierarchical structure extends above the foot. Feet are grouped into **prosodic words** (ω), which are grouped into **phonological phrases** (φ), which are grouped into **intonation phrases** (ι). At each level, one constituent is metrically **strong** and the others are weak — producing the nested structure that gives sentences their rhythmic shape. This is why English has primary stress, secondary stress, and unstressed syllables: primary stress is the head of the prosodic word, secondary stress marks subsidiary foot heads. The word *còmpensàtion* has secondary stress on the first syllable and primary stress on the third because two feet are built, the second of which is the prosodic word head.

The connection to constraint ranking is direct: many metrical phenomena that look like rule exceptions can be reanalyzed as constraint interactions. The **ALIGN** constraints (align the left/right edge of a foot with the left/right edge of the word) interact with **PARSE-σ** (every syllable must be parsed into a foot) and **FOOT-FORM** (feet must be the dominant type) to produce language-specific patterns without language-specific rules. This is one of the most successful applications of Optimality Theory — the shift from derivational rules ("build a trochee from the left") to ranked constraint satisfaction ("prefer left-alignment when it doesn't violate higher constraints") explains not just the attested patterns but also which violations are tolerated and in what order of priority. Working through a few languages' stress systems in OT tableaux will solidify your understanding of how metrical and constraint-based analyses converge.
