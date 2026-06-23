---
id: dominant-seventh-resolution
title: Dominant Seventh Chord Resolution
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: seventh-chords
  type: hard
- id: voice-leading-principles
  type: hard
- id: roman-numeral-analysis
  type: soft
- id: seventh-chord-types-and-qualities
  type: hard
builds-toward:
- secondary-dominants
- four-part-writing
- jazz-harmony-basics
tags:
- dominant-seventh
- resolution
- leading-tone
- tritone
stage: formal-systems
status: validated
---

# Dominant Seventh Chord Resolution

## Core Idea
The dominant seventh chord (V7) is the most structurally important chord in tonal harmony because it contains a tritone — the highly dissonant interval between the leading tone (scale degree 7) and the fourth scale degree. This tritone creates powerful tension that demands resolution: the leading tone resolves upward by half step to the tonic, and the seventh resolves downward by step to the third scale degree. In four-part writing, this dual resolution often yields an incomplete tonic chord (tripled root, no fifth) to avoid parallel fifths and accommodate both active tones correctly.

## How It's Best Learned
Play V7–I at the keyboard in multiple keys, paying close attention to the pull of the tritone. Practice the four-part resolution, confirming the leading tone goes up and the seventh goes down. Then practice V7 resolving to vi (deceptive cadence) to hear how the resolution can be redirected.

## Common Misconceptions
- Resolving the seventh upward instead of downward — the most common student error.
- Thinking the fifth of V7 must always be present: it is routinely omitted in four-part writing to allow correct resolution of both active tones.
- Forgetting that in minor keys, the dominant seventh uses the raised leading tone (harmonic minor scale), not the natural seventh.

## Questions

```yaml
- question: "In a V7 chord resolving to I in C major (G–B–D–F resolving to C major), the chordal seventh (F) must resolve to which note and in which direction?"
  type: multiple-choice
  options:
    - "Up to F#, because the leading tone's upward pull draws adjacent voices upward as well"
    - "Down to E (scale degree 3), because the seventh resolves downward by step to the third of the tonic chord"
    - "Down to D, because the seventh always falls to the nearest chord tone available in I"
    - "Up to G, returning to the root of the dominant chord via contrary motion with the bass"
  answer: 1
  explanation: "The seventh of V7 (F, scale degree 4 in C major) is an active tone that resolves downward by step to scale degree 3 (E), the third of the tonic chord. This is the mandatory voice-leading direction. Resolving F upward to F# is the most common student error: F# is not a member of the C major tonic triad and creates a voice-leading problem rather than resolving one. The tritone in V7 (between B and F) resolves by both tones moving inward: the leading tone B moves up to C, and the seventh F moves down to E."

- question: "In four-part writing, why is the fifth of the V7 chord routinely omitted when resolving to I?"
  type: multiple-choice
  options:
    - "Because the fifth of V7 forms a tritone with the root, creating additional dissonance that must be avoided"
    - "Because resolving both active tones correctly — leading tone up to tonic, seventh down to third — leaves no voice available to supply the fifth of the tonic chord without parallel fifths, so the fifth of V7 is dropped and the tonic chord is completed with a tripled root"
    - "Because the fifth of V7 is enharmonically equivalent to a tone in the tonic chord and would create octave parallels"
    - "Because listeners cannot perceive the fifth in a four-voice texture and its omission goes unnoticed"
  answer: 1
  explanation: "In a complete V7 chord (G–B–D–F in C major), correct resolution accounts for three voices: G resolves to C (root of I), B resolves up to C (leading tone to tonic), and F resolves down to E (seventh to third of I). Three voices arrive on C, C, and E. The fourth voice, D, has nowhere to go cleanly — moving it to G would typically produce parallel fifths with another voice. The standard solution is to omit D from V7 entirely (writing G–B–F) and resolve to an incomplete tonic with tripled root and single third. The ear supplies the missing fifth from harmonic expectation."

- question: "In a deceptive cadence (V7 resolving to vi), the leading tone abandons its normal half-step upward resolution because the destination chord has changed."
  type: true-false
  answer: false
  explanation: "False. In the deceptive cadence, the leading tone still resolves upward by half step — it just arrives on a different chord member than expected. In C major resolving V7 to Am (vi): B still moves up to C (now the third of Am rather than the root of C major), and F still moves down to E (now the fifth of Am). The 'deception' is entirely in the bass, which moves from G to A instead of G to C. The tritone resolution — the internal voice-leading logic — proceeds normally, which is why the deceptive cadence sounds harmonically satisfying despite the harmonic surprise."

- question: "The dominant seventh chord (V7) is structurally singular in tonal harmony because it contains a tritone that creates mandatory directional resolution for two distinct active tones simultaneously."
  type: true-false
  answer: true
  explanation: "True. The tritone between the leading tone (scale degree 7, the third of V7) and the fourth scale degree (the chordal seventh of V7) is the source of V7's exceptional drive. Scale degree 7 must resolve upward by half step to the tonic; scale degree 4 must resolve downward by step to scale degree 3. This dual, directed resolution distinguishes V7 from all other chords in the diatonic system — it contains two active tones with specific mandatory destinations, not one."

- question: "Explain why resolving the seventh of V7 upward rather than downward is considered an error in tonal voice leading, using C major as your example."
  type: short-answer
  answer: "The seventh of V7 in C major is F (scale degree 4). Its mandatory resolution is downward by step to E (scale degree 3, the third of the tonic chord C–E–G). If F resolves upward, it moves to F#, which is not a diatonic member of C major and is not a chord tone of the C major triad. This creates a non-harmonic tone that typically generates parallel fifths or other voice-leading problems with adjacent voices. The downward resolution is not arbitrary — it is the direction that completes the tritone's inward motion (B up to C, F down to E) and lands on an actual chord tone of the tonic."
  explanation: "Each active tone in V7 has a specific voice-leading tendency: the leading tone's entire function is to 'lead' upward by half step to the tonic, and the chordal seventh follows the convention that dissonant sevenths resolve downward by step. Treating the seventh as a free tone and moving it upward violates both the directional tendency and the harmonic goal — the resulting F# does not belong in the tonic chord and leaves the resolution incomplete."
```

