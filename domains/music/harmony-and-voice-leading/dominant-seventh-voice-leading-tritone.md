---
id: dominant-seventh-voice-leading-tritone
title: Dominant Seventh Chord Voice-Leading and Tritone Resolution
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: seventh-chords
  type: hard
- id: dominant-seventh-resolution
  type: hard
- id: voice-leading-principles
  type: hard
- id: tritone-resolution-direction
  type: hard
builds-toward:
- extended-harmony-upper-extensions-voice-leading
tags:
- seventh-chords
- tritone
- voice-leading
stage: formal-systems
status: validated
---

# Dominant Seventh Chord Voice-Leading and Tritone Resolution

## Core Idea
The dominant seventh chord contains a tritone (between the third and seventh scale degrees) that must resolve inward to the third and seventh of the tonic chord. Proper voice leading requires careful handling of this tritone and smooth resolution of tendency tones.

## How It's Best Learned
Write V7-I progressions focusing on tritone resolution; listen to how the tritone drives urgently to resolution in classical music.

## Questions

```yaml
- question: "In C major, a V7 chord (G–B–D–F) resolves to I. Which voices contain the tendency tones, and how do they move?"
  type: multiple-choice
  options:
    - "G (root) rises to C and D (fifth) falls to E — they are the tendency tones"
    - "B (leading tone) rises to C and F (seventh) falls to E — the tritone contracts inward"
    - "D (fifth) and F (seventh) both resolve downward by step to C and E"
    - "B (leading tone) and D (fifth) both resolve upward to C and E respectively"
  answer: 1
  explanation: "The tendency tones in V7 are B and F — the tritone. B is the leading tone (scale degree 7), a half-step below the tonic C, with a strong upward pull. F is the chordal seventh (scale degree 4), which wants to resolve downward by step to E (the third of I). Together they contract inward from the tritone B–F to the third C–E. G and D have no comparable harmonic urgency; they move to complete the tonic triad. This tritone contraction is the defining motion of every V7–I resolution."

- question: "When V7 resolves strictly to I in four-part writing — both tendency tones correctly resolved — which member of the tonic chord is most often missing?"
  type: multiple-choice
  options:
    - "The root — because C must be approached from both B and D simultaneously"
    - "The third — because E is already covered by F's downward resolution"
    - "The fifth — because both B→C and F→E lock two voices, leaving no remaining voice for G"
    - "Nothing is missing — all four members of I are always present when V7 resolves correctly"
  answer: 2
  explanation: "When B rises to C and F falls to E, two voices are committed to the root and third of I. The remaining voices (G and D) typically both move to C to fill out the tonic chord, resulting in a doubled root, the third E, but no fifth (G). This incomplete tonic is standard and acceptable: the root and third define harmonic identity, and the fifth is the most expendable chord member. Forcing G into the tonic would require one tendency tone to resolve unnaturally, which weakens the cadence."

- question: "In V7–I voice leading, the leading tone (B in C major) should ideally resolve downward to G to keep smooth, stepwise motion."
  type: true-false
  answer: false
  explanation: "The leading tone has a powerful upward pull to the tonic (B → C) because it lies a half-step below. Resolving it downward to G is a skip of a third, not a step, and contradicts the tendency-tone logic that gives V7 its harmonic drive. In an outer voice (soprano or bass), the leading tone must rise to the tonic — this is a firm rule in common-practice voice leading. Downward resolution of the leading tone weakens the sense of arrival. The only exception is in inner voices when necessary to avoid parallel octaves or fifths."

- question: "An incomplete tonic chord — missing the fifth, with the root doubled — is standard and acceptable when V7 resolves to I with both tendency tones correctly resolved."
  type: true-false
  answer: true
  explanation: "When the leading tone rises (B → C) and the chordal seventh falls (F → E), no voice is available to supply the fifth (G) of the tonic chord, resulting in a doubled root. This is entirely standard in common-practice four-part writing. The fifth is the most expendable member of a triad: the root establishes the harmonic root, and the third determines major or minor quality. A complete tonic triad at the cost of a misresolved tendency tone would be a worse outcome — the tendency-tone resolution is what creates the sense of arrival."

- question: "Explain why the tritone in the dominant seventh chord is called the 'engine' of tonal harmony."
  type: short-answer
  answer: "The tritone (B–F in G7 in C major) creates intense harmonic tension because both its notes are pulled by strong half-step or step motion toward resolution. B is a leading tone a half-step below C (tonic) and wants to rise; F is a chordal seventh that wants to fall a step to E. When V7 resolves to I, the dissonant tritone B–F contracts inward to the consonant third C–E. This specific contraction — dissonance resolving to consonance through directed half-step motion — is the defining harmonic event of tonal music. Every V7–I cadence in any key is driven by the same inward contraction, transposed. Without the tritone's urgency, dominant harmony would have no more pull toward the tonic than any other chord."
  explanation: "The engine metaphor captures the causal structure: the tritone is the stored tension that drives the resolution. Understanding this mechanism lets you both write convincingly in tonal idioms (always resolve the tritone correctly) and hear analytically (in any V7–I cadence you encounter, you can identify B and F moving to C and E in the appropriate key). It also explains why secondary dominants and applied chords work: borrowing a V7 from any key creates the same tritone-contraction pull toward that key's tonic."
```

## Explainer

The **dominant seventh chord** (V7) is the most powerful harmonic event in tonal music. You already understand seventh chords and the principle of dominant-seventh resolution. This topic gives you the mechanical tools to execute that resolution correctly in four voices. The chord contains four notes — root, third, fifth, and seventh — and each has a specific behavior in voice leading, but two are especially constrained: the **tritone** formed between the third and seventh scale degrees.

In C major, the V7 chord is G–B–D–F. The tritone spans B to F (or F to B, enharmonically). **B is the leading tone** — a half step below the tonic C, with a powerful upward tendency. **F is the chordal seventh** — it wants to resolve downward by step to E, the third of the tonic triad. When V7 resolves to I, the leading tone (B) rises to the tonic (C), and the chordal seventh (F) falls to the third of the tonic chord (E). The tritone *contracts inward* to a third — this is the defining motion of dominant-to-tonic resolution.

In four-part writing, this creates a specific practical challenge. If you resolve both tendency tones strictly — B→C (leading tone rises) and F→E (seventh falls) — the remaining voices must move to complete the tonic triad. With root doubling in both chords, the tonic chord often ends up **missing its fifth** (G), arriving with only C, E, and C again (doubled root, doubled tonic). This incomplete tonic is standard and acceptable: the root and third carry the harmonic identity, and the fifth is the most expendable chord member. The alternative — forcing the fifth into the tonic chord — often requires one of the tendency tones to move in an unnatural direction, which weakens the sense of resolution.

The tritone resolution is not merely a rule — it is the *engine* of tonal harmony. The entire system of dominant preparation, tension building, and release that characterizes common-practice music from Bach to Beethoven depends on this specific intervallic contraction. Every V7–I cadence you hear in the repertoire is driven by the same B-to-C and F-to-E motion (transposed to whatever key). Understanding the mechanics lets you write convincingly in tonal idioms; hearing it analytically transforms your perception of the music you listen to. The tritone is the tightest spring in tonal harmony — when it releases, everything resolves.
