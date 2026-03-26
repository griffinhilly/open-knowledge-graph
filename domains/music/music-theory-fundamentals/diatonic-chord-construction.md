---
id: diatonic-chord-construction
title: Building Diatonic Chords from Scales
domain: music
course: music-theory-fundamentals
prerequisites:
- id: major-scales
  type: hard
- id: triad-construction-major-minor-diminished
  type: hard
builds-toward:
- chord-function-application
- harmonic-progression-patterns
tags:
- harmony
- scales
- chord-construction
stage: formal-systems
status: validated
---

# Building Diatonic Chords from Scales

## Core Idea
Diatonic chords are built using only the pitches in a given scale. In major scales, triads built on scale degrees follow a pattern: I, ii, iii, IV, V, vi, vii°. In minor scales, the pattern varies depending on whether natural, harmonic, or melodic minor is used, creating different chord qualities.

## How It's Best Learned
Build chords on each scale degree of a major scale, then minor scales, and listen to the harmonic colors. Identify diatonic chords in song analyses.

## Common Misconceptions
Not all chords in a piece are diatonic to a single key—pieces often borrow chords from parallel keys or modulate to new keys, introducing chromatic harmony.

## Questions

```yaml
- question: "In the key of G major, a musician builds a triad on the 2nd scale degree (A) using only notes from the G major scale. What is the quality of this chord?"
  type: multiple-choice
  options:
    - "Major, because A is a natural note present in the scale"
    - "Minor, because stacking thirds above A using only G major scale tones produces a minor triad (A–C–E)"
    - "Diminished, because the second scale degree is always diminished in major keys"
    - "Augmented, because A to C is a minor third and C to E is a major third"
  answer: 1
  explanation: "Stacking thirds from A using only G major scale notes gives A–C–E. A to C is a minor third (1.5 steps), C to E is a major third (2 steps): minor + major = minor triad. The pattern I–ii–iii–IV–V–vi–vii° is fixed in every major key, so the chord on the 2nd degree is always minor. Option C is wrong — the diminished chord sits on the 7th degree, not the 2nd. Option D reverses the interval order."

- question: "Why do composers almost always use the raised seventh degree (from harmonic minor) rather than the natural seventh when writing the V chord in a minor key?"
  type: multiple-choice
  options:
    - "Because harmonic minor is always more correct than natural minor"
    - "To create a major V chord with a leading tone that produces strong resolution to the tonic"
    - "Because natural minor has no fifth scale degree"
    - "To avoid parallel octaves in four-part writing"
  answer: 1
  explanation: "In natural minor, the V chord is minor (e.g., in A minor: E–G–B). The G is a whole step below A, which produces only weak pull toward the tonic. Raising the seventh (G to G#) creates E–G#–B, a major V chord with G# as a leading tone — a half step below A — generating powerful upward resolution. This is the harmonic engine of nearly all tonal cadences in minor keys. The other options describe rules that are either incorrect or secondary considerations."

- question: "In every major key, the chord built on the seventh scale degree is a diminished triad."
  type: true-false
  answer: true
  explanation: "Stacking thirds from the seventh degree using only scale tones always produces two minor thirds in a row (m3 + m3), which is the definition of a diminished triad. In C major: B–D–F. B to D is a minor third; D to F is also a minor third. This pattern holds in every major key because the interval structure of the major scale is fixed. The seventh degree is the only one that produces diminished quality; all others produce major or minor triads."

- question: "Playing mainly diatonic chords in a key guarantees that the resulting progression will be fully consonant and contain no dissonance."
  type: true-false
  answer: false
  explanation: "Diatonic does not mean consonant. The vii° chord (diminished triad) is inherently dissonant — the interval between its outer notes is a diminished fifth (tritone), which creates significant tension. Even 'consonant' diatonic chords create functional tension: the V chord strongly wants to resolve to I regardless of its own internal consonance. Diatonic simply means 'using only notes from the scale'; the harmonic function and dissonance level of each chord is a separate question."

- question: "Why is the chord quality pattern I–ii–iii–IV–V–vi–vii° identical in every major key, regardless of which key you're in?"
  type: short-answer
  answer: "Because every major key has the same interval structure — whole, whole, half, whole, whole, whole, half steps — so stacking thirds above each scale degree using only scale tones always produces the same sequence of major and minor thirds. The relative spacing between notes is identical in every major key; only the pitch names change. The chord quality is determined by interval relationships, not by the specific pitches, so the pattern is invariant."
  explanation: "This is the key insight: the major scale formula is universal, so the diatonic chord pattern it generates is universal. A student who memorizes I–ii–iii–IV–V–vi–vii° has memorized a fact about every major key simultaneously, not just C major. The same logic applies to minor keys, but three variants of the minor scale mean three slightly different chord patterns are possible."
```

## Explainer

You already know how to build major and minor triads from intervals: a major triad is a major third plus a minor third (root–M3–m3), and a minor triad reverses the order (root–m3–M3). You also know how to build major scales. **Diatonic chord construction** is the result of applying triad-building systematically to every degree of a scale, using only the notes already in the scale. The result is a family of chords that all "belong" to the key together — and each has a distinct quality and function.

Here is how it works in C major. Take each scale degree (C, D, E, F, G, A, B) as a root, and stack thirds above it using only the white keys. C–E–G is a major triad (M3 + m3). D–F–A is a minor triad (m3 + M3). E–G–B is minor. F–A–C is major. G–B–D is major. A–C–E is minor. B–D–F is a **diminished triad** (m3 + m3) — the one quality that doesn't appear in the major-third/minor-third pairings of major and minor chords. In every major key, the pattern is the same: **I–ii–iii–IV–V–vi–vii°**. Roman numerals by convention use uppercase for major chords and lowercase for minor, with a degree symbol (°) for diminished. Memorizing this pattern is one of the most useful things you can do in music theory, because it tells you immediately what chords are available in any key.

Why does this pattern matter? Because it provides the harmonic vocabulary of tonal music. When you hear a chord progression in a pop song, a Bach chorale, or a jazz standard, you are almost always hearing relationships between scale-degree chords. The **I chord** (tonic) feels like home. The **V chord** (dominant) creates tension that wants to resolve back to I — this is the engine of nearly all tonal harmonic motion. The **IV chord** (subdominant) provides contrast without strong pull. The **ii chord** often prepares the V, creating the ii–V–I progression that is the backbone of jazz harmony. The **vi chord** (relative minor) shares two notes with the I chord and can substitute for it or provide a darker alternative. Understanding the chord's scale-degree number tells you its likely function before you've even heard how it sounds.

Minor keys are more complicated because there are three versions of the minor scale — natural, harmonic, and melodic — each producing slightly different diatonic chords. The key practical difference is that **harmonic minor** raises the seventh scale degree to create a leading tone, which makes the V chord major (rather than minor as it would be in natural minor). This is harmonically powerful: a major V chord in a minor key creates strong resolution to the tonic, which is why composers almost always use the harmonic minor's raised seventh when approaching cadences. In natural minor, the V chord is minor (v), which feels more ambiguous and modal. Knowing which scale you're drawing from explains why certain chord choices in minor keys sound "classical" versus "modal" versus "folk."
