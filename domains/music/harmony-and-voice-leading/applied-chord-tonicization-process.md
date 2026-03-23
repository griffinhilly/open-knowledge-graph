---
id: applied-chord-tonicization-process
title: Applied Chords and Tonicization Process
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: secondary-dominants
  type: hard
- id: tonicization
  type: hard
- id: harmonic-function-basics
  type: hard
builds-toward:
- voice-leading-structural-analysis-reduction
tags:
- applied-chords
- tonicization
- secondary
stage: formal-systems
status: validated
---

# Applied Chords and Tonicization Process

## Core Idea
Applied chords (V/ii, V/iii, V/IV, V/V, V/vi, V/vii°) temporarily establish a secondary tonal center, creating a small modulation that resolves back to the home key. Applied chords extend harmonic vocabulary and create structural interest through temporary harmonic goals within a single key.

## Questions

```yaml
- question: "In C major, a composer writes the progression E7 → Am. How should this be analyzed?"
  type: multiple-choice
  options:
    - "E7 is a borrowed chord from C minor, providing chromatic color without structural function"
    - "E7 functions as V/vi — briefly treating Am as a momentary local tonic, creating directional pull before returning to the home key context"
    - "E7 is an altered passing chord with no harmonic function beyond connecting I and vi"
    - "The progression represents a modulation to A minor, since E7 is the dominant of A"
  answer: 1
  explanation: "E7 contains G♯, the leading tone of A minor, which creates directed motion toward Am. This is the applied chord process: E7 functions as V in relation to Am (vi in C major), briefly treating Am as a momentary local tonic. This is tonicization, not modulation — the piece immediately continues in C major. The key analytical difference: tonicization is a brief local emphasis lasting a few beats, while modulation establishes a new key area for a substantial duration, typically confirmed by its own cadence."

- question: "What is the correct three-step process for constructing an applied chord targeting the ii chord (Dm) in C major?"
  type: multiple-choice
  options:
    - "Lower the fifth of the I chord to create chromatic motion leading into ii"
    - "Identify Dm as the target; build its dominant (a chord a fifth above D, containing C♯ as the leading tone of D); resolve that chord to Dm"
    - "Borrow the ii chord from C minor and resolve it downward to I using a plagal motion"
    - "Raise the root of the I chord by a half step to create a chromatic approach to ii"
  answer: 1
  explanation: "The three-step process: (1) Identify the target — Dm (ii in C major). (2) Build the dominant of D minor — an A major chord with C♯ as the leading tone of D (since D minor has C♯ as its leading tone). This is A-C♯-E, which functions as V/ii. (3) Resolve V/ii to ii — A major → Dm. The C♯ steps up to D (leading tone resolution) and the A can resolve by common tone or step. The applied chord momentarily redirects the listener's expectation toward Dm as a local center before the home key context resumes."

- question: "An applied chord like V/V indicates that the piece has modulated to the dominant key, since the dominant is now being tonicized."
  type: true-false
  answer: false
  explanation: "Tonicization and modulation differ in duration and commitment. Modulation establishes a new key area for a significant portion of the piece, usually confirmed by a cadence in the new key. Tonicization is brief — typically a few beats — and the home key context immediately resumes afterward. An applied chord is a momentary harmonic detour that highlights a scale degree without abandoning the home key. After V/V resolves to V, we remain in the home key; V is still the dominant, not a new tonic."

- question: "Any diatonic triad in a major key except the diminished VII° can serve as the target of an applied chord (tonicization)."
  type: true-false
  answer: true
  explanation: "Tonicization works by temporarily treating a chord as a local tonic and approaching it with its own dominant. This is possible for major and minor triads, which can convincingly function as temporary tonics. The diminished triad on VII° is excluded because diminished triads are tonally unstable — they don't function as convincing local tonics, and their 'dominant' would require unusual voice-leading. All other diatonic chords (I, ii, iii, IV, V, vi) can be tonicized, giving composers V/ii, V/iii, V/IV, V/V, and V/vi."

- question: "Why does the Explainer say that understanding applied chords transforms harmonic analysis 'from chord-by-chord labeling into narrative reasoning'? What does it mean to hear an applied chord as a momentary tonal direction rather than a chromatic accident?"
  type: short-answer
  answer: "Hearing an applied chord as a chromatic accident means noticing 'there is a raised note here' and moving on. Hearing it as a momentary tonal direction means asking 'where is this music pointing right now, and why?' The applied chord briefly redirects harmonic expectation toward a local center, making the arrival on that center feel earned rather than routine. Narrative reasoning treats the progression as a story: the music departs toward a secondary goal, achieves it, then returns home. This reframes analysis from a series of labeled chords into a dynamic account of harmonic tension, direction, and resolution."
  explanation: "The analytical shift is from static identification (what is this chord?) to dynamic interpretation (what is this chord doing?). An applied chord says 'we are briefly pointing here' — and understanding that changes how you hear everything that follows. The arrival on the tonicized chord feels like a small local climax; the return to the home key context feels like resumption of a larger journey. Without this narrative perspective, the same progression is just a sequence of Roman numerals with unexplained accidentals."
```

## Explainer

You've already encountered secondary dominants — chords that temporarily act as V in relation to a scale degree other than the home tonic. Applied chords formalize and systematize this idea. When you write V/V (the dominant of the dominant), you're not just borrowing an altered chord for color; you're briefly establishing the dominant scale degree as a temporary tonal center, making the arrival on V feel earned and directional rather than routine. **Tonicization** is the name for this process: treating a non-tonic chord as a momentary local tonic, without committing to a full key change.

The applied chord process works in three steps. First, identify the **target chord** — the diatonic chord you want to emphasize. Second, build the dominant (or leading-tone diminished seventh) of that target as if it were a temporary tonic: the applied chord's root sits a perfect fifth above the target, and it contains the leading tone of the target's hypothetical key. Third, resolve the applied chord to its target, confirming the temporary center before returning to the home key. The entire sequence typically lasts only a few beats, but within those beats the listener's harmonic expectation has been redirected. The return to the home key feels fresh rather than predictable.

Consider V/IV in C major as a concrete example. The IV chord is F major. The dominant of F major is a C major chord with B♮ as its leading tone (since F major has B♭, we use B♮ to serve as the leading tone pulling up to C). A C major triad with B♮ is just a standard C major triad, but now it functions as V in relation to F rather than as I in relation to C. The moment is subtle, but its effect is real: approaching IV via its own dominant makes the F major chord feel like a brief local tonic, adding depth to a motion that would otherwise feel like a plain I–IV stepwise drift.

The broader principle is that **any diatonic triad except the diminished VII° can be tonicized**, giving you V/ii, V/iii, V/IV, V/V, and V/vi, plus their leading-tone equivalents (vii°7/x). Learning to hear these as momentary tonicizations rather than chromatic accidents is the key analytical shift. Instead of noticing "there's a strange chord with a raised note," you hear "we're briefly treating the supertonic as a local tonic before returning home." This transforms harmonic analysis from chord-by-chord labeling into narrative reasoning about where the music is momentarily pointing and why.
