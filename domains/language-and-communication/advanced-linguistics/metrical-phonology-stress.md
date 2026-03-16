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
stage: advanced
status: draft
---

# Metrical Phonology and Stress Systems

## Core Idea
Metrical phonology models stress via hierarchical tree structures where syllables are grouped into metrical feet, and feet are grouped into prosodic words. Stress falls on metrically strong positions; variation in foot type (iambic vs. trochaic) and directionality (left vs. right) accounts for cross-linguistic stress patterns.

## How It's Best Learned
Map stress patterns in languages with fixed (Finnish, French) and bounded-variable (English, Spanish) stress rules; construct metrical trees and test predictions against exceptions.

## Common Misconceptions
Stress is not purely acoustic prominence; metrically weak syllables can be acoustically prominent if carrying other prosodic features (tone, duration).

## Explainer

From your work on suprasegmental phonology you know that stress is a property of syllables — a marking of relative prominence within a prosodic domain — and that it interacts with tone, length, and rhythm. From constraint ranking (OT) you know that phonological patterns can be analyzed as the optimal satisfaction of competing constraints. Metrical phonology adds a crucial structural layer: stress is not just assigned to individual syllables arbitrarily, but emerges from **grouping syllables into hierarchical constituents** called feet.

The basic unit is the **metrical foot**: a grouping of two (or sometimes three) syllables into a strong-weak or weak-strong pattern. A **trochee** is strong-weak (English *butter*, *doctor*); an **iamb** is weak-strong (English *above*, *begin*). Languages differ in which foot type they predominantly use — this is the **foot typology parameter**. They also differ in whether footing begins from the left edge or the right edge of the word — this is **directionality**. Finnish stress is fixed on the first syllable (leftmost trochee wins); French stress is fixed on the final syllable (rightmost foot wins); English stress is bounded and quantity-sensitive — the position of stress depends on whether syllables are heavy (containing long vowels or codas) or light, with heavy syllables attracting stress. These parameters together generate a surprisingly large proportion of the stress patterns attested cross-linguistically.

The hierarchical structure extends above the foot. Feet are grouped into **prosodic words** (ω), which are grouped into **phonological phrases** (φ), which are grouped into **intonation phrases** (ι). At each level, one constituent is metrically **strong** and the others are weak — producing the nested structure that gives sentences their rhythmic shape. This is why English has primary stress, secondary stress, and unstressed syllables: primary stress is the head of the prosodic word, secondary stress marks subsidiary foot heads. The word *còmpensàtion* has secondary stress on the first syllable and primary stress on the third because two feet are built, the second of which is the prosodic word head.

The connection to constraint ranking is direct: many metrical phenomena that look like rule exceptions can be reanalyzed as constraint interactions. The **ALIGN** constraints (align the left/right edge of a foot with the left/right edge of the word) interact with **PARSE-σ** (every syllable must be parsed into a foot) and **FOOT-FORM** (feet must be the dominant type) to produce language-specific patterns without language-specific rules. This is one of the most successful applications of Optimality Theory — the shift from derivational rules ("build a trochee from the left") to ranked constraint satisfaction ("prefer left-alignment when it doesn't violate higher constraints") explains not just the attested patterns but also which violations are tolerated and in what order of priority. Working through a few languages' stress systems in OT tableaux will solidify your understanding of how metrical and constraint-based analyses converge.
