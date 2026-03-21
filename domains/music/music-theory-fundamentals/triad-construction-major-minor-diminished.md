---
id: triad-construction-major-minor-diminished
title: 'Triad Construction: Major, Minor, and Diminished'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: interval-quality-basics
  type: hard
- id: triads
  type: hard
builds-toward:
- augmented-triads-construction
- seventh-chord-construction-fundamentals
tags:
- harmony
- triads
- chord-construction
stage: formal-systems
status: draft
---

# Triad Construction: Major, Minor, and Diminished

## Core Idea
Triads are three-note chords built by stacking thirds: a root, a third (either major or minor), and a fifth (either perfect or diminished). Major triads have a major third and perfect fifth; minor triads have a minor third and perfect fifth; diminished triads have a minor third and diminished fifth.

## How It's Best Learned
Construct triads on a staff and keyboard starting from various roots. Play examples and listen to the distinct colors: major (bright), minor (dark), and diminished (tense).

## Common Misconceptions
A triad is defined by its interval structure, not the order of its notes—C, E, G and G, C, E are the same C major triad in different inversions.

## Questions

```yaml
- question: "D-F#-A is a D major triad. Which change produces a D minor triad?"
  type: multiple-choice
  options:
    - "Lower the fifth from A to Ab, keeping the third at F#"
    - "Lower the third from F# to F natural, keeping the fifth at A"
    - "Raise the third from F# to G, keeping the fifth at A"
    - "Lower both the third and the fifth by one semitone"
  answer: 1
  explanation: "A minor triad differs from a major triad only in the quality of the third — the fifth remains a perfect fifth in both. Lowering F# to F natural changes the interval from root to third from a major third (4 semitones) to a minor third (3 semitones), producing D-F-A: a D minor triad. The fifth (A) stays put. Option A would produce a diminished-like chord; option D would move both, changing the fifth to a diminished fifth."

- question: "What makes the diminished triad fundamentally different from both major and minor triads?"
  type: multiple-choice
  options:
    - "It is built on only two notes instead of three"
    - "Its fifth is a diminished fifth (tritone, 6 semitones) rather than a perfect fifth (7 semitones)"
    - "It can only be built starting on the note B"
    - "It is the same as a minor triad with the notes in reverse order"
  answer: 1
  explanation: "Both major and minor triads share a perfect fifth (7 semitones) from root to fifth — what distinguishes them is only the quality of the third. The diminished triad is structurally different: it stacks two minor thirds (3 + 3 semitones), producing a diminished fifth (6 semitones, a tritone) from root to fifth. This unstable interval is why the diminished triad sounds tense and cannot serve as a stable resting point, unlike major or minor triads."

- question: "Both major and minor triads have a perfect fifth from root to fifth; they are distinguished only by whether the third above the root is a major third (4 semitones) or a minor third (3 semitones)."
  type: true-false
  answer: true
  explanation: "This is the key structural insight. Major: M3 (4 semitones) + m3 (3 semitones) = P5. Minor: m3 (3 semitones) + M3 (4 semitones) = P5. Same outer interval, different middle note position. The diminished triad, by contrast, breaks this pattern: m3 + m3 = d5 (6 semitones), not a perfect fifth."

- question: "A triad's quality (major, minor, or diminished) depends on which root note you start from — chords built on C are naturally major because C is the 'natural' home key in Western music."
  type: true-false
  answer: false
  explanation: "Triad quality is determined entirely by interval structure, not by the root note. You can build any quality on any root. C-E-G is major, but C-Eb-G is minor, and C-Eb-Gb is diminished — all starting on C. The root determines the pitch level; the intervals between the notes determine the quality. This is the foundational principle of chord construction."

- question: "Why do major and minor triads sound emotionally different even though both contain a perfect fifth from root to fifth?"
  type: short-answer
  answer: "The difference lies in where the middle note (the third) is positioned within the perfect fifth. In a major triad, the major third (4 semitones) sits below the minor third (3 semitones) — the bottom interval is wider, creating a more open, upward-leaning quality. In a minor triad, the minor third (3 semitones) sits below the major third — the bottom is compressed, creating a more inward or downward-leaning quality. This difference in interval weight produces distinct acoustical characters (bright vs. dark) rooted in the overtone series and reinforced by centuries of Western musical convention."
  explanation: "The emotional quality is not arbitrary or purely cultural — it has acoustic roots in how close the chord tones are to the natural harmonic series. But it is also deeply shaped by learned convention. Understanding this gives you the ability to predict how listeners will perceive any chord you build, and it explains why the major-minor distinction is so central to tonal music."
```

## Explainer

From your prerequisite work with intervals and basic triads, you know that intervals are measured in semitones and have quality (major, minor, perfect, diminished, augmented). You also know that a triad is a three-note chord. Now these two ideas combine precisely: the **quality of a triad is entirely determined by the intervals between its notes**. There is no other ingredient. A major triad is not a C-major-triad because it starts on C — it is a major triad because of its internal interval structure. Change that structure by a single half step and you change the triad type.

Every triad can be described by two stacked thirds: the interval from the root to the third, and the interval from the third to the fifth. The **major triad** stacks a major third (four semitones) plus a minor third (three semitones), producing a perfect fifth (seven semitones) from root to fifth. C-E-G is a major triad: C to E is a major third; E to G is a minor third. The **minor triad** reverses the order: a minor third (three semitones) plus a major third (four semitones), still producing a perfect fifth. C-Eb-G is a minor triad: C to Eb is a minor third; Eb to G is a major third. The key insight is that major and minor triads both have a perfect fifth from root to fifth — what distinguishes them is only where the middle note sits. In a major triad the middle note leans toward the top; in a minor triad it leans toward the bottom.

The **diminished triad** is different in a fundamental way: it stacks a minor third plus a minor third (three plus three), producing a **diminished fifth** (six semitones) from root to fifth — an interval one semitone smaller than a perfect fifth. B-D-F is a diminished triad: B to D is a minor third; D to F is a minor third. The diminished fifth (also called a tritone) is an unstable interval that wants to resolve, which is why the diminished triad sounds tense and cannot serve comfortably as a resting point. In tonal music, the diminished triad appears most commonly on the seventh scale degree, where its instability drives motion toward the tonic.

The practical test for triad type is: identify the root, count up four semitones (major third) or three semitones (minor third) to find the third, then count to the fifth. But a faster method, once internalized, is to hear the emotional quality directly. Major triads have a stable, open, often cheerful character — the major third ring is bright. Minor triads are stable but darker, with the compressed minor third creating a more inward or solemn quality. Diminished triads are unstable and tense. These are not arbitrary associations; they follow directly from the physics of the overtone series and centuries of musical convention that trained Western listeners to hear them this way. Build each triad type from several different roots until the construction is automatic, then drill recognition by ear so the interval math becomes a description of something you already hear.
