---
id: seventh-chord-function-and-sound
title: Seventh Chords and Their Function
domain: music
course: music-theory-fundamentals
prerequisites:
- id: diatonic-chord-construction
  type: hard
- id: interval-quality-by-semitone-count
  type: hard
builds-toward:
- voice-leading-smooth-motion-and-errors
- harmonic-analysis-roman-numerals-basics
tags:
- harmony
- seventh-chords
- dominant
- function
stage: formal-systems
status: validated
---

# Seventh Chords and Their Function

## Core Idea
Seventh chords add a seventh degree above the root, creating four-note chords. The dominant seventh (V7) is the most common—it combines the dominant chord's tendency to resolve upward with the tritone (formed by the third and seventh) that demands resolution. Other seventh chords include major seventh, minor seventh, and half-diminished seventh, each with distinct colors and functions.

## Questions

```yaml
- question: "What makes the dominant seventh chord (G7) more harmonically powerful than the dominant triad (G major)?"
  type: multiple-choice
  options:
    - "The added seventh makes the chord louder and more prominent in the texture"
    - "The seventh creates a suspension that delays resolution, building anticipation"
    - "The seventh adds a tritone between the third (B) and seventh (F), where B pulls up to C and F pulls down to E — both resolving by half step simultaneously toward the tonic chord"
    - "The fourth note increases harmonic mass, which strengthens gravitational pull toward the tonic"
  answer: 2
  explanation: "The dominant seventh's power is specific: it is the tritone formed between the third and seventh of the chord (B and F in G7) that creates irresistible momentum. B is the leading tone, wanting to resolve up by half step to C (the tonic). F is the seventh, wanting to resolve down by half step to E (the third of the tonic chord). These two voices squeeze inward simultaneously in contrary motion, making V7–I the strongest, most conclusive harmonic gesture in tonal music. A mere triad has only the leading-tone pull; V7 adds the downward pull of the seventh, doubling the resolution force."

- question: "A Cmaj7 chord appears at the end of a jazz ballad as the final chord. A G7 chord appears just before the final tonic in a Bach chorale. Which best describes the difference in their function?"
  type: multiple-choice
  options:
    - "Both are unstable chords requiring resolution to a more stable harmony"
    - "Cmaj7 is primarily coloristic — adding richness and warmth to a stable resting point; G7 is primarily functional — its tritone creates urgent tension demanding resolution"
    - "Cmaj7 is a weaker version of G7 because major sevenths are less dissonant and therefore less effective"
    - "Both function identically; the difference is purely stylistic between jazz and classical contexts"
  answer: 1
  explanation: "The distinction between coloristic and functional sevenths is the key analytical insight. The major seventh in Cmaj7 (the interval C to B) is a lush, wide interval that adds sophistication without creating urgent harmonic tension — it enriches a stable moment rather than destabilizing it. G7's minor seventh (G to F) contributes to the tritone between B and F, which *does* create urgent tension. Cmaj7 is a final resting place with added color; G7 is an unstable pivot demanding resolution. Treating them as equivalent (option D) misses the functional difference that makes V7 drive harmonic motion while Imaj7 doesn't."

- question: "In the dominant seventh chord G7 (G–B–D–F), the note B wants to resolve upward by half step and the note F wants to resolve downward by half step, because they form a tritone together."
  type: true-false
  answer: true
  explanation: "Exactly right. B is the leading tone of C major — by definition it pulls up to C, the tonic, by half step. F is the minor seventh of G7; in the context of G7 resolving to C major, F moves down by half step to E, the third of the tonic chord. These two resolutions happen simultaneously in contrary motion — B moves up while F moves down — and their combined pull is what gives V7 its characteristic urgency. The tritone (three whole steps = six semitones) is the most dissonant interval in tonal music, and its resolution is what drives V7–I."

- question: "Adding a seventh interval to any triad creates the same kind of urgent harmonic tension as the dominant seventh chord."
  type: true-false
  answer: false
  explanation: "The type of tension created depends entirely on the specific interval formed. The dominant seventh chord's urgency comes from the tritone between its third and seventh — a specific dissonance demanding resolution. A major seventh chord (e.g., Cmaj7: C–E–G–B) adds a major seventh interval, which is wide and lush rather than dissonant. It creates color and warmth without the urgent pull of a tritone. A minor seventh chord (Dm7: D–F–A–C) adds a minor seventh to a minor triad, creating a cooler, understated sound also lacking tritone tension. The V7's power is special, not generic to all seventh chords."

- question: "Explain why the dominant seventh creates 'irresistible harmonic momentum' toward the tonic, using the specific behavior of each note in the chord."
  type: short-answer
  answer: "G7 contains G (root), B (major third / leading tone), D (fifth), and F (minor seventh). B is the leading tone of C major and pulls up by half step to C. F is the seventh and pulls down by half step to E (the third of the C major chord). D moves to C or E with smooth voice leading. The root G moves to C by fourth. But the crucial drivers are B and F: they form a tritone, the most dissonant interval in tonal music, and both want to resolve by half step in opposite directions simultaneously. This dual half-step resolution in contrary motion creates the irresistible sense of arrival on the tonic."
  explanation: "Understanding V7 means understanding the tritone resolution specifically, not just that V7 is 'more tense' than V. The leading tone pull (B→C) existed already in the dominant triad. The seventh (F) adds a second voice pulling in the opposite direction, doubling the resolution force. This is why V7–I is the strongest harmonic gesture in tonal music and why the tritone was historically called diabolus in musica — its dissonance and its powerful resolution were both recognized as remarkable."
```

