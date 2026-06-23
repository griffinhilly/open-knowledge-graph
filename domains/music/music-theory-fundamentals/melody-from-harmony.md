---
id: melody-from-harmony
title: Melody from Harmony
domain: music
course: music-theory-fundamentals
prerequisites:
- id: triad-construction-major-minor
  type: hard
- id: melodic-phrase-structure
  type: soft
builds-toward:
- voice-leading-principles
tags:
- melody
- harmony
- chord-tones
stage: formal-systems
status: validated
---

# Melody from Harmony

## Core Idea
Melodies are constructed primarily from chord tones (the pitches that make up the underlying harmony), with non-chord tones adding movement and interest. Understanding how to select chord tones for melody and identify them in existing melodies is fundamental. This skill bridges harmony and melody, showing how they work together.

## How It's Best Learned
Analyze melodies by identifying which notes come from the underlying chord and which are non-chord tones. Compose melodies over given progressions by selecting mostly chord tones with strategic non-chord tones.

## Common Misconceptions
Every note in a melody is a chord tone (most include non-chord tones). Melodies must be independent of harmony (they're deeply connected). Misidentifying chord tones when harmony isn't explicitly shown.

## Questions

```yaml
- question: "A melody moves C–D–E over a sustained C major chord (C–E–G). The note D is:"
  type: multiple-choice
  options:
    - "A chord tone of the C major triad — D is in the key of C major, so it belongs to the chord."
    - "A passing tone — a non-chord tone filling the stepwise gap between the chord tones C and E."
    - "An error — D should not appear over a C major chord in tonal music."
    - "The chord seventh, making this a Cmaj7 harmony."
  answer: 1
  explanation: "D is not part of the C major triad (C–E–G), so it is a non-chord tone. It moves by step between the chord tones C and E, making it a passing tone — the most common type of non-chord tone. The confusion in option A arises from conflating being in the key with belonging to the chord: D is diatonic to C major, but the triad sounding at this moment consists only of C, E, and G."

- question: "A student composing a melody places the note C on a strong downbeat over a G major chord (G–B–D). This choice:"
  type: multiple-choice
  options:
    - "Is perfectly fine — melodies are independent of the underlying harmony."
    - "Is fine because any note diatonic to the key fits any chord within that key."
    - "Is problematic — C is a non-chord tone, and placing it on a strong beat without immediate stepwise resolution creates awkward dissonance that undermines harmonic clarity."
    - "Automatically resolves because the next chord will accommodate C."
  answer: 2
  explanation: "C is not a member of the G major triad (G–B–D), so it is a non-chord tone. Non-chord tones are most effective on weak beats or weak parts of beats, resolving by step to a chord tone. Placing a non-chord tone on a strong downbeat without preparing and resolving it carefully creates unwanted dissonance that obscures the harmony. This is the practical application of the scaffold model: strong beats should be anchored by chord tones."

- question: "Chord tones are the most stable melodic resting points over a given harmony — they are the pitches that belong to the current chord, and melodies typically emphasize them on strong beats."
  type: true-false
  answer: true
  explanation: "This is the central architectural principle of tonal melody writing. Chord tones (root, third, fifth — and seventh in seventh chords) are the pitches that sound consonant with the underlying harmony without requiring resolution. Placing them on strong metric positions (downbeats, beat 1, beat 3 in 4/4) establishes harmonic clarity. Non-chord tones, by contrast, introduce tension and must be handled with care — typically on weaker positions with stepwise departure and return."

- question: "Because non-chord tones don't belong to the underlying harmony, skilled composers avoid them and write melodies consisting almost largely of chord tones."
  type: true-false
  answer: false
  explanation: "Quite the opposite: non-chord tones are essential to virtually all expressive tonal melody. A melody consisting only of chord tones sounds mechanical and static — like arpeggios. Non-chord tones (passing tones, neighbor tones, suspensions, etc.) add motion, direction, tension, and melodic interest between the stable chord-tone anchors. Skilled composers use them deliberately, placing them on weak beats with stepwise resolution so they enrich rather than destabilize the harmony."

- question: "Explain the difference between a chord tone and a non-chord tone, and describe how non-chord tones are typically handled so they don't undermine the harmonic framework."
  type: short-answer
  answer: "A chord tone is a pitch that is part of the currently sounding harmony (root, third, fifth, or seventh of the chord). A non-chord tone is any melody pitch that falls outside the current chord. Non-chord tones are managed through two conventions: metric placement (weak beats or weak parts of beats) and stepwise motion (they typically arrive by step and leave by step, resolving to a nearby chord tone). This ensures they are heard as momentary tensions within the harmonic framework rather than as contradictions of it."
  explanation: "The passing tone (filling a step gap between two chord tones), neighbor tone (stepping away from a chord tone and immediately returning), and suspension (holding over a pitch from the previous chord before resolving) are all defined by this combination of metric subordination and stepwise resolution. When you hear an unstable note in a melody, you are hearing a non-chord tone; when it resolves, the harmonic framework reasserts itself."
```

## Explainer

From your study of triads, you know that a major or minor triad consists of three pitches — a root, a third, and a fifth — stacked in thirds. When a piece of music has an underlying harmony, say a C major triad (C–E–G), those three pitches are the **chord tones**: the pitches that "belong to" the current harmony. The central insight of this topic is that melody and harmony are not independent layers — a melody is built largely on top of the harmonic skeleton, and the chord tones of each underlying harmony are the most stable, natural resting points for a melody at that moment.

Think of the chord tones as a scaffold. A melody can use them directly — a melody over a C major chord might simply leap from C to E to G and back, outlining the chord as an arpeggiated figure. This is the safest and most harmonically clear approach: every note lands on a pitch that "fits" the chord, and the result sounds stable and grounded. Much of folk melody, bugle calls, and fanfares works this way — "Reveille" and "Taps" consist almost entirely of chord tones from a single triad, which is why they can be played on an instrument with no valves.

Real melodies, however, use **non-chord tones** to add motion, tension, and interest between the stable chord-tone anchors. The most common types are: **passing tones**, which fill the stepwise gap between two chord tones (C moving to E by passing through D); **neighbor tones**, which step away from a chord tone and immediately return (C up to D and back to C); and **suspensions**, in which a pitch from the previous chord is held over into the new chord before resolving down by step. Non-chord tones are typically placed on weak beats or weak parts of beats (making them rhythmically subordinate), and they resolve by step to a nearby chord tone (making them melodically purposeful). When you hear a melody note that sounds slightly tense or unstable, you are likely hearing a non-chord tone.

To analyze a melody in this framework, you must work from the bottom up: first identify the underlying harmony at each point, then determine which melody notes match the chord tones and which do not. In practice, the harmonic rhythm (how often the chord changes) tells you which chord is "active" at each moment. Once you know the active chord, any melody note that matches one of the chord tones is a chord tone; any note that does not is a non-chord tone, and you should then identify what type it is by observing how it moves. Composing melodies over given harmonies uses this in reverse: start by sketching chord tones on strong beats to establish harmonic clarity, then add non-chord tones on weaker beats to create motion and shape. The relationship between melody and harmony is not coincidence — it is architecture.


