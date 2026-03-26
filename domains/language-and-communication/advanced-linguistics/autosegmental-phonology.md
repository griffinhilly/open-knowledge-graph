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
- id: sound-change-mechanisms-diachronic
  type: soft
tags:
- phonology
- autosegmental
- features
stage: expert
status: validated
---
# Autosegmental Phonology

## Core Idea
Autosegmental phonology represents segments as bundles of features organized on parallel, independent tiers, allowing features to behave independently of segment boundaries. This framework elegantly explains tone spreading, vowel harmony, and geminate consonants that resist linear representation.

## How It's Best Learned
Draw autosegmental representations for tone and harmony systems in African and Finno-Ugric languages; test how features spread across segment boundaries.

## Common Misconceptions
Autosegmental tiers are not psychologically real; they are analytical abstractions that capture generalizations about feature behavior.

## Questions

```yaml
- question: "In a Bantu language, a vowel is deleted from a word, but the high tone that was associated with that vowel appears on the adjacent vowel. In autosegmental phonology, what does this 'floating tone' phenomenon demonstrate?"
  type: multiple-choice
  options:
    - "The deletion rule is incomplete — the vowel was reduced rather than fully deleted"
    - "Tones exist on an independent tier; when the segmental tier loses the vowel, the tone remains on the tonal tier and reassociates to an adjacent segment"
    - "The rule deleting the vowel also includes a compensatory copying step that transfers tone to the neighbor"
    - "High tones spread automatically across all adjacent segments regardless of vowel deletion"
  answer: 1
  explanation: "This is one of the core empirical motivations for autosegmental theory. A linear representation cannot explain tone survival after vowel deletion — if tones are properties of segments, a deleted segment takes its tone with it. The autosegmental solution is that tones are on an independent tier connected to segments by association lines. When the vowel is deleted on the segmental tier, the tone 'floats' on the tonal tier and then reassociates with an adjacent vowel under well-formedness constraints. The feature outlives the segment because it was never part of the segment — it was a separate object linked to it."

- question: "Finnish vowel harmony requires all vowels in a word to share the same value for [back] — all back or all front. How does autosegmental phonology explain this more parsimoniously than a linear approach?"
  type: multiple-choice
  options:
    - "A single copying rule iterates left-to-right, applying the [back] value of the first vowel to each subsequent vowel"
    - "A word-level filter rejects any word containing both [+back] and [-back] vowels after derivation"
    - "A single [±back] specification on the vocalic tier associates with all vowels in the word, so they share one feature rather than each having their own"
    - "Consonants between vowels block the spread of [back], so harmony operates only within syllables"
  answer: 2
  explanation: "The autosegmental account replaces multiple identical feature specifications with a single one. In a linear model, if four vowels all have [+back], you need four separate [+back] features and rules that copy or agree. Autosegmentally, there is one [+back] token on the vocalic tier that simply associates with multiple vowel slots — harmony is just a single feature with a wide scope of association. This is both more economical and naturally handles why harmony ignores consonants (consonants are on the segmental tier; the vocalic [back] tier skips over them). It also immediately explains why adding a new vowel to a word is automatically harmonized."

- question: "In autosegmental theory, a single tonal specification such as [H] can be associated with multiple vowel positions simultaneously, producing a level high tone across an entire domain."
  type: true-false
  answer: true
  explanation: "This is a defining feature of autosegmental representations. Association lines connect one tier to another, and a single tonal element can link to multiple segments. This is how spreading is represented: not as successive copying but as broadening the domain of association. A [H] associated with three vowels produces a level high tone across all three; if it were later restricted to one vowel, the other associations would be severed. This multilinear association is what makes autosegmental representations fundamentally different from feature matrices in standard segmental phonology."

- question: "The Obligatory Contour Principle (OCP) prohibits identical adjacent features from appearing anywhere on any tier, requiring that most adjacent segments differ in at least one feature."
  type: true-false
  answer: false
  explanation: "The OCP is a constraint on a *single* tier that prohibits two identical adjacent specifications on that tier. It applies tier-specifically, not as a general requirement for segments to differ in all features. The OCP on the tonal tier says you cannot have [H][H] adjacently — they must be merged into one [H] with dual association. But it says nothing about, say, adjacent consonants sharing the same place feature on the segmental tier. It is also not an absolute inviolable constraint but a strong tendency that interacts with other requirements. The formulation 'all adjacent segments must differ in at least one feature' is both too strong and confused about what the OCP governs."

- question: "A geminate consonant (like the double-t in Italian 'notte') resists deletion processes that would remove a 'single consonant.' How does autosegmental representation explain this resistance?"
  type: short-answer
  answer: "In autosegmental phonology, a geminate is represented as a single consonant specification on the segmental tier associated with two timing slots (two positions on the skeletal or timing tier). A deletion rule that removes 'one consonant' removes one timing slot. But since the single consonantal specification still has an association to the remaining timing slot, the consonant is not gone — it surfaces as a regular short consonant. Deleting a true geminate requires severing all associations, which is a more costly operation than single-segment deletion. The geminate's 'weight' comes from this dual timing association, not from being two separate consonants."
  explanation: "This is the elegance of autosegmental geminates: they explain why geminates behave as phonologically heavier (they occupy two timing slots) and why they resist deletion (deleting one association still leaves the consonant present). Linear phonology would need two separate identical consonant segments to represent a geminate and an ad hoc constraint preventing both from being deleted simultaneously."
```

