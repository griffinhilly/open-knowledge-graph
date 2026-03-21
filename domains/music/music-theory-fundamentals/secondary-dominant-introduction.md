---
id: secondary-dominant-introduction
title: 'Secondary Dominants: Temporary Tonicization'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: tonicization
  type: hard
- id: dominant-seventh-resolution
  type: soft
builds-toward:
- chromatic-harmony-borrowed-chords
- harmonic-progression-analysis
tags:
- secondary-dominant
- tonicization
- V-of-V
- chromatic-harmony
stage: formal-systems
status: draft
---

# Secondary Dominants: Temporary Tonicization

## Core Idea
A secondary dominant (like V/V or V7/IV) is a dominant chord that temporarily tonicizes a scale degree other than the tonic. For example, V of V creates dominant function toward IV, treating IV momentarily as a tonal center. Secondary dominants add chromatic interest and expand harmonic vocabulary while remaining within a single key. The secondary dominant must resolve down a perfect fifth to its target chord.

## How It's Best Learned
Analyze secondary dominants in classical and popular music. Practice building and resolving secondary dominants at the keyboard.

## Common Misconceptions
- Thinking V/V can resolve to anywhere (it must resolve to IV in standard practice).
- Not recognizing secondary dominants in unfamiliar key signatures (they often involve accidentals).

## Questions

```yaml
- question: "In the key of G major, what chord is V/V (the dominant of the dominant)?"
  type: multiple-choice
  options:
    - "A minor (A–C♮–E)"
    - "A major (A–C♯–E)"
    - "E major (E–G♯–B)"
    - "B major (B–D♯–F♯)"
  answer: 1
  explanation: "G major's dominant (V) is D. To find V/V, ask: what is the dominant chord of D major? D major's dominant is A major (A–C♯–E). In G major, C is naturally C♮, so the C♯ is the tell-tale accidental that marks this as a secondary dominant. A minor would be the diatonic ii chord of G major — it has no dominant function toward D."

- question: "While analyzing a piece in C major, you notice a chord containing F♯. A classmate concludes the piece has modulated to G major. What is a more likely explanation?"
  type: multiple-choice
  options:
    - "Your classmate is correct — F♯ signals a key change to G major"
    - "The F♯ is probably part of a secondary dominant (D major = V/V), tonicizing the G chord momentarily"
    - "F♯ is a chromatic passing tone with no harmonic function"
    - "The composer made an error in the score"
  answer: 1
  explanation: "An accidental within a passage is the primary diagnostic clue for a secondary dominant — not a modulation. If the music briefly uses D major (with F♯) and then resolves to G (V in C major) before continuing in C, it is tonicizing G without changing key. A true modulation would involve an extended stay in the new key, not just one chord. The two-level thinking skill is learning to distinguish 'visiting' (secondary dominant) from 'moving' (modulation)."

- question: "V/V in C major is D minor, built on the second scale degree with the notes D–F♮–A."
  type: true-false
  answer: false
  explanation: "V/V in C major is D major (D–F♯–A), not D minor. D minor is the naturally occurring ii chord of C major. To function as a secondary dominant, D must have dominant quality — a major triad (or major-minor seventh). The F♯ is borrowed from G major, where D is the dominant. D minor has no leading tone to G and therefore lacks the tension needed to tonicize it."

- question: "A secondary dominant must resolve to a chord a perfect fifth below it."
  type: true-false
  answer: true
  explanation: "This resolution rule is strict and parallels the ordinary V→I resolution: the secondary dominant (e.g., V/V) resolves down a perfect fifth to its target (V). V/IV resolves to IV; V/ii resolves to ii. The leading tone of the borrowed key resolves upward by a half step, and the fifth resolves downward, creating a local sense of arrival. A secondary dominant that doesn't resolve this way loses its functional identity."

- question: "What does it mean to 'hold two levels of tonal reference simultaneously' when analyzing secondary dominants, and why is this skill essential for understanding chromatic harmony?"
  type: short-answer
  answer: "It means tracking both the home key (what key is the piece in overall?) and the local key (what is this specific chord pointing toward right now?). A secondary dominant has dominant function relative to its target chord, even if that target is not the home tonic. For example, V/V in C major has dominant function relative to G, not relative to C. You must hold 'we are in C major' and 'this chord is behaving as if G is tonic' in mind at the same time."
  explanation: "This two-level thinking is the conceptual foundation of all chromatic harmony. Diatonic chords have functions only relative to the home key. Secondary dominants introduce a second level: a chord can simultaneously be a non-tonic scale degree in the home key and a dominant in a local context. Failing to think at both levels causes analysts to either miss the secondary function (treating it as just a color chord) or over-interpret it as a modulation."
```

## Explainer

You already understand **tonicization** — the idea that any chord can be temporarily treated as a local tonic, with its own dominant preparing it. A **secondary dominant** is the specific chord that performs this preparation: it is the dominant (V) or dominant seventh (V7) chord built above whatever scale degree you want to tonicize. The notation "V/V" is read "five of five" — the dominant of the dominant. "V/IV" means "the dominant of the fourth scale degree." That slash notation is the grammar of secondary dominants, and learning to parse it is the first skill.

Start with V/V in the key of C major. The fifth scale degree is G, so V/V asks: what is the dominant chord of G major? That's D major (D–F♯–A). In the key of C, an ordinary D chord would be D minor (D–F♮–A). But D major requires F♯, which is outside the C major scale — hence the accidental you'll see in the score. This chromatic note is the giveaway: secondary dominants almost always introduce at least one accidental because they're borrowing a note from a different key temporarily. When you see an unexpected sharp or natural sign in a chord, your first diagnostic question should be: is this a secondary dominant?

The resolution rule is strict: a secondary dominant resolves down a **perfect fifth** to its target chord. V/V → V. V/IV → IV. V/ii → ii. The resolution mimics the behavior of the ordinary dominant-to-tonic resolution you already know: the **leading tone** of the secondary dominant (the raised seventh of the borrowed key) resolves upward by a half step, and the fifth typically resolves downward. This creates a local sense of harmonic arrival even though the piece hasn't changed key. The music "visits" a new tonal center for a moment before continuing.

Secondary dominants add chromatic intensity and forward momentum to progressions. A chord sequence like I → V/V → V → I creates a sense of building anticipation — the V/V charges the V with extra energy before the final resolution. This is why secondary dominants appear so often at cadences, providing a more dramatic approach to the dominant than diatonic chords alone can offer. In jazz and popular music, the ii–V–I pattern in any key is essentially a local instance of the same logic: ii prepares V, which resolves to I — and a secondary dominant can strengthen any of those motions.

The conceptual leap secondary dominants require is thinking about harmonic function **locally** rather than only globally. In a simple diatonic progression, every chord has a function relative to the home key. Secondary dominants introduce **local tonicization** — a chord has dominant function relative to whatever follows it in that moment, even if that target isn't the home tonic. This requires you to hold two levels of tonal reference simultaneously: the home key (where are we overall?) and the local key (what is this chord pointing toward right now?). That two-level thinking is the foundation of everything in chromatic harmony that follows.
