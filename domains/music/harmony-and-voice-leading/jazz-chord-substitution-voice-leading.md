---
id: jazz-chord-substitution-voice-leading
title: Jazz Chord Substitution and Reharmonization
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: jazz-harmony-basics
  type: hard
- id: secondary-dominants
  type: hard
- id: voice-leading-principles
  type: hard
- id: diatonic-progression-voice-leading-patterns
  type: soft
- id: extended-chords-upper-extensions-voicing
  type: soft
- id: extended-harmony-voice-leading-handling
  type: soft
builds-toward: []
tags:
- jazz
- substitution
- reharmonization
stage: formal-systems
status: validated
---
# Jazz Chord Substitution and Reharmonization

## Core Idea
Jazz musicians substitute and reharmonize chords to create new harmonic colors while maintaining voice-leading logic. Tritone substitutions, secondary dominants, and chromatic approach chords extend the harmonic vocabulary. Voice-leading principles guide which substitutions work smoothly and which create jarring or effective transitions.

## How It's Best Learned
Reharmonize a simple melody using secondary dominants and tritone subs. Sing or play the result to hear which substitutions work musically. Study real jazz lead sheets to see how professionals substitute.

## Common Misconceptions
Substitutions are not random; they work because they share common tones or have strong voice-leading connections. Not every possible substitution sounds good.

## Questions

```yaml
- question: "A student argues that D♭7 can substitute for G7 in a C major context because 'both sound jazzy and bluesy.' A teacher insists this explanation misses the real reason. What is the correct account?"
  type: multiple-choice
  options:
    - "D♭7 is exactly a tritone away from G7 and tritone substitutions always sound good in jazz contexts"
    - "Both chords contain the same tritone: the B–F in G7 is enharmonically equivalent to the C♯–G♭ in D♭7, so both carry the same voice-leading tendency toward C major tonic, making them functionally interchangeable as dominant chords"
    - "D♭7 has the same number of altered tones as G7 has natural tones"
    - "Any two dominant seventh chords can substitute for each other because they share the same chord quality"
  answer: 1
  explanation: "The tritone substitution is not about style or general dominant interchangeability — it works because of a precise shared structure. G7 contains the tritone B–F; D♭7 contains C♯–G♭, which is enharmonically the same tritone. Because the tritone is the engine of dominant resolution (B resolves up to C, F resolves down to E), both chords create the same voice-leading pull toward C major. The substitution preserves functional logic while changing the bass line from a descending fifth to a descending half step."

- question: "What makes the bass line in a tritone substitution resolution (D♭7 → C) sound more striking than a standard dominant resolution (G7 → C)?"
  type: multiple-choice
  options:
    - "The substituted bass note is louder because D♭ is a lower note than G"
    - "Instead of the bass descending a perfect fifth (G → C), the tritone substitution produces a descending half step (D♭ → C) — a chromatic bass resolution that is more dramatic and tense"
    - "The tritone substitution always introduces a deceptive cadence to the vi chord"
    - "The bass line ascends by a tritone in the substitution, creating upward momentum"
  answer: 1
  explanation: "The standard V–I resolution in C has the bass falling a fifth (G down to C), which is a clean but conventional movement. With the tritone substitution, the bass falls only a half step (D♭ down to C), which is maximally tense — half-step motion has the strongest directional pull in Western harmony. This gives the resolution a chromatic 'lean' into tonic that is distinctive in jazz and bebop. The voice-leading logic is identical; only the bass approach is different."

- question: "Chord substitutions in jazz are primarily aesthetic choices — musicians substitute chords because they 'feel right' in the moment, without any underlying theoretical logic."
  type: true-false
  answer: false
  explanation: "Effective substitutions are grounded in voice-leading logic: shared tritones (tritone substitution), shared common tones (tonic and subdominant substitutes), or smooth half-step approach motion (chromatic approach chords). A substitution that violates these principles — introducing a chord with no logical relationship to the target and with poor voice-leading — produces a jarring or incoherent harmonic result. The feeling of 'rightness' in a good substitution is the perception of smooth voice-leading and functional coherence, not arbitrary intuition."

- question: "In jazz reharmonization, the vi chord (e.g., Am7 in C major) can substitute for the I chord because it shares common tones with the tonic triad and functions as a tonic substitute."
  type: true-false
  answer: true
  explanation: "In C major, the vi chord Am7 contains the notes A–C–E–G. Two of the three tonic triad tones (C and E) appear in Am7, giving it strong tonic coloring. Substituting vi for I provides a sense of repose without full closure — the harmony feels stable but the substitution adds color and avoids the finality of a root-position I chord. This tonic substitution relationship is one of the fundamental harmonic moves in jazz reharmonization."

- question: "Explain the voice-leading logic that makes a tritone substitution work, and why the resulting bass line sounds so characteristic of jazz."
  type: short-answer
  answer: "A dominant seventh chord's power to resolve comes from its tritone — in G7, the notes B and F want to resolve inward: B up to C (the leading tone) and F down to E. The chord a tritone away, D♭7, contains C♯ and G♭, which are enharmonically the same tritone with the same resolution tendencies. Both chords therefore pull equally toward C major, making them functionally equivalent as dominants. The characteristic effect comes from the bass: instead of the conventional perfect-fifth drop (G→C), the tritone substitution produces a descending half step (D♭→C), giving the resolution a tense chromatic lean into tonic that is central to bebop and modern jazz sound."
  explanation: "The tritone substitution is the most theoretical example of a broader principle: good substitutions preserve or improve voice-leading while changing harmonic color. Understanding *why* it works — shared tritone, same voice-leading tendency — also explains its limits. Substituting D♭7 for G7 works in contexts where the dominant function is clear; in ambiguous contexts, the unusual bass motion can confuse the harmonic direction rather than enhancing it."
```

