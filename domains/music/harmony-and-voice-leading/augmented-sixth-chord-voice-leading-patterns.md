---
id: augmented-sixth-chord-voice-leading-patterns
title: Augmented Sixth Chord Voice-Leading Patterns
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: augmented-sixth-chords
  type: hard
- id: voice-leading-smooth-stepwise-motion
  type: hard
- id: seventh-chord-voice-leading-resolution
  type: soft
builds-toward:
- chromatically-altered-harmony-mixture
tags:
- augmented-sixth
- Italian
- French
- German
- chromatic
stage: formal-systems
status: draft
---

# Augmented Sixth Chord Voice-Leading Patterns

## Core Idea
Augmented sixth chords (Italian, French, German) are chromatic chords that resolve to tonic 6/4, with the augmented sixth interval expanding outward to an octave. Each variant has specific voice-leading patterns: Italian (iv6/5), French (iv7/5#4), and German (iv6/5#3) each contain different chromatic pitches that must resolve correctly. Voices typically approach the 6/4 through stepwise motion, creating smooth resolution of the tritone interval.

## Questions

```yaml
- question: "The German augmented sixth chord differs from the Italian augmented sixth chord primarily because:"
  type: multiple-choice
  options:
    - "The German sixth resolves to the dominant seventh chord rather than the tonic 6/4"
    - "The German sixth contains an additional chromatic pitch — a minor third above the bass — giving it four distinct pitches compared to the Italian sixth's three"
    - "The German sixth's augmented sixth interval contracts inward to a unison rather than expanding outward to an octave"
    - "The German sixth is used exclusively in minor keys, while the Italian sixth appears only in major keys"
  answer: 1
  explanation: "All three augmented sixth chord types share the defining feature: a chromatic bass pitch (typically the lowered sixth scale degree) and a raised fourth scale degree forming an augmented sixth interval that expands to an octave. The Italian sixth has only three distinct pitches: the bass, the tonic above it, and the raised fourth. The French sixth adds the second scale degree (#4 above bass). The German sixth adds a minor third above the bass (the lowered third scale degree), producing four pitches — the same as a dominant seventh chord enharmonically. Each variant's extra chromatic pitch must resolve correctly."

- question: "In C major, an augmented sixth chord has Ab in the bass and F# in an upper voice — the augmented sixth interval. Where do these two voices move when resolving to the tonic 6/4?"
  type: multiple-choice
  options:
    - "Both voices move upward — Ab ascends to A♮ and F# ascends to G"
    - "Both voices converge on G by contrary stepwise motion — Ab descends a half step to G and F# ascends a half step to G — the augmented sixth expanding outward to a perfect octave"
    - "Ab moves up to A♮ (scale degree 6) while F# resolves down to E (scale degree 3)"
    - "The two outer voices hold while the inner voices resolve"
  answer: 1
  explanation: "The augmented sixth interval resolves by contrary outward motion: the lower voice (Ab, ♭6̂) descends by half step to G (5̂), and the upper voice (F#, ♯4̂) ascends by half step to G (5̂). Both voices land on the same pitch class — the dominant scale degree — creating a perfect octave. This outward expansion from the dissonant augmented sixth (enharmonically a minor seventh's width) to a consonant octave on the dominant is the defining voice-leading gesture of all augmented sixth chords, and the source of their characteristic forward drive."

- question: "The augmented sixth interval in augmented sixth chords expands outward to a perfect octave when resolving to the tonic 6/4 chord."
  type: true-false
  answer: true
  explanation: "This outward expansion is the defining voice-leading feature of the entire augmented sixth family. The ♭6̂ in the bass moves down by half step to 5̂; the ♯4̂ in an upper voice moves up by half step to 5̂. Both arrive on the dominant scale degree — the same pitch class — creating a perfect octave. This contrary half-step motion from the two chromatic notes is what gives these chords their characteristic urgency and forward pull toward the dominant."

- question: "The Italian, French, and German augmented sixth chords all contain exactly the same pitches and differ only in how those pitches are distributed among the voices."
  type: true-false
  answer: false
  explanation: "Each variant has a different number of distinct pitches and different chromatic content. The Italian sixth contains three pitches (♭6̂, 1̂, ♯4̂). The French sixth adds a fourth pitch: 2̂ (the supertonic). The German sixth also has four pitches but replaces 2̂ with ♭3̂ (the lowered mediant), making it enharmonically equivalent to a dominant seventh chord. These are genuinely different chords with different chromatic notes, not the same chord revoiced."

- question: "What makes the augmented sixth interval such an effective dominant preparation? Explain why the outward resolution of its two defining voices to an octave creates strong forward motion."
  type: short-answer
  answer: "The augmented sixth interval is highly dissonant and unstable, creating strong expectation of resolution. Its two defining pitches — the lowered sixth scale degree below and the raised fourth scale degree above — point in opposite directions: each is a half step away from the dominant scale degree (5̂), which they approach by contrary motion. This half-step pull from both sides simultaneously is maximally directed: both voices move toward the same goal by the smallest possible melodic motion. The resulting octave on the dominant creates strong arrival energy that propels the music toward the tonic six-four and ultimately the authentic cadence. No other pre-dominant harmony has quite this double chromatic half-step pressure toward the dominant."
  explanation: "The key mechanism is dual half-step approach: both ♭6̂ and ♯4̂ are chromatically adjacent to 5̂ and move toward it by contrary motion. This is different from diatonic pre-dominant chords (IV, ii), which approach the dominant by whole step or larger intervals. The augmented sixth's chromatic compression creates what theorists sometimes call a 'gravitational pull' — both voices are one step away from their goal, and they arrive simultaneously from opposite directions."
```
