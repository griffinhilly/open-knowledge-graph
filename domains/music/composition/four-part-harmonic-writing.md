---
id: four-part-harmonic-writing
title: Four-Part Voice Writing (SATB)
domain: music
course: composition
prerequisites:
- id: chord-inversions
  type: hard
- id: doubling-rules-root-fifth-third
  type: hard
- id: part-writing-doubling-and-spacing-rules
  type: hard
builds-toward:
  - voice-leading-smooth-motion-composition
tags:
- voice-leading
- harmony
- four-part
- satb
stage: formal-systems
status: draft
---
# Four-Part Voice Writing (SATB)

## Core Idea
Four-part writing (soprano, alto, tenor, bass) is the traditional standard for harmonic composition and analysis. Mastering proper doubling, spacing, and voice leading in four parts develops fundamental skills applicable to all harmonic composition. The constraints of four-part writing—voice ranges, movement rules, and spacing conventions—train composers to balance voice independence with overall blend and unity.

## How It's Best Learned
Begin with simple diatonic progressions, focusing on one rule at a time. Analyze Bach chorales to observe how masters apply these rules flexibly in context. Compose and arrange progressions, gradually increasing complexity.

## Common Misconceptions
All voice-leading rules must be followed without exception; rules are learned principles that can be broken strategically for musical effect when justified. Perfect fourths between outer voices are always forbidden—they are acceptable as long as the bass is not the root of a chord.

## Questions

```yaml
- question: "Soprano moves from C5 to D5 while alto simultaneously moves from G4 to A4 — both voices moving up by a major second, with the interval between them remaining a perfect fifth throughout. What voice-leading error has occurred?"
  type: multiple-choice
  options:
    - "No error — parallel motion is only forbidden between the soprano and bass"
    - "Parallel fifths — two voices moving in the same direction while maintaining a perfect fifth, collapsing their independence into a single composite sound"
    - "Hidden fifths — the voices don't arrive on a fifth, so this is only a mild concern"
    - "Voice crossing — the voices have moved into each other's range"
  answer: 1
  explanation: "This is parallel fifths: two voices moving in the same direction (both up) while preserving a perfect fifth between them. The prohibition exists because parallel fifths fuse two voices into a single, thicker sound — they stop behaving as independent melodic lines. The listener hears one voice doubled at a fifth rather than two distinct contrapuntal voices. The rule applies between any two voices, not just soprano and bass, though parallel motion in the outer voices is particularly exposed."

- question: "A student analyzes a Bach chorale and marks a perfect fourth (P4) between soprano and bass as an error, citing the rule that fourths between outer voices are forbidden. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — any P4 between soprano and bass is always a voice-leading error in SATB writing"
    - "Not necessarily — a P4 between outer voices is acceptable when the bass note is not the root of the chord (i.e., when the chord is in an inversion other than root position)"
    - "No — P4 between outer voices is always acceptable because fourths are consonant intervals"
    - "Yes, but only when the P4 is approached by contrary motion"
  answer: 1
  explanation: "This is one of the most commonly misapplied rules in four-part writing. The prohibition on P4 between outer voices applies specifically when the bass holds the root of the chord — in that context, the fourth above the bass creates an unstable, unresolved sound that demands treatment. When the chord is inverted (the bass holds the third or fifth), the same P4 interval is perfectly acceptable. Bach uses this constantly. Blanket application of the rule without understanding its harmonic context will flag legitimate writing as errors."

- question: "The prohibition on parallel fifths and octaves in four-part writing exists primarily to preserve the independence of each voice as a distinct melodic line."
  type: true-false
  answer: true
  explanation: "True — this is the underlying principle. When two voices move in parallel to a perfect fifth or octave, they begin to blend into a single sound rather than functioning as two independent contrapuntal lines. The entire purpose of four-part writing is to maintain four distinct, singable, melodically interesting voices simultaneously. Parallel motion at these intervals defeats that purpose by acoustically fusing two of those voices. The rule is not aesthetic whim; it follows from the psychoacoustics of how the ear groups simultaneous sounds."

- question: "In four-part SATB writing, the three upper voices (soprano, alto, tenor) must all remain within an octave of the bass voice."
  type: true-false
  answer: false
  explanation: "False — the spacing rule applies to the three upper voices relative to each other: soprano, alto, and tenor should generally stay within an octave of each other. The bass voice may sit considerably further below the tenor without violating spacing rules. This is why large gaps between bass and tenor (even two octaves) appear regularly in Bach chorales, while gaps larger than an octave between any two adjacent upper voices are typically avoided. Misapplying this rule to the bass will cause you to flag correct writing as errors."

- question: "Why are parallel fifths and octaves prohibited in four-part writing? Explain what they do to the texture and why that matters."
  type: short-answer
  answer: "Parallel fifths and octaves cause two voices to move as a single entity — the interval between them stays fixed, so the ear hears one voice doubled at a fifth or octave rather than two independently moving melodic lines. Four-part writing derives its richness from the simultaneous independence of four voices, each tracing its own melodic path. Parallel fifths collapse this into three effective lines (or fewer), reducing contrapuntal interest and the sense of harmonic fullness. The prohibition is ultimately a rule about voice independence: each line must behave as a distinct, self-contained melodic entity. This is grounded in psychoacoustics — the human ear groups sounds moving in fixed parallel ratios into a single composite source."
  explanation: "Understanding the principle behind the rule — voice independence — is more useful than memorizing the rule itself, because it lets you evaluate edge cases (e.g., brief parallel fifths in fast passing motion) and understand why Bach occasionally bends the rule when the musical context justifies it. The Common Misconceptions section notes that voice-leading rules are 'learned principles that can be broken strategically for musical effect when justified' — knowing the WHY makes you a better judge of when that justification applies."
```

