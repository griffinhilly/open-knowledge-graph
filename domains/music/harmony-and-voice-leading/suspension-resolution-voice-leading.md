---
id: suspension-resolution-voice-leading
title: Suspension and Non-Harmonic Tone Resolution in Voice Leading
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: suspension-preparation-and-resolution
  type: hard
- id: non-harmonic-tone-usage
  type: soft
builds-toward:
- voice-leading-error-recognition-and-correction
tags:
- suspension
- non-harmonic-tones
- voice-leading
- dissonance
stage: formal-systems
status: validated
---

# Suspension and Non-Harmonic Tone Resolution in Voice Leading

## Core Idea
Suspensions and non-harmonic tones create dissonance and require smooth resolution as part of overall voice leading. A suspension must be prepared (held from previous harmony), sustained (creating dissonance), and resolved (usually downward by step). Other non-harmonic tones like passing tones and neighbor tones must fit smoothly into the voice leading without creating awkward jumps. Treating non-harmonic tones as integral to voice leading rather than as ornaments ensures that the entire texture remains coherent.

## Questions

```yaml
- question: "A student writes a 7–6 suspension but the 7th above the bass appears without having been present in the preceding chord — it simply appears as a dissonance and then resolves down by step. Why does this not function as a proper suspension?"
  type: multiple-choice
  options:
    - "It is a proper suspension — any dissonance that resolves down by step qualifies"
    - "The preparation is missing: a suspension's dissonance is earned by the note having been consonant in the previous chord, which is what makes it expressive rather than simply wrong"
    - "The resolution should have been upward, not downward"
    - "7–6 suspensions require the 7th to be in the soprano voice"
  answer: 1
  explanation: "Preparation is what distinguishes a suspension from arbitrary dissonance. When the suspended note was already consonant in the preceding harmony, the listener hears the 'collision' as purposeful — the note belongs to the previous chord and is being delayed. Without preparation, the dissonant pitch appears with no prior grounding, making it sound like an error that happens to resolve rather than an intentional, structurally meaningful delay. The three-stage formula (prepare, suspend, resolve) is not bureaucratic — the preparation is the source of the suspension's expressive power."

- question: "In standard tonal voice leading, a suspended note must resolve downward by step. What is the perceptual logic behind this direction?"
  type: multiple-choice
  options:
    - "Downward melodic motion is physically easier for singers and instrumentalists"
    - "The suspended pitch is heard as a vestige of the previous chord — it is 'too high' for the new harmony and corrects itself by descending to the expected chord tone"
    - "Upward resolution always creates parallel fifths with the bass voice"
    - "The rule is purely conventional with no acoustic or perceptual basis"
  answer: 1
  explanation: "The suspension is heard as a pitch that the voice should have moved to the new chord tone but got 'stuck' at the previous note. Because the new harmony requires a note one step below, the suspended pitch is perceived as sitting above its correct destination. The downward step is not arbitrary — it is the direction that connects the delayed voice to where it should have gone from the beginning. The resolution corrects the delay by descending to the chord tone that 'should' have been there, releasing the accumulated tension."

- question: "A suspension is defined by its held-over consonant pitch from the previous chord, which becomes dissonant when the harmony changes beneath it."
  type: true-false
  answer: true
  explanation: "This is the defining structural feature of a suspension. The note itself does not change — it was consonant in the previous chord and the bass and other voices move, turning it into a dissonance. This is precisely the three-stage sequence: preparation (consonant in previous chord), suspension (now dissonant against the new chord), resolution (step down to the expected chord tone). The dissonance arises from the stability of the prior context being carried forward — which is what makes it coherent rather than arbitrary."

- question: "A suspension may resolve either upward or downward by step, depending on which direction produces smoother voice leading in context."
  type: true-false
  answer: false
  explanation: "Standard tonal practice requires downward resolution. Upward resolution is a rare exception reserved mainly for the leading tone (when suspended above the octave and resolving upward to the tonic), where the upward pull is exceptionally strong. Treating upward and downward resolution as equally available misunderstands the perceptual logic: the suspended pitch is heard as 'too high' for the new harmony — it corrects by descending, not by continuing to ascend. Allowing free-direction resolution treats the suspension as just any passing dissonance, losing its specific structural meaning."

- question: "What makes a suspension different from simply playing a dissonant note that happens to resolve stepwise, and why does this distinction matter for voice-leading analysis?"
  type: short-answer
  answer: "A suspension is prepared — the 'dissonant' note was consonant in the immediately preceding chord and is held over into the new harmony. This means the dissonance is not arbitrary: the listener has already heard the note in a stable context and understands it as a delayed voice rather than an error. A dissonant note with no preparation has no such grounding — it appears unexpectedly, making its stepwise resolution seem incidental rather than structural."
  explanation: "In analyzing Bach chorales, the preparation criterion is the analytical key that distinguishes suspensions from other non-chord tone types. If the note appeared in the previous chord as a chord tone, it is a suspension; if it appeared between chord tones without such preparation, it might be a passing tone, neighbor tone, or other non-harmonic tone type — each with different voice-leading implications. The preparation is what makes the suspension a planned, structurally meaningful event rather than a colorful accident."
```

