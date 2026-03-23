---
id: harmonic-function-voice-leading-analysis
title: Harmonic Function and Voice Leading Analysis with Roman Numerals
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: roman-numeral-analysis
  type: hard
- id: harmonic-function-basics
  type: hard
builds-toward:
- voice-leading-error-recognition-and-correction
tags:
- roman-numeral-analysis
- harmonic-function
- analysis
stage: formal-systems
status: validated
---

# Harmonic Function and Voice Leading Analysis with Roman Numerals

## Core Idea
Roman numerals indicate chord function, but voice leading reveals how that function is realized in the music. A V chord's function depends on how its tritone resolves and which voice carries the leading tone. Analysis combines harmonic function (indicated by Roman numerals) with voice leading patterns to understand how composers create coherence and meaning. The same Roman numeral progression can sound entirely different depending on voice leading choices.

## How It's Best Learned
Analyze a Bach chorale by first identifying Roman numerals, then examining the voice leading in each progression. Note where standard patterns appear, where exceptions occur, and how the voice leading enforces or contradicts the harmonic function.

## Questions

```yaml
- question: "In a V–I progression in C major, the leading tone B in the soprano voice should resolve to which pitch, and why?"
  type: multiple-choice
  options:
    - "G, because G is the root of the I chord and provides the strongest bass support"
    - "C, because the leading tone pulls upward by half step to the tonic"
    - "B, because common tones should be held over between adjacent chords"
    - "D, because contrary motion with the bass requires an upward leap"
  answer: 1
  explanation: "The leading tone (seventh scale degree, B in C major) has a strong half-step pull upward to the tonic (C). This resolution is the defining voice-leading behavior of dominant-to-tonic motion — it is what makes V feel unstable and I feel resolved. Failing to resolve the leading tone upward undermines the harmonic function of the V chord, even if the Roman numeral labels are correct. Holding B over as a common tone would be incorrect since B is not in the I chord in root position."

- question: "Two students analyze the same Bach chorale excerpt. Both produce the Roman numeral sequence I–ii–V–I. What can they NOT determine from this analysis alone?"
  type: multiple-choice
  options:
    - "The key of the piece"
    - "Which chord has dominant function"
    - "Whether the leading tone resolves correctly upward in the soprano"
    - "Whether the final chord is tonic function"
  answer: 2
  explanation: "Roman numerals tell you harmonic function and chord quality, but not how individual voices move between chords. Whether the soprano carries the leading tone and resolves it upward by half step, whether the bass moves by fifth or step, whether parallel fifths occur — all of these require examining the actual note-to-note voice movement. The Roman numerals I–ii–V–I could be realized with excellent or terrible voice leading; the symbols are agnostic about the specific melodic paths of each voice."

- question: "A Roman numeral analysis of a passage fully explains why that passage sounds emotionally effective or satisfying."
  type: true-false
  answer: false
  explanation: "Roman numerals identify harmonic function but not voice leading — and voice leading is precisely what generates emotional effects. A deceptive cadence surprises because the bass moves to vi instead of I while the soprano still resolves the leading tone upward; that surprise is invisible to Roman numeral analysis. Suspension resolutions, inner-voice passing tones, and the directionality of individual melodic lines all contribute to the emotional character of a passage but appear nowhere in the Roman numeral symbols."

- question: "Contrary motion between the soprano and bass voices makes parallel fifths and parallel octaves between those voices nearly impossible."
  type: true-false
  answer: true
  explanation: "Parallel fifths and octaves occur when two voices move in the same direction by the same interval. If soprano and bass move in opposite directions (contrary motion), they cannot maintain a constant interval between them across the chord change, which prevents the forbidden parallels from arising. This is why contrary motion between outer voices is the primary safeguard in common-practice voice leading and the first analytical checkpoint when examining a progression."

- question: "Explain why voice leading analysis reveals things that Roman numeral analysis alone cannot, using the concept of harmonic function as your starting point."
  type: short-answer
  answer: "Roman numerals indicate what role a chord plays (tonic, dominant, subdominant) but not how that role is enacted through the motion of individual voices. Harmonic function is 'activated' by specific voice-leading behaviors: the dominant's leading tone must rise to the tonic, the V7's chord seventh must fall. If these resolutions don't occur, the harmonic function is weakened or contradicted — but the Roman numeral label doesn't change. Voice leading analysis checks whether the functional labels assigned by Roman numerals are actually operative in the music, and reveals effects (deceptive cadences, elided phrases, suspension chains) that are otherwise invisible."
  explanation: "The key distinction: Roman numerals describe harmonic architecture; voice leading describes how that architecture is inhabited by moving melodic lines. Both layers are needed for a complete account of how a piece works."
```

## Explainer

Roman numeral analysis gives you a symbolic map of harmonic function: I is tonic, IV is subdominant, V is dominant — and from your study of harmonic function basics, you know that these labels describe not just chords but roles in a tension-resolution drama. What Roman numerals don't tell you is *how* those functions are realized in the actual voice movement. Two pieces can share the identical Roman numeral sequence — I–vi–IV–V–I — and sound utterly different depending on whether the soprano leaps or steps, whether the bass moves by fifth or by step, whether common tones are held or abandoned. Voice leading analysis is the missing layer that explains what the symbols alone cannot.

The key entry point is the **leading tone** and the **seventh**. In any dominant chord, the leading tone (the seventh scale degree) has a powerful pull toward the tonic — it is the specific pitch that makes V feel unstable and I feel resolved. In a V7 chord, the seventh of the chord (the fourth scale degree) pulls downward toward the third of I. When you analyze a V–I progression, you're not just noting the chord labels — you're tracking those two voices and confirming that the leading tone rises by half step and the chord seventh falls by step. If it doesn't, something unusual is happening, and the analysis must explain why. This is what makes voice leading analysis precise: it tests whether the harmonic function you've labeled is actually operative in the music or is being subverted.

**Contrary motion** between bass and soprano is the most reliable indicator of good voice leading practice in common-practice music, and it's your first analytical checkpoint. When bass and soprano move in opposite directions across a chord change, parallel fifths and octaves — the forbidden parallels that destroy voice independence — become nearly impossible. When you see soprano and bass moving in the same direction simultaneously, examine the other voices carefully: the composer has chosen that parallel motion for a reason, often to create a particular registral accent or textural effect, and the interior voices must compensate. Bach's chorales are the canonical training ground because they represent perhaps the densest concentration of all the standard voice-leading patterns: suspensions, passing tones in the inner voices, careful resolution of dissonances, and occasional deliberately broken rules that signal cadential emphasis.

The payoff of combined harmonic-function and voice-leading analysis is understanding **why certain progressions work emotionally**. A deceptive cadence (V–vi) surprises because the leading tone still resolves upward to the tonic pitch, but the bass moves to the submediant instead of the expected root — the listener hears the soprano reach the "correct" note but the bass pull in an unexpected direction. An elided cadence keeps the momentum of a phrase going by arriving at the expected chord one beat early and overlapping it with the beginning of the next phrase. These effects are invisible to pure harmonic analysis but become transparent once you layer voice leading into the examination. The Roman numerals explain the harmonic architecture; the voice leading explains how that architecture is inhabited.