## Explainer

You know from your study of seventh chords that a dominant seventh chord (V7) stacks a minor seventh on top of a major triad built on scale degree 5. In C major, that's G–B–D–F. What makes this chord structurally singular is the interval buried inside it: the **tritone** between B (scale degree 7, the leading tone) and F (scale degree 4). From your voice-leading principles, you know that dissonance creates motion — the tritone is the most dissonant interval available in tonal music, and it doesn't merely suggest resolution; it demands it. The V7 chord is tonal harmony's most powerful engine precisely because it contains two active tones simultaneously.

Each active tone has a specific destination. The **leading tone** (scale degree 7, the third of V7) resolves upward by half step to the tonic — this is the defining behavior of the leading tone, the note whose name describes its function. In C major, B moves to C. The **seventh** of the chord (scale degree 4, the chordal seventh) resolves downward by step to scale degree 3 — F moves to E. These two resolutions happen simultaneously, and they're not interchangeable: resolving the seventh upward is the most common student error because it treats the seventh like just another chord tone rather than an active tone with a mandatory direction. The half-step above F is F#, which is not a member of the tonic chord in C major and creates a voice-leading problem rather than solving one.

The mechanical consequence of resolving both active tones in four-part writing is that the **fifth of V7 is routinely omitted**. In a complete V7 chord (G–B–D–F), the root (G) resolves to the tonic (C), the third (B) resolves up to C, and the seventh (F) resolves down to E. That accounts for three voices arriving on the tonic chord: two on C (root doubled) and one on E (third). The fifth of the tonic chord (G) has no one left to play it — unless the D in V7 moves there, but D moving to G is a leap that often creates parallel fifths with another voice. The standard solution is to omit the fifth of V7 entirely, giving the chord as G–B–(no D)–F, and resolving to an incomplete tonic chord with a tripled root, single third, and no fifth. This sounds complete in context; the ear supplies the missing fifth from harmonic expectation.

The deceptive cadence (V–vi) exploits the same resolution logic while redirecting its destination. In C major, V7 resolves to A minor (vi) instead of C major (I). The two active tones still resolve correctly: B still moves up to C (which is now the third of Am rather than the root of C major), and F still moves down to E (the fifth of Am). The bass, however, moves from G not to C but to A — hence the "deception." The listener's ear follows the tritone resolution and hears a satisfying voice-leading motion, but arrives somewhere unexpected. This is why the deceptive cadence doesn't feel wrong — the internal logic of the active tones is honored — but creates surprise and often a sense of emotional continuation rather than closure.
