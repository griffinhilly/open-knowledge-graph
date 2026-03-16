---
id: roman-numeral-analysis
title: Roman Numeral Analysis
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: diatonic-harmony
  type: hard
- id: triads
  type: hard
- id: key-signatures
  type: hard
- id: chord-progressions
  type: soft
builds-toward:
- functional-harmony
- four-part-writing
- secondary-dominants
- figured-bass
tags:
- analysis
- roman-numerals
- harmony
- diatonic
stage: abstract-reasoning
status: validated
---

# Roman Numeral Analysis

## Core Idea
Roman numeral analysis labels chords by the scale degree of their root, using uppercase numerals (I, IV, V) for major chords and lowercase (ii, iii, vi) for minor chords. This system abstracts harmonic function away from any specific key, making it possible to analyze and compare progressions across different tonalities. Quality modifiers (°, +, 7) extend the system to account for diminished, augmented, and seventh chords. Roman numerals reveal the structural logic of tonal music — why certain progressions feel stable or tense, resolved or unresolved.

## How It's Best Learned
Begin by analyzing simple I–IV–V–I progressions in C major to match the abstract numeral to the familiar sound. Then transpose the same progression to other keys to verify that the numerals capture function independent of pitch. Analyze songs you already know by ear, then check your analysis against a chord chart.

## Common Misconceptions
- Confusing the numeral with the pitch class: V in C major is G, but V in G major is D — the numeral tracks function, not absolute pitch.
- Forgetting that chord quality (major/minor) is implicit from the scale, not assigned arbitrarily.
- Using uppercase for all numerals regardless of quality.

## Questions

```yaml
- question: "In G major, the chord built on the fifth scale degree is D major. What is the correct Roman numeral label for this chord?"
  type: multiple-choice
  options: ["v", "V", "IV", "D"]
  answer: 1
  explanation: "The fifth scale degree in any key receives the numeral V. Because the chord built there in a major key is major, it is written in uppercase: V. Writing 'D' is the most common beginner error — it confuses the pitch name with the functional label. The whole point of Roman numerals is to be key-independent."

- question: "The Roman numeral 'V' always refers to the same pitch class (e.g., the note G) regardless of which key you are in."
  type: true-false
  answer: false
  explanation: "Roman numerals track harmonic function, not absolute pitch. V in C major is G, but V in G major is D, and V in F major is C. Confusing numerals with pitch classes is the most common misconception in learning this system."

- question: "Why are some Roman numerals written in uppercase (I, IV, V) and others in lowercase (ii, iii, vi) in a major key analysis?"
  type: short-answer
  answer: "The case signals chord quality. Uppercase numerals denote major chords; lowercase denote minor chords. In a major key, the chords built on scale degrees 1, 4, and 5 are naturally major (I, IV, V), while those on degrees 2, 3, and 6 are naturally minor (ii, iii, vi). Quality is determined by the key's scale, not assigned arbitrarily."
  explanation: "The diatonic scale already determines whether a triad built on each degree is major or minor. By matching case to quality, Roman numeral notation lets you read off both the root's position in the scale AND the chord type in a single symbol — more information than a letter name alone would provide."
```

## Explainer

When you learned diatonic harmony and triads, you discovered that stacking thirds on each note of a major scale produces chords of different qualities — some major, some minor, one diminished. Roman numeral analysis is the naming system that labels each of those chords by *where* in the scale its root sits, while simultaneously signaling its quality through capitalization.

The key insight is that the numeral tracks function, not pitch. In C major, the chord on the fifth scale degree is G major — labeled V. Transpose the whole piece to G major and the chord on the fifth degree is now D major — still labeled V. The Roman numeral V doesn't tell you which notes are playing; it tells you the chord's *role* in the key. That role — dominant function, strong pull toward resolution — is the same regardless of what key you're in. This abstraction lets you say "this jazz standard and that classical sonata both use a ii-V-I progression" and immediately know they share the same harmonic grammar, even if they're in different keys and sound nothing alike.

Capitalization is not decoration — it is data. Uppercase means the chord is major; lowercase means minor. In a major key, the pattern is fixed by the scale: I, ii, iii, IV, V, vi, vii°. You don't decide the qualities; the scale determines them. When you see "vi," you automatically know it is a minor chord rooted on the sixth scale degree — you don't need to check. Learning to produce and recognize this pattern by ear and on paper is the core skill this system builds.

Quality modifiers extend the system further: the degree sign (°) marks diminished chords (vii°), a plus sign (+) marks augmented, and superscript 7 adds the seventh (V7). These extensions follow the same logic — the symbol packages root position and chord quality together.

Roman numeral analysis is the shared analytical language of Western tonal music. Once you are fluent in it, you can read a chord chart in any key, understand why a progression creates tension or release, and compose your own progressions with intention rather than trial and error. It is the foundation for everything ahead: secondary dominants, modulation, figured bass, and four-part writing.
