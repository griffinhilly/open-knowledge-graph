---
id: schenkerian-levels-analysis
title: Schenkerian Levels of Analysis
domain: music
course: advanced-music-theory
prerequisites:
- id: ursatz-fundamental-structure
  type: hard
builds-toward:
- schenkerian-voice-leading-graphs
tags:
- schenkerian
- analysis
- background
- middleground
- foreground
stage: expert
status: draft
---

# Schenkerian Levels of Analysis

## Core Idea
Schenkerian analysis operates across three hierarchical levels: the background (Ursatz), middleground (how prolongations shape form and phrase structure), and foreground (actual musical surface). Understanding the interaction between these levels reveals how local harmonic events participate in large-scale structure and narrative arc.

## How It's Best Learned
Analyze a single 16-bar phrase at all three levels. Create three separate graphs showing the same music at different levels of abstraction. Compare how different composers achieve similar middleground structures through different foreground techniques.

## Common Misconceptions
- There is a single 'correct' way to analyze at each level. - Each level must show equal amounts of detail. - The background level must be literally present in the score.

## Questions

```yaml
- question: "A dominant chord appears at measure 24 of a 32-measure piece. An analyst must decide whether it is the structural dominant (background-level) or a local embellishment (foreground-level). Which consideration is most decisive?"
  type: multiple-choice
  options:
    - "Its duration — a structural dominant must last at least four measures"
    - "Its position in the phrase — a structural dominant always falls in the second half of the piece"
    - "Whether it resolves to a tonic that closes the Urlinie, and whether the preceding music can be consistently read as elaborating a prolonged tonic up to this point"
    - "The dynamic marking — structural events are typically marked forte or fortissimo"
  answer: 2
  explanation: "Structural priority in Schenkerian analysis is determined by function within the hierarchical reading, not by surface features like duration or dynamics. The structural dominant is the event that drives the entire piece toward its final cadence — so the analysis must check whether the soprano note completing the Urlinie arrives at the subsequent tonic, and whether the intervening material can be coherently explained as middleground prolongations. A dominant is only 'structural' if the entire background and middleground reading hangs consistently from it."

- question: "In Schenkerian analysis, the foreground differs from the background primarily because:"
  type: multiple-choice
  options:
    - "The foreground shows music from the second half of the piece, the background from the first"
    - "The foreground is closest to the actual score surface; the background is the sparse Ursatz skeleton that all foreground events elaborate"
    - "The foreground contains only dissonances, while the background contains only consonances"
    - "The foreground is always correct; the background is the analyst's speculative interpretation"
  answer: 1
  explanation: "The three levels are about abstraction, not position in time. The background (Ursatz) is the most abstract — a stepwise melodic descent supported by I–V–I — and is never literally 'in' the score. The foreground is the level closest to the notated music, showing passing tones, neighbor notes, suspensions, and local harmonies. The middleground connects the two by showing how prolongation techniques expand the background into the richness of the surface. Both background and foreground apply to the entire piece simultaneously."

- question: "A correct Schenkerian background analysis can be directly read off the musical score without interpretive judgment."
  type: true-false
  answer: false
  explanation: "The background level is the Ursatz — a highly abstract skeleton that is emphatically *not* literally present in the score. Identifying it requires interpretive decisions about which events are structurally primary and which are subordinate elaborations. This is why different analysts produce different readings of the same piece, and why the Explainer states the analysis is 'an interpretation, not a transcription.' The foreground is closest to the score; the background is farthest from it."

- question: "Two analysts produce different Schenkerian graphs for the same Beethoven sonata movement — one places the structural dominant at measure 48, the other at measure 62. Both can be defensible."
  type: true-false
  answer: true
  explanation: "Schenkerian analysis at the middleground level involves genuine interpretive choice. There is no single correct reading, only more and less defensible ones. A defensible reading must be internally consistent — its background and middleground levels cannot contradict each other — and must account for the composer's phrase structure, cadential patterns, and registral choices. Two analysts who make different but internally consistent decisions about structural priority can both produce valid graphs. This interpretive plurality is a feature of the method, not a bug."

- question: "Why do Schenkerian analysts work from the background toward the foreground rather than analyzing the musical surface directly and working inward?"
  type: short-answer
  answer: "Working from background to foreground ensures internal consistency: you first anchor the deepest structural facts (where is the final cadence? what soprano note closes the Urlinie? where is the structural dominant?), then explain everything else as elaboration of that skeleton. If you begin from the surface, you risk assigning structural priority to local events that are actually ornamental, or missing how a seemingly insignificant moment participates in a large-scale structure. The background provides the 'frame' that determines how each layer of foreground elaboration is interpreted — without it, foreground events have no context for deciding which are structural and which are subordinate."
  explanation: "The background-to-foreground direction reflects the hierarchical logic of the theory: every foreground event is an elaboration of a middleground event, which is an elaboration of the background. Reversing the direction risks the error Schenker called 'foreground thinking' — mistaking the surface richness for the structural argument. By identifying the endpoints first (Urlinie completion, structural dominant, final cadence), the analyst can then interpret every intermediate event as either prolonging a structural harmony or embellishing a structural melody tone."
```

## Explainer

You already know the **Ursatz** — the background skeleton of tonal music: a stepwise melodic descent from scale degree 3̂, 5̂, or 8̂ to 1̂ (the Urlinie), supported by a I–V–I harmonic motion in the bass (the Bassbrechung). Schenkerian analysis at multiple levels is the practice of showing how a complete tonal piece is a prolongation of this Ursatz — and how intermediate structural layers connect the sparse background to the rich musical surface. The **three levels** are: (1) the **background** (Hintergrund), which is the Ursatz itself; (2) the **middleground** (Mittelgrund), which shows the primary prolongation techniques that elaborate and expand the background; and (3) the **foreground** (Vordergrund), which is closest to the actual score.

The middleground is where most analytical work happens. Here you identify the major prolongation techniques: **arpeggiation** (expanding a harmony by moving through its chord tones), **voice exchange** (two voices trading notes over a harmony), **neighbor motion** (a note moves away by step and returns), and the full elaboration of the bass into a recognizable harmonic progression. A dominant chord appearing in measure 16 might be a temporary embellishment of a broader tonic region, or it might be the structural dominant that drives the entire piece toward its final cadence. The middleground analysis is precisely the exercise of deciding which — and that decision determines how you hear everything before and after it.

The key analytical skill is identifying **structural priority**: which notes are prolonged (structural) and which notes elaborate structural notes (subordinate)? This is why different analysts produce different graphs for the same piece — the analysis is an interpretation, not a transcription. There is no single correct answer at the middleground level, but there are more and less defensible readings. A defensible reading must be internally consistent (if a dominant is structural at the background level, local events near it cannot contradict that reading) and must account for the composer's phrase structure, cadential patterns, and registral choices.

In practice, always work from the background toward the foreground rather than trying to read structure from the surface directly. First identify the final cadence and the soprano note that completes the Urlinie — this anchors both levels. Then locate where the structural dominant appears; everything between the opening tonic and the structural dominant is middleground elaboration of the tonic. Within each middleground region, identify the local structural progressions. The foreground then fills in with passing tones, neighbor notes, suspensions, and embellishing harmonies. Producing all three graphs side by side makes the hierarchical relationships visible and is the clearest way to check whether your reading is consistent across levels.
