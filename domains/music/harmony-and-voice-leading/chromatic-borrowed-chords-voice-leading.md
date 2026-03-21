---
id: chromatic-borrowed-chords-voice-leading
title: Borrowed Chords and Chromatic Voice Leading in Parallel Modes
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: borrowed-chords
  type: hard
- id: voice-leading-smooth-progressions
  type: hard
builds-toward:
- voice-leading-error-recognition-and-correction
tags:
- borrowed-chords
- parallel-mode
- chromatic-voice-leading
stage: formal-systems
status: draft
---

# Borrowed Chords and Chromatic Voice Leading in Parallel Modes

## Core Idea
Borrowed chords are chords from the parallel major or minor key, introducing chromatic voice leading into the harmony. Common borrowings include iv, v, and viidim7 from the parallel minor in a major key. Chromatic voice leading handles these chords differently from diatonic ones: chromatic alteration must resolve smoothly, often by stepwise motion. The voice leading of chromatic notes creates a distinctive color while maintaining overall coherence with the home key.

## Questions

```yaml
- question: "In C major, a composer uses the borrowed iv chord (F minor: F–A♭–C). How should the A♭ resolve in standard voice leading?"
  type: multiple-choice
  options:
    - "Down by half-step to G (the fifth of the tonic chord)"
    - "Up by half-step to A♮ (restoring the diatonic sixth)"
    - "Stay as a common tone — A♭ is shared between F minor and A♭ major"
    - "Move down by whole step to G♭, continuing the flat direction"
  answer: 0
  explanation: "The governing principle is that flatted chromatic tones resolve downward. A♭ is ♭6 imported from C minor; it resolves down by half-step to G (scale degree 5), which is the fifth of the C major tonic chord. This smooth semitone resolution is what gives the borrowed iv chord its characteristic poignancy. Option B (restoring A♮) could occur in some harmonic contexts but fights against the chromatic note's natural tendency and loses the expressiveness of the borrowed tone."

- question: "You encounter the chord B–D–F–A♭ in a passage clearly in C major. This chord is most likely:"
  type: multiple-choice
  options:
    - "The viidim7 borrowed from the parallel minor (C minor), where A♭ is ♭6"
    - "A secondary dominant seventh chord to the subdominant"
    - "The leading-tone seventh chord naturally occurring in C major"
    - "An augmented sixth chord with an enharmonic spelling"
  answer: 0
  explanation: "In C major, the diatonic leading-tone seventh is a half-diminished seventh: B–D–F–A♮. The fully-diminished version B–D–F–A♭ contains A♭, which is ♭6 — a note from C minor, not C major. This identifies it as a borrowed viidim7 from the parallel minor. All three non-root voices resolve by semitone: B→C, F→E (or F→G), A♭→G, giving it extraordinary voice-leading efficiency."

- question: "In a borrowed chord, a flatted chromatic tone (such as ♭6) should resolve downward by half-step, while a raised chromatic tone should resolve upward."
  type: true-false
  answer: true
  explanation: "This is the core principle of chromatic voice leading: chromatic tones resolve in the direction of their alteration. A flatted degree 'wants' to descend; a raised degree 'wants' to ascend. This mirrors the treatment of leading tones (raised 7̂ resolves up to 1̂) and chromatic passing tones. The logic is that the chromatic alteration creates a half-step tension that is released by moving in the direction the alteration points."

- question: "Borrowed chords destabilize the home key because their chromatic tones cannot be resolved without leaving the tonal center."
  type: true-false
  answer: false
  explanation: "Modal borrowing works precisely because the chromatic tones can resolve smoothly back into the home key. The A♭ in a borrowed iv chord resolves down to G (diatonic in C major); the B in the borrowed viidim7 resolves up to C (the tonic). The listener's tonal sense of home is maintained by the root motion and by the stepwise resolution of the chromatic voice. A borrowed chord is a guest that 'leaves gracefully' — the departure is the color, and the resolution maintains coherence."

- question: "What principle governs the voice leading of chromatic tones in borrowed chords, and why does following this principle make the borrowed chord sound coherent rather than arbitrary?"
  type: short-answer
  answer: "Chromatic tones must resolve in the direction of their alteration: flatted tones resolve down by half-step, raised tones resolve up by half-step. This principle makes borrowed chords coherent because the chromatic departure is immediately answered by a diatonic arrival — the borrowed tone slides into a pitch that belongs to the home key, maintaining tonal orientation while adding color. If the chromatic tone were voice-led against its natural tendency (forced into a leap or wrong direction), the borrowed chord would sound arbitrary and unresolved."
  explanation: "The expressiveness of borrowed chords comes from the combination of chromatic color and smooth resolution. The A♭ in a borrowed iv chord is 'exotic' relative to C major, but its half-step resolution to G is so smooth that the ear accepts the brief chromatic excursion as enriching rather than destabilizing. This is why half-step resolutions of chromatic tones are the default in tonal voice leading: they create maximum tension with minimum disruption to the tonal framework."
```

