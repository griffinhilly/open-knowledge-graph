---
id: secondary-harmony-functional
title: Secondary Harmony and Functional Extension
domain: music
course: composition
prerequisites:
- id: secondary-dominant-recognition
  type: hard
- id: harmonic-function-basics
  type: hard
- id: voice-leading-principles
  type: soft
builds-toward:
- borrowing-parallel-modes
tags:
- harmony
- secondary-function
- dominants
- voice-leading
stage: formal-systems
status: draft
---

# Secondary Harmony and Functional Extension

## Core Idea
Secondary dominants and other applied chords extend harmonic vocabulary beyond diatonic harmony, allowing temporary tonicizations and harmonic coloring. Their effective use requires understanding functional direction and smooth voice-leading resolution.

## Questions

```yaml
- question: "In C major, a composer writes A7 (A-C#-E-G) followed by Dm. What is happening harmonically?"
  type: multiple-choice
  options:
    - "A7 is a borrowed chord from the parallel minor key"
    - "A7 is functioning as V7/ii — a secondary dominant tonicizing D minor — with C# as the leading tone resolving to D"
    - "A7 is a coloristic chord with no directional function"
    - "A7 is the dominant of the dominant (V/V) in C major"
  answer: 1
  explanation: "A7 contains C# (one half step below D, acting as leading tone to D) and G (which resolves down to F# or back to the chord tone). This mirrors the G7 → C relationship in C major but aimed at D minor: A7 → Dm is V7/ii → ii. C# must resolve up to D for the applied chord to realize its function. V/V would be D7 (D-F#-A-C), which targets G — a different destination entirely."

- question: "A student labels any chord with a chromatically raised note as 'a secondary dominant.' Their teacher says the chord might instead be 'coloristic.' What is the key distinguishing factor?"
  type: multiple-choice
  options:
    - "Secondary dominants appear in major keys; coloristic chords appear in minor keys"
    - "Secondary dominants resolve their leading tone upward and their seventh downward to the target chord; coloristic applied chords skip this resolution"
    - "Secondary dominants are always V7 chords; coloristic chords are triads without sevenths"
    - "The difference is rhythmic: secondary dominants occupy strong beats, coloristic chords occupy weak beats"
  answer: 1
  explanation: "Functional secondary harmony is defined by resolution. The applied chord's leading tone (the raised note pointing toward the target chord's root) must resolve upward by half step, and the chordal seventh must resolve downward, to create the tonicization effect. If the progression moves elsewhere — if the resolution is avoided — the chord becomes coloristic (chromatic flavor without direction). The same chord can be functional or coloristic depending entirely on what follows it."

- question: "A secondary dominant always introduces at least one note that is chromatic — outside the home key's diatonic collection."
  type: true-false
  answer: true
  explanation: "The defining feature of a secondary dominant is its leading tone to the target chord's root — a pitch raised by a half step relative to the home key's scale degree at that position. This raised note is typically not part of the home key's diatonic collection, making secondary dominants chromatic chords. It is this chromatic leading tone that creates the applied chord's distinctive pull and the momentary brightening of the target chord's status."

- question: "If the leading tone of a secondary dominant does not resolve upward by a half step, the chord still functions as a secondary dominant because its function is determined by its chord tones, not its resolution."
  type: true-false
  answer: false
  explanation: "Harmonic function is realized through voice leading, not notation. Without the leading tone resolving upward to the target chord's root, the sense of tonicization — the 'promise' — is not kept. The chord becomes coloristic rather than functional: it adds chromatic color without creating directional momentum. The notation V/x describes the chord's potential function; the resolution is what activates that function. Both effects are musically valid, but you must know which you are creating."

- question: "What is tonicization, and how does a secondary dominant achieve it?"
  type: short-answer
  answer: "Tonicization is the momentary treatment of a chord other than the home tonic as though it were a temporary tonic — giving it a brief sense of arrival and weight. A secondary dominant achieves this by applying the dominant-to-tonic resolution logic to a new target: its leading tone (raised half step below the target root) resolves upward, and its chordal seventh resolves downward, creating the same charged pull that V7 → I has in the home key, but aimed at a different chord."
  explanation: "The mechanism of tonicization borrows the V7 → I resolution logic and applies it generatively to any chord in the key. This is why secondary dominants are called 'applied chords' — the dominant function is applied to a new temporary tonic. The key insight is that 'dominant' is a relational role, not an absolute chord identity: any chord can serve as a dominant to the chord a fifth below it, and secondary harmony exploits this generalization throughout common-practice music."
```

## Explainer

You already understand harmonic function — tonic, pre-dominant, and dominant chords each occupy a role in the phrase, and the dominant chord is defined by its strong pull back toward the tonic. Secondary harmony extends this logic by asking: what if we applied that dominant-to-tonic pull not just to the home key's tonic, but temporarily to any chord in the key? The result is an **applied chord** — a harmony that functions as a V (or V7, or vii°7) to a chord other than the tonic. The most common applied chord is the **secondary dominant**, typically notated V/x, meaning "the dominant of chord x."

Think of it this way: in C major, the chord G7 (V7) wants to resolve to C (I). That pull comes from the tritone between B and F — the third and seventh of G7 — which resolves inward to the third and root of C major. Now apply the same logic to the chord D minor (ii in C major). What chord would function as a "dominant" of D minor? The answer is A7 — it contains the notes C# (the leading tone of D) and G (which resolves down), just as G7 contains B and F relative to C. So A7 acts as V/ii, and when it resolves to Dm, the listener briefly hears D as a temporary tonic. This is **tonicization**: not a full modulation, but a momentary brightening or darkening of a chord's status through its applied dominant.

Secondary dominants are especially effective for coloring harmonically important chords or creating directional momentum through a progression. A V/V (D7 in C major) pushing to the dominant G creates an arrival on G that feels earned rather than routine. Consecutive tonicizations — for example, V/vi → vi → V/ii → ii → V → I — create a chain of applied dominants that passes through the key's diatonic harmonies while adding chromatic spice at each step. These chains, sometimes called **harmonic sequences**, appear everywhere in common-practice music.

The **voice-leading** requirements follow directly from what you know about dominant resolution. The applied chord's leading tone (the raised pitch that points toward the root of the target chord) must resolve upward by half step. The chordal seventh, if present, resolves downward by step. Following these rules maintains the sense of functional direction that makes tonicization convincing. If you break them — if the leading tone doesn't resolve, or the seventh leaps — the chord's applied function evaporates and it sounds like a coloristic chord rather than a directional one. Both effects are usable, but you need to know which one you're creating. Functional secondary harmony is the directional kind: every applied chord is a promise, and resolution is how you keep it.
