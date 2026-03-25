---
id: secondary-dominant-voice-leading
title: Secondary Dominant Voice Leading
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: secondary-dominants
  type: hard
- id: voice-leading-principles
  type: hard
- id: dominant-seventh-function-resolution
  type: soft
- id: chromatic-approach-notes-voice-leading
  type: soft
- id: chromatic-approach-voice-leading
  type: soft
- id: voice-leading-error-recognition-and-correction
  type: soft
- id: cadential-six-four-harmonic-function
  type: soft
- id: augmented-sixth-chord-voice-leading-patterns
  type: soft
builds-toward:
- applied-chord-tonicization-process
tags:
- secondary-dominant
- voice-leading
- chromatic
stage: formal-systems
status: validated
---
# Secondary Dominant Voice Leading

## Core Idea
Secondary dominants require careful voice leading to manage the tritone between chord tones. The tritone (typically between 3 and 7 of the secondary dominant chord) must resolve by semitone—the leading tone up, the scale degree down. Proper voice leading makes secondary dominants sound smooth and motivated rather than abrupt.

## Questions

```yaml
- question: "A student writes V7/V in C major (D7: D-F#-A-C) with F# in the soprano and C in the tenor, resolving to G major. The soprano moves F#→G and the tenor moves C→B. What have they done correctly, and what potential problem remains?"
  type: multiple-choice
  options:
    - "Both constrained voices are resolved correctly; the remaining voices have no further obligations"
    - "Both tritone voices are resolved correctly (F# up by semitone, C down by step), but the remaining voices must use contrary or oblique motion to avoid awkward parallel chromatic movement"
    - "The soprano's F# should have moved to F natural to soften the strong leading-tone emphasis"
    - "The tenor's C should have resolved upward to D, since sevenths are free to move in either direction"
  answer: 1
  explanation: "F# is the leading tone of G, correctly resolving up by semitone. C is the seventh of D7, correctly resolving down to B. Both constrained voices are handled right. The remaining concern is the other two voices: if they also move by chromatic semitones in the same direction, the resulting parallel motion 'calls too much attention to itself.' Contrary or oblique motion in the unconstrained voices distributes the voice-leading interest and keeps the texture smooth. Option D is wrong: the seventh of any V7 chord must resolve downward by step — this is non-negotiable in standard tonal voice leading."

- question: "In SATB writing, why is it recommended to plan the resolution chord BEFORE deciding on the voicing of the secondary dominant?"
  type: multiple-choice
  options:
    - "Because the resolution chord determines which scale degree is being tonicized"
    - "Because the constrained voices (leading tone up, seventh down) largely determine the resolution chord's spacing, so choosing the secondary dominant's voicing first may force awkward doublings or parallels"
    - "Because secondary dominants are always voiced in root position, which limits subsequent options"
    - "Because the resolution chord must be in second inversion to prepare a cadential 6/4"
  answer: 1
  explanation: "The leading tone and seventh are both obligated: the leading tone resolves up by semitone, the seventh resolves down by step. These two movements predetermine where two of the four voices land in the resolution chord. If you voice the secondary dominant without looking ahead, you may create a situation where the two obligated voices, following their resolutions correctly, force the remaining voices into parallel octaves or poor doublings. The professional approach is to decide the resolution voicing first, then work backward to find a secondary dominant voicing that leads cleanly into it."

- question: "In a secondary dominant seventh chord, the 'chromatic voice' — the altered pitch that doesn't belong to the home key — is the seventh of the chord."
  type: true-false
  answer: false
  explanation: "The chromatic voice is the leading tone of the tonicized chord, which is the *third* of the secondary dominant chord, not the seventh. In V7/V in C major (D7), the chromatic tone is F# (absent from C major's diatonic collection), and F# is the third of D7. It functions as the leading tone of G and resolves up by semitone to G. The seventh (C in D7) is actually diatonic to C major — it's the seventh that resolves downward, but it's not the chromatic pitch."

- question: "The resolution of a secondary dominant seventh chord is largely predictable because two of its four voices — the leading tone and the seventh — must resolve by specific intervals in specific directions."
  type: true-false
  answer: true
  explanation: "This is the central practical principle. The leading tone (the third of the secondary dominant) resolves up by semitone to the root of the tonicized chord. The seventh resolves down by step. Both constraints are non-negotiable in standard tonal voice leading. Because two of the four voices are predetermined, the resolution chord's voicing is largely determined before you write it — you have discretion only in how the remaining two voices move, and even those should aim for smooth contrary or oblique motion."

- question: "Why does the secondary dominant contain a tritone, and what role does that tritone play in driving the voice leading?"
  type: short-answer
  answer: "Every dominant seventh chord contains a tritone between its third (the leading tone) and its seventh. The secondary dominant replicates this structure with respect to the tonicized chord rather than the home tonic. The tritone is acoustically unstable and demands resolution by contrary semitone motion: the lower pitch of the tritone resolves up, the upper resolves down (or by inversion). This motion is the 'forward drive' of dominant function — it's what makes the resolution to the target chord feel smooth and purposeful."
  explanation: "Understanding the tritone as the engine makes voice-leading decisions logical rather than rule-following. Once you identify the tritone in the secondary dominant, you know which two voices are constrained, and resolving them 'correctly' is simply obeying the acoustic pull already built into the chord's structure. This is also why a secondary dominant without the seventh (just a major triad) has weaker directional force: no tritone means no obligated contrary-semitone resolution, and the forward pull is reduced."
```

## Explainer

You already know what a secondary dominant is: a chord borrowed from the dominant-function relationship and applied to a non-tonic scale degree. V/V in C major is a D major chord — not diatonic to C major, but functioning as the dominant of G. The chromatic note in V/V (F# instead of F natural) is what gives it its forward drive toward V. Voice leading is how you harness that drive and direct it cleanly.

Every dominant seventh chord contains a **tritone** — the interval of an augmented fourth or diminished fifth — between scale degrees 4 and 7 of the chord. In the home V7, this is the tension that defines the dominant function and demands resolution. In a secondary dominant seventh, the same structure applies but the scale degrees involved are temporary — they belong to the tonicized chord, not the home key. When you use V7/V in C major (A7 chord), the tritone is between C# and G. These notes must resolve: the C# (functioning as the leading tone of D) resolves up to D, and the G (functioning as the seventh) resolves down to F#. Understanding this means you can predict where each voice needs to go before you even write the resolution chord.

The **chromatic voice** — the altered pitch that makes the secondary dominant chromatic — is the leading tone of the tonicized chord. Voice leading principle demands it moves upward by semitone to the root of the tonicized chord. In SATB writing, if this chromatic tone appears in the soprano, the resolution sounds particularly clear and purposeful. If it's buried in an inner voice, the effect is gentler. What you want to avoid is **chromatic voice leading in parallel** — if the bass and tenor both move by semitone in the same direction into the resolution chord, the parallel motion calls too much attention to itself. Interleave the voices so that the chromatic resolution in one voice is offset by contrary or oblique motion in others.

The **seventh of the secondary dominant** also creates an obligation: it must resolve downward by step, just as the seventh of any V7 resolves. This gives you two constrained voices (the leading tone up, the seventh down) that largely determine the resolution chord's voicing. The remaining voices fill in the chord with smooth, preferably stepwise motion. If you plan the resolution before writing the secondary dominant, you can choose a secondary dominant voicing that makes the resolution's voice leading clean — which is a general principle of voice-leading craft: always look ahead one chord when making voicing decisions.
