---
id: applied-chords-voice-leading-tonicization
title: Applied Chords and Voice-Leading in Tonicization
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: secondary-dominants
  type: hard
- id: voice-leading-principles
  type: hard
builds-toward:
- chromatic-approach-voice-leading
- voice-leading-in-composition
tags:
- applied-chords
- secondary-dominants
- tonicization
stage: formal-systems
status: draft
---

# Applied Chords and Voice-Leading in Tonicization

## Core Idea
Applied dominant and secondary seventh chords momentarily tonicize scale degrees other than tonic. Voice leading these chords requires resolving tritones and tendency tones to the tonicized chord, creating harmonic color while maintaining voice independence.

## How It's Best Learned
Analyze applied chords in classical pieces; write progressions with applied dominants, focusing on smooth voice leading to the tonicized chord.

## Questions

```yaml
- question: "In C major, a composer wants to tonicize the ii chord (D minor) using an applied dominant. Which chord achieves this?"
  type: multiple-choice
  options:
    - "E minor (iii in C major), because it shares two notes with the ii chord"
    - "A major (A–C#–E), because it is the dominant of D and introduces the leading tone to D"
    - "G dominant seventh (V7 of C), because it resolves to the tonic which precedes ii"
    - "F major (IV in C major), because it moves by step to the ii chord"
  answer: 1
  explanation: "The applied dominant of ii is V/ii — the dominant chord of D minor, which is A major (A–C#–E). The C# is the leading tone of D, and its presence temporarily makes D feel like a local tonic. This is the mechanism of tonicization: borrowing dominant function from another key to give a non-tonic scale degree momentary tonal weight. G7 is the home-key dominant (V7 of C major), not the applied dominant of D."

- question: "When resolving an applied dominant chord (e.g., V/V → V in C major), how should the raised chromatic note — the temporary leading tone — move?"
  type: multiple-choice
  options:
    - "It should descend by a half step to avoid creating an angular chromatic line"
    - "It should remain stationary to preserve voice-leading smoothness"
    - "It should ascend by a half step to resolve to the root of the tonicized chord"
    - "It may move freely in either direction since applied chords are non-functional"
  answer: 2
  explanation: "The raised chromatic note in an applied chord functions as a leading tone to the tonicized chord — it sits a half step below the root of the chord it tonicizes. Like the regular leading tone in the home key, it carries strong upward tendency and should resolve upward by a half step. In V/V → V in C major (D major → G major), the F# resolves up to G. Allowing it to descend wastes the expressive pull of the chromatic inflection and weakens the voice leading."

- question: "An applied chord (such as V/IV) permanently shifts the tonal center of a piece away from the home key."
  type: true-false
  answer: false
  explanation: "Applied chords produce tonicization, not modulation. Tonicization is a temporary, brief emphasis on a non-tonic scale degree — typically lasting one or two chords — after which the music returns to the home key. Modulation involves an extended commitment to a new key with cadential confirmation. A single applied chord followed by a return to home-key function is tonicization; the tonal center of the piece has not changed."

- question: "The tritone in an applied dominant seventh chord resolves in the same way as the tritone in the home-key dominant seventh — with each voice moving by half step toward the other."
  type: true-false
  answer: true
  explanation: "Applied dominant seventh chords contain tritones that behave exactly like the tritone in the home-key V7: the diminished fifth resolves inward (both voices move by half step toward each other). The resolution is to the tonicized chord rather than the home tonic, but the voice-leading logic is identical. This consistency is what makes applied chords effective: the listener hears a familiar tension-resolution pattern, momentarily oriented toward a new goal."

- question: "What is the difference between tonicization and modulation, and how does the use of applied chords relate to each?"
  type: short-answer
  answer: "Tonicization is a brief, temporary emphasis on a non-tonic scale degree, typically through one or a few applied chords, after which the piece returns to the home key without establishing a new one. Modulation is an extended change of key with cadential confirmation in the new key. Applied chords are the primary tool of tonicization — a V/ii chord gives the ii chord momentary tonal weight — but they do not by themselves establish a new key. Modulation requires the new key to be confirmed by authentic cadences and sustained harmonic activity."
  explanation: "The distinction matters for analysis and composition. A single applied chord followed by a return to home-key function is tonicization — a local color event. A passage that moves through V/V → V and then cadences fully in the dominant (with its own ii–V–I) is likely a modulation. Applied chords are the gateway to tonicization, but the surrounding harmonic commitment determines whether the effect is local color or genuine key change."
```
