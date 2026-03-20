---
id: pitch-and-frequency
title: Pitch and Frequency
domain: music
course: music-theory-fundamentals
prerequisites:
- id: ratios
  type: soft
- id: logarithms-intro
  type: soft
builds-toward:
- staff-and-clefs
- note-names-and-octaves
- intervals-basics
tags:
- pitch
- acoustics
- fundamentals
stage: formal-systems
status: validated
---

# Pitch and Frequency

## Core Idea
Pitch refers to how high or low a musical sound is, determined by the frequency of its sound wave measured in hertz (Hz). Higher frequencies produce higher pitches; doubling the frequency raises the pitch by one octave. Western music organizes pitch into discrete named notes rather than a continuous spectrum. The perception of pitch is both physical (frequency) and psychological (how the ear and brain interpret sound).

## How It's Best Learned
Experiment with instruments or a piano keyboard to hear how pitch changes as you move higher or lower. Use a tuner app to see frequency values for notes you sing or play. Compare pitches that are one octave apart to hear the doubling relationship.

## Common Misconceptions
- Pitch and volume are often confused — a louder sound is not a higher-pitched sound.
- 'Frequency' and 'pitch' are related but not identical: frequency is a physical measurement, pitch is the perceptual experience.

## Questions

```yaml
- question: "If A4 has a frequency of 440 Hz, what is the frequency of A5, one octave higher?"
  type: multiple-choice
  options: ["480 Hz", "880 Hz", "220 Hz", "540 Hz"]
  answer: 1
  explanation: "An octave corresponds to a 2:1 frequency ratio. Going up one octave from A4 (440 Hz) doubles the frequency: 440 × 2 = 880 Hz. Going down one octave to A3 halves it: 440 ÷ 2 = 220 Hz. This doubling relationship is consistent across every pair of octave-related notes in Western music."

- question: "A louder sound has a higher pitch than the same note played quietly."
  type: true-false
  answer: false
  explanation: "Loudness (amplitude) and pitch (frequency) are independent properties of a sound wave. A trumpet and a flute can both play A4 at 440 Hz — the same pitch — at very different volumes. Increasing amplitude makes a sound louder but does not raise its frequency or its perceived pitch. Confusing these two dimensions is one of the most common errors for beginners."

- question: "What is the difference between frequency and pitch, and why does the distinction matter?"
  type: short-answer
  answer: "Frequency is the physical measurement of how many complete vibration cycles occur per second (Hz). Pitch is the perceptual experience of how high or low a sound seems to a listener. They are closely correlated but not identical: pitch perception is also influenced by loudness, duration, and context, whereas frequency is an objective property of the sound wave."
  explanation: "The distinction matters because tuning, acoustics, and psychoacoustics each operate at different levels. An audio engineer measures frequency; a musician hears pitch. Two tones at the same frequency can seem slightly different in pitch at very different loudness levels (a psychoacoustic effect called the Stevens effect). Keeping the concepts separate prevents confusion when moving between physics and music."
```

## Explainer

Every musical sound begins as a vibration — a rapid back-and-forth movement of air molecules set in motion by a string, a column of air, or a vibrating surface. The **frequency** of that vibration is measured in hertz (Hz): a frequency of 440 Hz means the air completes 440 full oscillation cycles every second. Higher frequency means faster oscillation; lower frequency means slower oscillation. This is a purely physical quantity that can be measured with a microphone and a spectrum analyzer.

**Pitch** is how the ear and brain interpret that frequency. When frequency is higher, we perceive a higher pitch. But pitch is a perceptual event, not a physical one. The same frequency can seem slightly different in pitch depending on its loudness, duration, and surrounding context — a phenomenon studied in psychoacoustics. Under ordinary musical listening conditions the two track each other so closely that musicians often use the terms interchangeably, but the distinction becomes important when studying tuning, acoustics, or why our perception of music doesn't reduce neatly to physics. A common error is conflating pitch with loudness: a loud note and a soft note at the same frequency have the same pitch but different volumes. They are independent dimensions of sound.

The most fundamental pitch relationship in Western music is the **octave**. Two notes an octave apart have a 2:1 frequency ratio. A4 vibrates at 440 Hz; A5 vibrates at 880 Hz; A3 at 220 Hz. Doubling the frequency always raises pitch by exactly one octave; halving it lowers by one octave. This relationship emerges from physics — it appears naturally in the harmonic series produced by vibrating strings and air columns — and from psychoacoustics, since the auditory cortex treats frequency doublings as a special kind of sameness. The result is **octave equivalence**: notes an octave apart are perceived as remarkably related, almost as the "same note in a different register."

Western music further divides each octave into 12 equal steps called semitones, using a tuning system called **equal temperament**. Because the octave spans a 2:1 ratio and is divided into 12 equal steps, each semitone represents a frequency ratio of the twelfth root of 2 (approximately 1.0595). Going up 12 semitones multiplies the frequency by 2 — arriving back at the octave. This logarithmic structure is why pitch perception feels linear (each semitone sounds like the same "size" of step) even though the underlying frequencies grow exponentially. If you've studied logarithms, you can see that the cent — a unit for measuring tiny pitch differences — is defined in terms of the logarithm base 2 precisely to make equal steps feel equal.
