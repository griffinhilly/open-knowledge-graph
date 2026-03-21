---
id: harmonic-function-and-voice-leading-analysis
title: Harmonic Function and Voice-Leading Analysis
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: roman-numeral-analysis
  type: hard
- id: functional-harmony
  type: hard
- id: voice-leading-principles
  type: hard
builds-toward:
- chord-progression-patterns-and-function
- voice-leading-in-composition
tags:
- harmonic-analysis
- voice-leading
- function
stage: formal-systems
status: draft
---

# Harmonic Function and Voice-Leading Analysis

## Core Idea
Roman numeral analysis combined with voice-leading principles reveals how harmonic function shapes the movement of voices. Dominant chords drive resolution to tonic; subdominant chords prepare dominant; voice leading clarifies these functional relationships.

## How It's Best Learned
Analyze complete phrases from classical music, identifying both the Roman numerals and the voice-leading strategies that clarify harmonic function.

## Common Misconceptions
- Function is determined only by chord quality; voice leading is independent.
- All chords can be voiced equally well; some voicings obscure harmonic function.

## Questions

```yaml
- question: "In a V7–I resolution, which two voices carry the primary functional pull, and where do they resolve?"
  type: multiple-choice
  options:
    - "The root of V moves down a fifth to the root of I; the fifth of V leaps up a fourth"
    - "The leading tone (7̂) resolves up by half step to 1̂; the chordal seventh (4̂) resolves down by step to 3̂"
    - "All voices move in parallel motion to the nearest available chord tones of I"
    - "The leading tone resolves down by step; the seventh resolves up to avoid parallel motion"
  answer: 1
  explanation: "The leading tone (the third of V, scale degree 7̂) has a half-step upward pull toward the tonic (1̂) — this is the defining voice-leading signature of dominant function. The chordal seventh (4̂) has a downward pull, resolving by step to the third of I (3̂) — sevenths resolve down. These two simultaneous voice-leading motions ARE what creates the V7–I effect; they are not arbitrary rules but the mechanism of dominant function. When a voicing frustrates either resolution, the functional sense of arrival weakens."

- question: "You hear a voice in a harmonic progression ascend by half step into a chord tone. Without knowing the Roman numerals, what harmonic function does this most strongly suggest?"
  type: multiple-choice
  options:
    - "Subdominant function — stepwise motion prepares the dominant"
    - "Tonic function — the voice has arrived at a stable resting point"
    - "Dominant function — half-step ascent into a chord tone is characteristic leading-tone behavior"
    - "No specific function — voice-leading motion alone cannot indicate harmonic function"
  answer: 2
  explanation: "A half-step ascent into a chord tone is the hallmark of leading-tone behavior, and leading-tone behavior defines dominant function. This is the deeper point of the topic: you can read harmonic function from voice-leading motion, even before labeling the chord. Roman numerals predict voice-leading behaviors; voice-leading behaviors imply harmonic functions. A chord that contains a voice moving by half step toward a chord tone creates dominant tension regardless of its chord quality label."

- question: "Harmonic function (tonic, subdominant, dominant) is determined primarily by chord quality — major chords carry tonic function, diminished chords carry dominant function."
  type: true-false
  answer: false
  explanation: "Chord quality is not the basis of harmonic function. The vi chord (minor) has tonic function; the vii° chord (diminished) has dominant function; the ii chord (minor) has subdominant function. Function is determined by a chord's role in the T→S→D→T trajectory and by its voice-leading implications — particularly whether it contains the leading tone (dominant function), creates a sense of departure from rest (subdominant), or provides stability (tonic). A major chord on IV has subdominant function. Quality and function are correlated in some cases but are not the same thing."

- question: "A V7 chord that places the leading tone in the bass, then resolves to I with the bass leaping down a fifth to the root of I, produces a weaker dominant resolution because it frustrates the expected voice-leading behavior of the leading tone."
  type: true-false
  answer: true
  explanation: "The leading tone (7̂) has a strong half-step pull upward to 1̂. When the leading tone is in the bass, the strongest voice-leading resolution would be for the bass to step up by half step to the tonic. Instead, leaping the bass down a fifth fulfills the root-motion expectation but sacrifices the leading-tone resolution — the voice-leading mechanism of dominant function is frustrated. The resulting I chord may be harmonically labeled correct, but the functional pull has been dissipated. Voice-leading analysis explains *why* certain voicings feel weaker."

- question: "Explain why the claim that 'voice leading and harmonic function are two separate analytical tools' is misleading."
  type: short-answer
  answer: "Voice leading is the mechanism through which harmonic function is enacted — they are the same phenomenon viewed from different angles. When V7 resolves to I, the leading tone ascends by half step and the seventh descends by step not as a stylistic convention but because those specific motions create the tension-resolution effect that constitutes dominant function. Reading music analytically means using both lenses simultaneously: Roman numerals predict specific voice-leading behaviors, and observed voice-leading motions imply specific harmonic functions. When expected voice leading is fulfilled, function is reinforced; when frustrated, the functional sense weakens. Treating them as independent layers misses the point that one is the cause and the other is the effect of the same underlying logic."
  explanation: "The practical payoff is bidirectional analysis: you can start from Roman numerals and predict how voices should move, then check whether they do; or you can start from voice-leading observations (a half-step ascent, a descending seventh) and infer the harmonic function. Violations of expected voice leading — when they occur deliberately — are among the most expressive choices in tonal music, which only becomes visible when you understand the expected behavior being violated."
```