## Explainer

A suspension is one of the most carefully managed events in tonal voice leading: it takes a consonant note from the previous chord, holds it into the new chord where it becomes momentarily dissonant, and then resolves by step to a consonant tone of the new chord. The three-stage label captures the mechanics precisely — **preparation**, **suspension**, **resolution** — and each stage has a strict requirement. The preparation stage means the suspension pitch must appear as a consonant chord tone in the preceding harmony, so the listener has already heard it in its stable context. When it is then retained while the bass and other voices move, it creates a dissonance that is coherent rather than arbitrary — the listener recognizes it as "belonging" to what just happened, now in conflict with what is happening now.

The preparation is what makes suspensions feel expressive rather than simply wrong. The dissonance is *earned* by the consonance that preceded it: you introduced the note in a stable context, then kept it just long enough for the harmony to move underneath it, creating a collision. The **4-3 suspension** names the intervals against the bass: the suspended note is a fourth above the bass, which was the third of the previous chord in many standard progressions; it resolves down to the third, which is the consonant chord tone that "should" have been there from the start. The **7-6 suspension** works the same way: the seventh above the bass hangs over, then resolves down to the sixth. In each case, the resolution corrects the dissonance by moving down by step to where the voice "should" have gone from the beginning.

The resolution must move **downward by step** in standard practice. This reflects perceptual logic: the suspended pitch is heard as too high relative to the new harmony (it still belongs to the previous chord), and the resolution corrects this by descending to the expected chord tone. Upward resolution is rare and marked — it typically occurs only when the suspended pitch is the leading tone resolving to the octave, where the upward pull is even stronger than the downward resolution tendency. When composers delay the suspension's resolution (either extending the dissonance or adding ornamental figuration before the step-down), they intensify the listener's expectation and the eventual relief when the resolution arrives. The expressive power of suspension lies precisely in this withheld resolution.

Non-harmonic tones more broadly — **passing tones** (filling a stepwise gap between two chord tones), **neighbor tones** (a step away and back), **anticipations** (a chord tone arrived at early) — work on the same underlying principle: they are pitches that sit outside the current chord but are justified by their linear context. The key insight for voice-leading is to think of each vocal line as having two layers simultaneously: the **harmonic skeleton** (the chord tones that define the harmony at each moment) and the **melodic surface** (which includes non-harmonic tones moving between those chord tones). Analysis strips away the melodic surface to reveal the harmonic skeleton; composition adds the melodic surface back in, using non-harmonic tones to create smooth, logical motion between the structural chord tones. A Bach chorale, analyzed this way, reveals that almost every non-chord tone has a clear functional role — none are decorative in the casual sense, all are integral to the voice-leading logic of the texture.

## How It's Best Learned
Identify all suspensions and non-harmonic tones in a Bach chorale, noting how they are prepared and resolved. Then compose progressions featuring 4-3 and 7-6 suspensions, ensuring the resolution moves smoothly to the next chord tone.
