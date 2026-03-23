---
id: schenkerian-analysis-fundamentals
title: Schenkerian Analysis Fundamentals
domain: music
course: advanced-music-theory
prerequisites:
- id: roman-numeral-analysis
  type: hard
- id: functional-harmony
  type: soft
builds-toward:
- ursatz-fundamental-structure
- schenkerian-levels-analysis
tags:
- analysis
- schenkerian
- structure
- reduction
stage: expert
status: draft
---

# Schenkerian Analysis Fundamentals

## Core Idea
Schenkerian analysis is a method of understanding how music achieves coherence through hierarchical levels of structure, where prolongation (the extension of a single harmony across measures or phrases) creates musical architecture. Unlike surface-level harmonic analysis, Schenkerian theory reveals the deep structure underlying complex works through systematic reduction.

## How It's Best Learned
Begin with simple binary or ternary form pieces, then progress to sonata movements. Work through multiple analyses of the same piece to compare reduction approaches. Use graphing software or colored pencils to make hierarchies visually clear.

## Common Misconceptions
- Schenkerian analysis is primarily about finding the 'correct' reduction rather than understanding structural relationships. - The Ursatz must appear literally in every piece. - Foreground details are irrelevant to structural analysis.

## Questions

```yaml
- question: "A Schenkerian analyst examines a 32-measure passage and says 'the entire passage prolongs tonic.' A Roman numeral analyst identifies IV, ii, V7, vi, IV, V, I chords within it. Which statement best reconciles these two analyses?"
  type: multiple-choice
  options:
    - "They contradict each other; if there are ii and vi chords present, the passage cannot be prolonging tonic"
    - "The Schenkerian analysis says the IV, ii, V7, vi, and IV chords are structurally subordinate elaborations of the I that governs the whole passage"
    - "The Roman numeral analyst made errors; prolonged passages must consist only of I chords"
    - "Both analyses describe the same level of structure in different notation systems"
  answer: 1
  explanation: "Schenkerian prolongation does not deny the existence of intermediate chords — it reinterprets their structural status. Roman numeral analysis treats every chord as equally meaningful; Schenkerian analysis asks which harmonies are *structurally fundamental* and which are *elaborations* of those fundamentals. To say 'the passage prolongs tonic' means the I at the beginning and the I at the end are the same structural harmony, and the IV, ii, V7, vi in between are delaying, embellishing, or decorating that tonic — passing or neighbor chords in a large-scale voice-leading motion, not structural harmonies of equal weight."

- question: "A student learning Schenkerian analysis decides to identify the Ursatz (background fundamental structure) directly, treating foreground details as irrelevant distractions. Why is this approach problematic?"
  type: multiple-choice
  options:
    - "It is not problematic; identifying the Ursatz is the only goal of Schenkerian analysis"
    - "The Ursatz cannot be identified without working through the foreground; reduction proceeds layer by layer from surface to background"
    - "Foreground details determine the key of the piece, which must be known before locating the Ursatz"
    - "The Ursatz only applies to sonata form, not to binary or ternary forms"
  answer: 1
  explanation: "Schenkerian analysis proceeds through hierarchical reduction: you begin with the foreground (actual notes), identify which are structural and which are passing/neighbor motions to produce a middleground, then reduce further to reach the background Ursatz. The foreground is not irrelevant — it is the starting material, and the hierarchical relationships between levels are the substance of the analysis. Skipping to the Ursatz without working through the reductions misses the analytical insight: how exactly does the foreground elaborate the middleground, and how does the middleground elaborate the background?"

- question: "In Schenkerian analysis, a V chord that appears between two tonic (I) chords could be analyzed as structurally subordinate to the surrounding tonic harmonies, depending on the level of analysis being considered."
  type: true-false
  answer: true
  explanation: "This is precisely the kind of reinterpretation that Schenkerian analysis enables. At the foreground level, the V is a separate chord; at the middleground level, it might function as a neighbor chord that temporarily destabilizes the tonic before resolving back — making the entire I–V–I pattern a tonic prolongation at that level. Whether a V is a structural harmony equal in weight to surrounding I chords, or a subordinate element in a larger prolongation, depends on the structural level being analyzed and on the melodic and voice-leading context."

- question: "The Ursatz (fundamental structure) in Schenkerian analysis must appear literally in the score — as explicit notes in the melody and bass — for the analysis to be valid."
  type: true-false
  answer: false
  explanation: "The Ursatz is an abstract background structure, not a literal musical passage that appears in the score. It is the skeleton that the entire piece elaborates through prolongation and voice-leading operations. The analyst derives it by successively reducing the foreground and middleground layers, stripping away elaborations until the underlying structural skeleton becomes visible. The Ursatz may never appear literally and simultaneously in the notation; it is inferred as the structural foundation — a theoretical construct describing the piece's deep coherence, not a theme hidden in the score."

- question: "What does 'prolongation' mean in Schenkerian analysis, and why is it the central concept of the theory?"
  type: short-answer
  answer: "Prolongation is the extension of a single harmony's structural influence across a span of music — measures, phrases, or an entire movement. When a harmony is 'prolonged,' all the notes and chords that occur during that span are understood as elaborating or delaying that harmony rather than as structurally independent events. For example, a tonic chord can be prolonged by neighbor chords, arpeggiation, passing chords, and apparent motion to other harmonies, as long as the tonic remains the governing structural reference point. Prolongation is central because it is the mechanism by which Schenkerian theory explains large-scale tonal coherence: a piece hangs together not because every chord is equally important, but because deeper structural harmonies govern extended spans of musical time, unifying surface variety into a single directed motion."
  explanation: "Without prolongation, Schenkerian analysis collapses into Roman numeral analysis — a list of chords without architectural meaning. Prolongation is what allows the theory to explain why a long movement feels like a unified whole rather than a sequence of disconnected harmonies. It is the tonal equivalent of grammatical constituency: individual chords are organized into prolongations that have higher-level meaning beyond their parts."
```