## Explainer

Your study of borrowed chords established that parallel modes — C major and C minor, for instance — share a root but differ in their scale degrees. C major has a natural A (scale degree 6), B♮ (scale degree 7), and E♮ (scale degree 3); C minor has A♭, B♭, and E♭. **Modal borrowing** means reaching into the parallel minor to pull out one of its chords and placing it in an otherwise major-key context. The effect is a sudden darkening or shading — a chromatic intrusion that enriches the harmonic color without abandoning the tonic. The borrowed chord introduces one or more flatted scale degrees that do not belong to the major scale, creating the chromatic voice leading challenge.

The most common borrowing in a major key is the **iv chord** (minor subdominant): in C major, that is an F minor chord (F–A♭–C). The A♭ is the borrowed note — it is ♭6, imported from C minor. When this chord appears, the A♭ must be voice-led carefully. In a iv–I progression, the A♭ most naturally resolves down by half-step to G (the fifth of the tonic chord). This smooth semitone resolution is what gives borrowed chords their characteristic expressiveness: the chromatic note slides into the diatonic note, creating a poignant, slightly bittersweet quality. If you voice-led that A♭ as if it were diatonic — skipping it or leaving it stranded — the borrowed chord sounds clumsy and arbitrary. The chromatic alteration earns its place by the smoothness of its resolution.

From your work with smooth voice-leading progressions, you know the foundational principles: prefer contrary motion, keep common tones, move voices by step when possible, avoid parallel perfect intervals. Borrowed chords add a new layer: **chromatic tones must resolve in the direction of their alteration**. A flatted degree (like ♭6) resolves downward; a raised degree resolves upward. This is analogous to the treatment of chromatic passing tones and leading tones you learned in earlier harmonic study. The ♭6 in the iv chord wants to descend. The ♭7 in the v chord (the borrowed minor dominant) similarly needs careful handling. Voice the chromatic tones to move stepwise in their natural direction, and the borrowed chord integrates smoothly. Force them into leaps or contrary directions, and the chromaticism feels unresolved.

The **viidim7 from the parallel minor** (in C major: B–D–F–A♭) is another common borrowing, especially as a leading-tone diminished seventh used for its strong resolution to tonic. Here three of the four notes resolve by half-step — B up to C, F down to E, A♭ down to G — making it a vehicle of powerful, compressed chromatic resolution. The voice leading writes itself: let each voice resolve by its natural semitone motion. When you see this chord in a major-key passage, recognize it as a borrowed diminished seventh and apply the same resolution logic you would use in a minor-key context.

The deeper principle is that modal borrowing works because the ear tolerates temporary chromatic intrusions as long as they resolve logically. The listener's tonal sense of "home" is maintained by the root and by smooth voice leading — a single flatted note in one voice does not destabilize the key as long as that note moves purposefully to a diatonic resolution. Think of the borrowed chord as a guest that brings an exotic flavor but knows how to leave gracefully. The chromatic departure is the color; the stepwise resolution is the coherence that keeps the harmony from feeling random.

## How It's Best Learned
Write progressions like I-iv-I in a major key, analyzing how the chromatic voices move and what happens if you try to voice-lead them diatonically instead. Compare the effect of different chromatic resolutions.
