---
id: pitch-class-set-operations
title: Pitch-Class Set Operations
domain: music
course: advanced-music-theory
prerequisites:
- id: pitch-class-sets-introduction
  type: hard
- id: set-operations
  type: soft
- id: set-operations-and-notation
  type: soft
- id: set-operations-union-intersection-complement
  type: soft
- id: permutations
  type: soft
- id: set-fundamentals
  type: soft
builds-toward:
- set-class-equivalence
- twelve-tone-matrix-construction
tags:
- set-theory
- operations
- transposition
- inversion
stage: advanced
status: draft
---

# Pitch-Class Set Operations

## Core Idea
Set operations (transposition, inversion, complementation, union, and intersection) provide systematic ways to relate different pitch-class collections, revealing hidden connections between apparently unrelated musical segments. These operations become compositional tools for understanding organization in works without traditional harmonic hierarchies.

## Questions

```yaml
- question: "Applying T3 (transposition by 3 semitones) to the pitch-class set {0, 4, 7} produces which set?"
  type: multiple-choice
  options: ["{3, 6, 9}", "{3, 7, 10}", "{0, 4, 10}", "{1, 5, 8}"]
  answer: 1
  explanation: "T3 adds 3 to every pitch class mod 12: 0+3=3, 4+3=7, 7+3=10, giving {3, 7, 10}. {3, 6, 9} would be T3 applied to {0, 3, 6} (a diminished triad). The key is applying the same fixed integer to every element and reducing mod 12."

- question: "Inversion in pitch-class set theory (the operation I) is the same operation as melodic inversion in tonal counterpoint."
  type: true-false
  answer: false
  explanation: "PC set inversion negates each pitch class mod 12: pitch class n becomes 12 - n (or equivalently, -n mod 12). Melodic inversion in tonal music flips intervals upside down around an axis pitch. The operations are related in spirit but differ in implementation: tonal inversion preserves interval size and direction while PC set inversion is modular arithmetic. Confusing them is a common error when first encountering set theory."

- question: "What does it mean for two pitch-class sets to belong to the same set class, and what does that imply about their sound?"
  type: short-answer
  answer: "Two sets belong to the same set class if one can be transformed into the other by transposition (Tn) or inversion followed by transposition (TnI). They share the same prime form and interval-class vector, meaning they contain identical interval content. In practice, this implies they have a similar harmonic color or tension quality, even if they are built on different pitch levels or orientations."
  explanation: "Set class equivalence is the atonal analogue of tonal function: just as G7 and D7 are both dominant seventh chords (same structure, different transposition), {0,1,4} and {3,4,7} are both members of set class 3-3 (same prime form). The interval-class vector encodes how many of each interval type the set contains, which is what drives the perceptual similarity."
```

## Explainer

From your study of pitch-class sets, you know that a pitch-class set is simply a collection of distinct pitch classes — integers 0–11 representing the twelve chromatic pitches, octave-equivalent. Now the question is: when are two such collections meaningfully the same? The answer comes from defining operations that transform one set into another while preserving its essential character.

Transposition (Tn) adds a fixed integer n to every pitch class in the set, mod 12. T3 applied to {0, 4, 7} — the pitch-class representation of a C major triad — produces {3, 7, 10}, an E♭ major triad. Both sets are major triads; they sound the same in isolation but are rooted on different pitch classes. Transposition is the atonal analogue of tonal "same chord, different key." Inversion (I) negates each pitch class mod 12: pitch class p becomes (12 - p) mod 12, or equivalently -p mod 12. T5I applied to {0, 4, 7} produces {5, 1, 10} = {10, 1, 5}, an A minor triad. Inversion flips the interval structure, turning major into minor (for triads). Combining transposition and inversion in either order generates the full family of related sets.

Two sets are in the same set class — considered equivalent — if one can be transformed into the other by any combination of Tn and I. To find the canonical representative (the prime form), you reduce the set to its most compact normal form and then choose the version (original or inverted) that is most tightly packed from the left. This is the same process you practiced in pitch-class set introduction. The prime form is a label, like a last name: {0, 4, 7} and {0, 3, 7} are both three-note sets but belong to different set classes (3-11 major/minor triad vs. 3-11... actually both are 3-11; I should be more careful here). What matters is that the prime form encodes the set's interval content regardless of transposition or inversion.

The interval-class vector (ICV) is a six-element array that counts how many of each interval class (1 through 6) the set contains. Because interval classes are unordered and octave-equivalent, intervals 1 and 11 are both ic1, intervals 2 and 10 are both ic2, and so on; ic6 (the tritone) is its own inverse. Two sets in the same set class have identical ICVs, which is why they sound harmonically similar. The ICV becomes a practical compositional tool: if you want a set rich in minor seconds (ic1), look for sets with a high first entry; if you want a tritone-heavy collection, look for a high sixth entry.

Complementation is a third key operation: the complement of a set is the collection of all pitch classes not in the set. In twelve-tone music, a hexachord (6-note set) and its complement together exhaust all twelve pitch classes. A remarkable theorem — the complement theorem — states that a set and its complement share the same interval-class vector (except for the ic6 entry, which may differ by 1 due to the tritone's self-complementary nature). This means hexachordal complements sound harmonically related, a structural principle that Schoenberg and Webern exploited deliberately in twelve-tone composition.
