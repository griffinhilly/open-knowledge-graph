---
id: voice-leading-parallel-perfect-intervals
title: Avoiding Parallel Perfect Intervals
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: voice-leading-basics
  type: hard
builds-toward:
- four-part-writing
- voice-leading-in-composition
tags:
- voice-leading
- counterpoint
- rules
stage: formal-systems
status: draft
---

# Avoiding Parallel Perfect Intervals

## Core Idea
Parallel fifths and octaves between two voices undermine voice independence and create weak voice leading. This fundamental rule—forbidding consecutive perfect intervals reached by similar motion—is essential in traditional harmony.

## How It's Best Learned
Listen to examples with and without parallel fifths; transcribe Bach chorale excerpts and identify where parallels are used or avoided.

## Common Misconceptions
- Parallel fifths are always wrong; some composers use them intentionally for effect.
- The rule applies equally to all voice pairs; outer voices (soprano-bass) are more critical than inner voices.

## Questions

```yaml
- question: "The soprano moves from C4 to D4 (up a whole step) while the bass moves from F3 to G3 (up a whole step). Both intervals — C4-F3 and D4-G3 — are perfect fifths. A student claims: 'This is fine because both voices move by the same amount.' Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — moving by the same interval is required for good voice leading"
    - "No — this is an example of parallel fifths, which is forbidden in strict tonal style"
    - "Yes — the rule only applies when the voices move to a unison, not a fifth"
    - "No — but only because the soprano is in the wrong register"
  answer: 1
  explanation: "This is exactly the definition of parallel fifths: two voices moving by similar motion and arriving at another perfect fifth. The student has described the situation correctly (same interval maintained) but drawn the wrong conclusion. Moving by the same interval while maintaining a perfect fifth is the problem, not a sign of good technique."

- question: "A student writes a four-part chorale with parallel fifths between the alto and tenor voices. They argue that this is permitted because the rule only forbids parallel fifths between the soprano and bass. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — only outer-voice parallels are forbidden; inner-voice parallels are fine in strict style"
    - "No — parallel fifths between any voice pair are forbidden in strict tonal style, but outer-voice parallels are most audibly critical and receive the most scrutiny"
    - "No — parallel fifths are only forbidden when they involve the tenor voice specifically"
    - "Yes — Bach himself wrote parallel fifths between inner voices, so the rule does not apply there"
  answer: 1
  explanation: "In strict four-part style, parallel perfect intervals are prohibited between any pair of voices. However, outer-voice parallels (soprano-bass) are the most perceptually salient because those are the structural anchors the ear follows most closely. Inner-voice parallels are also errors — they're simply less immediately audible. The checking procedure should still cover all voice pairs."

- question: "Two voices moving in parallel perfect octaves effectively reduce the perceived number of independent voices in a four-part texture."
  type: true-false
  answer: true
  explanation: "Two voices an octave apart are the same pitch in different registers. In parallel octaves, they reinforce each other at every moment rather than contributing independent melodic content. A four-part texture gains its richness from four genuinely distinct lines; parallel octaves collapse two of those lines into one, effectively reducing the texture to three (or even two) independent voices."

- question: "The prohibition on parallel fifths in tonal harmony is an arbitrary stylistic convention with no acoustic basis."
  type: true-false
  answer: false
  explanation: "The rule has a direct acoustic foundation. A perfect fifth has a frequency ratio of 3:2 — one of the simplest and most acoustically pure intervals. This purity causes two voices in a perfect fifth to fuse perceptually into a single tonal entity. When two voices maintain parallel fifths across a motion, they preserve that fusion throughout, and the listener hears one thick line rather than two independent voices. The rule protects voice independence, which is the architectural foundation of the tonal voice-leading tradition."

- question: "Explain why parallel octaves are considered more problematic than parallel fifths in traditional voice leading."
  type: short-answer
  answer: "A perfect octave is the most extreme case of acoustic fusion: two voices an octave apart are literally the same pitch class, differing only in register. They reinforce each other completely rather than contributing distinct harmonic content. In parallel octaves, those two voices become inseparable for the duration of the passage — the texture is reduced by a full voice. A parallel fifth also causes fusion, but the two pitches remain distinct (a fifth apart), so there is at least some harmonic content from both. The octave is the limiting case where voice independence is entirely lost."
  explanation: "This is why careful composers treat parallel octaves as the more severe violation. Parallel fifths weaken independence; parallel octaves eliminate it. The outer-voice octave is the most egregious form because soprano and bass are the framing voices the ear relies on to define the harmonic progression."
```

## Explainer

The rule against parallel perfect intervals isn't an arbitrary stylistic convention — it follows directly from what makes perfect intervals acoustically special. A **perfect fifth** (frequency ratio 3:2) is so acoustically pure that two voices singing it fuse into a single perceived entity. When two voices move in parallel fifths, they maintain that fused quality across the motion, arriving at another perfect fifth. The listener hears a single, thick line rather than two independent voices. The rule exists because the entire tradition of voice-leading in Western harmony assumes **independent voices** — lines that each contribute their own melodic identity. Parallel perfect intervals collapse that independence.

The same logic applies to **parallel octaves** with even more force. Two voices an octave apart are essentially the same pitch at different registers; in parallel octaves they are literally doubling each other at every moment. The two voices become one. In a four-part texture, parallel octaves between any pair of voices effectively reduces the harmonic event to three voices (or two, if inner voices double). The richness of four-part writing comes from four genuinely independent contributions; the rule against parallel octaves protects that richness.

The most important distinction to understand is the difference between **parallel** and **similar** motion. Similar motion is when two voices both go up or both go down — but they don't have to maintain the same interval. Parallel motion is similar motion *at the same interval*. A passage where soprano and bass both rise but by different intervals (ending at a third instead of a fifth) is fine; it's only when they both arrive at *another* perfect fifth or octave by *similar motion* that the prohibition applies. **Contrary motion** (one voice rises while the other falls) is always the safest choice when approaching a perfect interval, because it maximally demonstrates independence.

Context and voice pair matter for how audible a parallel perfect interval is. Parallels between the **outer voices** (soprano and bass) are the most perceptible because those are the structural anchors the ear tracks most carefully. Parallels between inner voices (alto-tenor) are also forbidden in strict style but are less immediately glaring. The strictness with outer voices is why careful four-part writing always subjects the soprano-bass frame to special scrutiny. When you're checking a passage, trace the soprano against the bass for the whole passage first — any parallel fifths or octaves there will be unmistakable to a trained ear. Inner-voice parallels are checked second, after the structural outer frame is clean.
