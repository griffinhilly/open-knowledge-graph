---
id: extended-chords-ninths-elevenths-thirteenths
title: 'Extended Chords: Ninths, Elevenths, and Thirteenths'
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: seventh-chords
  type: hard
- id: intervals-basics
  type: soft
- id: chord-inversions
  type: soft
builds-toward:
- jazz-chord-symbols
- jazz-harmony-basics
tags:
- extended-chords
- ninth
- eleventh
- thirteenth
- jazz
stage: formal-systems
status: validated
---

# Extended Chords: Ninths, Elevenths, and Thirteenths

## Core Idea
Extended chords add intervals beyond the seventh to a chord's basic structure: the ninth (an octave plus a second above the root), the eleventh (an octave plus a fourth), and the thirteenth (an octave plus a sixth). These chords are built by stacking diatonic thirds above a seventh chord, producing rich sonorities characteristic of jazz, impressionism, and late Romantic harmony. In practice, not all chord tones are voiced simultaneously — the eleventh is often omitted from major chords because it clashes with the third, and the fifth is routinely dropped to keep voicings manageable. The ninth can be major (natural), minor (flat nine), or augmented (sharp nine), each with a distinctive color.

## How It's Best Learned
Build extended chords from the root up at the keyboard, naming each interval as you add it. Then practice jazz voicings that omit the root and fifth, focusing on the third, seventh, and the extended tone. Listen to jazz piano recordings (Bill Evans, McCoy Tyner) to hear how extended chords are used in context.

