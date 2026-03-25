---
id: schenkerian-voice-leading-graphs
title: Schenkerian Graphs and Reduction Notation
domain: music
course: advanced-music-theory
prerequisites:
- id: schenkerian-levels-analysis
  type: hard
- id: graphic-notation-interpretation
  type: soft
- id: schenkerian-linear-progression
  type: soft
builds-toward:
- prolongation-structural-reduction
tags:
- schenkerian
- notation
- graphs
- reduction
stage: expert
status: validated
---
# Schenkerian Graphs and Reduction Notation

## Core Idea
Schenkerian graphs use specialized notation (reduction notation with lines, stems, beams, and beaming patterns) to show how musical materials are nested and related across structural levels. Mastering graph notation is essential for communicating reductions and comparing different analytical interpretations systematically.

## Questions

```yaml
- question: "In a Schenkerian graph, a note appears without a stem. What does this signify?"
  type: multiple-choice
  options:
    - "The note is performed without accent or dynamic emphasis"
    - "The note belongs to a lower structural level — it is an embellishment of a nearby stemmed note"
    - "The note is part of the bass arpeggiation"
    - "The note is the Kopfton, the opening note of the Urlinie"
  answer: 1
  explanation: "Stemming encodes structural importance. Stemmed notes belong to structurally significant levels (the Urlinie or bass arpeggiation); unstemmed notes are elaborations at a lower structural level, filling in the space defined by the stemmed notes around them. The distinction between stemmed and unstemmed is the graph's primary tool for showing the hierarchy of structural levels."

- question: "Two analysts produce different Schenkerian graphs of the same piece. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "At least one analyst made an error transcribing the score"
    - "They are making different analytical claims about how the piece achieves tonal coherence"
    - "The piece is too complex for Schenkerian methods"
    - "One analyst is using the wrong key signature"
  answer: 1
  explanation: "Schenkerian analysis is a practice of argumentation, not a readout of objective facts. Different reductions reflect different interpretations of which notes are structurally primary, where the Kopfton lies, and how prolongations operate across the middle ground. Disagreement between graphs is normal and productive — each graph is a claim about how the music works, and those claims can be compared and debated with rigor."

- question: "A beam connecting several notes in a Schenkerian graph indicates that those notes should be played more smoothly (legato) than unbeamed notes."
  type: true-false
  answer: false
  explanation: "Schenkerian graphs are not performance scores. Beams carry no articulation instruction. In a reduction graph, a beam means that the connected notes belong to the same structural level and form a coherent linear motion — for example, the stepwise Urlinie descent from 3̂ to 1̂ beamed across many measures of surface music. The graph makes a structural claim about how these notes relate over the span of the piece, not how they should be articulated in performance."

- question: "The Ursatz, the deepest structural level in Schenkerian analysis, consists of an ascending melodic line supported by harmonic motion from I to V to I."
  type: true-false
  answer: false
  explanation: "The Ursatz consists of a *descending* melodic line — the Urlinie — moving stepwise from the Kopfton (typically 3̂ or 5̂) down to 1̂, supported by a bass arpeggiation from I through V to I. The descent is essential to Schenker's theory: it represents the fundamental voice-leading motion that all foreground detail prolongs and elaborates. An ascending fundamental line would contradict the harmonic closure the theory is built around."

- question: "Explain what it means to say that a Schenkerian graph is a 'claim' rather than a 'description,' and why this distinction matters for analysis."
  type: short-answer
  answer: "A description catalogs what is in the score — the actual notes, rhythms, and harmonies. A claim is an interpretive argument about structural function: which notes prolong a harmony, which voices form a linear descent to the tonic, and how all foreground detail derives from a deeper background structure. Because these are interpretive choices, two analysts can produce different graphs of the same piece — both defensible, but prioritizing different structural readings. The graphs can then be compared and evaluated on analytical grounds, which is impossible if analysis is treated as mere description."
  explanation: "This is what makes Schenkerian analysis a practice of argumentation. The specialized notation (stems, beams, slurs) is the vocabulary for making those analytical claims precisely enough to be read, debated, and revised."
```

## Explainer

From your work in **Schenkerian levels analysis**, you know the core analytical claim: tonal music is organized across multiple structural levels, from the note-by-note foreground to the large-scale background structure (the *Ursatz*). The challenge is how to represent this hierarchy visually. Schenkerian graphs solve this by using a specialized notational system that encodes both the structural level of each note and the voice-leading relationships between notes — all on a single staff.

The most important notational tool is **stemming**. A note with a stem belongs to a structurally significant level: stems pointing up generally indicate the *Urlinie* (fundamental melodic line), while stems pointing down indicate the bass arpeggiation or important inner voices. A note without a stem is at a lower structural level — it is a neighbor tone, passing tone, or other embellishment elaborating a stemmed note. **Beams** connect notes of the same structural level that form a coherent linear motion: a descending stepwise line from 3̂ to 1̂ in the Urlinie might be beamed together to show its unity across many measures of surface music. **Slurs** indicate prolongations — a slur spanning many notes shows that one structural harmony is being prolonged through all the embellishing material beneath it.

The graph is read simultaneously as a pitch reduction and a voice-leading statement. When two notes at the same structural level are connected by a beam, the claim is that these notes are structurally equivalent and that all surface notes between them elaborate the space those structural tones define. The **Kopfton** — the initial note of the Urlinie, usually 3̂ or 5̂ — appears as the first stemmed note in the graph, and its descent to 1̂ is the organizing melodic arc of the entire piece. The bass arpeggiation from I through V to I mirrors this descent in the bass register. Together they form the *Ursatz*, the background structure from which all foreground detail is understood to derive.

The practical skill is learning to read graphs in both directions: from graph to music (using the graph as a guide for where to listen in the score) and from music to graph (making analytical decisions about which notes warrant stems and how to connect them). Different analysts sometimes produce different graphs of the same piece, and Schenkerian analysis is partly a practice of argumentation about which reductions best explain a work's coherence. The graph is not a description of what the music is; it is a claim about how the music works. Mastering the notation means you can read, produce, and debate those claims with rigor and clarity.
