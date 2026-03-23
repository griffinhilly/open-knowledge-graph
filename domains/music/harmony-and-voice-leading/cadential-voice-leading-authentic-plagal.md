---
id: cadential-voice-leading-authentic-plagal
title: Voice Leading in Authentic and Plagal Cadences
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: cadence-types-and-function
  type: hard
- id: voice-leading-smooth-stepwise-motion
  type: hard
- id: harmonic-function-voice-leading-tension-resolution
  type: hard
builds-toward:
- cadential-six-four-harmonic-function
- tonicization-and-modulation-voice-leading
tags:
- cadence
- authentic
- plagal
- voice-leading
- phrase-ending
stage: formal-systems
status: validated
---

# Voice Leading in Authentic and Plagal Cadences

## Core Idea
Cadential voice leading is the culmination of a phrase's harmonic and linear motion, where voice-leading patterns create a sense of closure. In authentic cadences (V-I), the leading tone must resolve upward to the tonic, and the bass typically moves down a fifth. Plagal cadences (IV-I) create a different voice-leading effect with smooth motion that provides a softer sense of resolution.

## Questions

```yaml
- question: "In a perfect authentic cadence in C major (V→I), the leading tone B appears in the alto voice. What must happen to this B?"
  type: multiple-choice
  options:
    - "B moves down to G to create smooth voice leading and avoid doubling issues"
    - "B moves up to C, even if this means the tonic chord ends with a doubled third"
    - "B sustains as a common tone, since B is present in both the V and the following chord"
    - "B moves down to E to provide the third of the tonic triad"
  answer: 1
  explanation: "The leading tone's upward resolution to tonic is obligatory in an authentic cadence — it is the defining voice-leading event of the V-I motion. B is not a common tone (it does not appear in C major's I chord), so sustaining it is impossible. Moving down to G or E abandons the semitone pull that gives the authentic cadence its sense of closure. If the mandatory B→C resolution means the tonic chord ends with a doubled third (E) rather than a doubled root, that doubling is accepted as a necessary consequence."

- question: "Which quality most fundamentally distinguishes a plagal cadence from a perfect authentic cadence?"
  type: multiple-choice
  options:
    - "The plagal cadence uses a minor iv chord, giving it a darker, more ambiguous sound"
    - "The plagal cadence lacks the leading tone, so there is no semitone pull creating urgency — resolution feels gentle and settled"
    - "The plagal cadence resolves to the dominant rather than returning to the tonic"
    - "The plagal cadence occurs only at the beginning of phrases as a point of departure"
  answer: 1
  explanation: "The core difference is the leading tone. In V-I, the seventh scale degree (a half step below tonic) creates intense upward pressure that resolves with urgency. IV contains no leading tone: the motion from IV to I involves whole-step and common-tone motion with no semitone pull. This is why plagal cadences sound settled and hymnal rather than conclusive and directed. Option A is incorrect because the plagal cadence can use major IV as well."

- question: "In an authentic cadence, if the leading tone appears in an inner voice rather than the soprano, its upward resolution to tonic can be omitted to create a smoother voice leading."
  type: true-false
  answer: false
  explanation: "The leading tone's upward resolution is obligatory regardless of which voice carries it. There is no exception based on register or voice placement. Even if resolving B up to C in the alto creates an awkward leap elsewhere or results in a doubled third in the tonic chord, the resolution must still occur. The leading tone's role in creating cadential closure is so fundamental that departing from it weakens the cadence significantly."

- question: "Plagal cadences often appear after an authentic cadence because they provide a final, gentle layer of closure to a phrase that has already formally ended."
  type: true-false
  answer: true
  explanation: "Because the plagal cadence does not have the driving urgency of V-I, it rarely functions as the primary cadential arrival by itself. Instead, it commonly follows a perfect authentic cadence as a kind of 'amen' — adding a soft, harmonically stable confirmation of tonic after the formal close has already been achieved. This usage is especially common in hymns and choral music, where the plagal 'amen' became a convention precisely because of its settled, non-urgent character."

- question: "Why does the leading tone resolution feel nearly inevitable in an authentic cadence, and what happens to this sense of urgency in a plagal cadence?"
  type: short-answer
  answer: "The leading tone is a semitone below the tonic, creating intense acoustic and psychological tension. The half-step interval has the smallest possible distance to resolve, making the upward pull feel almost mechanical. In a plagal cadence (IV→I), the chord contains no leading tone — the fourth scale degree moves down by whole step to the third of the tonic, and other voices move smoothly or hold common tones. Without the semitone pull, there is no urgency, no sense of arrival forced by acoustic pressure. The resolution is harmonically stable but not tonally directed."
  explanation: "This voice-leading difference explains the emotional contrast: authentic cadences arrive with a sense of finality and release of tension (the leading tone 'snaps' into place), while plagal cadences settle without drama. Composers exploit this contrast intentionally — using authentic cadences for structural arrivals and plagal cadences for gentle, lyrical closes or post-cadential extensions."
```

## Explainer

Cadences are the punctuation of tonal music: they mark phrase endings, create moments of closure or suspension, and define the listener's sense of arrival. From your study of cadence types, you know the difference between authentic (V-I), plagal (IV-I), half (ending on V), and deceptive (V-vi) cadences. Cadential voice leading asks a more specific question: given a particular harmonic motion at a phrase ending, exactly how does each individual voice move? The answer reveals why certain cadences feel closed and final while others feel gentle or ambiguous — the closure is not just harmonic but linear.

In the **authentic cadence**, the governing voice-leading event is the resolution of the **leading tone** — the seventh scale degree — upward by semitone to the tonic. In a G major V chord in C major (G-B-D), the B is the leading tone; when this chord resolves to I, that B must rise to C. This is not merely convention — it reflects the acoustic and psychological pull of the semitone below the tonic. The leading tone is harmonically destabilized by its proximity to the tonic; the semitone resolution is almost mechanical in its inevitability. Any voice carrying the leading tone at the cadential moment must complete this upward resolution. If the leading tone is in an inner voice rather than the soprano, it still resolves upward, even if this means the tonic chord ends with a doubled third — this doubling is acceptable precisely because the leading tone's resolution is obligatory.

The bass motion in a perfect authentic cadence is a **descending fifth** (or ascending fourth) from the dominant to the tonic root. This bass motion combined with the leading tone resolution in an upper voice creates what is called the **double resolution**: the tonic is approached from below in the bass and from the semitone above in an inner or upper voice simultaneously. When the tonic also appears in the soprano at the point of arrival, the sense of closure is maximized — this is the **perfect authentic cadence**, the strongest phrase-ending in tonal music. Remove any one of these conditions (put a different note in the soprano, or use an imperfect bass approach) and the cadence weakens measurably.

The **plagal cadence** (IV-I) creates a fundamentally different character because IV does not contain the leading tone. The fourth scale degree (F in C major) moves down by step to the third of the tonic (E), and the sixth scale degree (A) typically moves either down to G or sustains as a common tone. There is no semitone pull, no urgency — instead, plagal resolution has a settled, hymnal quality. The motion from IV to I is harmonically stable rather than tonally directed, which is why plagal cadences so often appear *after* an authentic cadence, adding a final "amen" to a phrase that has already formally closed. Understanding both cadence types as voice-leading events — not just chord labels — lets you hear the specific linear motions that create each kind of closure and control them deliberately in your own writing.
