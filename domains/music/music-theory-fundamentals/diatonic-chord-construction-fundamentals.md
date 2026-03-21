---
id: diatonic-chord-construction-fundamentals
title: Understanding Diatonic Chords in Major and Minor Keys
domain: music
course: music-theory-fundamentals
prerequisites:
- id: triad-construction-from-scale-degrees
  type: hard
builds-toward:
- primary-harmony-functions
- harmonic-analysis-roman-numerals-basics
tags:
- harmony
- diatonic
- chords
- major-minor
stage: formal-systems
status: draft
---

# Understanding Diatonic Chords in Major and Minor Keys

## Core Idea
Diatonic chords are those built from the scale degrees of a key, containing only the notes of that scale. In C major, the diatonic chords include C major (I), D minor (ii), E minor (iii), F major (IV), G major (V), A minor (vi), and B diminished (vii°). These seven chords form the harmonic vocabulary of a key and can be analyzed using Roman numeral notation.

## Questions

```yaml
- question: "In G major, what is the quality of the chord built on scale degree ii?"
  type: multiple-choice
  options:
    - "Major — because G major is a 'bright' key with many sharps"
    - "Minor — because scale degree ii always produces a minor triad in any major key"
    - "Diminished — because ii is a dissonant scale degree"
    - "It depends on which version of G major (natural, harmonic, or melodic) is used"
  answer: 1
  explanation: "In every major key, the triad built on scale degree ii is minor. This is not arbitrary — it follows necessarily from the intervals of the major scale. Starting on the second scale degree and stacking two thirds using only scale tones always produces a minor third followed by a major third (a minor triad). The full pattern — major, minor, minor, major, major, minor, diminished — is universal across all major keys. The question of natural/harmonic/melodic forms only applies to minor keys."

- question: "A student says: 'The I-IV-V-I progression sounds different in D major than in F major because the IV chord is a different chord in each key.' What important concept is the student missing?"
  type: multiple-choice
  options:
    - "The IV chord has a different quality in each key, making the progressions genuinely different"
    - "Roman numeral notation captures harmonic function, not specific pitches — IV is always a major triad a perfect fourth above the tonic, regardless of key"
    - "IV is only a valid chord in major keys, not minor, so the comparison doesn't apply"
    - "The progression should be written as I-IV-V₇-I to be harmonically complete"
  answer: 1
  explanation: "Roman numeral notation is key-agnostic: IV always denotes a major triad built on scale degree 4, regardless of what key you're in. In D major, IV is G major; in F major, IV is B♭ major — different pitches, same harmonic function and quality. The progression I-IV-V-I sounds structurally identical in both keys because the relationships between scale degrees are preserved. This key-agnostic thinking is precisely why Roman numerals are more useful for analysis than chord names like 'G major.'"

- question: "In every major key, the chord built on scale degree vii is diminished."
  type: true-false
  answer: true
  explanation: "Building a triad on scale degree 7 of any major scale — using only the notes of that scale — always produces two stacked minor thirds, which defines a diminished triad. In C major: B-D-F (B to D is a minor third, D to F is also a minor third). In G major: F#-A-C (same interval pattern). This is the only diminished chord in the diatonic set and the only chord built from two consecutive minor thirds. Its quality is a direct consequence of the major scale's interval structure, not a special rule."

- question: "Roman numeral analysis applies specifically to classical music and cannot be used to analyze popular or jazz chord progressions."
  type: true-false
  answer: false
  explanation: "Roman numeral analysis is widely used for popular, folk, blues, and jazz music. The I-IV-V-I progression underlying blues and classic rock, the I-V-vi-IV loop common in pop music, and jazz standards built on ii-V-I progressions all use the same Roman numeral framework. The notation is a language for harmonic function that applies wherever diatonic harmony appears — which spans virtually all Western tonal music from the Baroque era through contemporary pop."

- question: "Why does every major key produce the same pattern of chord qualities (major, minor, minor, major, major, minor, diminished), and why does this make Roman numeral notation useful?"
  type: short-answer
  answer: "Every major key shares the same pattern of whole and half steps (W-W-H-W-W-W-H). When you build triads on each scale degree using only the notes within the key, you always stack the same interval relationships relative to each scale degree — the key's interval structure is fixed, so the chord quality pattern is fixed. Roman numerals exploit this: 'IV' always means a major triad on scale degree 4, with the same harmonic function, regardless of the specific pitches involved in a given key. This makes knowledge of harmonic function — like V resolving strongly to I — transferable across all keys without relearning it for each."
  explanation: "The universality of the pattern (major, minor, minor, major, major, minor, diminished) is why musicians can play in any key without memorizing a separate chord system for each. The interval relationships between scale degrees are the same in every major key, so the functional relationships between chords — tension, resolution, color — are also the same. Roman numerals encode these relationships, not the specific pitches, making them the right abstraction for music analysis."
```

## Explainer

From your study of triad construction, you know how to build a major, minor, or diminished triad from any root: stack intervals of a third and a fifth above it. Now the question is: what happens when you apply that same process to every note of a major scale, using only the pitches already in that scale? The answer is the set of **diatonic chords** — the complete harmonic vocabulary of a key.

Take C major: its scale is C-D-E-F-G-A-B. Starting on C and building a triad with scale tones gives you C-E-G (a major triad). Starting on D gives you D-F-A (a minor triad, because the interval from D to F is a minor third). Starting on E gives you E-G-B (another minor triad). The pattern continues: F major, G major, A minor, and finally B-D-F — a **diminished triad**, the only one in the set, because it stacks two minor thirds. This pattern — major, minor, minor, major, major, minor, diminished — is not arbitrary. It's the inevitable result of building triads exclusively from a major scale's intervals. Every major key produces exactly this sequence, just starting on different root pitches.

**Roman numeral notation** labels each chord by its scale degree position: uppercase for major (I, IV, V), lowercase for minor (ii, iii, vi), and lowercase with a degree symbol for diminished (vii°). This notation is key-agnostic — "V" means the same harmonic function in C major, G major, or F# major. Once you understand that V (the dominant) has a strong tendency to move to I (the tonic), that knowledge applies everywhere. The Roman numeral system is therefore a language for describing harmonic function and motion independently of the specific key you're in.

Minor keys add a layer of complexity because of the three forms of the minor scale (natural, harmonic, melodic), each with different raised or lowered degrees. The harmonic minor raises scale degree 7 to create a leading tone — the half-step below the tonic that so strongly pulls toward resolution. This raised 7th changes the chord built on scale degree 5: in natural minor, v is a minor triad; in harmonic minor, V becomes a major triad, with the same dominant energy as in major keys. The chord on scale degree 7 also shifts from major (VII in natural minor) to diminished (vii°) in harmonic minor. Understanding why composers typically use these raised forms in harmonic contexts — not just which chord symbols result — gives you insight into why tonal music works the way it does.

The diatonic chord set is where music theory becomes genuinely useful for analysis and composition. Nearly every tonal piece from 1600 to 1900 — and most popular music today — can be analyzed almost entirely with these seven chords. Roman numeral analysis lets you identify patterns (the I-IV-V-I progression that underlies blues, folk, and classical music alike), understand why certain progressions sound complete and others don't, and recognize when a composer ventures beyond the diatonic set to create tension or surprise. This set is the harmonic home base from which all tonal music departs and to which it returns.

