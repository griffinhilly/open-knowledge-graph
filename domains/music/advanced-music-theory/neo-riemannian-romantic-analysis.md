---
id: neo-riemannian-romantic-analysis
title: Neo-Riemannian Analysis of Romantic Music
domain: music
course: advanced-music-theory
prerequisites:
- id: neo-riemannian-operations
  type: hard
- id: romantic-period-overview
  type: soft
tags:
- neo-riemannian
- romantic
- analysis
- 19th-century
stage: advanced
status: draft
---

# Neo-Riemannian Analysis of Romantic Music

## Core Idea
The music of late Romantic composers like Wagner, Liszt, and Brahms can be understood through neo-Riemannian operations, showing how chromatic harmony creates smooth voice leading while obscuring or reimagining traditional tonal function. This framework explains stylistic innovation in the 19th century without abandoning pitch-centric analysis.

## Questions

```yaml
- question: "A Romantic passage moves E major → C major → Ab major. A student labels these as 'I → bVI → bIII in E major' using Roman numerals. What does this analysis fail to explain that neo-Riemannian analysis captures?"
  type: multiple-choice
  options:
    - "It fails to identify the key center of the passage"
    - "It fails to explain why the progression sounds smooth: each chord shares two common tones with the next, and only one voice moves, making the voice leading maximally efficient"
    - "It incorrectly identifies the roots — C major is not a bVI in E major"
    - "Roman numeral analysis cannot be applied to chromatic passages at all"
  answer: 1
  explanation: "Roman numeral analysis correctly identifies functional distance (these chords are 'far' from tonic in key-space) but doesn't explain the perceived smoothness. Neo-Riemannian analysis reveals that E→C and C→Ab are each PLR operations sharing two common tones, with only one voice moving by a half or whole step. This hexatonic cycle has a structural logic — maximally smooth voice leading — that functional analysis labels but does not illuminate. Option C is wrong: C major can indeed be analyzed as bVI in E major."

- question: "Which of the following best describes the analytical advantage of tracing a passage as a 'path through the Tonnetz' rather than using functional harmonic analysis?"
  type: multiple-choice
  options:
    - "It reveals the key of the passage more accurately than Roman numerals"
    - "It allows analysis of chromatic harmony that avoids or defers tonal centers by describing voice-leading efficiency geometrically, without requiring a reference tonic"
    - "It proves that late Romantic composers abandoned tonality entirely"
    - "It applies only to Wagner's music, not Liszt or Brahms"
  answer: 1
  explanation: "The Tonnetz models pitch-class relationships geometrically. When Romantic composers chain PLR operations to navigate distant harmonic regions, these paths are coherent on the Tonnetz even when no functional V–I anchors establish a key. This is not 'atonal' music — it still uses triads — but it operates by a different logic (voice-leading proximity on the Tonnetz) rather than functional direction toward a tonic. Options C and D are factually wrong."

- question: "Traditional Roman numeral analysis fully explains the smooth, connected quality of mediant (third-related) chord progressions in late Romantic music."
  type: true-false
  answer: false
  explanation: "False. Roman numeral analysis identifies the functional distance — for example, E major to C major as 'I to bVI' — and correctly notes that they are not closely related in functional terms. But it does not explain why this progression *sounds* smooth. Neo-Riemannian analysis provides the explanation: these chords share two common tones and require only a single voice to move. The smooth quality is a property of voice-leading geometry, which Roman numerals do not capture."

- question: "In neo-Riemannian theory, each P, L, and R operation changes exactly one voice while holding the other two voices fixed (or nearly so)."
  type: true-false
  answer: true
  explanation: "True — this is the defining property of PLR operations. P (Parallel) holds the fifth and moves the third by a half step; L (Leading-tone exchange) holds two tones and moves one by a half step; R (Relative) holds two tones and moves one by a whole step. The preservation of two common tones while a single voice moves a minimal distance is precisely what makes these operations 'parsimonious' and what accounts for the characteristic smooth sound of neo-Riemannian progressions in Romantic music."

- question: "Why is neo-Riemannian theory particularly well-suited for analyzing Wagner, Liszt, and late Brahms, and what gap in functional analysis does it fill?"
  type: short-answer
  answer: "Late Romantic composers frequently avoid or defer functional V–I cadences, moving between harmonically distant chords in ways that sound smooth but resist key-center analysis. Neo-Riemannian theory fills the gap by describing the voice-leading logic that makes these progressions cohere: PLR operations connect triads through shared tones and minimal voice movement, tracing paths on the Tonnetz that are structurally consistent even without a tonic. Functional analysis can label chords but predicts they should sound disjunct; neo-Riemannian analysis explains why they don't."
  explanation: "The key insight is that Romantic composers moved to a different harmonic logic — not broken tonality but a geometry of voice-leading efficiency. Functional analysis was designed for music organized around dominant-tonic motion; it mislabels or ignores the structural principle actually at work in chromatic mediant progressions and hexatonic cycles."
```

## Explainer

You already know the three fundamental **neo-Riemannian operations**: P (Parallel), L (Leading-tone exchange), and R (Relative). Each transforms a triad into an adjacent triad by moving a single voice by a half step or whole step, preserving the other two voices. P converts a major triad to its parallel minor (or vice versa); L moves from major to its leading-tone minor (or vice versa); R moves between relative major and minor. What you now apply is these tools to real Romantic repertoire, where functional harmony — dominant-to-tonic progressions that anchor a key — becomes increasingly unstable, deferred, or absent.

The defining harmonic feature of late Romantic music is **chromatic saturation**: chords move through distant keys without the traditional V–I anchors that establish tonic. In Wagner's *Tristan und Isolde*, the famous "Tristan chord" resolves not to a tonic but to another dominant-quality harmony, creating an unrelenting sense of suspended yearning. Neo-Riemannian analysis captures this: chains of P, L, and R operations navigate the **Tonnetz** (the pitch-class network underlying these operations) through maximally smooth voice-leading paths that cover large distances in key-space without requiring functional preparation. The harmony moves but nothing is "resolved" in the traditional sense.

Liszt and late Brahms also favor **mediant relationships** — chord progressions a third apart (E major to C major, for instance) — that sound surprisingly smooth despite being harmonically distant. These are exactly the relationships that neo-Riemannian operations describe: an R operation from E major gives C# minor; an L from E major gives G# minor. The Tonnetz makes it visible why these progressions feel connected: they share two common tones. Traditional Roman numeral analysis, which labels these as "III" or "VI" chords, describes their functional distance but doesn't explain the smooth, connected quality of the voice leading. Neo-Riemannian analysis does.

The analytical payoff is that you can trace entire passages of chromatic harmony as **paths through the Tonnetz** without invoking a key at all. A sequence like E major → C major → Ab major (three major triads each a major third apart) is a PLR chain that cycles back to E after six steps — a structure Cohn calls the **hexatonic cycle**. These cycles appear frequently in late Romantic music as agents of harmonic color-shifting rather than tonal direction. The framework reveals that what sounds like tonal instability is, from a voice-leading perspective, maximally efficient and structurally consistent. Romantic composers did not abandon harmonic logic — they moved to a different kind of logic that neo-Riemannian theory is designed to model.