## Explainer

From your study of phonological features, you know that segments are not atomic units but bundles of distinctive features — [+voice], [-nasal], [+high], and so on. From suprasegmental phonology, you know that properties like tone, stress, and length operate over domains larger than individual segments. Autosegmental phonology is the theoretical framework that unifies these observations and resolves a fundamental problem with standard linear representations: why do some phonological properties behave as if they belong to the segment, while others spread, jump, or persist independently of what happens to individual segments?

The core problem that motivated autosegmental theory — developed by John Goldsmith in the mid-1970s — is **tone spreading** in African languages. In many Bantu languages, a high tone on one vowel spreads to neighboring vowels even when consonants (which are not toned) intervene. In a purely linear representation, each segment has its own tone specification, so spreading requires elaborate copying rules. More troubling: when a vowel is deleted, its tone often "survives" on the adjacent vowel — a ghost of the deleted segment. A linear model has no natural way to represent a tone that persists after its segment is gone. The autosegmental solution is simple and elegant: **tones are represented on a separate tier**, connected to segments by **association lines**, and the two tiers are governed by their own independent well-formedness conditions.

The key innovation is the **multi-tiered representation**. Instead of a single linear string of feature bundles, autosegmental phonology posits parallel tiers — a segmental tier, a tonal tier, a laryngeal tier, a place tier, and so on — each tier governed by its own constraints, connected to others through association lines. A single tonal specification can associate with multiple segments (producing tone spreading), or a single segment can associate with multiple tonal specifications (producing contour tones). The **Obligatory Contour Principle (OCP)** — the constraint that identical adjacent elements on any tier must be represented as a single unit — explains why the same tone rarely occurs twice in a row on the tonal tier: they merge into a single specification with dual association. This accounts for a surprising range of morphological and phonological patterns across languages.

**Vowel harmony** is the other phenomenon where autosegmental analysis earns its keep. In Finnish or Turkish, all vowels in a word must share the same value for a feature like [back] or [round] — back vowels trigger back vowels, front vowels trigger front vowels, across the whole word. Linearly, this requires a copying operation that must skip consonants and apply repeatedly. Autosegmentally, a single [+back] or [-back] specification on the vocalic tier simply associates with all vowels in the word — the harmony is just a single feature with a wide domain of association. **Geminate** consonants — doubly long segments that in many languages resist certain processes — are similarly handled as a single segment specification associated with two timing slots, explaining why processes that delete "one consonant" often leave a geminate intact.

What makes autosegmental phonology powerful is that it recasts phonological rules as operations on tiers and association lines, governed by universal constraints like the OCP and the prohibition on crossing association lines. This moves phonology from a set of language-particular rules to a constrained space of possible grammars. It was a major step toward the modular, constraint-based approach that later crystallized in Optimality Theory. The representations may be abstractions rather than cognitive reality, but they capture genuine generalizations about what phonological processes look like across the world's languages.


