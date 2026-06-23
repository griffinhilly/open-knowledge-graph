---
id: voice-leading-principles
title: Voice Leading Principles
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: intervals-basics
  type: hard
- id: interval-quality
  type: hard
- id: diatonic-harmony
  type: soft
- id: triads
  type: soft
- id: figured-bass
  type: soft
- id: non-chord-tones
  type: soft
- id: diatonic-chords-major-minor-keys
  type: soft
- id: harmonic-progression-analysis
  type: soft
- id: voice-leading-basics
  type: soft
builds-toward:
- four-part-writing
- counterpoint-basics
- dominant-seventh-resolution
tags:
- voice-leading
- parallel-fifths
- contrary-motion
- voice-independence
stage: formal-systems
status: validated
---
# Voice Leading Principles

## Core Idea
Voice leading refers to the horizontal motion of individual voices as harmony changes. The central principle is smoothness: voices should move by step when possible and avoid large leaps, preserving the independence and singability of each line. The two most important prohibitions in tonal voice leading are parallel perfect fifths and parallel perfect octaves — when two voices move in the same direction to the same interval class, their independence collapses. Contrary motion (voices moving in opposite directions) is the strongest tool for maintaining independence, while oblique and similar motion provide variety.

## How It's Best Learned
Work through pairs of chords mapping each voice's motion before writing anything. Use the 'sing-ability test': can a choral singer comfortably sing your line? Study Bach four-part chorales, tracking the motion of each voice pair and noting how parallel fifths and octaves are systematically avoided.

## Common Misconceptions
- Confusing parallel fifths (same two voices moving in the same direction, staying a fifth apart) with contrary fifths — only the former is prohibited.
- Thinking that any skip is problematic: in four-part writing, the bass frequently leaps by fourth, fifth, or octave.
- Treating voice-leading rules as arbitrary conventions rather than principles derived from perceptual clarity and voice independence.

## Questions

```yaml
- question: "Two voices both move upward from a perfect fifth to another perfect fifth. Which of the following best describes this?"
  type: multiple-choice
  options: ["Contrary motion, which is always acceptable", "Parallel fifths, which collapse voice independence", "Oblique motion between the two voices", "Similar motion that is permitted because the interval is consonant"]
  answer: 1
  explanation: "When two voices move in the same direction and maintain the same interval class (a perfect fifth), this is parallel fifths — one of the two most strictly prohibited patterns in tonal voice leading. The independence of the voices merges perceptually, undermining the texture. Contrary fifths, where voices move in opposite directions and arrive at a fifth, are perfectly acceptable."

- question: "A bass voice that leaps a perfect fifth between two chords violates standard voice-leading principles."
  type: true-false
  answer: false
  explanation: "Bass leaps of a fourth, fifth, or octave are common and stylistically normal in four-part writing. The prohibition on parallel fifths applies to two voices moving together in the same direction maintaining a fifth — not to any single voice leaping a fifth. The bass has the most freedom to leap because it defines harmonic roots rather than carrying a melodic line."

- question: "Why is contrary motion considered the strongest tool for maintaining voice independence?"
  type: short-answer
  answer: "When voices move in opposite directions, they cannot simultaneously arrive at the same interval by parallel motion, which prevents parallel fifths and octaves structurally. The diverging paths also emphasize the distinctness of each line perceptually."
  explanation: "Parallel and similar motion both risk landing voices on the same interval class simultaneously, which is how parallel fifths and octaves arise. Contrary motion eliminates that risk by construction — if one voice goes up and the other goes down, they cannot be moving in parallel. This is why contrary motion is the default preference when independence needs reinforcing."
```

## Explainer

Voice leading is the study of how individual voices — soprano, alto, tenor, bass — move horizontally as chords change. From your study of intervals, you know that a perfect fifth sounds open and stable, and a unison or octave sounds completely fused. These perceptual properties are exactly why voice leading has rules: harmony works when individual lines sound like independent voices with their own melodic identities, rather than a single blob of sound.

The guiding principle is smoothness. Stepwise motion (moving by a second) is preferred because it sounds singable and maintains the melodic identity of each voice. Leaps are acceptable, especially in the bass, but large or repeated leaps make a voice feel angular and hard to follow. The "singability test" is practical: could a real choral singer perform this line with ease and expression?

The most famous prohibition is parallel perfect fifths and parallel perfect octaves. When two voices both move in the same direction and stay a perfect fifth (or octave) apart, their independence collapses — the listener hears them as one voice, not two. This matters because four-part writing is a texture of four distinct lines; anything that merges two voices undermines the entire design. Contrary fifths — where one voice goes up and one goes down and they happen to arrive at a fifth — are fine, because the independent motion is audible.

The four motion types give you a vocabulary for thinking about voice pairs: contrary motion (opposite directions) is safest and most independence-preserving; oblique motion (one voice holds, one moves) is also unambiguous; similar motion (same direction, different interval) is usually fine but requires care at perfect intervals; parallel motion (same direction, same interval) is the one that must be managed most carefully. In practice, a good voice leading passage mixes all four types to keep the texture varied and each line interesting.

Studying Bach's four-part chorales is the single best way to internalize these principles. Track any two voices through a chorale and notice how rarely they move in parallel for more than one step, how the bass leaps freely while upper voices move by step, and how phrase endings use contrary motion to create strong closure. The rules are not arbitrary — they are the systematic description of what made Bach's textures sound so alive.