## Explainer

Jazz harmony extends and reharmonizes standard chord progressions by applying a core insight: chords are interchangeable when they share the **voice-leading functions** of the original. From your prerequisite work in secondary dominants, you know that any dominant seventh chord — wherever it appears — has the same structural job: its tritone (the third and seventh) wants to resolve inward to the tonic. Jazz substitution systematically exploits this fact to create harmonic color, surprise, and forward motion.

The **tritone substitution** is the most fundamental jazz reharmonization technique, and it builds directly on what you know about dominant function. A dominant seventh chord (say, G7 in C major) contains the tritone B–F. The chord a tritone away — D♭7 — contains the *same* tritone, just spelled differently (C♯–G♭, which is enharmonically B–F♯/G♭). Because both chords contain the same tritone and therefore the same voice-leading tendency, D♭7 can substitute for G7. The practical effect is striking: instead of V7 resolving by a descending fifth (G down to C), the substituted chord resolves by a descending half step (D♭ down to C). The bass line gains a dramatic, chromatic color while the resolution logic remains intact. This is not arbitrary — it is precise voice-leading logic applied to jazz vocabulary.

**Secondary dominant substitution** extends the network further. Rather than moving directly to a chord, you approach it with a secondary dominant — a V7 of whatever the next chord is. The ii–V–I progression that underlies most jazz harmony is itself an application of this: the ii chord acts as a pre-dominant (often functioning as a IV substitute), and the V resolves to I. Reharmonization means replacing any chord in this chain with something that fulfills the same voice-leading role. You can substitute ii for IV, vi for I (the tonic substitute), or ♭VII for V (a common modal substitution where the dominant function is replaced with a subtonic chord that descends by step to I).

**Chromatic approach chords** work on a different principle: instead of sharing functional voice-leading with the target chord, they simply arrive at it from a half step above or below. Because half-step motion has such strong directionality, a chord that moves into the target by chromatic approach "borrows" the target's functional importance. This technique creates the characteristic sound of bebop, where chromatic passing chords cluster around stable harmonic targets. The key principle binding all substitution techniques together is **common tones plus smooth voice leading**: a good substitution minimizes the number of voices that move dramatically, maximizes the number that stay on the same or adjacent notes, and produces a logical bass line. When voice leading is smooth, even unexpected harmonic moves sound purposeful rather than disorienting.