## Explainer

From Roman numeral analysis, you can label every chord in a piece: I, ii, V7, IV, and so on. This surface labeling is accurate but does not answer the question: which of these chords matter structurally, and which are subordinate elaborations? In a 32-measure chorale, if you count 87 Roman numerals, do they all have equal structural weight? Schenkerian analysis says no. Its central claim is that tonal music achieves coherence through **hierarchical levels** — some harmonies prolong and embellish more fundamental harmonies below the surface, and there is ultimately a single underlying structure (the **Ursatz**) that the entire piece elaborates.

The key concept is **prolongation**: the extension of a single harmony's influence across multiple measures, phrases, or even an entire movement. When you see a V chord followed by a measure of I⁶, then a passing V⁴₃, then I, then vi, then IV, then V, the Schenkerian reading might hear all of this as a prolonged tonic, with all intermediate chords as decorations of the I. The Roman numerals are all technically accurate, but they miss the forest for the trees. Prolongation says: the I at the start and the I at the end are the same structural harmony; everything in between delays the conclusion rather than replacing the tonic. This is the move from **foreground** (actual notes) to **middleground** (prolonged harmonies, voice-leading patterns that span multiple measures).

The **Ursatz** ("fundamental structure") is the background level — the skeleton underlying the entire piece. It has two components: the **Bassbrechung** (bass arpeggiation, typically I–V–I) and the **Urlinie** (fundamental melodic line, descending stepwise from scale degree 3, 5, or 8 down to 1). The Ursatz is not meant to appear literally in the score; it is the abstract structural skeleton that the entire foreground elaborates. Finding it requires working backward: reduce the foreground by identifying which notes are structural and which are passing, neighbor, or arpeggiating motions; then reduce the middleground by identifying which harmonies prolong more fundamental ones; at the background, only the Ursatz remains. This process is called **reduction**, and it is the analytical method: successively stripping away elaborations to reveal the underlying structure.

The practical skill is reading **Schenkerian graphs**, which use a combination of stems, beams, and slurs to indicate structural levels. Notes on stems are structural; notes as open note heads or unstemmed are subordinate. A slur indicates a prolongation — the notes under the slur are all elaborating the structural note at the slur's origin. Learning to read and construct these graphs is the core exercise. Begin with simple binary or ternary forms where the large-scale harmonic motion is clear (I to V in the first half, V to I in the second), and practice identifying which soprano notes form a stepwise descent and which are ornamental. Over time, more complex structures become legible as elaborations of simpler underlying patterns, and you develop the capacity to hear large-scale tonal architecture — not just the chord-by-chord surface, but the long-range voice-leading that binds a piece together.
