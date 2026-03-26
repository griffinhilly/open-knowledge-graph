---
id: triad-construction-major-minor
title: 'Triad Construction: Major and Minor'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: interval-quality
  type: hard
- id: intervals-basics
  type: hard
- id: key-signatures-reading-writing
  type: soft
builds-toward:
- triad-quality-diminished-augmented
- seventh-chord-construction
- harmonic-function-basics
- chord-progressions
tags:
- chords
- triads
- major
- minor
stage: formal-systems
status: validated
---
# Triad Construction: Major and Minor

## Core Idea
A triad is a three-note chord built by stacking two 3rd intervals above a root note. A major triad consists of a major 3rd plus a perfect 5th, while a minor triad has a minor 3rd plus a perfect 5th. These two types are the foundation of tonal harmony with distinctly different characters—major sounds bright, minor sounds dark.

## How It's Best Learned
Build major and minor triads above various roots on staff and keyboard, using interval knowledge to verify. Listen to major vs. minor triads and practice identifying them by ear.

## Common Misconceptions
Building a triad with a major 3rd and major 5th (there is no 'major 5th'—the 5th is perfect). Thinking minor triads have a diminished 5th (they have perfect 5th). Confusing letter-name distances with interval quality.

## Questions

```yaml
- question: "A student builds a chord by stacking a minor third (3 semitones) from C to E♭, then a major third (4 semitones) from E♭ to G. What chord has she built?"
  type: multiple-choice
  options:
    - "C major, because the top and bottom notes (C and G) form the same interval as in C major"
    - "C minor, because the bottom interval is a minor third"
    - "C diminished, because the chord contains a flattened note (E♭)"
    - "Neither major nor minor — stacking a minor third below a major third does not produce a standard triad"
  answer: 1
  explanation: "C minor is built with a minor third on the bottom (C to E♭, 3 semitones) and a major third on top (E♭ to G, 4 semitones). The outer interval C to G is a perfect fifth (7 semitones), the same as in C major. The chord is C minor precisely because the bottom third is minor — this is the only structural difference between C major (C-E-G) and C minor (C-E♭-G). The presence of E♭ does not make a chord diminished; diminished triads have a diminished fifth (6 semitones), not a perfect fifth."

- question: "What interval separates the root and fifth of a minor triad?"
  type: multiple-choice
  options:
    - "A diminished fifth (6 semitones), which gives minor triads their darker sound"
    - "A minor fifth (6 semitones), equivalent to a tritone"
    - "A perfect fifth (7 semitones), the same interval as in a major triad"
    - "It depends on the root note — some minor triads have perfect fifths, others have diminished fifths"
  answer: 2
  explanation: "Both major and minor triads span a perfect fifth (7 semitones) from root to fifth. This is the most common misconception about minor triads — the 'darkness' or 'sadness' of minor is caused by the minor third on the bottom (3 semitones), not by any alteration to the fifth. A diminished fifth (6 semitones) appears only in a diminished triad, which is a different chord type entirely. Checking the outer interval first is a reliable error-catching step: if it's not a perfect fifth, something has gone wrong."

- question: "A minor triad differs from a major triad built on the same root because the minor triad has a diminished fifth instead of a perfect fifth."
  type: true-false
  answer: false
  explanation: "Both major and minor triads have a perfect fifth (7 semitones) from root to fifth. The only structural difference is the quality of the bottom third: major triads use a major third (4 semitones) from root to middle note, while minor triads use a minor third (3 semitones). The middle note shifts by one semitone (e.g., E in C major vs. E♭ in C minor), but the top note (the fifth, G) stays the same. Diminished triads are a separate category with an actual diminished fifth."

- question: "Both a C major triad and a C minor triad contain the note G as their top note (fifth)."
  type: true-false
  answer: true
  explanation: "C major = C-E-G and C minor = C-E♭-G. The fifth (G) is the same in both because both chords span a perfect fifth (7 semitones) from the root C. The only difference is the middle note: E (major third, 4 semitones above C) in C major versus E♭ (minor third, 3 semitones above C) in C minor. This illustrates that the outer interval is shared; the quality of the inner third determines major vs. minor."

- question: "Both a major triad and a minor triad built on the same root span a perfect fifth on the outside. If the fifth is the same, what creates the perceptual difference between major and minor — and where exactly does that difference come from?"
  type: short-answer
  answer: "The difference comes entirely from the middle note — specifically, which type of third sits on the bottom. In a major triad, the major third (4 semitones) is on the bottom; in a minor triad, the minor third (3 semitones) is on the bottom. This single semitone shift of the middle note changes the internal structure of the chord despite leaving the outer interval unchanged, producing the characteristic bright (major) versus dark (minor) contrast."
  explanation: "Understanding that the fifth is shared while the third differs is the key structural insight. It explains why the two-step check works: verify the perfect fifth first (both types pass), then check the bottom third (4 semitones = major, 3 semitones = minor). It also explains why beginning students misidentify minor triads as having diminished fifths — they hear the darker sound and assume the outer interval must differ, when in fact the difference is entirely interior."
```

## Explainer

You already know how to measure intervals precisely — both the letter-name distance and the quality (major, minor, perfect). A **triad** puts that knowledge to work by stacking two thirds above a root. The root is the bottom note and gives the chord its name. The middle note is a third above the root, and the top note — the **fifth** — is a third above the middle note, which makes it a fifth above the root. Three notes, two stacked thirds: that is the definition of a triad.

The difference between a major triad and a minor triad comes down to a single semitone. A **major triad** uses a major third from root to middle note (4 semitones), then a minor third from middle to top (3 semitones), giving a total of 7 semitones from root to fifth. A **minor triad** uses a minor third from root to middle note (3 semitones), then a major third from middle to top (4 semitones), also giving 7 semitones from root to fifth. Both have a **perfect fifth** spanning the outside two notes; the only difference is which note sits in the middle. To build C major: C up a major third to E, then E up a minor third to G — result: C-E-G. To build C minor: C up a minor third to E♭, then E♭ up a major third to G — result: C-E♭-G.

This structure explains why major and minor triads sound so different despite sharing the same outer interval. The perfect fifth is acoustically stable and consonant in both cases. What creates the perceptual contrast is the placement of the third. In a major triad, the major third is on the bottom, which means the chord's interior emphasis falls on a brighter, higher-tension interval. In a minor triad, the minor third is on the bottom, producing a darker interior quality. Experienced listeners often describe this as major sounding "open" or "bright" and minor sounding "closed" or "dark," though these associations vary across cultures and contexts.

A common error is to think minor triads have a diminished fifth — they do not. Both major and minor triads span a perfect fifth (7 semitones). The diminished triad, which you will encounter next, is different precisely because its fifth is diminished (6 semitones). When checking your triad construction, always verify the outer interval first: if it is not a perfect fifth, something has gone wrong. Then check the quality of the third to determine major or minor. This two-step check — fifth first, then third — is the fastest way to catch errors when building triads at the keyboard or on staff paper.
