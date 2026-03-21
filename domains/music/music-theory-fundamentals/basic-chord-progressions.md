---
id: basic-chord-progressions
title: Basic Chord Progressions
domain: music
course: music-theory-fundamentals
prerequisites:
- id: harmonic-function-basics
  type: hard
- id: chord-progressions
  type: soft
builds-toward:
- chord-progressions
- song-form
- cadence-authentic-plagal
tags:
- chords
- progressions
- function
stage: formal-systems
status: draft
---

# Basic Chord Progressions

## Core Idea
The most fundamental progressions follow predictable patterns based on harmonic function: I-IV-V-I, I-V-I, and IV-I cycle through tonic, subdominant, and dominant in musically satisfying ways. These patterns repeat countless times in Western music and provide templates for harmonic understanding. Learning to recognize and compose these basic progressions is essential.

## How It's Best Learned
Play or sing basic progressions on keyboard or instrument, feeling how each function leads to the next. Analyze existing songs to identify underlying progressions. Compose eight-measure progressions using I, IV, and V with smooth voice leading.

## Common Misconceptions
Progressions must always follow function strictly (exceptions exist for expressive effect). V always appears before I (IV can lead directly to I). Neglecting voice leading while focusing only on function.

## Questions

```yaml
- question: "A songwriter trying to create a strong cadence uses the progression V–IV–I instead of IV–V–I. Why does the first feel weaker as a final cadence, even though it uses the same three chords?"
  type: multiple-choice
  options:
    - "V–IV–I is weaker because the IV chord is higher in the scale than V, creating an awkward descent"
    - "V–IV–I moves from high tension back through departure before arriving home, which interrupts rather than intensifies the pull toward resolution"
    - "IV–V–I is stronger simply because it's more commonly used in Western music"
    - "The dominant (V) always sounds better when it comes last, just before the tonic"
  answer: 1
  explanation: "Harmonic function is directional: IV moves away from home (departure), V intensifies the need to return (tension), and I is arrival. In IV–V–I, the functions build logically: departure → intensification → resolution. In V–IV–I, the dominant creates tension but then the progression moves to subdominant — which is a 'departure' function — before arriving home. This releases some tension prematurely, weakening the final resolution. The functions are the same, but their order determines whether they accumulate or dissipate."

- question: "What is voice leading, and why does it matter even when every chord in a progression is harmonically correct?"
  type: multiple-choice
  options:
    - "Voice leading is the process of choosing which chord roots to use — it determines harmonic function"
    - "Voice leading refers to the smooth or stepwise motion of individual notes between chords; it determines whether a progression sounds polished or clunky even when the chord symbols are right"
    - "Voice leading is the assignment of chords to specific instruments or vocal parts"
    - "Voice leading means the melody notes always belong to the current chord"
  answer: 1
  explanation: "Two progressions can use identical chord symbols (e.g., I–IV–V–I) but sound very different depending on how individual voices move between chords. Good voice leading means each part moves by step or holds a common tone, avoiding large leaps. A progression with correct harmonic function but poor voice leading will sound clunky — notes jumping around unnecessarily, parallel fifths creating acoustic roughness. The harmony provides the functional logic; voice leading provides the smooth surface that makes it convincing."

- question: "The tension that makes the dominant (V) chord want to resolve to tonic comes partly from the leading tone — the note a half step below the tonic that creates a strong pull upward."
  type: true-false
  answer: true
  explanation: "In a major key, the dominant seventh chord (V7) contains the leading tone (scale degree 7), which is a half step below the tonic. This creates strong voice-leading pressure toward resolution: the leading tone 'wants' to rise a half step to the tonic, while the seventh of the chord 'wants' to fall a step to the third of I. This double resolution impulse is why the V–I cadence is so satisfying and why the dominant has the strongest directional pull of any chord function."

- question: "The dominant chord (V) must always appear immediately before tonic (I) — it cannot be followed by any other chord without destroying the progression's functionality."
  type: true-false
  answer: false
  explanation: "This is one of the common misconceptions the topic explicitly addresses. V can resolve deceptively to other chords (such as vi in a deceptive cadence), and IV can lead directly to I in a plagal cadence without V at all. Conventions exist and are musically meaningful, but they describe tendencies and defaults, not inviolable rules. Composers exploit these tendencies for expressive effect — a deceptive cadence (V–vi) creates surprise precisely because it withholds the expected resolution."

- question: "Why does the progression I–IV–V–I feel more satisfying than I–V–I, and what functional role does the IV chord specifically contribute?"
  type: short-answer
  answer: "The IV (subdominant) adds a sense of departure and expansion before the tension of V. I–V–I is the skeleton of tonal motion, but it jumps directly to tension without first moving away from home. Adding IV between I and V creates a three-part journey: establish home (I), move away (IV), intensify the need to return (V), arrive (I). The IV chord also introduces a different quality of motion — it's restless but not as sharply tense as V — which makes the eventual V and then I feel more earned."
  explanation: "Think of IV as providing 'narrative arc' to the progression. A story that goes 'home → away → adventure → home' is richer than one that goes 'home → back home again.' The subdominant is the 'moving away' function; it prepares the dominant rather than competing with it. This is why the blues progression (I–I–I–I / IV–IV–I–I / V–IV–I–I) works: the IV adds expansiveness in measures 5-6, and the V in measure 9 feels like a climax precisely because the departure and return have been given space."
```

## Explainer

You already know that chords have harmonic functions — **tonic** (home, rest), **dominant** (tension, pull toward home), and **subdominant** (motion away from home, preparation for dominant). A chord progression is what happens when you move through those functions in time. The most fundamental insight is that Western tonal music has a preferred direction of travel: away from home, through increasing tension, and back to rest. Chord progressions encode that journey.

The simplest progression, **I–V–I**, is the skeleton of that journey. The tonic (I) establishes home. The dominant (V) creates tension — in a major key, the dominant chord contains a leading tone just a half step below the tonic, and that half step desperately wants to resolve upward. When V resolves to I, you hear the tension release. Nearly every other progression in Western music is an elaboration of this fundamental pull. Play a G chord (V in C major) on a piano and leave it hanging — you'll physically feel the incompleteness. Then resolve to C (I) and feel the arrival.

The **subdominant** (IV) adds a different quality of motion: departure rather than return. I–IV moves away from home without creating the sharp tension of the dominant. That's why IV–V–I works so well: IV moves you away, V intensifies the need to return, and I completes the circuit. Listen to the blues progression — I–I–I–I / IV–IV–I–I / V–IV–I–I — and you can hear each function doing its job. Hundreds of rock, folk, and pop songs boil down to variations on these three chords because the functional relationships are inherently satisfying.

**Voice leading** is the craft that makes progressions smooth rather than lurching. When you move from one chord to the next, each individual note (voice) should move as smoothly as possible — preferably by step (one scale degree) or common tone (the note stays the same). In a I–V progression in C major, the E in the tonic chord (C–E–G) can stay as the third of the G chord (G–B–D becomes E... no wait — let's be concrete). The C moves down a step to B, the G stays as the fifth, and the E moves up to... this gets worked out in four-part voice leading. The principle is: avoid large leaps when small steps will do, and hold common tones when possible. Good voice leading is the difference between a progression that sounds polished and one that sounds clunky even when the chords are "correct."