## Common Misconceptions
- Treating 9th, 11th, and 13th chords as always requiring all lower extensions: a '13th chord' in jazz often contains only selected notes, not a complete stack.
- Confusing the interval number with the scale degree number: the 9th in a C9 chord is D (same pitch class as scale degree 2), but the distance is a ninth from the root.
- Adding an 11th indiscriminately to a major chord: the natural 11th creates a strong dissonance with the major third and is usually raised (#11) or omitted.

## Questions

```yaml
- question: "A jazz pianist needs to voice a Cmaj13 chord. The full theoretical chord contains seven tones: C, E, G, B, D, F, A. Which tones should be prioritized in a practical shell voicing?"
  type: multiple-choice
  options:
    - "Root (C), third (E), and seventh (B) — the foundational tones that define the chord quality"
    - "Root (C), fifth (G), and thirteenth (A) — the outermost tones for maximum harmonic span"
    - "Third (E), seventh (B), and thirteenth (A) — shell voicing drops root and fifth"
    - "Fifth (G), eleventh (F), and thirteenth (A) — the upper extensions provide the most color"
  answer: 2
  explanation: "Shell voicing drops the root (covered by the bass player) and the fifth (acoustically redundant — the overtone series implies it). The essential tones that must remain are: the third (defines major/minor quality), the seventh (defines chord type: dominant, major 7th, or minor 7th), and the extension that gives the chord its characteristic color (here, the thirteenth). These three tones imply the full extended chord in context without crowding any register. Option A wastes a voice on the root while leaving out the extension entirely."

- question: "Why is the natural 11th (perfect fourth above the octave) typically omitted or raised to a #11 in major seventh chords?"
  type: multiple-choice
  options:
    - "It is too high in register to blend smoothly with the lower chord tones"
    - "It creates an unresolved tritone with the seventh that makes the chord sound dominant"
    - "It forms a half-step dissonance with the major third, creating a clash that obscures the chord's quality"
    - "It duplicates scale degree 4, which is already implied by the root's position in the key"
  answer: 2
  explanation: "The natural 11th (F in a C major chord) is only a half-step above the major third (E). This minor-second clash creates a harsh dissonance that obscures whether the chord is major or suspended — it actively undermines the chord's identity. Raising it to #11 (F#) solves this: the augmented fourth creates a tritone with the root, producing the lush Lydian sound characteristic of Cmaj#11 chords. The solution to the 11th problem is not just omission but the choice between omission and raising."

- question: "The '9' in a C9 chord refers to the same note as scale degree 2 (D), so a C9 chord functions the same way as a C major chord with an added 2nd."
  type: true-false
  answer: false
  explanation: "Though the pitch class is the same, the function and context are entirely different. A 'C add2' places D in the context of a triad, while a C9 chord is a complete dominant seventh chord (C–E–G–B♭) with a ninth stacked on top. The '9' rather than '2' signals this: it communicates that the note functions as an extension above a seventh chord structure, not as a simple added tone to a triad. The B♭ is essential to the C9 sound. Chord symbol numbers carry functional information about the harmonic context in which the tone appears."

- question: "In jazz voicings, the fifth of an extended chord is routinely omitted because it adds little harmonic information in context."
  type: true-false
  answer: true
  explanation: "The fifth is acoustically redundant because it is strongly implied by the overtone series of the root — the ear infers it without hearing it explicitly. More importantly, the fifth adds no information about chord quality (major/minor) or function (dominant/major7/minor7) — that information comes from the third and seventh. Dropping the fifth frees a voice for an extension (9th, 11th, or 13th) that adds genuine color. Shell voicings became standard jazz piano practice precisely because they maximize harmonic information with minimum notes."

- question: "Why do extended chord tones use numbers beyond the octave (9, 11, 13) rather than simply restarting at 2, 4, and 6 after the octave?"
  type: short-answer
  answer: "The higher numbers signal that these tones function as extensions above a complete seventh chord structure, not as simple added intervals to a triad. A 'C add2' places D in a triadic context; a 'C9' implies a full dominant seventh chord with D stacked on top. The number '9' rather than '2' communicates this functional difference to performers — it tells them a 7th must also be present. Interval numbers in chord symbols are not just distance measurements; they carry information about the note's harmonic role and what lower chord tones are implied."
  explanation: "The spiral metaphor is useful: after 8 (octave), the numbering continues rather than restarting. Scale degree 2 and interval 9 are the same pitch class but different functional contexts. A 9th chord requires a 7th chord underneath it; an added 2nd does not. This distinction matters practically: a jazz musician seeing '9' knows to include the 7th; seeing 'add2' knows not to. The notation system encodes theoretical function efficiently."
```

## Explainer

You've built seventh chords — triads with a seventh stacked above the root, creating four-note sonorities that carry new tension and color. You understand intervals as measured diatonic distances. Extended chords simply continue the stacking process: if a seventh chord is a triad plus a third on top, a **ninth chord** is a seventh chord plus one more third, and so on up the diatonic stack. The interval names reflect the total distance from the root — the ninth is one octave plus a major or minor second, the eleventh is one octave plus a perfect fourth, the thirteenth is one octave plus a major or minor sixth.

Think of the interval numbers as a spiral rather than a straight line. After the octave (8), we don't restart at 1 — we continue: 9 is the same pitch class as scale degree 2, 11 is the same pitch class as scale degree 4, 13 is the same pitch class as scale degree 6. The distinction matters because the number signals the note's function. In a Cmaj9 chord (C–E–G–B–D), the D functions as a **ninth** — an extension above a complete seventh chord — not as a simple second within a triad. The context of the full chord changes how the note is heard and how it should be voiced.

The practical reality is that these chords are rarely voiced with all their theoretical notes. A C13 chord contains seven distinct pitches (C, E, G, B♭, D, F, A) — one per voice in a full orchestra, but far too many for two hands at a piano. Jazz practice developed **shell voicings** to solve this: drop the root (the bassist covers it), drop the fifth (acoustically redundant in most contexts), and keep the third (defines major/minor quality), the seventh (defines dominant/major 7th/minor 7th quality), and the extension that gives the chord its color. This produces a compact 3–4 note voicing that implies the full extended chord without crowding any register.

The most important expressive distinctions involve the ninth. A **major 9th** (♮9) is warm and open — characteristic of major seventh chords and lush Romantic harmony. A **flat 9** (♭9) places a half-step crunch above the root, giving dominant seventh chords a tense, dissonant quality used in flamenco, jazz, and late Romantic chromaticism. The **sharp 9** (#9) produces a collision: the #9 sounds like a minor third above the octave while the chord's major third is also present, creating an ambiguous major-minor clash heard in blues, rock, and funk. The "Hendrix chord" (E7#9) is the most famous example. These three flavors of the ninth alone give the dominant seventh chord enormous expressive range within a single harmonic function.
