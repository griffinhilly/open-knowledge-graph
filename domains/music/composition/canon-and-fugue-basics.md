---
id: canon-and-fugue-basics
title: Canon and Fugal Writing Foundations
domain: music
course: composition
prerequisites:
- id: counterpoint-two-voice
  type: hard
- id: fugal-analysis-counterpoint
  type: soft
tags:
- counterpoint
- canon
- fugue
- imitation
stage: formal-systems
status: validated
---

# Canon and Fugal Writing Foundations

## Core Idea
Canons and fugues are highly structured contrapuntal forms in which melodic material is restated and developed through systematic imitation. In a canon, one voice presents a melody that subsequent voices replicate at a time interval, creating both unity and independence through constrained repetition. Fugues extend this principle with subject statements in multiple voices, development sections, and sophisticated contrapuntal combinations. Understanding these forms reveals how compositional unity emerges from the disciplined treatment of a single melodic idea.

## Questions

```yaml
- question: "A student writes a beautiful melody and uses it as the dux of a two-voice canon, having the comes enter four beats later playing the exact same line. What problem are they likely to encounter?"
  type: multiple-choice
  options:
    - "The comes will be too loud relative to the dux"
    - "The moments where both voices sound simultaneously may produce unintended dissonances"
    - "A four-beat interval is too long for imitation to be recognizable as a canon"
    - "The interval of imitation must always be an octave, not a unison"
  answer: 1
  explanation: "In a canon, the melody must be designed so that its beginning harmonizes with its middle and its middle harmonizes with its ending — wherever the dux and comes overlap, the combination must be consonant. A melody crafted purely for solo appeal carries no such guarantee; the canon constraint requires the melody to serve simultaneously as both melody and its own accompaniment. Choosing a beautiful but unconstrained melody and then adding delayed imitation is likely to produce voice-leading errors at the overlap points."

- question: "What does 'invertible counterpoint' mean in fugue writing, and why must a composer plan for it from the very beginning?"
  type: multiple-choice
  options:
    - "The subject can be played in retrograde (backwards) without losing its harmonic character"
    - "The subject and countersubject can swap registers so that whichever is on top, the voice-leading between them remains valid"
    - "The fugue can be transposed to any key without altering the subject"
    - "The answer always enters in the dominant, which inverts the tonal relationship with the subject"
  answer: 1
  explanation: "Invertible counterpoint means the subject and countersubject are designed so that when one moves to the upper register and the other to the lower, the harmonic intervals between them remain acceptable. When voices invert, intervals transform: a sixth becomes a third, and critically, a fifth becomes a fourth — which was a dissonance in Renaissance practice. A subject chosen without this in mind may create unresolvable voice-leading problems the moment the composer attempts to invert the pair, which is why the design must be simultaneous, not sequential."

- question: "In a strict canon at the octave, the follower voice plays the exact same pitches and rhythms as the leader, beginning at a later time."
  type: true-false
  answer: true
  explanation: "This is precisely what defines a strict canon: the dux (leader) presents a melody, and after a fixed time interval the comes (follower) replicates it exactly — same pitches, same rhythms, just offset in time. The word 'canon' means 'rule,' and the rule is exact imitation. Other canons may imitate at a fifth, a third, or another interval (transposing the pitch content), but they still replicate the rhythm and relative pitch intervals exactly."

- question: "A fugue subject can be any melodically distinctive idea; a skilled composer can typically write a suitable countersubject for it afterward."
  type: true-false
  answer: false
  explanation: "The subject and countersubject must be conceived as an integrated system with invertible counterpoint in mind from the start. A subject chosen purely for melodic character may generate counterpoint problems that cannot be resolved when inversion is required later — the intervals between them may become dissonant in the swapped register. Fugue composition requires long-range thinking: the subject's design constrains and is constrained by the countersubject's design, and both must satisfy invertibility as a joint requirement."

- question: "Why is it insufficient to simply write a good melody and add a delayed imitation to create a canon? What specific compositional requirement must the melody satisfy?"
  type: short-answer
  answer: "The melody must be its own counterpoint: at every point where the leading voice (dux) and following voice (comes) sound simultaneously, the combination must form consonant, voice-leading-valid harmonies. This requires that the melody's opening bars harmonize with its middle bars (which the comes will be playing at the same moment) and its middle bars harmonize with its final bars. A melody crafted in isolation carries no such guarantee and is likely to produce parallel fifths, unresolved dissonances, or other errors wherever the two voices overlap."
  explanation: "This is the fundamental compositional discipline of canon: the composer must hear the melody simultaneously in two temporal positions while writing it, designing a single line that works both as melody and as accompaniment to itself. The constraint is total — no segment of the melody is 'free' from the obligation to harmonize with its own displaced echo."
```

## Explainer

Canon and fugue build directly on two-voice counterpoint. In counterpoint, you learned to write two independent melodic lines that work together harmonically while each makes sense on its own. Canon and fugue take that independence and add a new organizing principle: **imitation**, where one voice restates what another voice just sang or played. The compositional discipline is that the melody must be its own counterpoint — whatever the leading voice plays must harmonize with what the following voice will be playing at the same time.

A **canon** is the simplest form of imitative counterpoint. One voice (the **dux**, or leader) presents a melody. After a fixed time interval, a second voice (the **comes**, or follower) begins the exact same melody, while the first voice continues. You already know the most familiar example: "Row, Row, Row Your Boat" sung as a round. Each entrance works because the melody was constructed so that its opening harmonizes with its middle and its middle harmonizes with its ending. Canon makes this constraint explicit and total — the composer must write a single line that counterpoints itself at a specified interval of time and pitch.

A **fugue** extends this logic into a full formal structure. The **subject** — a short, distinctive melodic idea — is announced alone in one voice, then imitated by a second voice (the **answer**) while the first continues with a **countersubject**. Once all voices have entered in the **exposition**, the fugue opens into **episodes** (passages where the subject is absent, often using sequence and fragmentation) and further entries that restate the subject in new keys. The distinguishing feature of fugue is not just imitation but the systematic harmonic journey of a single subject through development, combination, and return.

The deepest technical requirement is **invertible counterpoint**: the subject and countersubject must be designed so that either can be placed on top without violating voice-leading rules. When the two parts swap registers, the intervals between them change (a sixth becomes a third, a fifth becomes a fourth), and what worked as a consonance can become a dissonance. Fugue composers design subject-countersubject pairs with this inversion in mind from the start — a discipline that forces long-range thinking and gives fugues their characteristic contrapuntal density.
