---
id: harmonic-function-and-progression
title: Harmonic Function and Chord Progressions
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: harmonic-function-basics
  type: hard
- id: harmonic-analysis-roman-numeral-function
  type: hard
- id: voice-leading-serves-harmonic-function
  type: soft
builds-toward:
- secondary-dominant-extended-voice-leading
- cadential-voice-leading-patterns
- applied-chord-tonicization-process
tags:
- harmony
- function
- progression
stage: formal-systems
status: validated
---
# Harmonic Function and Chord Progressions

## Core Idea
Chords function in progressions according to their relationship to the tonic: tonic chords provide stability, subdominant chords create tension and forward motion, and dominant chords demand resolution. Understanding harmonic function helps you construct progressions with inherent logic and directional drive.

## How It's Best Learned
Label progressions with their harmonic functions (T, SD, D) rather than just Roman numerals. Listen to how progressions feel: does IV→V make sense? What about V→IV? Build progressions using functional logic rather than random chords.

## Common Misconceptions
A V chord does not always resolve to I; context and function matter. Not all I chords feel equally 'tonic'—context and voice leading affect the sense of arrival.

## Questions

```yaml
- question: "A composer writes the progression V → IV in the middle of a piece in C major. A student says this is fine because both chords are diatonic. What harmonic problem is the student missing?"
  type: multiple-choice
  options:
    - "IV is not a diatonic chord in C major"
    - "V and IV cannot appear in the same phrase under any circumstances"
    - "V → IV moves backward in harmonic function — from dominant to subdominant — undermining the sense of forward motion toward resolution"
    - "The progression skips the tonic, which is required between any two non-tonic chords"
  answer: 2
  explanation: "Harmonic function describes each chord's role relative to the tonic. Dominant (V) creates high tension demanding resolution to tonic; subdominant (IV) creates forward momentum toward the dominant. V → IV reverses this logic, retreating from high-tension dominant back to subdominant. Both chords are diatonic, but functional logic requires motion from subdominant toward dominant, not backward. The progression fights against the directional grain of tonal music."

- question: "Which of the following progressions most clearly exemplifies the T → SD → D → T functional arc?"
  type: multiple-choice
  options:
    - "I → V → IV → I"
    - "I → IV → V → I"
    - "IV → I → V → IV"
    - "I → V → I → IV"
  answer: 1
  explanation: "I → IV → V → I traces the canonical tonic → subdominant → dominant → tonic arc. The I chord establishes stability; IV creates tension and forward motion; V intensifies the pull toward resolution; I fulfills it. Option A (I → V → IV → I) breaks the functional ordering by placing dominant before subdominant, then ending with a plagal IV → I motion that lacks the drive of an authentic V → I cadence."

- question: "A dominant seventh chord (V7) that resolves to vi instead of I no longer expresses dominant function — the unexpected move reassigns it a different harmonic role."
  type: true-false
  answer: false
  explanation: "V7 → vi is a deceptive cadence, but V7 still expresses dominant function. The dominant chord creates tension and expectation; the deceptive resolution to vi sidesteps that expectation rather than canceling the underlying function. The vi chord substitutes for I (they share two common tones) and temporarily defuses the tension, but it is precisely V7's dominant function that makes the deception effective — the listener expects I and gets vi. Function is a property of the chord's position and behavior, not only its resolution target."

- question: "A I chord always provides a complete sense of rest and stability whenever it appears in a progression."
  type: true-false
  answer: false
  explanation: "Context and voice leading dramatically affect how stable a I chord feels. A I chord in first inversion (third in the bass) feels less stable than root-position I. A I chord arriving mid-phrase may feel like a momentary landing rather than a final cadence. The Common Misconceptions note directly states that 'not all I chords feel equally tonic.' Tonic function is contextual, not automatic — the same chord can feel conclusive or provisional depending on what surrounds it."

- question: "Explain why V → IV feels harmonically awkward in tonal music. Use the concept of harmonic function in your answer."
  type: short-answer
  answer: "V has dominant function: it creates high tension and a strong pull toward resolution on the tonic. IV has subdominant function: it provides forward momentum in the direction of the dominant. Moving V → IV reverses the functional order — retreating from dominant 'back' to subdominant rather than resolving forward to tonic. Tonal progressions derive their sense of direction from the T → SD → D → T arc; V → IV undermines this by releasing tension in the wrong direction and retracing harmonic ground."
  explanation: "The functional hierarchy (T → SD → D → T) is what gives tonal progressions their sense of inevitability. Any motion that moves backward in that hierarchy fights the grain of tonal logic and sounds like a step in the wrong direction. This is independent of whether both chords belong to the key — diatonicism and harmonic function are separate questions. A student who knows Roman numerals but not functional logic will accept V → IV as 'two diatonic chords'; a student who grasps function recognizes it as backward motion."
```

## Explainer

From your prerequisites in harmonic function basics and Roman numeral analysis, you can label chords by their scale-degree root and recognize their general roles in a key. Harmonic function and chord progressions deepens this by organizing those roles into a **directional hierarchy** — tonic (T), subdominant (SD), and dominant (D) — that explains why some progressions sound inevitable while others sound aimless. The core insight is that chords do not simply "belong to a key"; they have specific functional roles that create directional flow when arranged properly and resist it when arranged improperly.

The canonical functional arc is **T-SD-D-T**: tonic establishes stability, subdominant creates forward motion, dominant intensifies the pull toward resolution, and tonic fulfills it. In C major, the progression I-IV-V-I traces this arc cleanly: C major (tonic, stable) moves to F major (subdominant, creating motion) to G major (dominant, demanding resolution) back to C major (tonic, resolution achieved). Each step in the arc increases tension until the final return to tonic. This is not merely a convention — it reflects the acoustic relationship between these chords and the perceptual hierarchy listeners construct when tracking harmonic motion.

Understanding why **V-IV feels awkward** is the key test of functional thinking. Both V and IV are diatonic chords in C major, and a student who knows only Roman numerals might see no problem. But functionally, V-IV moves **backward** — retreating from dominant (high tension, demanding resolution) to subdominant (forward momentum, preparing dominant). The progression fights the directional grain of tonal music: it releases dominant tension in the wrong direction instead of resolving it forward to tonic. This is not an absolute prohibition — rock music uses IV after V regularly, and plagal motion (IV-I) has its own gentler character — but in common-practice tonal syntax, the functional ordering T-SD-D-T is the gravitational framework that makes progressions feel directed.

Chords that share a functional category can substitute for each other. The ii chord and the IV chord both serve subdominant function — ii-V-I and IV-V-I both trace the SD-D-T arc. The vi chord can substitute for I in a deceptive cadence (V-vi) because vi shares two common tones with I and partially satisfies the tonic function. These substitutions are not arbitrary — they work because the substitute chord shares the functional role of the chord it replaces. A deceptive cadence is "deceptive" precisely because vi delivers partial tonic function without full resolution, leaving the listener expecting the real I to arrive. Labeling chords with their functions (T, SD, D) rather than just their Roman numerals reveals this logic: you see the functional arc of the progression, not just its chord-by-chord identity, and you can explain why the progression drives forward or stalls.