## Explainer

Four-part writing assigns every harmony to four independent melodic lines — soprano, alto, tenor, and bass — named after the four human voice ranges. You already know how to identify chord inversions (which note is in the bass) and the basic doubling rules (which chord tone to double for fullness and clarity). Four-part writing pulls those concepts together into a complete system: at every moment, four voices must produce a valid chord while each one traces a coherent melodic line through time.

The **vertical** dimension is what you hear at any given beat: which chord is sounding, what inversion it's in, and whether the voices are spaced properly. **Spacing rules** keep the texture balanced — the three upper voices (soprano, alto, tenor) should generally stay within an octave of each other, while the bass can sit further below. The **horizontal** dimension is each voice's melodic path: it should stay within a comfortable range, prefer stepwise motion, and avoid awkward leaps. A perfect authentic cadence in four parts isn't just a V–I chord change — it's four voices each arriving on their chord tones in the most efficient and singable way possible.

The classic errors in four-part writing are **parallel fifths** and **parallel octaves** — when two voices move in the same direction by the same interval, landing on a fifth or octave. These are prohibited because they collapse two independent lines into a single, less interesting one: the voices stop behaving as separate melodic entities. The rule against parallel fifths isn't arbitrary; it enforces the independence that makes polyphony interesting. Similarly, the prohibition on **hidden fifths/octaves** in the outer voices (soprano and bass moving in the same direction to a fifth or octave) prevents a similar effect at the most exposed part of the texture.

Learning four-part writing from Bach chorales is the standard approach for a reason: Bach wrote hundreds of them, each demonstrating the same principles applied to a different harmonization. Analyzing a Bach chorale, you'll see that he almost never makes the awkward choices — each voice moves with a minimum of leaps, common tones are held between chords, and dissonances resolve by step. These aren't mathematical accidents; they reflect a deep internalization of what sounds natural to singing voices. The rules of four-part writing are, at their core, rules about what human voices can do comfortably and expressively. Understanding this transforms them from arbitrary constraints into a logical grammar of vocal music.
