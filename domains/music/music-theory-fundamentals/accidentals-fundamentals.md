---
id: accidentals-fundamentals
title: 'Accidentals: Sharps, Flats, and Naturals'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: note-names-and-octaves
  type: hard
builds-toward:
- enharmonic-equivalence-basics
- key-signatures
tags:
- pitch
- notation
- accidentals
stage: formal-systems
status: draft
---

# Accidentals: Sharps, Flats, and Naturals

## Core Idea
Accidentals modify the pitch of a note: sharps raise a pitch by one semitone, flats lower it by one semitone, and naturals cancel previous accidentals. They are essential for notating chromatic pitches and creating pitches outside the diatonic scale.

## How It's Best Learned
Write accidentals on a staff, play them on an instrument, and listen to the sound changes. Practice identifying accidentals in written music.

## Common Misconceptions
Sharps and flats are not specific pitches—they're modifications of existing notes. A sharp doesn't always mean 'higher' in absolute terms; F# is lower than G.

## Questions

```yaml
- question: "A piece is written in B♭ major, meaning every B is played as B♭. In measure 5, the composer writes B♮. What should the performer play?"
  type: multiple-choice
  options:
    - "B♭, because the key signature overrides any accidental in the measure"
    - "The natural B — one semitone higher than B♭ — for that note and the rest of measure 5"
    - "A note one semitone above B♭, which would be B♯"
    - "Skip the note, since a natural sign cancels the pitch entirely"
  answer: 1
  explanation: "A natural sign (♮) cancels the flat established by the key signature for that note, restoring it to the unmodified natural pitch. So B♮ means 'play the natural B, not B♭.' The natural sign applies for the rest of the measure. This is a core skill in sight-reading: accidentals override the key signature within the measure where they appear."

- question: "In measure 3 of a piece, a C♯ appears on the second beat. On the fourth beat of the same measure, there is another C with no accidental marked. How should it be played?"
  type: multiple-choice
  options:
    - "As C natural, because the sharp only applies to the specific note it precedes"
    - "As C♯, because an accidental applies to all subsequent notes of that pitch within the same measure"
    - "As C natural, because the sharp resets after each beat"
    - "As C♯, because sharps apply for the entire piece once introduced"
  answer: 1
  explanation: "Accidentals apply for the rest of the measure in which they appear. Once C♯ appears in measure 3, every subsequent C in that measure is also C♯ unless explicitly cancelled with a natural sign. This is one of the most common reading errors for beginners, who assume the sharp only affects the one note it directly precedes."

- question: "A sharp (♯) raises a note by exactly one semitone relative to its natural form."
  type: true-false
  answer: true
  explanation: "By definition, a sharp raises the pitch of a named note by one semitone — the smallest step in standard Western music. C♯ is one semitone above C; F♯ is one semitone above F. Accidentals are precisely defined relative modifiers, not vague indications of 'higher.'"

- question: "F♯ is a higher pitch than G because the sharp symbol indicates upward movement."
  type: true-false
  answer: false
  explanation: "F♯ is one semitone above F, but G is two semitones above F — so F♯ is actually one semitone BELOW G, not above it. This is the key misconception the topic warns against: sharps indicate 'higher relative to the natural note they modify,' not 'higher than everything.' A sharp on F still produces a pitch lower than G."

- question: "Why are sharps and flats described as 'relative modifiers' rather than absolute pitch names? What does this mean in practice?"
  type: short-answer
  answer: "A sharp or flat doesn't name a fixed pitch on its own — it names the result of adjusting a specific natural note up or down by one semitone. F♯ means 'F raised by one semitone'; D♭ means 'D lowered by one semitone.' In practice, this means the same physical pitch (like the black key between C and D) can be named either C♯ or D♭ depending on which natural note it is modifying. The accidental is always understood in relation to the letter name it modifies."
  explanation: "This is the foundation of enharmonic equivalence: C♯ and D♭ are the same piano key, reached by two different relative modifications. Understanding accidentals as modifiers — not absolute labels — is essential for reading key signatures, understanding enharmonic spellings, and later analyzing chromatic harmony."
```

## Explainer

You already know the seven natural note names — A, B, C, D, E, F, G — and how they repeat across octaves. But these seven notes only account for seven of the twelve pitches within an octave. The remaining five pitches are the **chromatic** pitches, and **accidentals** are the notation symbols that give us access to them.

A **sharp** (♯) raises a note by exactly one **semitone** — the smallest step available in standard Western music, equivalent to moving one key to the right on a piano. So C♯ is one semitone above C, and F♯ is one semitone above F. A **flat** (♭) lowers a note by one semitone: B♭ is one semitone below B, E♭ is one semitone below E. The **natural sign** (♮) cancels a previous accidental, returning a note to its unmodified pitch. If a piece is in a key that includes B♭ (meaning every B in the piece is flattened by default), writing B♮ explicitly tells the performer to play the natural B instead.

The key insight the Common Misconceptions section points toward is that accidentals are relative modifiers, not absolute labels. "F♯" doesn't name a unique, fixed thing the way "F" does — it names the result of applying a sharp to F. That's why, on a piano, you can reach the same physical key either as C♯ (C raised) or D♭ (D lowered): two different names, one sound. This is called **enharmonic equivalence**, which you'll study soon. For now, the important thing is to understand that a sharp or flat always belongs to a named note and tells you which direction and by how much to adjust it.

In written music, accidentals apply for the rest of the measure in which they appear, then reset. If you see a C♯ in measure 3, every subsequent C in that same measure is also C♯ unless marked otherwise with a natural sign. This rule — accidentals last for the measure — is one of the most common sources of reading errors, so it's worth memorizing explicitly. Accidentals are how composers reach pitches outside the seven-note **diatonic scale** of a given key, whether to create passing color, signal a key change, or introduce the chromatic richness of chords like secondary dominants (which you'll study later). Mastering accidentals at the reading level is the foundation for all of that later work.
