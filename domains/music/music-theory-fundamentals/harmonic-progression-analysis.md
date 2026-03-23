---
id: harmonic-progression-analysis
title: 'Harmonic Progression: Analyzing Chord Sequences'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: chord-progressions
  type: hard
- id: harmonic-function-basics
  type: hard
- id: diatonic-triad-harmonization
  type: soft
builds-toward:
- roman-numeral-analysis
- voice-leading-principles
tags:
- harmonic-progression
- chord-sequence
- analysis
- function
stage: formal-systems
status: validated
---

# Harmonic Progression: Analyzing Chord Sequences

## Core Idea
Harmonic progressions move through a series of chords that create tension and resolution within a tonal framework. Strong progressions typically move from subdominant through dominant to tonic. Understanding progression patterns (I–IV–I, I–vi–IV–V, etc.) and how chords function within sequences helps analyze existing music and compose convincing progressions. Roman numeral analysis clearly notates harmonic function and makes progression structures transparent.

## How It's Best Learned
Analyze progressions in familiar songs and classical pieces. Compose short progressions using diatonic chords and identify their harmonic function.

## Common Misconceptions
- Thinking all progressions must follow V–I resolution (many progressions move through multiple functional areas).
- Not recognizing that progression strength depends on voice leading and context, not just chord choices.

## Questions

```yaml
- question: "In C major, the G major chord functions as V and creates strong tension pulling toward I. In D major, the same G major chord appears. A student claims 'G major always functions as dominant because it's G major.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "G major can never function as dominant in D major because it lacks the leading tone of D major"
    - "Harmonic function is determined by a chord's relationship to the current tonic, not its pitch content; G major is V in C major but IV in D major — the same chord can have entirely different function depending on key context"
    - "The student is wrong because G major is always a tonic chord, never dominant"
    - "The student is correct that G major always functions as dominant, but only in the context of major keys"
  answer: 1
  explanation: "This is the central insight of Roman numeral analysis: function is relational, not absolute. The chord G major contains the notes G, B, D — but what those notes *do* depends entirely on what key you're in. In C major, G is scale degree 5 (the dominant), B is the leading tone (scale degree 7), and the chord strongly pulls toward C. In D major, G is scale degree 4 (the subdominant), and there is no such pull toward D. Roman numerals make this explicit: V in C major and IV in D major are functionally different chords even though they share the same pitch content."

- question: "A pop song repeats the progression I–V–vi–IV. How should a functional analyst best describe the harmonic arc of this progression?"
  type: multiple-choice
  options:
    - "It traces a T–D–T–S arc: tonic departs through dominant, arrives at vi as a tonic substitute (the relative minor), then continues through subdominant before cycling back to tonic"
    - "It is a dominant-centric progression because V appears in position two, making it harmonically unstable throughout"
    - "It is a perfect authentic cadence (V–I) embedded in a longer sequence"
    - "The progression is entirely subdominant because IV resolves directly back to I"
  answer: 0
  explanation: "The I–V–vi–IV progression traces the full T–S–D arc but begins mid-cycle. I is tonic. V is dominant — creates tension. vi is the relative minor, which shares two notes with I and functions as a tonic *substitute* (deceptive arrival — the ear expected I but got vi). IV is subdominant — a departure that cycles back. This is why the same progression in different starting positions (I–V–vi–IV, vi–IV–I–V, IV–I–V–vi, V–vi–IV–I) sounds recognizable: it's the same functional journey in different rotations. The 'axis' progression derives its ubiquity from cycling through all four functional areas."

- question: "Roman numeral analysis is primarily a labeling system that identifies chord quality and root — it does not convey harmonic function or tell you what role a chord plays in a progression."
  type: true-false
  answer: false
  explanation: "Roman numerals are specifically designed to encode harmonic function, not just chord identity. Writing 'G major' names a chord; writing 'V in C major' tells you that chord is the dominant — it creates directed tension toward tonic, contains the leading tone, and produces a strong authentic cadence when it resolves to I. The same chord written as IV in D major conveys a completely different function: subdominant departure rather than dominant tension. Roman numeral analysis reveals the harmonic *narrative* of a piece — what each chord does, not just what it is."

- question: "The V–I progression feels conclusive partly because the leading tone (scale degree 7) has a strong tendency to resolve upward to the tonic (scale degree 1)."
  type: true-false
  answer: true
  explanation: "The strength of the V–I cadence comes from tendency tones — pitches with strong directional pull. The leading tone (one half step below tonic) has the strongest upward pull in tonal music. In a V7 chord, there is also a seventh above the root that has a downward pull toward the third of the tonic chord. When these tendency tones resolve simultaneously — leading tone rising to 1, seventh falling to 3 — the arrival at tonic feels conclusive and satisfying. IV–I (a 'plagal' cadence) lacks these tendency-tone mechanics, which is why it feels gentler and less decisive."

- question: "Why does a V–I progression feel more conclusive than a IV–I progression? Describe the specific voice-leading tendencies that make dominant-to-tonic resolution so strong."
  type: short-answer
  answer: "The V chord contains the leading tone (scale degree 7), which sits one half step below tonic and has a powerful upward tendency to resolve to scale degree 1. In a dominant seventh chord (V7), there is also the seventh of the chord (scale degree 4), which has a downward tendency to resolve to scale degree 3 in the tonic chord. These two tendency tones move in contrary motion toward the tonic chord's root and third, creating a sense of simultaneous pull from two directions. IV–I lacks both of these: IV contains scale degree 4 but no leading tone, and scale degree 4 resolves downward to 3, producing a gentler, less directed motion. The half-step pull of the leading tone is what gives V–I its sense of inevitability."
  explanation: "This is why deceptive cadences (V–vi) are so effective: the dominant's tendency tones are still there and still resolve — scale degree 7 rises to 1 (part of vi), scale degree 4 falls toward 3 (also in vi) — but the bass moves to 6 instead of 1, creating a surprising arrival. The tension releases but lands somewhere unexpected."
```