## Explainer

You already know how to assign Roman numerals to chords and understand the principles of smooth voice leading — contrary motion, stepwise movement, avoidance of parallel fifths and octaves. This topic brings those two knowledge streams together: learning to see how voice leading *enacts* harmonic function, not merely accompanies it. Function and voice leading are not two separate analyses of the same music; they are the same phenomenon viewed from different angles.

**Harmonic function** divides chords into three families based on their role in the tonal drama. **Tonic function** chords (I, vi, iii) create stability and rest — they are home, or home-like. **Dominant function** chords (V, vii°) create tension that demands resolution to tonic — they contain the leading tone and often a tritone, both of which generate strong voice-leading pull. **Subdominant function** chords (IV, ii) create a sense of departure from tonic and preparation for dominant — they move the harmony away from rest without yet creating the sharp tension of dominant. The classical phrase typically moves T → S → D → T: depart, prepare, intensify, resolve. Every common chord progression in tonal music is a variation on this trajectory.

What makes this analysis powerful is recognizing that **voice leading is the mechanism of function**. When a dominant seventh chord resolves to tonic, it is not merely obeying a rule — specific voices are moving in specific ways that create the effect. The **leading tone** (7̂, the third of V) resolves upward by half step to the tonic (8̂/1̂) because it is a semitone below its target and has strong upward pull. The **seventh of V7** (4̂) resolves downward by step to the third of I (3̂) because sevenths resolve down. These two voices moving simultaneously create the characteristic V7–I sound. When you analyze a progression and see a V moving to I, ask: where is the leading tone in this voicing? Where is the seventh? Are they resolving as they should? A voicing that puts the leading tone in the bass and then skips it to a non-tonic note sounds weak because the voice-leading logic of function has been frustrated.

The deeper analytical skill is working in reverse: hearing a voice-leading motion and inferring the harmonic function. A half-step ascent in any voice toward a chord tone signals leading-tone behavior and suggests dominant function even if the chord is not V. A descending step through a dissonant interval suggests a seventh resolving and implies dominant or secondary dominant harmony. When you analyze music this way, Roman numerals become shorthand for predicted voice-leading behaviors — and when the voice leading violates the prediction, that is analytically significant. The interplay between expected function and actual voice motion is one of the richest resources for expression in tonal music.
