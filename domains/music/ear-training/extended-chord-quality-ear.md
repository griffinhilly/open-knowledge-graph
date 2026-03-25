---
id: extended-chord-quality-ear
title: Extended Chord Quality Recognition by Ear
domain: music
course: ear-training
prerequisites:
- id: seventh-chord-ear-training
  type: hard
- id: chord-quality-by-ear
  type: hard
- id: extended-chord-ear-training
  type: soft
builds-toward:
- borrowed-chord-recognition-ear
tags:
- extended-harmony
- chord-quality
- jazz
stage: formal-systems
status: validated
---
# Extended Chord Quality Recognition by Ear

## Core Idea
Extended harmonies (9ths, 11ths, 13ths) add color and sophistication beyond simple triadic and seventh-chord harmony. Upper extensions alter the sonic character in specific ways: major 9ths add brightness, minor 9ths add darkness, 11ths add openness or pungency, and 13ths add warmth. Recognizing these coloristic variants by ear is essential for jazz and contemporary harmonic analysis.

## Questions

```yaml
- question: "A student hears a chord and correctly identifies it contains a seventh. She now wants to determine whether it is a ninth chord. What should she listen for next?"
  type: multiple-choice
  options:
    - "Whether the root and fifth form a perfect fifth or tritone, which determines if an extension is present"
    - "The quality of the tone floating above the seventh — whether it adds brightness (major 9th) or a biting edge (minor ♭9)"
    - "Whether the chord resolves to a tonic, since extensions only appear in dominant chords"
    - "The bass note, since ninth chords always have the ninth in the lowest voice"
  answer: 1
  explanation: "The key strategy for hearing extensions is 'hear the seventh first, then listen for what floats above it.' Once you've identified the seventh, the ninth is the next note up — and its quality has a characteristic sound: a major 9th adds brightness and warmth; a minor ♭9 adds a biting, dissonant edge. This quality-relative-to-seventh approach is more reliable than trying to identify extensions from the root up."

- question: "Why does the sharp eleven (♯11) appear so frequently in jazz major-seventh chords rather than the natural eleventh?"
  type: multiple-choice
  options:
    - "The sharp eleven creates a stronger perfect-fifth consonance with the root than the natural eleventh"
    - "The natural eleventh clashes with the major third, creating a minor-second dissonance; the sharp eleven avoids this conflict and creates the characteristic Lydian brightness"
    - "The sharp eleven is easier to voice on piano because it avoids the middle register"
    - "Jazz convention inherited the sharp eleven from bebop comping where it was used to avoid bass-note doubling"
  answer: 1
  explanation: "The natural eleventh (perfect fourth above the root) is only a minor second away from the major third of the chord, creating a harsh dissonance. The ♯11 (augmented fourth/tritone above root) skips that clash and creates the Lydian sound — floating, bright, suspended. This is why the Lydian mode became so important in jazz and film music: the ♯11 over a major seventh chord is one of the most characteristic colors in the idiom."

- question: "A dominant ninth chord (C9) sounds brighter and more dreamy than a dominant seventh with a minor ninth (C7♭9) because the major ninth above always adds warmth and brightness."
  type: true-false
  answer: false
  explanation: "The sound of an extension depends heavily on what seventh it floats above. The C9 (minor seventh + major ninth) sounds 'rich and open' with drive and tension from the minor seventh — not simply dreamy. The C7♭9 (minor seventh + minor ninth) sounds biting and dissonant. It is the Cmaj9 (major seventh + major ninth) that has the bright, dreamy character. Always identify the seventh first — the same ninth sounds completely different over a minor versus major seventh."

- question: "Recognizing extended chords by ear requires identifying each chord tone individually from the lowest note to the highest before naming the chord type."
  type: true-false
  answer: false
  explanation: "The Explainer explicitly recommends the opposite approach: start from the seventh (already recognizable) and listen for what floats above, rather than building up interval by interval from the root. Jazz voicings often omit chord tones entirely, so individual-tone identification is unreliable. The goal is to recognize a characteristic quality — the brightness of a major ninth, the biting edge of a ♭9, the warm saturation of a thirteenth — and associate it immediately with the structure that produces it."

- question: "How does the quality of the seventh affect the perception of extensions above it? Use the contrast between Cmaj9 and C9 (dominant ninth) as your example."
  type: short-answer
  answer: "The seventh sets the harmonic context that colors everything above it. In Cmaj9, the major seventh creates a bright, stable, floating quality — the major ninth adds warmth and expansion to an already bright sound. In C9 (dominant ninth), the minor seventh introduces tension and drive; the same major ninth now floats above that tension, creating a rich but harmonically unstable sound that wants to resolve. Same ninth, completely different effect because the seventh differs."
  explanation: "You don't hear extensions in isolation — you hear them in context of the chord's foundational quality. Training the ear to hear extensions means training it to hear the seventh first, establishing a harmonic baseline, then registering the added color above. This layered listening approach is more reliable than trying to identify every interval from scratch."
```

## Explainer

You can already identify chord quality — major, minor, diminished, augmented — and you can recognize seventh chords by ear. Extended harmonies build directly on that foundation. A **ninth chord** is simply a seventh chord with one more third stacked on top; an **eleventh chord** adds another; a **thirteenth chord** adds yet another. In practice, not all tones are sounded simultaneously — a jazz pianist voicing a Cmaj13 will likely omit the fifth and sometimes the eleventh. What you're hearing is a characteristic cluster of intervals that colors the sound, not a complete stacking of thirds.

The key to recognizing extensions by ear is learning to hear the **quality of the upper extensions relative to the root**. A dominant ninth chord (V9) has a major seventh and a major ninth; it sounds rich and open, like a dominant seventh with added warmth. A minor ninth (♭9) above a dominant seventh creates a much more dissonant, biting sound — you'll hear it in tense jazz passages and film noir scores. The difference between a Cmaj9 and a C9 (dominant ninth) is the quality of the seventh: the major seventh on top of the major triad creates a bright, dreamy sound; the minor seventh on the same root creates drive and tension. Hear the seventh first, then listen for what floats above it.

**The eleventh** is trickier because the natural eleventh (perfect fourth above the root) clashes with the major third, creating a minor-second dissonance. This is why the **sharp eleven** (♯11, or augmented fourth) appears so often in jazz: the Lydian sound of a raised eleventh over a major seventh chord is one of the most distinctive colors in the idiom — bright, floating, suspended. The **thirteenth** is a major sixth above the root, and its effect is warmth and completion. A dominant thirteenth chord (V13) sounds fully saturated, rich, and final — it's the chord that sounds like everything has arrived at once.

Train your ear by isolating the extensions from familiar roots. Take a Cmaj7 you know well — that distinctive ring of the major seventh — and then add the ninth: hear how the sound expands upward. Then try a dominant 9th (C9): the minor seventh contracts the sound slightly and adds tension. Compare the two nines (major vs. minor) over their respective sevenths until the contrast is automatic. Then do the same process for thirteenths versus ninths. The goal is not to name the chord from scratch but to hear a quality you recognize — that particular brightness, that biting edge, that warm saturation — and associate it immediately with the structure that produces it.
