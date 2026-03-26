---
id: fugal-analysis-counterpoint
title: Fugal Analysis and Structure
domain: music
course: advanced-music-theory
prerequisites:
- id: baroque-counterpoint-and-fugue
  type: hard
- id: species-counterpoint
  type: hard
builds-toward:
- invertible-counterpoint-advanced
tags:
- fugue
- counterpoint
- analysis
- baroque
stage: expert
status: validated
---

# Fugal Analysis and Structure

## Core Idea
Fugal analysis examines how the subject, answer, countersubject, and episodes create structure across a fugue, how voices interact through voice leading and canonic imitation, and how harmonic motion supports the large-scale architecture. The fugue represents the pinnacle of contrapuntal organization in tonal music and demonstrates systematic development of material.

## Questions

```yaml
- question: "In a four-voice fugue exposition, the second voice enters with the answer rather than restating the subject exactly. What is the primary purpose of the answer?"
  type: multiple-choice
  options:
    - "To provide rhythmic contrast by entering at a different point in the meter"
    - "To avoid monotony by using different melodic intervals than the subject"
    - "To transpose the subject (usually to the dominant) so all voices enter without repeating the same tonal area"
    - "To demonstrate invertible counterpoint by placing the subject in a higher register"
  answer: 2
  explanation: "The answer is the subject transposed to the dominant key (a fifth above), and its function is tonal: it begins the process of establishing tonal contrast in the exposition by moving to a closely related key. A tonal answer may adjust a few intervals to smooth out key-area transitions; a real answer transposes exactly. The countersubject (option D's hint) is a separate melody accompanying the answer, not the answer itself. Options A and B misidentify the answer's role — rhythmic variety and melodic contrast are incidental, not primary."

- question: "A fugue episode appears between two subject entries in the development section. Which of the following best describes the episode's function?"
  type: multiple-choice
  options:
    - "The episode presents the subject in inversion, showing the theme from a new angle"
    - "The episode is a passage without a complete subject statement, typically developing motivic fragments and modulating to prepare the next entry"
    - "The episode is where the countersubject is heard alone, without the subject, for the first time"
    - "The episode introduces a new, contrasting theme to provide relief from the subject's domination"
  answer: 1
  explanation: "Episodes are transitional passages that lack a complete subject statement. They develop motivic material — often from the countersubject or the subject's tail — and perform the crucial harmonic function of modulating between key areas, setting up the next subject entry in a new tonal center. They are not where new themes appear (a fugue derives everything from its subject) and they are not inversions of the subject (that would still be a subject entry). Option A describes a development technique (inversion), not an episode."

- question: "In stretto, subject entries overlap: a new voice enters with the subject before the previous entry has finished. Stretto typically occurs at the same time interval between entries throughout a fugue."
  type: true-false
  answer: false
  explanation: "Stretto intervals vary. Bach and other composers frequently tighten the time interval between entries as the fugue progresses, creating increasing urgency as entries overlap more closely. A fugue might introduce stretto at a four-bar interval and later compress it to one bar or even half a bar. The compression itself is a compositional technique for building intensity. The stretto interval is determined by what the subject's melodic and harmonic profile allows — not all subjects permit tight stretto, and the best subjects are designed to admit it at multiple time intervals."

- question: "The countersubject is freely composed for each fugue entry and may change depending on which voice carries the subject."
  type: true-false
  answer: false
  explanation: "The countersubject is a consistent melodic idea designed to accompany the subject contrapuntally throughout the fugue. It follows the subject from voice to voice — when the subject enters in the alto, the countersubject appears in the soprano; when the subject moves to the bass, the countersubject appears in the tenor, etc. This consistency is precisely what makes it a countersubject rather than free counterpoint. Its consistent harmonic and rhythmic relationship to the subject is what enables the fugue to develop the two ideas in combination throughout the piece."

- question: "What does it mean to analyze a fugue 'at two levels simultaneously,' and why is either level alone insufficient?"
  type: short-answer
  answer: "Fugal analysis operates at the local level (beat-by-beat voice leading: intervals between voices, suspensions, resolutions, parallel fifths) and the large-scale architectural level (when and where subject entries occur, in what keys and voices, how episodes modulate between them, where the structural climax falls). Local analysis alone reduces the fugue to a series of harmonic snapshots without explaining its overall shape or purpose. Large-scale analysis alone treats entries as structural pillars without understanding how the lines interact between them. The fugue's logic — how motivic material generates both the moment-to-moment counterpoint and the large-scale architecture — only becomes clear when both levels are tracked simultaneously."
  explanation: "The two-level framework captures what makes fugue distinctive as a form: it is simultaneously a harmonic journey (analyzable like any tonal piece by its key areas and modulations) and a contrapuntal texture (where every beat is governed by voice-leading rules). Understanding the subject's role in both dimensions — as a harmonic entity that defines key areas when it enters, and as a melodic entity whose intervals generate the local counterpoint — is the goal of fugal analysis at its most complete."
```

## Explainer

From your work with baroque counterpoint and species counterpoint, you already know how to write independent melodic lines that combine harmonically and avoid parallel fifths and octaves. A fugue takes those principles and organizes them into a large-scale form driven by a single motivic cell — the **subject**. Understanding a fugue analytically means tracing exactly how that subject is introduced, imitated, varied, and developed across all voices throughout the piece. Everything in a fugue is either the subject or commentary on it.

The **exposition** is the opening section where each voice enters in turn with the subject. The first voice states the subject in the tonic; the second voice responds with the **answer** — typically the same melody transposed to the dominant, either exactly (**real answer**) or with small adjustments to preserve tonal coherence (**tonal answer**). While the second voice presents the answer, the first voice usually continues with the **countersubject**, a new melody designed to complement the subject contrapuntally. The countersubject follows the answer voice by voice through the remaining entries, so its harmonic and rhythmic relationship to the subject remains consistent. When all voices have entered, the exposition ends. A useful heuristic: count the number of voices, and you know how many entries the exposition contains.

After the exposition, the fugue moves through **development sections** and **episodes**. Development sections bring back the subject in new keys or with varied treatments — inverted (melodic contour flipped upside-down), augmented (note values doubled), diminished (note values halved), or in **stretto** (entries overlapping before the previous statement is complete). Stretto creates urgency through compression; Bach's Well-Tempered Clavier contains famous examples where the subject overlaps at shorter and shorter intervals as the fugue builds toward its climax. **Episodes** are transitional passages without a complete subject statement — they develop motivic fragments, often from the countersubject or the tail of the subject, and modulate toward new keys in preparation for the next entry.

Analyzing a fugue well means working at two levels simultaneously: **local voice leading** (how the lines interact beat by beat, what intervals they form, how suspensions and resolutions behave) and **large-scale architecture** (when subject entries occur, in what keys and voices, how episodes function as transitions, where the structural climax falls). The harmonic plan of a fugue is largely determined by the subject entries: each entry establishes a tonal center, and the sequence of entries traces the harmonic journey — typically moving through closely related keys in the middle section before returning to the tonic. Episodes do the modulatory work between entries.

The deepest skill in fugal analysis is recognizing how the subject's melodic and rhythmic profile generates all the subsequent material. The best fugue subjects (think the C minor subject from WTC Book I, or the B-flat minor from Book II) contain within themselves the seeds of stretto, inversion, and development — the composer designs the subject knowing what can be done with it. When you analyze a fugue, you are reverse-engineering that compositional logic: why does this subject admit these transformations? How does the formal architecture exploit the specific properties of this melody? Answering those questions is fugal analysis at its most sophisticated.