## Explainer

You already know how to build diatonic chords — triads constructed by stacking thirds within a key — and you've studied interval quality by counting semitones. A **seventh chord** extends this stacking one step further: take a triad and add one more third on top, creating a four-note chord whose highest note is a seventh above the root. Each diatonic scale position produces a characteristic seventh chord type depending on the quality of the triad and the quality of the added seventh interval.

The most important is the **dominant seventh (V7)**. In C major, V7 is G-B-D-F. The triad G-B-D was already the dominant chord with its leading-tone energy; adding the minor seventh F introduces something new — a **tritone** between B and F. You know from interval quality that the tritone (three whole steps) is the most dissonant interval in tonal music, the one medieval theorists called *diabolus in musica*. In G7, B wants to resolve *up* by half step to C (it's the leading tone), and F wants to resolve *down* by half step to E (it's the seventh, pulling toward the third of the tonic chord). These two half-step resolutions squeeze inward simultaneously, creating irresistible harmonic momentum toward the tonic. This is why V7-I is the strongest, most conclusive harmonic motion in tonal music.

The other seventh chord types have different characters. A **major seventh chord** (e.g., Cmaj7: C-E-G-B) adds a major seventh — a wide, lush interval that creates a dreamy, sophisticated sound. The major seventh doesn't create the same urgent resolution pull as the tritone; instead it adds color and warmth. This is why major seventh chords are common in jazz and ballads but rare in classical functional harmony where clear resolution is the priority. A **minor seventh chord** (e.g., Dm7: D-F-A-C) adds a minor seventh to a minor triad, producing a cooler, more understated sound — common on the ii chord (in C major: D-F-A-C) where it adds smooth voice leading into the V chord.

Understanding seventh chords means understanding the difference between **color** and **function**. The V7 chord is primarily *functional* — its internal tritone drives harmonic motion. Major seventh chords are primarily *coloristic* — they extend a sound without creating urgent tension. In analysis, you need to distinguish these: a Imaj7 at the end of a piece is a final resting place with added richness; a V7 is an unstable pivot demanding resolution. As you encounter harmonic progressions, notice not just what the chord is, but whether the added seventh is creating tension that needs releasing or simply extending the color of a stable moment.


