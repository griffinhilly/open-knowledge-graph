---
id: pitch-class-set-subsets-supsets
title: Pitch-Class Set Subsets and Supersets
domain: music
course: advanced-music-theory
prerequisites:
- id: pitch-class-sets-introduction
  type: hard
- id: pitch-class-set-operations
  type: hard
- id: set-operations
  type: soft
- id: set-operations-union-intersection-complement
  type: soft
builds-toward:
- z-related-pitch-class-sets
- twelve-tone-aggregate-formations
tags:
- set-theory
- post-tonal
- structural-analysis
stage: advanced
status: draft
---

# Pitch-Class Set Subsets and Supersets

## Core Idea
Subset and superset relationships organize pitch-class sets hierarchically; smaller sets nest within larger sets in compositional structures. Understanding these relationships reveals how composers derive unity from a few prime sets through expansion or contraction. Subset relationships often parallel motivic development in atonal and twelve-tone works.

## How It's Best Learned
Analyze a Webern piece, mapping subset relationships between its pitch sets and creating Hasse diagrams showing subset containment. Correlate diagram structure with phrase boundaries and motivic transformation in the score.

## Common Misconceptions
- Assuming all subsets are compositionally significant; only aurally and structurally relevant subsets matter. - Confusing subset relationships with transposition or inversion; subset is a cardinality relationship, not a transformation. - Overestimating subset importance in free atonal music, where formal subset organization may be minimal.

## Explainer

From your study of pitch-class sets and pitch-class set operations, you can identify sets, reduce them to prime form, and apply transposition and inversion to relate sets of the same cardinality. Subset and superset relationships add a different dimension: rather than asking "is this set a transformed copy of that set?", you ask "does this set fit *inside* that set?" This is a question about **inclusion** — the same set-theoretic relationship you know from your soft prerequisite on set operations — applied to the pitch-class universe.

Set A is a **subset** of set B if every pitch class in A is also in B. In post-tonal music, subset relationships reveal how composers derive unity from a small inventory of pitch material. A governing large set — perhaps a hexachord or a complete 12-tone row — acts as the **superset**, and smaller sets extracted from it (trichords, tetrachords) act as its **subsets**, recurring as motivic cells throughout the work. In Webern's Op. 27 Variations for Piano, for instance, trichords extracted from the row's prime form reappear as the melodic building blocks of each variation. Finding these subset relationships maps the compositional logic at a structural level that a measure-by-measure pitch analysis would miss.

The standard tool for visualizing subset relationships is the **Hasse diagram**: nodes are pitch-class sets (usually represented by prime form), and an upward edge from A to B indicates that A is a proper subset of B with no intermediate set of the same cardinality between them. Nodes are stacked by cardinality — dyads at the bottom, trichords above them, tetrachords above those. Reading the diagram bottom-up shows how small cells combine to form larger complexes; reading top-down shows which subsets a larger set contains. In a tightly organized atonal work, the diagram's structure maps directly onto the piece's motivic architecture: connected paths in the Hasse diagram correspond to passages where material contracts or expands.

A critical distinction that your common misconceptions highlight: subset containment is not the same as transposition or inversion equivalence, and it is easy to confuse them. The trichord {0, 1, 4} is a subset of {0, 1, 4, 6} — this is a membership claim. Whether {0, 1, 4} is a transposition of {2, 3, 6} is an equivalence claim under Tn/TnI. A set may be *both* a subset of a larger collection *and* transpositionally related to another set in the piece, but these are independent relationships and must be tracked separately. Conflating them leads to overclaiming: finding that a pitch class appears in two different sets does not itself establish a structural relationship between those sets.

Some prime forms are compositionally more generative than others because of how richly they contain distinct subset prime forms. Sets with maximum **interval-class diversity** — like the all-interval tetrachords [0,1,4,6] and [0,1,3,7], which together contain all six interval classes — have a wide variety of distinct subsets, making them rich sources of motivic material. This structural richness partly explains why these set classes appear so frequently in atonal and twelve-tone repertoire: a composer working from such a superset has access to a large and varied palette of subsets, each with its own interval-class profile and expressive potential.
