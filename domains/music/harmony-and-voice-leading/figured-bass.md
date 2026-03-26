---
id: figured-bass
title: Figured Bass
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: chord-inversions
  type: hard
- id: intervals-basics
  type: hard
- id: roman-numeral-analysis
  type: soft
builds-toward:
- four-part-writing
- voice-leading-principles
tags:
- figured-bass
- notation
- inversions
- baroque
stage: formal-systems
status: validated
---

# Figured Bass

## Core Idea
Figured bass is a notational shorthand originating in Baroque music, placing Arabic numerals below a bass note to indicate the intervals (and thus the chord) built above it. A 6 below a bass note indicates a first-inversion chord (6/3), while 6/4 indicates second inversion. Accidentals in the figures modify the implied intervals. The system guided keyboard continuo players who improvised chords from a bass line, and it remains central to the analysis and notation of voice-leading in academic harmony study.

## How It's Best Learned
Practice reading figured bass by playing the bass note in the left hand and identifying which intervals to add in the right. Work from Bach continuo parts or textbook exercises, realizing short passages before attempting full chorales. Cross-reference with Roman numeral analysis to see how both systems describe the same harmony from different perspectives.

## Common Misconceptions
- Thinking the numbers represent scale degrees rather than intervals above the bass note.
- Forgetting that an unfigured bass (no numbers) implies a root-position triad (5/3).
- Misreading accidentals attached to figures: a sharp or flat modifies only the interval it accompanies.

## Questions

```yaml
- question: "A bass note E appears with the figure '6' written below it. What does this indicate?"
  type: multiple-choice
  options:
    - "Play an E major chord in root position — the '6' identifies the sixth scale degree"
    - "Play a chord containing a 6th and an implied 3rd above E, making E the bass of a first-inversion triad"
    - "Play a chord where E functions as the sixth of the chord"
    - "Play six ascending notes above E"
  answer: 1
  explanation: "Figured bass numbers indicate intervals above the bass note, not scale degrees. A '6' (shorthand for 6/3) means the chord contains a 6th and a 3rd measured upward from the bass. This describes a first-inversion triad, where the third of the chord sits in the bass. The '6' does not name E as the sixth of anything — it measures the intervallic distance up from E. Intervals above the bass versus scale degrees is the core conceptual distinction in reading figured bass."

- question: "A bass note in a figured bass passage has no figures written beneath it. What does the continuo player realize?"
  type: multiple-choice
  options:
    - "The player improvises freely since no chord is specified"
    - "A first-inversion chord, the most common default in Baroque practice"
    - "A root-position triad (5/3): the bass note is the root, with a third and a fifth above it"
    - "A dominant seventh chord, the default when no figure appears"
  answer: 2
  explanation: "An unfigured bass is a convention meaning 5/3 — a root-position triad with the bass note as the root, a third above, and a fifth above. This is the default realization; no figure does not mean free improvisation. Students often assume silence about figures means freedom, but the system has a specific convention: no numbers = root-position triad."

- question: "The figure '6/4' written below a bass note indicates a second-inversion chord."
  type: true-false
  answer: true
  explanation: "6/4 specifies a chord with a 6th and a 4th above the bass. Since the fifth of the chord sits in the bass, this describes a second-inversion triad (also called a 'six-four chord'). For example, in C major, bass note G with '6/4' indicates the second-inversion C major chord (G–C–E). This contrasts with '6' alone (or 6/3), which indicates first inversion."

- question: "An accidental attached to a figure in figured bass raises or lowers most of the intervals in the chord, not just the one it accompanies."
  type: true-false
  answer: false
  explanation: "An accidental in figured bass modifies only the specific interval it directly accompanies. For example, a sharp next to '6' raises only the 6th above the bass, leaving the 3rd unchanged. Each figure is independent; an accidental applies to exactly one interval. Misapplying an accidental to the whole chord produces incorrect realizations — a common error for students new to the notation."

- question: "Explain why figured bass numbers cannot represent scale degrees, and what they actually indicate about the chord to be played."
  type: short-answer
  answer: "Scale degrees are fixed positions in a key and do not change with the bass note. Figured bass numbers measure intervals — staff-step distances — upward from the current bass note. The same figure '6' above different bass notes produces entirely different pitches and chords; only the intervallic relationship to the bass stays constant. This interval-above-bass interpretation is what makes figured bass a compact, key-independent notation: the numbers always describe the chord's structure relative to wherever the bass happens to be."
  explanation: "If the numbers meant scale degrees, the notation would break every time the bass moved. The interval interpretation is universal: given any bass note and the figures above it, the continuo player can immediately construct the correct chord in any key or register."
```

## Explainer

From your prerequisites in chord inversions and interval basics, you understand that a triad can appear in root position (root in the bass), first inversion (third in the bass), or second inversion (fifth in the bass), and you can measure intervals by counting staff steps. Figured bass is a **notational shorthand** that combines these two concepts: Arabic numerals written below a bass note indicate the intervals — measured upward from that bass note — that form the chord to be played above it. This system originated in Baroque keyboard practice, where continuo players (typically harpsichordists or organists) improvised chords from a single bass line annotated with figures.

The core convention is simple. An unfigured bass note (no numbers) means a root-position triad: you build a 5th and a 3rd above the bass (the full figure would be 5/3, but it is left implicit). A **6** below a bass note indicates first inversion (6/3, abbreviated to just 6): the chord contains a 6th and a 3rd above the bass. A **6/4** indicates second inversion: a 6th and a 4th above the bass, with the fifth of the chord sitting in the bass. For seventh chords, **7** indicates root position (7/5/3), **6/5** indicates first inversion, **4/3** indicates second inversion, and **4/2** (or just **2**) indicates third inversion. Each figure describes the chord's structure relative to its bass note, not its position in the key — the same figure produces different chords depending on which bass note it appears above.

The conceptual trap is confusing figured bass numbers with **scale degrees**. Scale degrees are fixed positions in a key (1 is always tonic, 5 is always dominant). Figured bass numbers are intervals measured from the current bass note — they change meaning every time the bass moves. A "6" above E means a 6th above E (C), while a "6" above G means a 6th above G (E). The number "6" does not refer to scale degree 6; it measures a distance. Accidentals in figures modify only the specific interval they accompany: a sharp next to "6" raises the 6th above the bass by a half step, leaving all other intervals unchanged. A slash through a number also indicates raising that interval by a half step.

Figured bass remains central to academic harmony study because it makes voice-leading relationships visible in a way that Roman numeral analysis does not. Roman numerals identify chords by their scale-degree root and quality (I, IV, V7), abstracting away from specific voicing. Figured bass specifies the vertical intervals above the bass, making the actual spacing and inversion audible on the page. A "6" tells you exactly which voice configuration to play; a Roman numeral tells you the chord's harmonic function but not its voicing. Both systems describe the same harmony from different angles, and learning to translate between them — seeing that a "6" on E in C major means a first-inversion C major chord, which Roman numeral analysis labels I6 — is one of the most valuable cross-referencing skills in harmony study.
