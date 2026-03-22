---
id: augmented-sixth-chords
title: Augmented Sixth Chords
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: interval-quality
  type: hard
- id: roman-numeral-analysis
  type: hard
- id: neapolitan-chord
  type: soft
- id: chord-inversions
  type: soft
builds-toward:
- modulation-techniques
tags:
- augmented-sixth
- Italian-sixth
- French-sixth
- German-sixth
- chromatic-harmony
stage: formal-systems
status: validated
---

# Augmented Sixth Chords

## Core Idea
Augmented sixth chords are chromatic pre-dominant harmonies built on the flattened sixth scale degree, characterized by an augmented sixth interval between the bass (b6) and an upper voice (raised 4, enharmonically equivalent to the leading tone of the dominant). This interval expands outward by half step to the octave on scale degree 5, creating a powerful pull toward the dominant. The three standard varieties differ by their inner voices: the Italian (It+6) contains only b6, 1, and #4; the French (Fr+6) adds scale degree 2; and the German (Ger+6) adds b3. The German augmented sixth is enharmonically equivalent to a dominant seventh chord and can be exploited for enharmonic modulation.

## How It's Best Learned
Learn to spell each variety from the bass note up: 'It has 3 notes, Fr adds 2, Ger adds b3.' Play each in C minor to hear the characteristic augmented sixth interval expanding to the octave on G. Find examples in Schubert lieder and Beethoven sonatas, where these chords are especially frequent.

## Common Misconceptions
- Confusing the German augmented sixth with a dominant seventh: they are enharmonically equivalent but have different spellings and functions (the Aug6 resolves to the dominant, not the tonic).
- Thinking the augmented sixth interval is the chord's root interval: it refers specifically to the interval between the bass and a particular upper voice.
- Misidentifying these chords in minor keys where accidentals are already present: look for the characteristic b6–#4 pair.

## Questions

```yaml
- question: "In C minor, you encounter the chord Ab–C–Eb–F#. A student labels it 'Ab7' (an Ab dominant seventh chord). Why is this label wrong, even though the pitches look identical to an Ab dominant seventh?"
  type: multiple-choice
  options:
    - "The student is correct — Ab7 and the German augmented sixth are the same chord and function identically"
    - "The label is wrong because Ab is not a valid chord root in C minor"
    - "The label is wrong because the spelling reveals the function: F# resolves up to G (dominant), while Gb in Ab7 would resolve down to F. Same pitches, different functions and spellings"
    - "The label is wrong because dominant seventh chords cannot appear in minor keys"
  answer: 2
  explanation: "The German augmented sixth (Ab–C–Eb–F# in C minor) is enharmonically identical to Ab7 (Ab–C–Eb–Gb), but the spelling determines the function. F# is the raised fourth scale degree of C, which resolves upward by half step to G (scale degree 5 — the dominant). Ab resolves downward by half step to G. Both voices converge on the dominant — the chord's function is pre-dominant, resolving to V. If respelled as Ab7, the Gb would resolve down to F, targeting Db major. Same notes on the keyboard; completely different harmonic destinations. The spelling is not optional decoration — it declares the chord's intent."

- question: "What distinguishes the French augmented sixth from the Italian augmented sixth?"
  type: multiple-choice
  options:
    - "The French sixth uses the raised fourth in the bass; the Italian sixth puts the flattened sixth in the bass"
    - "The French sixth adds scale degree 2 to the Italian sixth's three notes (b6, 1, #4)"
    - "The French sixth omits scale degree 1 that is present in the Italian sixth"
    - "The French sixth replaces the augmented sixth interval with a minor seventh interval"
  answer: 1
  explanation: "The Italian augmented sixth contains exactly three pitch classes: the flattened sixth (b6), scale degree 1 (tonic), and the raised fourth (#4) — the two notes that form the augmented sixth interval plus the tonic. The French augmented sixth adds scale degree 2 to this collection, giving it four distinct pitch classes and a slightly more dissonant, colorful sound. The German augmented sixth instead adds the flattened third (b3), which produces the chord that is enharmonically equivalent to a dominant seventh. All three share the defining b6–#4 augmented sixth interval in the outer voices."

- question: "Augmented sixth chords are pre-dominant harmonies — they resolve to the dominant (V), not directly to the tonic (I)."
  type: true-false
  answer: true
  explanation: "This is the defining functional characteristic of the entire augmented sixth family. The augmented sixth interval between b6 (bass) and #4 (upper voice) resolves outward by contrary half-step motion: b6 moves down to scale degree 5, and #4 moves up to scale degree 5. Both voices arrive on the same pitch — the dominant scale degree — making the resolution to V both acoustically powerful and harmonically unambiguous. These chords intensify the approach to the dominant, functioning as a chromatic intensification of the pre-dominant function (like an elaborated IV or ii chord)."

- question: "The augmented sixth interval in these chords resolves by both voices moving inward — converging toward the middle — to land on the dominant."
  type: true-false
  answer: false
  explanation: "The resolution is outward, not inward. The bass (b6) moves down by half step to scale degree 5; the upper voice (#4) moves up by half step to scale degree 5. They converge on the same note (the dominant) but from opposite directions — one coming from below, one from above. This outward expansion is acoustically distinctive and is what gives augmented sixth chords their sense of urgent release. Inward resolution would mean the two notes moved toward each other; instead they both expand to land on the same pitch from opposite sides."

- question: "How do composers exploit the enharmonic equivalence between the German augmented sixth and a dominant seventh chord, and why does spelling still matter?"
  type: short-answer
  answer: "Composers reinterpret a German augmented sixth as a dominant seventh (or vice versa) to pivot between distantly related keys. For example, the German augmented sixth in C (Ab–C–Eb–F#) can be respelled as Ab7 (Ab–C–Eb–Gb) and resolved as a dominant seventh to Db major — a key far from C. The listener hears the same sonority but the harmonic destination suddenly shifts. Spelling matters because it signals resolution: F# points up to G (dominant of C), while Gb points down to F (third of Db). The two spellings declare completely different harmonic intentions even though the notes sound identical on a keyboard."
  explanation: "This technique appears frequently in Schubert and Beethoven, where a chord suddenly seems to 'warp' to a new key. The enharmonic pivot works because equal temperament makes F# and Gb acoustically indistinguishable — the ambiguity is real and audible. But in tonal analysis, the spelling is never arbitrary: it is the composer's declaration of where the chord is going. A student who conflates the two spellings will misread the modulation and be confused about the key structure."
```

