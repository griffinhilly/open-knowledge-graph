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
stage: expert
status: validated
---

# Pitch-Class Set Subsets and Supersets

## Core Idea
Subset and superset relationships organize pitch-class sets hierarchically; smaller sets nest within larger sets in compositional structures. Understanding these relationships reveals how composers derive unity from a few prime sets through expansion or contraction. Subset relationships often parallel motivic development in atonal and twelve-tone works.

## How It's Best Learned
Analyze a Webern piece, mapping subset relationships between its pitch sets and creating Hasse diagrams showing subset containment. Correlate diagram structure with phrase boundaries and motivic transformation in the score.

## Common Misconceptions
- Assuming all subsets are compositionally significant; only aurally and structurally relevant subsets matter. - Confusing subset relationships with transposition or inversion; subset is a cardinality relationship, not a transformation. - Overestimating subset importance in free atonal music, where formal subset organization may be minimal.

## Questions

```yaml
- question: "The trichord {0, 1, 4} appears within the tetrachord {0, 1, 4, 6}. How should this relationship be classified?"
  type: multiple-choice
  options:
    - "A transposition relationship — {0, 1, 4} is a Tn-transform of {0, 1, 4, 6}"
    - "A subset relationship — every pitch class in {0, 1, 4} is also contained in {0, 1, 4, 6}"
    - "An inversion relationship — {0, 1, 4} is the TnI-transform of the remaining element {6}"
    - "A complement relationship — {0, 1, 4} and {0, 1, 4, 6} together fill a larger aggregate"
  answer: 1
  explanation: "Subset containment is a membership relationship: A ⊆ B if every element of A is also in B. Here {0, 1, 4} ⊆ {0, 1, 4, 6} because 0, 1, and 4 all appear in the larger set. Transposition and inversion are transformations between sets of the same cardinality that preserve interval structure — they cannot relate a trichord to a tetrachord. The common mistake is treating any structural relationship between sets as a form of Tn/TnI equivalence."

- question: "In post-tonal analysis, a Hasse diagram is used primarily to:"
  type: multiple-choice
  options:
    - "Show all possible transpositions and inversions of a pitch-class set under Tn and TnI"
    - "Display which pitch-class sets share the same interval-class vector"
    - "Visualize hierarchical subset containment, with sets ordered vertically by cardinality"
    - "Map prime forms to show which set classes are most common in atonal repertoire"
  answer: 2
  explanation: "A Hasse diagram places pitch-class sets (usually in prime form) as nodes, stacked vertically by cardinality — dyads at the bottom, trichords above, tetrachords above those. An upward edge from A to B means A is a proper subset of B with no intermediate set between them. Reading the diagram reveals how small motivic cells nest inside larger structural collections, mapping the compositional logic of subset expansion and contraction. It is a tool for containment relationships, not transformation equivalences."

- question: "A pitch-class set can simultaneously be a subset of a larger collection AND transpositionally equivalent to another set in the same piece — these are independent, non-contradictory relationships."
  type: true-false
  answer: true
  explanation: "Subset containment (A ⊆ B) and transpositional equivalence (A = TnC for some C) are entirely independent claims. A trichord might be extracted from a governing hexachord (subset relationship) while also being a transposition of a trichord from a different section of the piece (equivalence relationship). Both can hold simultaneously without contradiction. Conflating them — e.g., assuming that shared pitch classes between two sets establish a structural connection — leads to overclaiming."

- question: "If pitch-class set A is a subset of set B, then A should be transpositionally or inversionally equivalent to at least one other subset of B."
  type: true-false
  answer: false
  explanation: "Subset containment makes no guarantee about transformation equivalences. Set B may contain subsets with distinct interval-class profiles, none of which are Tn or TnI related to each other. A can be a unique subset of B with no other subset of the same cardinality sharing its prime form. Equivalence relationships are about interval structure; subset relationships are about membership. They must be tracked separately."

- question: "Explain why subset relationships and transposition/inversion equivalences must be tracked separately in post-tonal analysis."
  type: short-answer
  answer: "Subset containment is a membership claim: A ⊆ B means every pitch class in A appears in B, regardless of their interval structures or cardinalities. Transposition/inversion equivalence is a transformation claim: A and C are Tn-equivalent if C = A + n (mod 12), which requires equal cardinality and the same interval-class vector. A set can be contained in another without any transformation relationship holding, and two sets can be transformation-equivalent without one containing the other."
  explanation: "The distinction matters analytically: subset relationships reveal compositional derivation (how smaller cells are drawn from larger structural collections), while Tn/TnI relationships reveal motivic unity through transformation (the same interval structure recurring at different pitch levels). Conflating them produces false claims — e.g., concluding that a shared pitch class establishes a structural relationship between two sets."
```

## Explainer

From your study of pitch-class sets and pitch-class set operations, you can identify sets, reduce them to prime form, and apply transposition and inversion to relate sets of the same cardinality. Subset and superset relationships add a different dimension: rather than asking "is this set a transformed copy of that set?", you ask "does this set fit *inside* that set?" This is a question about **inclusion** — the same set-theoretic relationship you know from your soft prerequisite on set operations — applied to the pitch-class universe.

Set A is a **subset** of set B if every pitch class in A is also in B. In post-tonal music, subset relationships reveal how composers derive unity from a small inventory of pitch material. A governing large set — perhaps a hexachord or a complete 12-tone row — acts as the **superset**, and smaller sets extracted from it (trichords, tetrachords) act as its **subsets**, recurring as motivic cells throughout the work. In Webern's Op. 27 Variations for Piano, for instance, trichords extracted from the row's prime form reappear as the melodic building blocks of each variation. Finding these subset relationships maps the compositional logic at a structural level that a measure-by-measure pitch analysis would miss.

The standard tool for visualizing subset relationships is the **Hasse diagram**: nodes are pitch-class sets (usually represented by prime form), and an upward edge from A to B indicates that A is a proper subset of B with no intermediate set of the same cardinality between them. Nodes are stacked by cardinality — dyads at the bottom, trichords above them, tetrachords above those. Reading the diagram bottom-up shows how small cells combine to form larger complexes; reading top-down shows which subsets a larger set contains. In a tightly organized atonal work, the diagram's structure maps directly onto the piece's motivic architecture: connected paths in the Hasse diagram correspond to passages where material contracts or expands.

A critical distinction that your common misconceptions highlight: subset containment is not the same as transposition or inversion equivalence, and it is easy to confuse them. The trichord {0, 1, 4} is a subset of {0, 1, 4, 6} — this is a membership claim. Whether {0, 1, 4} is a transposition of {2, 3, 6} is an equivalence claim under Tn/TnI. A set may be *both* a subset of a larger collection *and* transpositionally related to another set in the piece, but these are independent relationships and must be tracked separately. Conflating them leads to overclaiming: finding that a pitch class appears in two different sets does not itself establish a structural relationship between those sets.

Some prime forms are compositionally more generative than others because of how richly they contain distinct subset prime forms. Sets with maximum **interval-class diversity** — like the all-interval tetrachords [0,1,4,6] and [0,1,3,7], which together contain all six interval classes — have a wide variety of distinct subsets, making them rich sources of motivic material. This structural richness partly explains why these set classes appear so frequently in atonal and twelve-tone repertoire: a composer working from such a superset has access to a large and varied palette of subsets, each with its own interval-class profile and expressive potential.
