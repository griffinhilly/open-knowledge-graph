---
id: canon-techniques-advanced
title: Canon Techniques and Forms
domain: music
course: advanced-music-theory
prerequisites:
- id: invertible-counterpoint-advanced
  type: hard
tags:
- canon
- counterpoint
- imitation
- advanced-forms
stage: expert
status: validated
---

# Canon Techniques and Forms

## Core Idea
Canons range from simple round-robins to complex proportional canons where different voices move at different speeds, crab canons that play backward, and mirror canons that flip across an axis. These techniques reveal deep structural relationships and have been exploited by composers from the Renaissance through contemporary classical music for both structural and playful purposes.

## Questions

```yaml
- question: "In Bach's Musical Offering, one canonic piece makes perfect musical sense when the score is turned upside-down and read from right to left. What type of canon is this?"
  type: multiple-choice
  options:
    - "Canon by inversion — the follower mirrors the melodic intervals upside down"
    - "Crab canon (cancrizans) — the follower performs the leader's melody backward"
    - "Proportional canon — the follower performs at half the original speed"
    - "Round — the voices enter at the unison after a fixed time interval"
  answer: 1
  explanation: "A crab canon (cancrizans) is defined by the follower performing the dux melody in retrograde — backward. The result is a piece that is palindromic in some sense: the score works equally well in reverse. A canon by inversion flips the melodic intervals vertically (ascending becomes descending), which is a different transformation. A proportional (mensuration) canon varies tempo, not direction."

- question: "A composer wants to write a mensuration canon where the soprano sings the melody at normal speed while the alto sings the same melody at half speed. Which skill from invertible counterpoint is most critical, and why?"
  type: multiple-choice
  options:
    - "The ability to write florid ornamentation, since the slower voice needs more notes to fill time"
    - "The ability to compose a melody that produces legal vertical intervals with itself at every possible temporal offset, since voices will be at different positions in the melody simultaneously"
    - "Mastery of voice-leading in parallel motion, since both voices share the same pitches"
    - "Knowledge of modal harmony, since proportional canons require a different harmonic language than tonal music"
  answer: 1
  explanation: "In a mensuration canon, while the soprano sings beat 10 of the melody, the alto (at half speed) is singing beat 5. These two melody points sound simultaneously, so the vertical interval between them must be acceptable counterpoint. This must hold at EVERY temporal offset throughout the piece — meaning the melody must produce legal counterpoint with every displaced version of itself. This is precisely invertible counterpoint applied temporally: the constraint that any point in the melody can serve as either the upper or lower voice against any other point."

- question: "In a crab canon, the follower (comes) enters performing the same melody as the leader (dux) but transposed to a different pitch."
  type: true-false
  answer: false
  explanation: "In a crab canon, the follower performs the leader's melody in RETROGRADE — backward from end to beginning. Pitch transposition is the defining feature of a standard canon (e.g., a canon at the fifth), but crab canons are defined by temporal retrograde, not pitch transposition. A mirror canon combines both retrograde AND inversion. Confusing crab canons with standard canons at a different pitch is a common error."

- question: "A canon is fundamentally a compositional constraint — it derives an entire texture from a single melodic idea subjected to rule-governed transformation."
  type: true-false
  answer: true
  explanation: "This is the central insight about canon as a structural form. Unlike free counterpoint where you can add whatever notes sound best, a canon commits the composer to deriving everything from the dux. The constraint simultaneously limits freedom (you can't insert a convenient note that isn't already in the melody) and generates coherence (the texture has an organic unity because it all comes from one source). This is why Bach and later composers like Bartók and Ligeti found canons so powerful: the constraint IS the compositional engine."

- question: "Explain why understanding invertible counterpoint is a prerequisite for writing proportional (mensuration) canons."
  type: short-answer
  answer: "In a proportional canon, different voices perform the same melody simultaneously at different tempos. At any moment, the vertical interval between two voices is determined by which beats of the melody are sounding at the same time. Because voices move at different speeds, every possible combination of melody-points will eventually sound against every other. The melody must produce acceptable counterpoint with itself at ALL temporal offsets — which means every interval combination that arises must avoid forbidden parallels and dissonances. Invertible counterpoint is exactly the skill of writing lines that work regardless of which voice is on top; mensuration canons extend this to temporal displacement."
  explanation: "Josquin's mensuration canons in the 'L'homme armé' Mass work because his single melody, when played against a 2:1 or 3:1 slowed version of itself, never produces consecutive fifths or octaves. Achieving this is not luck — it requires systematic understanding of which intervals at which offsets remain legal. That is invertible counterpoint applied in the time dimension."
```

## Explainer

You already know invertible counterpoint — the technique of writing two or more voices so that either can serve as the bass beneath the other without producing forbidden parallels. A **canon** is invertible counterpoint in time: the same melody serves as both the leader (**dux** or antecedent) and the follower (**comes** or consequent), with the consequent entering after a fixed time interval at a fixed pitch interval. The basic round (like "Frère Jacques") is the simplest form — voices at the unison, entering one phrase apart, with no pitch transformation. Every advanced canon technique is a systematic modification of one or both of these parameters.

Advanced canon forms introduce rule-governed transformations to the relationship between dux and comes. In a **canon by inversion**, the follower mirrors the leader's melodic intervals upside down — ascending steps become descending steps, a leap up becomes a leap down. In a **crab canon** (cancrizans), the follower plays the leader's melody backward; the result is a piece that makes equally good musical sense performed in reverse. A **mirror canon** combines both transformations simultaneously. Bach's *Musical Offering* contains famous examples of all three types, and recognizing them in score requires identifying the transformation rule and then verifying it holds throughout.

**Proportional canons** (mensuration canons) are among the structurally most complex forms: different voices perform the same melody at different tempos simultaneously. In a 2:1 proportion, the follower moves at half speed, so while the leader completes the entire melody, the follower reaches only the midpoint. Josquin des Prez's "L'homme armé" Mass uses this technique — the challenge is composing a melody that produces acceptable counterpoint with itself regardless of the speed relationship. The invertible counterpoint you studied is precisely what constrains which melodies can work: the melodic intervals at each temporal offset must produce legal vertical intervals.

The analytical payoff of understanding these techniques is pattern recognition: when you encounter a complex contrapuntal texture in music from Bach to Bartók to Ligeti, the question "is this a canon, and if so, at what interval, with what transformation?" becomes answerable. A canon is not just a compositional device but a structural commitment — the composer derives an entire texture from a single melodic idea subjected to rule-governed transformation. This constraint is simultaneously a limitation (you can't freely add whatever notes sound good) and a generative engine (the constraint creates coherence that free composition cannot match).
