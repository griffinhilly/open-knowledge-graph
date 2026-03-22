---
id: diatonic-chords-major-minor-keys
title: Diatonic Chords in Major and Minor Keys
domain: music
course: music-theory-fundamentals
prerequisites:
- id: diatonic-triad-harmonization
  type: hard
- id: minor-scale-types-comparison
  type: soft
builds-toward:
- harmonic-progression-analysis
- voice-leading-principles
tags:
- diatonic
- major-key
- minor-key
- harmony
stage: formal-systems
status: draft
---

# Diatonic Chords in Major and Minor Keys

## Core Idea
Each major and minor key contains seven diatonic triads built from its scale degrees. In major keys, triads are I (major), ii (minor), iii (minor), IV (major), V (major), vi (minor), and vii° (diminished). In minor keys, the diatonic chords vary depending on whether natural, harmonic, or melodic minor is used. The harmonic minor scale (with its raised seventh) provides a strong V chord natural to the key. Learning diatonic chords enables composition and analysis within keys without accidentals.

## How It's Best Learned
Build all diatonic triads in multiple major and minor keys. Analyze progressions in pieces to identify how composers use diatonic chords.

## Common Misconceptions
- Thinking minor keys have a single set of diatonic chords (the choice of minor scale variant affects chord qualities).
- Not recognizing that the vii° chord (diminished) is rarely used in root position and functions almost exclusively in first inversion.

## Questions

```yaml
- question: "A composer writing a cadence in A minor wants a strong dominant-to-tonic resolution. Why would they use E major (V) rather than E minor (v)?"
  type: multiple-choice
  options:
    - "E major is always brighter-sounding, which is required at cadence points by common-practice convention"
    - "E major comes from the harmonic minor scale and contains G#, the leading tone a half-step below the tonic, creating a strong gravitational pull toward resolution on A"
    - "E minor is not a diatonic chord in any form of A minor and therefore cannot be used"
    - "E major produces the parallel octaves that define an authentic cadence"
  answer: 1
  explanation: "The dominant's harmonic strength comes from the leading tone — the note a half-step below the tonic. In A minor, the tonic is A, so the leading tone is G#. E major (E–G#–B) contains G#; E minor (E–G–B) does not. G natural is a whole step below A, creating a much weaker pull. Harmonic minor was developed specifically to provide this G#, transforming the weak v into a powerful V. Option C is false: E minor (v) does occur in natural minor."

- question: "In natural A minor, what is the quality of the chord built on scale degree 5 (the notes E–G–B)?"
  type: multiple-choice
  options:
    - "Major — all dominant chords are major by definition in tonal harmony"
    - "Minor — and this lack of a leading tone weakens its pull toward the tonic"
    - "Diminished — the fifth scale degree always produces a diminished chord in minor"
    - "Augmented — the raised intervals from the minor scale create an augmented fifth"
  answer: 1
  explanation: "Natural minor uses only the unaltered scale tones. In A natural minor (A B C D E F G), the chord on scale degree 5 is E–G–B, which is a minor triad (minor third + major third). Because G is a whole step below the tonic A (not a half step), it lacks the leading tone's gravitational pull. This is why natural minor produces a weak 'v' and why harmonic minor raises the 7th to G# — restoring the major V and its strong resolution tendency."

- question: "Just as major keys have a single fixed pattern of diatonic chord qualities (I ii iii IV V vi vii°), each minor key also has exactly one set of diatonic chord qualities."
  type: true-false
  answer: false
  explanation: "This is the central misconception about minor-key harmony. Unlike major keys, minor keys draw chords from multiple scale variants — natural, harmonic, and melodic minor — each producing different qualities on certain scale degrees. For example, the chord on scale degree 7 in A minor is G major (natural minor) or G# diminished (harmonic minor). Composers freely mix these variants; there is no single 'correct' set of minor diatonic chords."

- question: "Raising the seventh scale degree in harmonic minor converts the v chord (minor triad) into a V chord (major triad), restoring the dominant's strong pull toward the tonic."
  type: true-false
  answer: true
  explanation: "This is precisely why harmonic minor exists. The seventh scale degree is the third of the dominant chord. In natural minor the seventh is lowered (e.g., G in A minor), making the dominant a minor triad (v) without a leading tone. Raising it by a half step (to G# in A minor) makes the dominant a major triad (V) containing the leading tone, which creates the tense half-step pull toward the tonic. The label 'harmonic' minor reflects this harmonic function."

- question: "Why does harmonic minor exist as a separate scale variant? What specific harmonic problem does it solve that natural minor cannot?"
  type: short-answer
  answer: "Harmonic minor exists to provide a major V chord in minor keys. Natural minor's seventh scale degree is a whole step below the tonic, so the dominant chord built on scale degree 5 is a minor triad lacking the leading tone. The leading tone — a note a half-step below the tonic — is what gives the dominant chord its strong pull toward resolution. By raising the seventh scale degree a half step, harmonic minor restores the leading tone and converts the weak v into a powerful V, enabling the authentic cadences that drive tonal harmony."
  explanation: "This question goes to the heart of why harmonic minor is called 'harmonic': it was shaped by harmonic necessity, not melodic preference. Composers kept natural minor for vocal lines (avoiding the awkward augmented second between scale degrees 6 and 7 that harmonic minor creates) but switched to harmonic minor at cadence points to get the V–i resolution. Understanding this explains both why harmonic minor has the interval structure it does and why composers treat the two variants as complementary rather than competing."
```

