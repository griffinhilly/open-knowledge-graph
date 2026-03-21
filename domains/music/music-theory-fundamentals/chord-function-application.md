---
id: chord-function-application
title: 'Harmonic Function: Tonic, Subdominant, and Dominant'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: harmonic-function-basics
  type: hard
- id: diatonic-chord-construction
  type: hard
builds-toward:
- harmonic-progression-patterns
- cadence-types-and-function
tags:
- harmony
- function
- analysis
stage: formal-systems
status: draft
---

# Harmonic Function: Tonic, Subdominant, and Dominant

## Core Idea
Harmonic function classifies chords by their role in creating tonal motion: tonic chords (I, vi) establish home; subdominant chords (IV, ii) create motion away from tonic; dominant chords (V, vii°) create tension and pull toward resolution. Understanding function is essential for analyzing progressions and composing coherent harmonic sequences.

## How It's Best Learned
Analyze chord progressions in songs and classical pieces, identifying functional roles. Compose progressions using functional relationships rather than random chord choices.

## Common Misconceptions
Function is not determined by Roman numeral alone—a V chord functioning as a substitute tonic in deceptive cadence is subdominant in function, not dominant.

## Questions

```yaml
- question: "In a deceptive cadence (V–vi), the vi chord works as a surprise because it temporarily substitutes for which function?"
  type: multiple-choice
  options:
    - "Dominant function — vi shares notes with V and can extend the tension"
    - "Subdominant function — vi creates motion away from tonic just as IV does"
    - "Tonic function — vi shares enough pitches with I to feel like a weakened form of rest"
    - "No function — deceptive cadences break the functional system entirely"
  answer: 2
  explanation: "The deceptive cadence works precisely because vi can stand in for I (tonic function). In C major, the I chord contains C–E–G; the vi chord contains A–C–E — two of the three notes are shared. The listener expects I (tonic resolution) after V, and gets vi instead — a chord that still provides some sense of rest because of those shared tones, but not full resolution. Calling vi 'dominant' or 'subdominant' would mischaracterize what it does in this context."

- question: "Why does the V chord create stronger pull toward resolution than the IV chord does?"
  type: multiple-choice
  options:
    - "The V chord is louder by convention in tonal music"
    - "The V chord contains the leading tone — the seventh scale degree, a semitone below tonic — which creates upward pressure toward resolution"
    - "The V chord has more notes in common with I than IV does"
    - "The V chord is always played as a dominant seventh, adding dissonance that demands resolution"
  answer: 1
  explanation: "The leading tone (scale degree 7, one semitone below tonic) is the acoustic engine of dominant function. Its half-step proximity to the tonic creates a strong gravitational pull upward. The V chord contains scale degrees 5, 7, and 2; the 7 is the leading tone. The IV chord (scale degrees 4, 6, 1) does not contain the leading tone, which is why it creates directed departure rather than urgent tension. Option D is partially true (V7 is common) but misses the root cause — even a plain V triad exerts dominant pull because of the leading tone."

- question: "The subdominant chord (IV) creates strong harmonic tension that demands immediate resolution, similar to the dominant chord."
  type: true-false
  answer: false
  explanation: "Subdominant function creates departure and directed motion — a sense of leaving home — but not the urgent tension of dominant function. IV sounds stable enough to linger on; V feels unstable and pushes for resolution. This distinction is why the classic progression I–IV–V–I works: IV takes us away from tonic gently, V creates the tension that makes the final I feel satisfying. Confusing subdominant with dominant undermines the whole three-function model."

- question: "The ii chord can serve subdominant function in a ii–V–I progression because it shares most of its pitches with the IV chord."
  type: true-false
  answer: true
  explanation: "In C major: IV = F–A–C; ii = D–F–A. Three of the four notes in a ii7 chord (D–F–A–C) match notes in IV or IV7 (F–A–C–E). This overlap gives ii a similar acoustic weight and directional character to IV — both create a sense of moving away from tonic toward the dominant. The ii–V–I progression is ubiquitous in jazz precisely because ii is a smooth functional substitute for IV, leading into V with particular momentum."

- question: "Why is asking 'what is this chord doing?' a more powerful analytical question than 'what Roman numeral is this?'"
  type: short-answer
  answer: "Roman numerals identify chords by their scale position, but the same chord can serve different functions depending on context. A vi chord usually provides tonic-substitute function, but the same pitches in a different harmonic context could behave differently. Functional thinking reveals the underlying drama of tonal music — departure from home (subdominant), accumulation of tension (dominant), return to rest (tonic) — which is the real engine of progression. It also explains exceptions: why a deceptive cadence works, why ii substitutes for IV, why diminished chords are so restless."
  explanation: "Functional analysis unlocks harmonic substitution, explains cadence types, and reveals the emotional logic behind progressions. A student who only knows Roman numerals can label chords; a student who understands function can explain why progressions move the way they do and compose convincing music. The three functions (tonic, subdominant, dominant) act as a grammar for tonal music — knowing the grammar lets you understand and generate sentences, not just label individual words."
```

## Explainer

You know from diatonic chord construction how to build the seven chords of a key by stacking thirds. You know from harmonic function basics that chords can be grouped by their behavior. This topic gives you the full vocabulary to analyze and compose with those categories. The three functions — **tonic**, **subdominant**, and **dominant** — describe not what a chord is built from, but what it *does* in the context of a key.

**Tonic function** is stability: it's home. The I chord is the clearest expression of tonic, but the vi chord (built on the sixth scale degree) shares enough pitches with I to feel like a weaker or "colored" version of rest — this is why V–vi (the deceptive cadence) works at all. **Subdominant function** is departure: these chords create a sense of moving away from tonic without yet demanding resolution. The IV chord is the prototype; the ii chord carries similar function because it contains three of the same pitches as IV and has a similar acoustic weight. Neither IV nor ii creates strong tension — they create directed motion, a sense of the music leaving home and heading somewhere. **Dominant function** is tension: these chords pull hard toward resolution. The V chord owes its pull partly to the **leading tone** (the 7th scale degree, one semitone below the tonic), which creates a strong upward pressure. The vii° chord contains the same leading tone plus a tritone, making it even more dissonant and urgent.

The power of functional thinking is that it reveals how most tonal progressions are structured around a single underlying drama: departure from home, accumulation of tension, return. The classic I–IV–V–I tells this story in four chords. But functional categories also explain harmonic substitution and exception. A **deceptive cadence** (V–vi) works because vi can temporarily substitute for I — it shares two of I's three notes and provides a moment of rest that isn't full resolution. The extremely common **ii–V–I** progression (prevalent in jazz and classical music alike) works because ii prepares the dominant with directed departure before V delivers the tension that resolves to I. When analyzing any chord progression, train yourself to ask not "what Roman numeral is this?" but "what is this chord *doing*?" — that question is where harmonic understanding actually lives.