## Explainer

Your prerequisite study of chord progressions and harmonic function introduced you to the basic vocabulary: chords built on scale degrees, labeled I through VII, each with a characteristic role. Harmonic progression analysis takes this further by examining *sequences* — how chords move through time, creating the experience of tension and release that makes tonal music feel like it goes somewhere. The fundamental insight is that chords do not just coexist; they create directed motion toward resolution.

The core framework is the **T–S–D–T arc** (tonic–subdominant–dominant–tonic), which describes the most common shape of a harmonic journey. Tonic chords (I, vi, sometimes iii) feel stable — they are home. Subdominant chords (IV, ii) create a sense of departure, moving away from home without yet creating urgency. Dominant chords (V, vii°) create strong directed tension — they pull powerfully toward tonic resolution, because the leading tone (scale degree 7) wants to rise to the tonic, and the seventh of the V7 chord wants to fall. When dominant resolves to tonic, the motion of those tendency tones satisfying their pull is what creates the sensation of arrival. This is why the V–I progression feels conclusive in a way that, say, IV–I does not.

**Roman numeral analysis** is the notation system that makes all of this transparent. Rather than writing "G major chord," you write "V in C major" — which tells you not just what the chord contains but what it *does* in context. The same chord of G major functions as V in C major, as IV in D major, and as I in G major. Its identity in a progression is functional, not absolute. When you annotate a piece with Roman numerals, you are mapping its harmonic narrative: here is the departure from tonic (ii), here is the dominant preparation (IV–V), here is the resolution (I). Some progressions move through all three functional areas in clear sequence; others linger on dominant, building tension before resolving; others substitute functional equivalents (vi for I as a **deceptive cadence** — V resolving unexpectedly to vi rather than I).

A common learning milestone is recognizing stock patterns. The **I–vi–IV–V** progression underlies hundreds of pop songs from the 1950s doo-wop era to the present precisely because it traces the full T–S–D arc in four chords. The **I–V–vi–IV** (the so-called "axis" progression) does the same journey in different rotation — beginning on tonic, departing through dominant, arriving on relative minor as a kind of subdominant replacement, then continuing through IV before cycling back. Once you can hear these functional moves, you begin to hear large chunks of Western popular and classical music as variations on a shared harmonic grammar.

What makes analysis genuinely useful rather than just labeling is using it to understand *decisions*. When Beethoven delays the expected tonic resolution at the end of a development section, the extended dominant creates structural suspense. When a blues progression stays on I for four bars before moving to IV, that lingering intensifies the eventual departure. When a rock song suddenly substitutes ♭VII for V (a non-functional borrowed chord that does not strongly resolve to I), the effect is modal ambiguity rather than directed tension. Recognizing these choices — why a composer or songwriter chose *this* progression rather than the expected one — is what transforms harmonic analysis from transcription into interpretation.
