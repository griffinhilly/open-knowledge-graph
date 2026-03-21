---
id: minor-harmony-voice-leading-choices
title: Minor Tonality and Voice-Leading Choices
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: harmonic-minor-scale
  type: hard
- id: melodic-minor-scale
  type: hard
- id: voice-leading-basics
  type: hard
builds-toward:
- diatonic-progression-voice-leading-patterns
- voice-leading-in-composition
tags:
- minor-tonality
- harmonic-minor
- voice-leading
stage: formal-systems
status: draft
---

# Minor Tonality and Voice-Leading Choices

## Core Idea
Minor keys present voice-leading choices between harmonic minor (which provides the major V chord via raised 7) and melodic minor (which raises both 6 and 7 in ascending passages). These choices affect voice-leading fluency and harmonic color.

## Questions

```yaml
- question: "In a four-part harmonization in A minor, you are writing the V chord. The soprano holds the third of the chord. Which note must the soprano sing?"
  type: multiple-choice
  options:
    - "G♮ — natural minor uses an unraised seventh throughout"
    - "F♯ — the melodic minor raises scale degree 6, which is needed here"
    - "G♯ — the third of E major (the V chord) requires the raised leading tone"
    - "Either G♮ or G♯ is acceptable depending on the desired color"
  answer: 2
  explanation: "The dominant chord in minor must be a major triad (E major in A minor) to function properly — this requires the raised seventh, G♯. Without it, the V chord becomes E minor, which lacks the leading-tone half-step pull toward the tonic A. This is not a stylistic option; it is a structural requirement. A V chord with a minor third (G♮) loses its cadential force dramatically. Scale degree 7 must be raised whenever it forms part of a dominant harmony or ascends to the tonic by half-step."

- question: "In A minor, a soprano voice is moving stepwise upward from E through F, G, to A (scale degrees 5–6–7–8). Which notes should be used for scale degrees 6 and 7?"
  type: multiple-choice
  options:
    - "F♮ and G♮ (natural minor — both unraised)"
    - "F♯ and G♯ (melodic minor ascending — both raised)"
    - "F♮ and G♯ (harmonic minor — only 7 raised)"
    - "F♯ and G♮ (only 6 raised, no special reason)"
  answer: 1
  explanation: "When a voice ascends stepwise through scale degrees 6–7–8, melodic minor is used: both 6 and 7 are raised. The reason is the augmented second — harmonic minor (F♮–G♯) creates an awkward F♮ to G♯ leap of an augmented second (three semitones), which is difficult to sing and sounds angular. Raising both to F♯–G♯ creates a smooth, all-whole-step-or-half-step ascent. Descending, the alterations are dropped (natural minor), giving the line a darker, flatter character."

- question: "In minor-key four-part harmony, different voices may simultaneously use different forms of the minor scale depending on their function in the current chord."
  type: true-false
  answer: true
  explanation: "This is one of the defining features of minor tonality in tonal harmony. The bass may use natural minor (natural 6 and 7) while the soprano simultaneously uses the raised 7 for a leading tone. A tenor forming the third of a V chord must have G♯ in A minor, while the alto on a passing tone may use F♮. The scale selection is voice-by-voice and moment-by-moment, driven by each voice's melodic direction and harmonic function — not by a single consistent scale choice for the whole texture."

- question: "In minor-key voice leading, when a voice descends through scale degrees 8–7–6–5, it should use the raised 7th and 6th (melodic minor descending)."
  type: true-false
  answer: false
  explanation: "The asymmetry is the key point: melodic minor uses raised 6 and 7 only when ascending (to avoid the augmented second in the upward approach to the tonic). When descending through the same territory, the natural minor is used — unraised 6 and 7. The descending line in A minor would use G♮ and F♮. This gives the descending line a characteristic darker, flatter sound that suits falling motion. Using raised alterations descending is not wrong in all styles, but it is not the standard tonal pattern."

- question: "Why is the raised 7th (leading tone) structurally necessary in the dominant chord in a minor key, rather than merely a stylistic choice?"
  type: short-answer
  answer: "The dominant chord's function in tonal harmony is to create strong pull toward the tonic — this pull depends critically on the leading tone, the raised 7th, which is only a half-step below the tonic. In A minor, G♯ is a half-step below A; G♮ is a whole-step below A. A whole-step creates weak pull; a half-step creates the strong voice-leading tension that drives harmonic motion. Without the raised 7th, the V chord becomes a minor triad (E minor instead of E major), losing its leading-tone function entirely. The V–I cadential motion requires this half-step resolution, so the raised 7th is not optional coloring — it is the mechanism that makes dominant harmony function."
  explanation: "This is the structural reason the harmonic minor scale exists at all: the natural minor scale lacks a leading tone, which weakens cadences. The harmonic minor was developed precisely to fix this by providing a raised 7th. Understanding this explains why the scale is called 'harmonic' minor — it was created to serve harmonic (functional) needs, not melodic ones. Melodic minor then fixes the awkward augmented second that the raised 7th creates when moving stepwise."
```

## Explainer

From your prerequisite study of the harmonic and melodic minor scales, you know that minor keys are not a single fixed scale but a flexible tonal resource that exists in several forms. The harmonic minor raises scale degree 7 to create a leading tone; the melodic minor additionally raises scale degree 6 when ascending to avoid the awkward augmented second between 6 and the raised 7; and the natural minor uses neither alteration. In four-part harmony, each voice may need a different form of the scale at any given moment, and choosing which form to use is one of the defining practical challenges of minor-key writing.

The central principle is **function-driven scale selection**. The raised seventh (the leading tone) is required whenever the dominant chord must function as a major triad — without it, the V chord becomes a minor triad lacking the leading tone's half-step pull to the tonic, and the cadential force is drastically weakened. In any voice that forms the third of a V chord, or that moves upward by half-step to the tonic, harmonic minor is required. This is not optional coloring; it is a structural necessity. In A minor, the note G♯ must appear in the tenor or soprano when spelling the E major (V) chord, regardless of what form the scale "normally" uses.

The choice between natural and melodic minor becomes more nuanced in upper voices. When an upper voice ascends stepwise through scale degrees 6 and 7 toward the tonic (la-ti-do), the melodic minor is preferred — raising both 6 and 7 avoids the **augmented second** (the interval F–G♯ in A minor) that creates an angular, difficult-to-sing leap. When a voice descends through that same territory, both alterations are dropped: descending, the natural minor's lower sixth and seventh give the line a flatter, darker character. This asymmetry — ascending melodic minor, descending natural minor — is one of the defining patterns of tonal minor voice leading.

A useful mental model: before writing any note in a minor-key passage, ask two questions about that voice. First, does it need the leading tone (raised 7) because it is ascending to the tonic by half-step, or because it forms the third of a dominant chord? If yes, raise it. Second, is it ascending stepwise through scale degrees 5–6–7–8? If yes, use melodic minor (raise both 6 and 7) to avoid the augmented second. These two questions cover the vast majority of minor-key decisions. The remaining cases — leaping motion, non-dominant harmonies, deliberately modal passages — can be handled by ear once the default rules are internalized. The underlying goal is always voice-leading fluency: each voice should move smoothly, with no awkward intervals, while supporting the harmonic function of each chord.
