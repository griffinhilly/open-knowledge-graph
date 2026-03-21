---
id: part-writing-doubling-and-spacing-rules
title: Doubling and Spacing in Four-Part Writing
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: four-part-writing
  type: hard
- id: voice-leading-principles
  type: hard
builds-toward:
- voice-leading-smooth-stepwise-motion
- harmonic-function-voice-leading-tension-resolution
tags:
- four-part-writing
- spacing
- doubling
- voice-leading
stage: formal-systems
status: draft
---

# Doubling and Spacing in Four-Part Writing

## Core Idea
Doubling decisions and voice spacing are fundamental to effective four-part writing. In SATB textures, the root is typically doubled, with specific rules for weak inversions and chromatic chords. Proper spacing between adjacent voices (no more than an octave between soprano/alto, alto/tenor, and up to two octaves between tenor/bass) ensures acoustic blend and singability.

## Questions

```yaml
- question: "In a second-inversion triad (⁶₄ chord), which pitch should typically be doubled in four-part SATB writing?"
  type: multiple-choice
  options:
    - "The root of the chord, as always"
    - "The third of the chord, since it is in the soprano"
    - "The fifth of the chord, which is also the bass note"
    - "Any pitch may be doubled; second inversion has no preference"
  answer: 2
  explanation: "In second inversion, the fifth is in the bass. Because the second-inversion chord is harmonically unstable (the dissonant fourth above the bass), the convention is to double the bass note — the fifth — to anchor the chord. Doubling the root or third in second inversion would leave the chord without sufficient grounding and often leads to awkward voice-leading. This rule differs from root position (double the root) and first inversion (more flexibility, often double the soprano)."

- question: "A student is realizing a secondary dominant chord (V/IV) in SATB. Why should the raised scale degree — the chromatic note that makes it a secondary dominant — generally not be doubled?"
  type: multiple-choice
  options:
    - "Chromatic notes have unstable frequencies that cause acoustic beating"
    - "The chromatic pitch has a specific obligatory resolution direction; doubling it forces two voices into the same obligatory motion, which typically produces parallel octaves or awkward leaps"
    - "Doubling any altered pitch is forbidden in all species counterpoint rules"
    - "The chromatic note is always in the bass, so it cannot be doubled in upper voices"
  answer: 1
  explanation: "The chromatic pitch in a secondary dominant (e.g., a raised 4th scale degree) is a tendency tone that must resolve in a specific direction. If it is doubled, two voices are both obligated to resolve the same way — typically stepwise in the same direction — which almost inevitably produces parallel octaves. Avoiding the doubling leaves only one voice with that obligation, giving the other voices freedom to move in contrary motion and avoid parallels."

- question: "In four-part SATB writing, the standard spacing rule requires no more than an octave between any two adjacent upper voices (soprano-alto and alto-tenor)."
  type: true-false
  answer: true
  explanation: "This rule reflects acoustic blend: when soprano, alto, and tenor are spread more than an octave apart from their neighbors, the texture becomes thin or disconnected. The rule applies between adjacent pairs in the upper voices. The tenor-bass interval is given more freedom because the low register projects differently and a wider gap (a tenth or eleventh) is common and acoustically natural. The rule does NOT apply equally to all voice pairs — only to the three upper voices' adjacent spacing."

- question: "In a root-position major triad realized in four-part SATB writing, the fifth of the chord should be doubled because it provides the most harmonic stability."
  type: true-false
  answer: false
  explanation: "The standard choice in a root-position triad is to double the root, not the fifth. Doubling the root reinforces the harmonic foundation of the chord. Doubling the fifth is possible but less common and can lead to awkward voice-leading, particularly when the fifth must resolve in a specific way. Doubling the leading tone (the third of a dominant chord) is actively avoided because it forces both voices to resolve upward to the tonic, nearly guaranteeing parallel octaves."

- question: "Why is the chromatic pitch in chords like secondary dominants or augmented sixth chords typically avoided in doublings, and what happens when it is doubled?"
  type: short-answer
  answer: "The chromatic pitch is a tendency tone with a specific obligatory resolution — for example, a raised note must typically resolve upward by half step. If it is doubled, two voices are both forced into the same directional resolution, and since they are resolving to the same pitch in the same direction, the result is almost inevitably parallel octaves between those two voices. By keeping the chromatic pitch in only one voice, the other voices retain freedom to move in contrary or oblique motion, allowing the chromatic resolution to occur without generating prohibited parallels."
  explanation: "This is why the 'don't double the chromatic pitch' rule is really a voice-leading efficiency rule in disguise. Understanding it as a consequence of tendency-tone logic — rather than a memorized prohibition — allows you to apply it correctly to any chord containing an altered pitch, even in styles or contexts where the exact rules differ from common-practice conventions."
```

## Explainer

You've studied four-part writing and voice-leading principles. Now the focus sharpens: within any given chord, you have two simultaneous decisions to make — which pitch to double, and how far apart to space the four voices. These are related but distinct, and the reasons behind each rule illuminate what good four-part writing is trying to accomplish acoustically and functionally.

**Spacing** is about register and blend. The rule — no more than an octave between soprano and alto, or between alto and tenor, with more freedom between tenor and bass — reflects how human voices naturally blend in ensemble. When the upper three voices (soprano, alto, tenor) are crowded within a small range, the texture sounds dense and muddy. When they are spaced an octave or more apart, the sound opens up and each voice can be heard distinctly. The bass, by contrast, is given more range because the low register naturally projects differently; a tenor-bass gap of a tenth or eleventh is common in practice. **Close position** (all three upper voices within an octave of each other) and **open position** (voices spread more widely, each roughly an octave apart) are both valid; the choice affects color and weight, not correctness.

**Doubling** is about harmonic emphasis and voice-leading freedom, as you've begun to explore. In root-position triads, doubling the root is standard. In **first inversion** (third in the bass), you have more flexibility — the bass pitch is already the third, so the upper voices can distribute root, third, and fifth in various ways, and doubling the soprano note (whatever it is) often produces the smoothest connections. In **second inversion** (fifth in the bass, which is a weaker, more dissonant position used in specific contexts), the convention is to double the bass note — the fifth — because the chord is unstable and the doubled fifth helps anchor it. **Chromatic chords** — secondary dominants, borrowed chords, augmented sixths — carry their own specific constraints: the chromatic pitch (the raised or lowered note that gives the chord its color) is usually not doubled, both because it demands specific directional resolution and because doubling it would force two voices into the same obligatory motion.

The practical skill is developing an instinct for which combination of spacing and doubling produces the smoothest path through a progression. When you are given a series of Roman numerals to realize in SATB, your first move should be to place the bass (determined by the inversion), then place the soprano (often given or chosen for melodic interest), and then distribute the remaining chord tones between alto and tenor. The constraint is that each inner voice should move as little as possible — ideally by step or staying on a common tone — while landing on a pitch that makes the chord complete without forbidden doublings. Parallel octaves and fifths almost always result from one of two causes: a doubled leading tone that forces two voices to resolve to the same pitch, or an inner voice that leaps unnecessarily when a common tone or step was available. Learning to see these potential collisions before writing the next chord is the core skill that four-part writing exercises are training.