## Explainer

You understand interval quality from your prerequisite work, so think about what an augmented sixth actually sounds like: it's one semitone wider than a major sixth. An augmented sixth from Ab to F# spans 10 semitones. That stretched interval creates an acute sense of outward tension — the two pitches want to move *away* from each other by half step. This is the defining acoustic property of augmented sixth chords: the Ab resolves *down* to G (scale degree 5), and the F# resolves *up* to G. Both outer voices converge on the same pitch from opposite directions, arriving on an octave. That arrival note — G — is scale degree 5, the dominant. This is why augmented sixth chords are **pre-dominant** harmonies: their resolution is to the dominant, not the tonic.

To spell any augmented sixth chord, start from the bass note, which is always the flattened sixth scale degree (b6). In C major or C minor, that's Ab. The characteristic upper voice is the raised fourth scale degree (#4), which in C is F#. These two notes form the augmented sixth interval (Ab–F#) that gives the chord family its name. The three standard varieties differ by what fills the middle: the **Italian augmented sixth** (It+6) contains only those two notes plus scale degree 1 — the thinnest, most austere version. The **French augmented sixth** (Fr+6) adds scale degree 2, giving it a slightly more dissonant, colorful sound. The **German augmented sixth** (Ger+6) adds the flattened third (b3), producing a chord that, if you respell the F# as Gb, is enharmonically identical to a dominant seventh chord.

That enharmonic equivalence — Ger+6 in C = Ab7 spelled enharmonically — is both a notational trap and a compositional opportunity. As a trap: the chords look the same on paper but function completely differently. Ab7 (as a dominant seventh) resolves to Db major (its tonic). The German augmented sixth in C resolves to G (the dominant of C). The spelling tells you the function. As an opportunity: composers exploit this enharmonic equivalence to pivot between keys. A Ger+6 in one key is reinterpreted as a dominant seventh chord in another key, enabling smooth modulation. This technique appears in Schubert and Beethoven, where a chord suddenly shifts its tonal function under the enharmonic reinterpretation.

In Roman numeral analysis, you've learned to label chords by their scale degree. Augmented sixth chords don't fit cleanly into this system — they're best labeled by variety (It+6, Fr+6, Ger+6) and understood functionally as pre-dominant chromaticisms. When analyzing, look for the b6 in the bass and the #4 in an upper voice. In minor keys, b6 is already in the key signature; in major keys, it requires a flat accidental. The #4 always requires an accidental, since it's raised above the diatonic scale. Those two accidentals together — one flatted bass note, one sharped upper voice — are your signal to label what follows as an augmented sixth chord.