## Explainer

From your work with diatonic triad harmonization, you know how to build a triad on any scale degree. Now the goal is to internalize the complete family of chords that lives inside a single key — the **diatonic chord system**. Think of it as the palette a composer in a given key is working with: seven chords, each with a characteristic quality and a characteristic function, and together they define what "staying in the key" means.

In **major keys**, the seven diatonic triads follow a fixed pattern of qualities: I (major), ii (minor), iii (minor), IV (major), V (major), vi (minor), vii° (diminished). The uppercase Roman numerals indicate major triads, lowercase indicate minor, and the degree symbol indicates diminished. In C major: C major (I), D minor (ii), E minor (iii), F major (IV), G major (V), A minor (vi), B diminished (vii°). These qualities are not arbitrary — they fall out directly from the major scale's interval pattern. You don't need to memorize them as disconnected facts if you remember the scale structure and know your triad intervals.

**Minor keys** introduce a complication because there are three versions of the minor scale, each producing different chord qualities on some degrees. Using **natural minor** (the unaltered descending form), the diatonic triads in A minor are: i (minor), ii° (diminished), III (major), iv (minor), v (minor), VI (major), VII (major). Notice that the v chord in natural minor is *minor*, not major — this matters enormously for harmonic strength. The dominant chord V derives its powerful pull toward the tonic from the leading tone (the note a half step below the tonic). In natural minor, that note is a whole step below (the subtonic), so the "dominant" chord lacks the leading tone's gravitational pull. **Harmonic minor** fixes this by raising the seventh scale degree, which converts the v chord into a major V — restoring the strong dominant-to-tonic resolution. This is why harmonic minor exists as a separate scale variant: it exists to provide a functional V chord in minor keys.

The practical consequence is that when analyzing or composing in a minor key, you must specify which scale degree is being used for chords built on scale degrees involving the 6th and 7th. The chord on scale degree VII might be B-flat major (natural minor) or B diminished (harmonic minor) in A minor. Composers mix freely — using natural minor for melodic lines and harmonic minor for cadential chord progressions — which is why minor-key music sounds richer and less predictable than major-key music. The **vii°** chord (diminished triad), present in both major and harmonic minor, almost always appears in first inversion (the third of the chord in the bass), where its characteristic tension resolves most smoothly into the tonic chord.
