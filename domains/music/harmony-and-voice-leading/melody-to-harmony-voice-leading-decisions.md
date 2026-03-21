---
id: melody-to-harmony-voice-leading-decisions
title: 'Harmonizing Melody: Voice Leading Choices'
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: melody-harmonization-with-voice-leading
  type: hard
- id: harmonic-function-basics
  type: hard
builds-toward:
- reharmonization-voice-leading-techniques
tags:
- melody-harmonization
- chord-selection
- voice-leading
stage: formal-systems
status: draft
---

# Harmonizing Melody: Voice Leading Choices

## Core Idea
Harmonizing a melody requires selecting appropriate chords that support the melody and then voicing those chords with smooth voice leading. The melody note should appear in an appropriate voice (usually soprano), and the remaining voices must complete the harmony while following spacing, doubling, and motion rules. Multiple correct harmonizations may exist for the same melody, each creating a different harmonic context. Voice leading considerations often determine which harmony is most effective.

## Questions

```yaml
- question: "A student harmonizing a melody has two chord choices that both support the melody note and serve the correct harmonic function. In one option, the alto and tenor move by step; in the other, they leap a sixth. Which principle most directly favors the stepwise option?"
  type: multiple-choice
  options:
    - "The melody note must always be in the soprano, so inner voice motion doesn't matter"
    - "Voice leading prefers smooth stepwise motion in inner voices — large leaps are avoided when smaller intervals can achieve the same harmonic result"
    - "Harmonic function requires that inner voices resolve by half-step at all times"
    - "The bass voice is the only voice whose motion determines the quality of the harmonization"
  answer: 1
  explanation: "When two chord choices are equally valid harmonically and functionally, voice leading serves as the tie-breaker. The core voice-leading principle is smooth motion: prefer contrary motion, minimize leaps, resolve tendency tones, avoid parallel perfect intervals. If both IV and ii6 serve pre-dominant function equally well, but ii6 allows stepwise inner-voice motion while IV requires leaps, ii6 wins on voice-leading grounds. This is the third layer of the constraint hierarchy: melody first, function second, voice leading to decide among remaining options."

- question: "A melody note E in C major appears mid-phrase. Several chords contain E (I, iii, IV with extensions, vi). What factor most immediately narrows the list to appropriate chords at this moment?"
  type: multiple-choice
  options:
    - "The register of E in the soprano — higher notes require specific chord types"
    - "Harmonic function: the T–PD–D–T framework determines which chord roles are needed at this structural point in the phrase"
    - "The key signature alone determines which chords contain E"
    - "The number of chord tones the melody note represents — root position is always preferred"
  answer: 1
  explanation: "Harmonic function is the second layer of the constraint hierarchy and the first filter after the melody. Mid-phrase, the music needs forward momentum — tonic function may be appropriate for stability, pre-dominant for moving away, dominant for building tension. The T–PD–D–T framework eliminates chord choices that would cause the wrong functional effect at this structural moment. Voice leading then decides among chords that pass the function test. Neither register nor position alone narrows the field the way harmonic function does."

- question: "For a given melody, there is exactly one correct harmonization that satisfies both harmonic function and voice-leading rules."
  type: true-false
  answer: false
  explanation: "Multiple valid harmonizations of the same melody routinely exist — Bach harmonized the same chorale melodies multiple times with different results, each musically coherent. Within harmonic function constraints, different chords can serve the same role (IV and ii6 both function as pre-dominant). Among those, different voice-leading solutions may all follow the rules while producing different expressive effects. 'Correct' means satisfying the constraints; it does not mean uniquely determined. Recognizing this is essential for understanding harmonization as creative decision-making, not rule-following with one answer."

- question: "Voice leading considerations can serve as a tie-breaker when two chord options equally satisfy harmonic function requirements at a given point in a melody harmonization."
  type: true-false
  answer: true
  explanation: "This is precisely how the three-layer constraint hierarchy works in practice. When harmonic function narrows the field but doesn't uniquely determine a chord, voice leading makes the final selection: prefer the option that keeps lower voices moving smoothly (by step, by contrary motion to the soprano, resolving tendency tones). The tie-breaker role of voice leading is what makes it the third layer rather than an overriding first principle — it operates after function has narrowed the candidates."

- question: "Describe the three-layer constraint hierarchy used when harmonizing a melody, explaining what each layer contributes and how the layers interact."
  type: short-answer
  answer: "The melody is the fixed constraint — it cannot be changed. Harmonic function (the T–PD–D–T framework) narrows the field of plausible chords for each melody note by eliminating those that serve the wrong functional role at that structural moment. Voice leading then decides among the remaining options by favoring progressions where inner voices move smoothly — by step, by contrary motion, resolving tendency tones, avoiding parallel perfect intervals. The layers interact sequentially: melody → function → voice leading, with each layer reducing the field further."
  explanation: "Understanding this hierarchy prevents two common errors: (1) choosing chords based purely on which ones contain the melody note, ignoring function; (2) choosing chords based purely on function, ignoring which produces the smoothest voice leading. The hierarchy also explains why multiple valid harmonizations exist: different chord combinations can satisfy both function and voice-leading constraints, each producing a different expressive character. Studying multiple harmonizations of the same melody reveals this most clearly."
```

