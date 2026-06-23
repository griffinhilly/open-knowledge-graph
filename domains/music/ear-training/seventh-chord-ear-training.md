---
id: seventh-chord-ear-training
title: Seventh Chord Identification by Ear
domain: music
course: ear-training
prerequisites:
- id: seventh-chord-construction
  type: hard
- id: chord-quality-by-ear
  type: hard
- id: diatonic-chord-quality-ear
  type: soft
- id: suspension-identification-ear
  type: soft
- id: dominant-seventh-chord-unique-quality
  type: soft
- id: tritone-dissonant-intervals-ear
  type: soft
builds-toward:
- extended-chord-ear-training
- secondary-dominants-ear
- harmonic-dictation-basic
tags:
- chords
- sevenths
- dominant
- maj7
- min7
- dim7
- dissonance
stage: formal-systems
status: validated
---
# Seventh Chord Identification by Ear

## Core Idea
Seventh chords add a dissonant seventh interval above the root, creating distinct harmonic colors. The dominant seventh (V7) is the most unstable and must resolve, while maj7 and min7 are more open in function. Diminished seventh chords (dim7) have a tight, symmetrical quality. Each seventh chord type has a characteristic sound that extends harmonic vocabulary beyond triads.

## How It's Best Learned
Start with V7 resolving to I in multiple keys, hearing the tritone pull inward. Then explore min7 and maj7 chords in jazz contexts, recognizing their stability compared to V7.

## Common Misconceptions
Treating seventh chords as fundamentally 'wrong' or 'dissonant' in all contexts—some sevenths (maj7, min7) are quite stable. Confusing maj7 with V7; maj7 has a quality 7th above the root, while V7 has a minor 7th.

## Questions

```yaml
- question: "You hear a four-note chord that sounds tense and directional — it seems to want to move somewhere else. Which chord type best matches this description, and what interval inside it creates that feeling?"
  type: multiple-choice
  options:
    - "Major seventh chord (maj7) — the major seventh interval creates the pull"
    - "Dominant seventh (V7) — it contains a tritone between the third and seventh that demands resolution"
    - "Minor seventh chord (min7) — the minor seventh is the most unstable interval"
    - "Diminished seventh (dim7) — its symmetrical structure creates tension without direction"
  answer: 1
  explanation: "The dominant seventh (V7) is defined by its tritone — the interval between its third and seventh. The tritone (augmented fourth / diminished fifth) is the most dissonant interval in tonal music and pulls inward toward resolution: the third rises by half step to the tonic, and the seventh falls by half step to the third of the tonic chord. This gives V7 its directional quality. Maj7 and min7 are more stable and open-ended. Dim7 is highly tense but symmetrical — it doesn't pull toward a single resolution the way V7 does."

- question: "A student confuses a major seventh chord (Cmaj7) with a dominant seventh chord (C7). What is the key structural difference they should listen for?"
  type: multiple-choice
  options:
    - "Cmaj7 has a minor third on top; C7 has a major third on top"
    - "Cmaj7 contains a major seventh interval above the root (only a half-step below the octave); C7 contains a minor seventh (a whole step below the octave), creating the tritone"
    - "They sound identical — the distinction is only visible in notation, not audible"
    - "Cmaj7 resolves to F; C7 resolves to G"
  answer: 1
  explanation: "The critical difference is the quality of the seventh. In Cmaj7 (C-E-G-B), the interval C→B is a major seventh — just a half-step below the octave, creating a dreamy, open sound. In C7 (C-E-G-B♭), the interval C→B♭ is a minor seventh — a whole step below the octave. This B♭ combined with the E creates the tritone (E→B♭), which gives C7 its tension and pull toward resolution on F major. Maj7 is stable and lush; V7 is tense and directional."

- question: "A diminished seventh chord has a distinctive symmetrical structure because every interval in the chord is a minor third."
  type: true-false
  answer: true
  explanation: "Yes — a dim7 chord (e.g., C-E♭-G♭-B♭♭) stacks four minor thirds, each exactly three semitones apart. This equal spacing creates perfect symmetry: the chord divides the octave into four equal parts. A consequence is that each of its four inversions is enharmonically equivalent to another dim7 chord in root position — there are only three genuinely distinct dim7 sounds. This symmetry makes dim7 harmonically ambiguous and useful for modulation in Romantic music."

- question: "A major seventh chord (maj7) is functionally unstable and demands resolution to the tonic, similar to a dominant seventh chord."
  type: true-false
  answer: false
  explanation: "Maj7 is among the more stable seventh chord types. It most often appears on the tonic (Imaj7) or subdominant (IVmaj7) and doesn't demand resolution — in jazz, Imaj7 IS the stable resting point. The dominant seventh (V7) demands resolution because of its tritone. Maj7's seventh is only a half-step from the octave, creating a rich, lush color without the pushing tension of the tritone. Conflating these two is one of the most common errors in seventh chord ear training."

- question: "What is the tritone, and why does its presence in the dominant seventh chord give V7 its characteristic urgency and pull toward resolution?"
  type: short-answer
  answer: "The tritone is the interval of three whole tones (6 semitones) — an augmented fourth or diminished fifth. In a dominant seventh chord (e.g., G7: G-B-D-F), the tritone occurs between the third (B) and seventh (F). This interval is maximally dissonant in tonal music and wants to resolve inward: B rises a half-step to C (the tonic), and F falls a half-step to E (the third of the tonic chord). This double voice-leading motion is what makes V7 resolve so strongly to I."
  explanation: "The tritone's instability is both acoustic (its frequency ratios are complex) and contextual (centuries of tonal practice have conditioned listeners to hear it as needing resolution). Its resolution in V7→I is the most powerful cadential gesture in Western tonal music. Recognizing the tritone by ear — that particular tense, hanging quality — is the key to identifying dominant sevenths quickly."
```

## Explainer

Every chord you've identified by ear so far has been a triad—a stack of thirds comprising three pitches. Seventh chords add a fourth pitch, creating a dissonant interval (the seventh) above the root. That dissonance is not a flaw to be avoided; it is a functional resource. Different seventh chord types produce different qualities of dissonance, and recognizing those qualities by ear is the gateway to hearing harmonic color in jazz, classical, and virtually all Western tonal music.

Start with the **dominant seventh** (V7), the most functionally charged seventh chord in tonal music. It contains a **tritone** between its third and seventh—the interval that creates maximum tension and pulls the chord toward resolution. The tritone wants to collapse inward, with the third rising to the tonic and the seventh falling to the third of the tonic triad. The V7 sounds tense, directional, almost urgent in its need to resolve. Listen for this quality—it distinguishes V7 from every other seventh chord type.

The **major seventh chord** (maj7) sits at the opposite end of the stability spectrum. Built on major triads (most often on I or IV), the major seventh is only a half-step below the octave, creating a dreamy, open-ended quality rather than a pulling tension. In jazz, maj7 is a default tonic color—stable but richer than a simple triad. The **minor seventh chord** (min7) similarly softens the dominant's urgency; it appears on ii and iii in major keys, carrying subdominant or tonic function respectively. Neither maj7 nor min7 demands resolution the way V7 does.

The **diminished seventh chord** (dim7) deserves special attention because of its **symmetrical structure**: every interval is a minor third, making it divisible into four equal parts within the octave. This symmetry means a dim7 chord has only three distinct sound-types in terms of inversion (each inversion is enharmonically equivalent to another root position). Its tight, stacked quality and high dissonance create a distinctive tense character—the chord of melodrama and heightened emotion in Romantic music. Hearing the dim7 against V7 and min7 trains your ear to discriminate the most common seventh-chord types you'll encounter.
