---
id: accidental-detection-in-performance
title: Accidental Detection in Performance by Ear
domain: music
course: ear-training
prerequisites:
- id: accidentals-and-enharmonics
  type: hard
- id: key-signatures
  type: hard
builds-toward:
- error-detection-in-score
- chromatic-approach-voice-leading
tags:
- accidentals
- error-detection
- ear-training
- notation
stage: formal-systems
status: validated
---

# Accidental Detection in Performance by Ear

## Core Idea
Accidentals modify the natural pitch of scale tones, creating chromatic movement and harmonic color. The ability to hear when an accidental has been played incorrectly (or omitted entirely) develops critical listening skills and strengthens the connection between notation and sound.

## How It's Best Learned
Have a pianist or instrumentalist play a passage with some accidentals played correctly and some incorrectly. Your task is to identify which notes were played wrong and which were correct. Practice with single notes first, then chords with accidentals.

## Questions

```yaml
- question: "A performer plays a melody in D major (F# and C# in the key signature) and plays an F-natural instead of F#. The error passes almost unnoticed. Which explanation best accounts for this?"
  type: multiple-choice
  options:
    - "F-natural is not actually wrong in D major — it is an acceptable diatonic variant"
    - "The note was approached by step and the passage moved quickly, so the melodic contour masked the harmonic violation"
    - "Only trained musicians with perfect pitch can detect accidental errors, and the listener lacks that ability"
    - "The F-natural was a borrowed chord tone from D minor and was played intentionally"
  answer: 1
  explanation: "The explainer specifically notes that notes approached by step in fast-moving passages are hardest to detect because melodic contour can mask harmonic wrongness. The F-natural is wrong; the context conceals the error. Accidental errors are easiest to catch when the note is isolated, slow, or surrounded by context that makes the harmonic violation accumulate clearly."

- question: "A performer plays a C# in a passage notated in F major. After the C#, the line resolves upward to D as expected from the harmonic context. This is most likely:"
  type: multiple-choice
  options:
    - "A performance error — C# is foreign to F major and must have been played incorrectly"
    - "An intentional chromatic tone (a raised fourth degree pulling upward), correctly identified by its purposeful resolution"
    - "An enharmonic respelling of Db, which is a diatonic note in F major"
    - "A random error that happened to resolve in the right direction by coincidence"
  answer: 1
  explanation: "Intentional chromatic tones resolve purposefully: a raised fourth degree pulls upward, a lowered seventh pulls downward. The C# in F major resolving up to D fits this pattern exactly. The explainer's detective rule applies: if the 'wrong' accidental resolves as expected and fits the harmonic motion, it was probably intended. Option C is wrong — Db and C# are enharmonic, but Db is the correct diatonic note in F major, not C#."

- question: "Detecting accidental errors in performance is possible even before consciously naming the wrong note, because the ear automatically generates pitch expectations from an internalized key signature."
  type: true-false
  answer: true
  explanation: "The fundamental mechanism described in the explainer is expectation and violation. When you internalize a key signature, your ear automatically predicts which pitches are expected. A wrong note triggers a sense of wrongness before you consciously identify it. Training sharpens the gap between perception and naming until they happen nearly simultaneously."

- question: "A wrong accidental in a fast-moving passage is generally easier to detect than one in a slow passage, because fast notes draw more listener attention."
  type: true-false
  answer: false
  explanation: "The explainer states the opposite: notes moving quickly or approached by step are harder to detect because melodic contour masks the harmonic wrongness. Slow, isolated notes give the ear time to register and compare against expectations. In a fast passage, the sequence of pitches can produce an overall melodic shape that sounds plausible even if one pitch is wrong."

- question: "How does the concept of 'expectation and violation' explain why detecting accidental errors in performance is a distinct skill from knowing which notes belong to a key?"
  type: short-answer
  answer: "Knowing which notes belong to a key is declarative knowledge you can look up. Detecting errors in real time requires that knowledge to be automatic and predictive: your ear must be generating active expectations about each upcoming pitch moment to moment. When a wrong note arrives, it registers as a violation of that expectation — a sense of wrongness — before you have consciously checked it against the key signature. This predictive listening is trained separately from theoretical knowledge. A musician who knows D major theoretically but hasn't internalized it perceptually will not catch F-natural in a fast passage; one who has internalized the key will feel the violation immediately and then identify it."
  explanation: "The distinction between declarative and procedural knowledge is important here. Ear training is fundamentally about converting theoretical knowledge into automatic perceptual response. The 'expectation' is the internalized key grammar; the 'violation' is the detected error."
```

## Explainer

You already understand what accidentals *are* — sharps, flats, and naturals that alter a pitch away from the key signature's default. You know that a key signature establishes the expected pitch collection for a passage. Accidental detection in performance is the skill of using that knowledge in real time: hearing a pitch and immediately judging whether it matches the expected note or has been altered incorrectly.

The fundamental mechanism is **expectation and violation**. When you internalize a key signature — say, D major with F# and C# — your ear automatically predicts that any F or C in the music will be sharp. If a performer plays an F-natural in a D major context, the note sounds "off" in a very specific way: not just wrong in the abstract, but wrong relative to the harmonic grammar. That wrongness is perceptible even before you consciously name it, and training this skill means sharpening the gap between perception and naming until they happen nearly simultaneously.

The hardest situations are ones where the incorrect note is diatonically close to the correct one. A misplayed F-natural instead of F# may pass unnoticed if the passage is moving quickly or the note is approached by step — the melodic contour can mask the harmonic wrongness. This is why you practice not just single isolated notes but melodies in context: a note that sounds almost right in isolation often sounds obviously wrong in a longer phrase, because the phrase's harmonic implications accumulate. The wrong note fails to resolve where it should, or creates an unexpected harmonic color against an accompanying chord.

**Chromatic accidentals** — those used temporarily, outside the key — require a different kind of detection. When a composer intentionally writes a C# in an F major passage, the resulting chromatic tone is correct but distinctive: it sounds purposefully colorful. Learning to distinguish intentional chromaticism from performance error is a more advanced skill, requiring that you track both the written score (or your memory of the expected passage) and the harmonic logic. In practice, intentional chromatic tones typically resolve somewhere specific — a raised fourth degree pulls upward, a lowered seventh degree pulls downward. If the "wrong" accidental resolves as expected and fits the harmonic motion, it was probably intended; if it creates an ambiguous non-resolution, suspect error. This detective work is what makes ear training not just an academic exercise but a genuinely practical performance skill.
