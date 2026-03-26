---
id: melody-harmonization-with-voice-leading
title: Melody Harmonization with Voice-Leading Principles
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: voice-leading-basics
  type: hard
- id: harmonic-function-basics
  type: hard
- id: chord-progressions
  type: soft
- id: bass-line-writing-harmonic-function
  type: soft
builds-toward:
- four-part-writing
- voice-leading-in-composition
tags:
- harmonization
- melody
- voice-leading
stage: formal-systems
status: validated
---
# Melody Harmonization with Voice-Leading Principles

## Core Idea
Harmonizing a melody requires choosing appropriate chords and then voicing them to create smooth voice leading. The melody note becomes the soprano; inner voices and bass must move smoothly while supporting the harmonic progression.

## How It's Best Learned
Harmonize folk melodies with progressions; analyze how Bach harmonizes chorales; compare your solutions with existing harmonizations.

## Common Misconceptions
- The first appropriate chord is always the best choice; harmonic progression and voice leading may suggest a different chord.
- Voice leading rules are secondary to melody support; good voice leading enhances the melody's effect.

## Questions

```yaml
- question: "A melody has E on a strong beat. A student harmonizes it with E minor because 'E is the root of E minor.' The harmonization sounds weak in context. What is the most likely problem?"
  type: multiple-choice
  options:
    - "The chord was chosen by note-matching rather than by evaluating whether E minor creates a coherent harmonic progression in context"
    - "E minor is never an appropriate chord for harmonizing the note E"
    - "The student should have used a dominant chord on every strong beat for maximum harmonic drive"
    - "The melody note E forces a specific chord choice — only one chord is ever correct for a given note"
  answer: 0
  explanation: "Note E is a chord tone in several chords (E minor, C major, A minor, G major as the sixth, etc.). Choosing the chord that 'contains E' without considering context is note-matching. The real questions are: what function does this chord serve in the progression? Does it connect smoothly to the previous and next chord? Does it support the phrase's harmonic direction toward a cadence? A chord can contain the melody note and still produce a weak or incoherent progression."

- question: "A melody note falls on a weak beat and is clearly a passing tone between two structural chord tones. When harmonizing, you should..."
  type: multiple-choice
  options:
    - "Maintain the surrounding chord — passing tones do not require their own chord change"
    - "Find a chord that contains this passing tone as a chord tone, since every melody note must be supported harmonically"
    - "Insert a dominant chord on weak beats to create consistent rhythmic harmonic interest"
    - "Change the harmony on every beat to prevent the progression from sounding static"
  answer: 0
  explanation: "Non-harmonic tones — passing tones, neighbor tones, suspensions — exist between chord tones and do not need to be harmonized as if they were structural melody notes. Trying to give every note its own chord leads to over-harmonization: a congested, directionless progression where the actual harmonic rhythm becomes unclear. Recognizing which melody notes are structural and which are embellishing is one of the core analytical skills in harmonization."

- question: "In melody harmonization, non-harmonic tones such as passing tones do not require a new chord."
  type: true-false
  answer: true
  explanation: "True. Non-harmonic tones are melodic embellishments — they decorate the structural melody notes but are not chord tones themselves. Assigning a new chord to every melody note (including passing tones and neighbor tones) results in over-harmonization, which blurs the harmonic rhythm and weakens the sense of progression. The skill is knowing which beats are structurally important enough to require a chord change and which carry embellishing tones that should be sustained over an existing chord."

- question: "The chord that contains the melody note as a chord tone is typically the best harmonization choice."
  type: true-false
  answer: false
  explanation: "False. Most melody notes are chord tones in several different chords. The best choice among them depends on the harmonic progression: which chord connects smoothly to the previous and next chord? Which functional category (tonic, pre-dominant, dominant) does this moment in the phrase call for? Does the choice support a cadential arrival later? Note-matching alone gives no answers to these questions, and locally 'correct' chords can produce globally weak or directionless progressions."

- question: "Why should you analyze the entire melody — identifying cadence points and structural beats — before choosing any chords, rather than harmonizing note by note?"
  type: short-answer
  answer: "The structural cadence points (where the phrase comes to rest) are the anchors of the harmonization — they demand specific chord types (authentic cadence, half cadence) and constrain what must happen harmonically on the way there. If you choose chords note by note without knowing where the phrase is going, you may reach the cadence point with the wrong chord already in place, or create a progression that lacks functional direction. Analyzing the whole melody first reveals which notes are structural chord tones (requiring harmonization) and which are passing or neighbor tones (not requiring chord changes), and shows the harmonic rhythm and phrase direction."
  explanation: "This top-down approach is what separates harmonization from note-matching. Bach's chorales are canonical models precisely because every local choice — which chord, which inversion, how to move the inner voices — serves a larger phrase-level plan. The structural cadences are planned first; the rest fills in a functional path between them."
```

## Explainer

You already know the fundamentals of voice leading—smooth motion, contrary motion preferred, avoid parallel perfect intervals—and you understand harmonic function: how chords group into pre-dominant, dominant, and tonic categories, and how progressions create forward motion. Harmonizing a melody integrates these skills under a new constraint: the soprano line is *given*, and everything else must serve it while also forming a coherent progression. This is different from writing a progression from scratch; you're working backwards from melody to harmony and then layering voice leading on top.

The first step is **analyzing the melody before adding any chords**. Which scale degrees does each note represent? Notes on strong beats are often chord tones, especially at cadence points; notes on weak beats may be passing tones or neighbor tones that don't need to be harmonized as chord tones. Look for the structural cadence points: where does the melody come to rest? Those moments demand an authentic or half cadence. The melody itself suggests a harmonic rhythm—how often chords change—and sometimes the melodic contour implies a functional direction (a rising phrase pushing toward dominant, a stepwise descent pushing toward a final tonic).

Once you've identified the structural points and the implied harmonic rhythm, choose chords based on **functional logic, not just note-matching**. Every melody note above a given chord must be explainable as either a chord tone or a non-harmonic tone—but that still leaves several chord options for most notes. The choice between them should be guided by progression quality: does this chord connect smoothly to the next? Does the progression move through pre-dominant and dominant toward tonic at cadence points? Avoid choosing chords that are individually "correct" but produce a weak or repetitive progression when heard in sequence.

The final layer is **voice leading the inner voices** once the chord roots are chosen. Your soprano is fixed; your bass is largely determined (often the root, sometimes an inversion for smoother bass motion); your alto and tenor must fill in the chord tones while moving as smoothly as possible. Apply everything you know: prefer stepwise motion, resolve tendency tones (leading tone up, chordal seventh down), and maintain voice independence. Bach's four-part chorales are the canonical model precisely because he navigates all of these constraints simultaneously with extraordinary craft—analyzing even two or three chorales will teach you more about integrated harmonization than hours of abstract exercise.
