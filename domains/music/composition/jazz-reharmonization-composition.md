---
id: jazz-reharmonization-composition
title: Jazz Reharmonization and Substitution in Composition
domain: music
course: composition
prerequisites:
- id: jazz-reharmonization-substitution
  type: hard
- id: jazz-harmony-basics
  type: hard
- id: jazz-chord-substitution-voice-leading
  type: soft
- id: lead-sheet-notation
  type: soft
tags:
- jazz
- reharmonization
- substitution
- harmony
stage: advanced
status: validated
---
# Jazz Reharmonization and Substitution in Composition

## Core Idea
Jazz reharmonization replaces simple chord progressions with sophisticated substitutions using tritone substitutes, related ii-V changes, and chromatic passing chords. This technique adds harmonic richness while maintaining melodic integrity, applicable to both jazz and contemporary classical contexts.

## Questions

```yaml
- question: "A composer wants to replace G7 → Cmaj7 with a tritone substitution. Which chord replaces G7, and what is the harmonic reason it works?"
  type: multiple-choice
  options:
    - "F7 — it lies a whole step below the target and creates smooth voice-leading"
    - "Ab7 — it is built on the relative minor of C and shares several chord tones"
    - "Db7 — it shares the tritone interval (notes B and F) with G7, so the harmonic tension is preserved and the bass descends chromatically into C"
    - "E7 — it is the dominant of the parallel minor and creates chromatic color"
  answer: 2
  explanation: "The tritone substitution works because Db7 and G7 share the same tritone: the note B is the major third of G7 and the enharmonic minor seventh (Cb) of Db7; F is the minor seventh of G7 and the major third of Db7. These two notes carry the harmonic tension of the dominant chord. Because they appear in both chords, a melody note functioning over G7 will typically still function over Db7. Additionally, the bass moves Db → C (a half step down), creating smoother chromatic voice-leading than the G → C root movement by fifth."

- question: "A student reharmonizes a 32-bar jazz standard by replacing every dominant chord with a tritone substitute and preceding each with a related ii–V insertion. Why might this approach undermine the musical effect?"
  type: multiple-choice
  options:
    - "Tritone substitutes clash with the melody when used more than twice in a row"
    - "Related ii–V insertions are only valid before ii–V–I progressions, not before individual dominants"
    - "Harmonic saturation exhausts the listener's ear — constant substitution removes the tonal landmarks that give reharmonization its impact when used selectively"
    - "Using tritone substitutes on every chord violates standard voice-leading rules by creating parallel tritones"
  answer: 2
  explanation: "Reharmonization is most effective when used selectively: at a repeated phrase that needs freshening, a cadence that wants delay, or a climactic moment. When every chord is substituted, there are no simple reference points left for the ear to orient against. The sophistication of the substitution is perceived only in contrast to simpler harmonies. Constant substitution also fatigues the ear and can obscure the melodic line. The craft is knowing which moments to leave alone."

- question: "When replacing G7 with its tritone substitute Db7, the tritone interval B–F appears in both chords (as different chord tones), which is why melody notes that work over G7 tend to also work over Db7."
  type: true-false
  answer: true
  explanation: "In G7, B is the major third and F is the minor seventh. In Db7, F is the major third and B (= Cb enharmonically) is the minor seventh — the roles are swapped, but the interval is preserved. Since these two notes carry the harmonic identity and tension of the dominant chord, a melody note that functions as a chord tone or usable tension over G7 will typically function similarly over Db7. This shared tritone content is the entire mechanical basis for why the substitution preserves harmonic integrity."

- question: "Because tritone substitutes preserve melodic integrity through shared chord tones, they can be applied uniformly to every dominant chord in a progression for maximum harmonic sophistication."
  type: true-false
  answer: false
  explanation: "Selective use is the essence of the craft. Reharmonization succeeds when it provides contrast — freshening a repeated phrase, coloring a climax, delaying a cadence — precisely because simpler harmonies elsewhere give the ear reference points. Applying substitutions uniformly removes this contrast effect, creates harmonic saturation, and may obscure the melody. The decision of *where* to substitute is as important as knowing *how* to substitute."

- question: "Explain why tritone substitution preserves the harmonic tension of the original dominant chord, using the structure of the two chords involved."
  type: short-answer
  answer: "A dominant seventh chord's tension comes from its tritone interval — the third and seventh of the chord form an interval of three whole steps (a tritone) that creates strong harmonic instability resolving to the tonic. G7's tritone is B–F. The tritone substitute Db7 contains the same tritone: F is now the third of Db7 and B (Cb) is the seventh. Because both chords share this tritone, they carry the same essential harmonic tension and both resolve convincingly to Cmaj7, just via different bass motion (G→C by fifth vs. Db→C by half step)."
  explanation: "The shared tritone is the entire basis of the substitution. Without it, replacing G7 with an arbitrary dominant would work only by coincidence. Understanding *why* the substitution works (not just *which* chord to use) lets you extend the principle: any time two dominant chords share a tritone, they are interchangeable as tension-bearers, and you can choose based on bass line, voice-leading economy, or melodic fit."
```

## Explainer

Reharmonization is essentially a compositional act of translation: you take a melody — which has its own logic and identity — and find new harmonic support beneath it that is richer, more chromatic, or more surprising than what was originally there. Because you already understand jazz harmony basics and substitution techniques, you can now think about applying those substitutions not just as performance choices but as compositional decisions baked into the score from the start.

The **tritone substitution** is the most powerful single tool in jazz reharmonization. A tritone substitute replaces a dominant chord with another dominant chord whose root is a tritone away. For example, instead of G7 resolving to Cmaj7, you write Db7 resolving to Cmaj7. Why does it work? Because Db7 and G7 share the same tritone — the notes B and F appear in both (as the third and seventh, just swapped). The melody note that worked over G7 typically also works over Db7, because the shared tritone provides harmonic continuity. The result is a chromatic bass line (Db descends by half step to C) that feels smoother and more sophisticated than the diatonic root motion.

**Related ii–V insertions** extend this toolkit. Before any dominant chord, you can insert the ii chord that belongs to the same temporary key area. Instead of just landing on G7, you write Dm7–G7. This creates a two-chord preparation — a local ii–V — that intensifies the pull toward the tonic. You can also combine this with tritone substitution: if you're replacing G7 with Db7, you can precede it with Abm7 (the ii chord relative to Db7). The full substitution chain Dm7–G7 becomes Abm7–Db7, and both versions lead convincingly to Cmaj7, but with very different harmonic textures.

**Chromatic passing chords** fill gaps between diatonic harmonies using chords that share no diatonic function — they exist purely to voice-lead smoothly into the next chord. A common example is inserting a chord whose root is a half step above or below the destination. These chords borrow their logic from voice-leading: every voice moves as smoothly as possible, and the chord happens to be whatever is produced by that smooth motion. The key to maintaining **melodic integrity** throughout all of these substitutions is to check each new chord against the melody note: does the melody note function as a chord tone, a ninth, an eleventh, or a thirteenth of the substitute? A chord that clashes with the melody defeats the purpose. Reharmonization succeeds when the melody sounds freshly supported, not harmonically contradicted.

As a compositional practice, reharmonization is most powerful when used selectively. Replacing every chord creates harmonic saturation that fatigues the listener. The craft is in knowing which moments are ripe for substitution — a repeated phrase that needs freshening on its second appearance, a cadence that wants to be delayed or colored, a climactic moment that deserves richer harmonic support — and which moments should remain simple, giving the ear room to breathe and orient itself.
