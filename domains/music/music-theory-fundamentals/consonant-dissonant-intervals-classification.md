---
id: consonant-dissonant-intervals-classification
title: Consonant and Dissonant Intervals
domain: music
course: music-theory-fundamentals
prerequisites:
- id: interval-quality-basics
  type: hard
- id: interval-recognition-by-ear
  type: soft
- id: consonance-dissonance-harmonic-function
  type: soft
builds-toward:
- triad-construction-from-intervals
- harmonic-function-basics
tags:
- interval
- consonance
- dissonance
- harmony
stage: formal-systems
status: validated
---
# Consonant and Dissonant Intervals

## Core Idea
Intervals are classified as consonant (stable, restful) or dissonant (tense, requiring resolution). Perfect unisons, fourths, fifths, and octaves, along with major and minor thirds and sixths are consonant. Seconds, sevenths, and tritones are dissonant. This classification is fundamental to voice leading and harmonic progression.

## How It's Best Learned
Listen carefully to pairs of consonant and dissonant intervals to internalize the sonic difference. Practice identifying them by ear as part of interval recognition training.

## Common Misconceptions
- Thinking the perfect fourth is always consonant (it can function as dissonant in voice leading when it appears above the bass).
- Confusing interval size with consonance/dissonance (a minor seventh is dissonant despite being large).

## Questions

```yaml
- question: "A student classifies the minor seventh as consonant, arguing it 'sounds fuller and richer' than the minor second. What is the error in this reasoning?"
  type: multiple-choice
  options:
    - "The student is right — the minor seventh is a consonance in most tonal contexts"
    - "Consonance and dissonance are not determined by perceived richness or fullness, but by whether an interval creates harmonic tension requiring resolution — the minor seventh does, so it is dissonant"
    - "Both the minor seventh and the minor second are consonances; neither requires resolution"
    - "The minor seventh is consonant only when it appears between upper voices, not above the bass"
  answer: 1
  explanation: "The student is confusing acoustic richness (a perceptual quality of timbre and complexity) with harmonic stability (the functional question of whether an interval requires resolution). A minor seventh may sound 'full' in isolation, but in tonal music it creates tension that demands resolution — typically by one voice moving down by step. Consonance and dissonance are functional categories: dissonances drive harmonic motion by creating expectations; consonances fulfill them. Size alone does not determine which category an interval belongs to."

- question: "In a four-voice chorale, a perfect fourth appears between two upper voices. In a second version, the same interval appears between the bass and a tenor voice. Which statement correctly describes these two contexts?"
  type: multiple-choice
  options:
    - "Both instances sound equally consonant because the interval size and quality are identical"
    - "Both instances are dissonant and require the same voice-leading resolution"
    - "The upper-voice instance functions as a consonance; the above-bass instance functions as a dissonance requiring resolution"
    - "The perfect fourth is always dissonant regardless of register or voicing"
  answer: 2
  explanation: "The perfect fourth is the canonical borderline case in tonal consonance/dissonance. Between two upper voices, it sounds stable and consonant — it can sit without resolving. But when a perfect fourth appears above the bass, it creates a second-inversion chord (6/4), which functions as a dissonance in tonal voice leading: the fourth must resolve downward to a third. This context-dependence is not arbitrary — it reflects the role the bass plays as the harmonic foundation. The same interval can be consonant or dissonant depending on its relationship to the lowest voice."

- question: "The tritone is the most harmonically unstable interval in tonal music, spanning exactly half an octave, and requires resolution in voice leading."
  type: true-false
  answer: true
  explanation: "The tritone (augmented fourth or diminished fifth) divides the octave precisely in half and creates maximum tonal instability. In a dominant seventh chord, the tritone between the third and seventh is what drives the chord's resolution: the two voices move inward (diminished fifth resolving to a third) or outward (augmented fourth resolving to a sixth). Composers have used the tritone's tension and instability deliberately throughout tonal music, and 20th-century composers exploited unresolved tritones specifically for their unsettling effect — which only works because the expectation of resolution is so strong."

- question: "In tonal music, larger intervals are always more dissonant than smaller intervals."
  type: true-false
  answer: false
  explanation: "This is a common misconception: interval size and dissonance are not correlated. Major and minor thirds (smaller intervals) are imperfect consonances — restful and stable. Major and minor sixths (larger intervals) are also consonant. Meanwhile, the minor second (very small) and major seventh (large) are both dissonant. The tritone, a medium-sized interval, is the most dissonant. Consonance and dissonance reflect acoustic and functional properties of the interval, not its size. A student who relies on size as a proxy for dissonance will misclassify most intervals."

- question: "Why is the perfect fourth classified as a 'borderline' case in consonance/dissonance classification, and what determines whether it functions as a consonance or dissonance in practice?"
  type: short-answer
  answer: "The perfect fourth is borderline because its classification is context-dependent rather than fixed. Between two upper voices in a chord or two-voice texture, the fourth sounds stable and consonant — it does not create tension requiring resolution. But when the perfect fourth appears above the bass voice, it creates a second-inversion sonority (a 6/4 chord) that functions as a dissonance in tonal voice leading: the fourth is heard as an unstable suspension over the bass that must resolve downward by step to a third. The determining factor is the interval's relationship to the bass: the bass is the harmonic foundation, and a fourth built on it creates a conflict between the bass pitch and the expected root-position harmony above it."
  explanation: "This context-dependence reveals that consonance/dissonance is not purely an acoustic property of an interval in isolation — it is a functional property that depends on harmonic context. The same interval can fulfill different roles. This is why the interval must be analyzed within its voice-leading and harmonic context, not simply classified by its size or quality."
```

## Explainer

From your study of interval quality basics, you can already identify intervals by their size (seconds, thirds, fourths...) and quality (major, minor, perfect, augmented, diminished). Now we add a second axis of classification that is equally important for harmony: whether an interval sounds **stable** or **unstable** — consonant or dissonant.

The distinction is primarily perceptual. Play a major third (C–E) and then a minor second (C–D♭) on any instrument. The first settles; the second creates tension that seems to want to move somewhere. This difference in acoustic character underlies the entire tonal system. Tonal music is fundamentally a drama of tension and release, and consonance/dissonance is its mechanism: dissonances create the tension, resolutions to consonances release it.

The classification groups are worth memorizing in order of stability. **Perfect consonances** — unisons, octaves, and perfect fifths — are the most stable, sounding open and hollow, providing structural pillars in composition. **Imperfect consonances** — major and minor thirds, major and minor sixths — are slightly less stable but still restful; these intervals give chords their characteristic warmth. **Dissonances** include major and minor seconds, major and minor sevenths, and the **tritone** (augmented fourth/diminished fifth) — the most unstable interval in tonal music, spanning exactly half an octave. The perfect fourth is a borderline case: between two upper voices it sounds consonant, but above the bass in a chord it functions as a dissonance requiring resolution.

The practical application is voice leading. Because dissonant intervals create expectation, they must be **resolved** — typically by one or both voices moving by step to a consonant interval. A seventh resolves down by step; a tritone tends to resolve inward (both voices moving toward each other) or outward. This is not merely a convention but a feature of how listeners process harmonic tension: a dissonance sets up an expectation, and the resolution fulfills it. When composers deliberately leave dissonances unresolved — as 20th-century modernists did — the effect is unsettling precisely because that expectation is being denied.