## Explainer

When you harmonize a melody, you are working with a constraint hierarchy. The melody is fixed — it is your given. **Harmonic function** (from your study of tonic, pre-dominant, and dominant functions) narrows the field of plausible chords for each melody note. And finally, **voice leading** decides among the remaining options by favoring the progression that keeps lower voices moving smoothly. These three layers — melody, function, voice leading — interact at every chord choice, and the most effective harmonizations are those where all three align.

Start with the melody note's membership in potential chords. A melody note of E in C major could belong to the I chord (as the third), the iii chord (as the root), the IV chord (as the major seventh, if you include extensions), the vi chord (as the fifth), or potentially as a non-harmonic tone over other chords. That is a lot of options. Harmonic function prunes this list: at a phrase ending, you need a cadential formula (typically dominant–tonic or half-cadence on V). Mid-phrase, you need harmonic motion that propels forward without settling prematurely. The **T–PD–D–T** framework from your harmonic function study provides the roadmap: tonic chords establish, pre-dominants move away, dominants create tension, tonic returns for resolution. When a melody note can support a chord that serves the right function at the right moment, that is a strong candidate.

Voice leading then evaluates candidates by their smoothness in context. Suppose at a particular moment both IV and ii6 would support the melody note and serve pre-dominant function equally well. The tie-breaker is how the lower voices arrive at each option and depart from it. If the alto and tenor can reach the ii6 chord by step from the previous chord but would require a leap to reach IV, the ii6 is probably better voice-leading. If the IV chord creates a particularly smooth bass line by contrary motion to the soprano, it may be preferred. The point is that this decision is not arbitrary — it follows from the principle you already know: prefer contrary motion, minimize leaps, resolve tendency tones, avoid parallel perfect intervals.

The soprano voice's harmonic position matters too. When the melody note is the root of the chord (**root position in soprano**), the harmony feels stable and direct. When the melody note is the third (**third in soprano**), the harmony feels softer and slightly open. When the melody note is the fifth (**fifth in soprano**), the effect depends on context — it can sound noble in a perfect authentic cadence, or slightly ambiguous mid-phrase. Learning to choose a chord inversion partly based on what melodic position the soprano occupies is an advanced harmonization skill: a final cadence where the soprano lands on scale degree 1 (the root) over a root-position I chord sounds conclusive; landing on 3 or 5 sounds incomplete, which may be exactly what you want for a half-cadence or an interior phrase ending.

Multiple harmonizations of the same melody are not only possible but illustrative. Bach harmonized many of the same chorale melodies multiple times over his career, and the different harmonizations illuminate how the same melodic constraints can support different expressive narratives. The melody that ends on E in C major might be harmonized I in the first version (landing on the third, soft ending), iii in a second version (more modal color), or even as a deceptive cadence (V–vi, where E appears as the third of vi). Studying multiple harmonizations of the same melody teaches you more about voice leading and harmonic function than any amount of abstract rule-following, because it makes visible the web of decisions behind each option.

## How It's Best Learned
Choose a simple melody (hymn tune or folk song) and write multiple harmonizations for the first phrase, comparing how different chord choices and voice leading create different effects. Analyze existing harmonizations to reverse-engineer the decision process.
