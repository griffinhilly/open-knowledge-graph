---
id: working-memory-model
title: Working Memory
domain: psychology
course: cognitive-psychology
prerequisites:
- id: cognitive-psychology-overview
  type: hard
builds-toward:
- long-term-memory-types
- memory-encoding-strategies
- cognitive-load-theory
- expertise-and-chunking
tags:
- memory
- working-memory
- baddeley
- short-term
stage: advanced
status: validated
---

# Working Memory

## Core Idea
Working memory is a limited-capacity system that holds and manipulates information for use in ongoing cognitive tasks. Baddeley and Hitch's multicomponent model distinguishes the phonological loop (verbal and acoustic information), the visuospatial sketchpad (visual and spatial information), the episodic buffer (integrative storage), and the central executive (attentional control). Capacity limits of approximately four chunks and the recency effect in recall are core empirical signatures of working memory.

## How It's Best Learned
Explore the phonological loop through articulatory suppression — repeating 'the the the' while memorizing a word list disrupts the loop selectively. The word-length effect (longer words are harder to serially recall) demonstrates that the loop is time-limited rather than item-limited.

## Common Misconceptions
- Working memory is not simply short-term memory — it emphasizes active manipulation, not just temporary storage.
- The capacity limit refers to chunks, not raw items — experts can pack more information into each chunk, effectively expanding functional capacity in their domain.

## Questions

```yaml
- question: "A student tries to hold a phone number in mind while simultaneously repeating 'the the the' aloud. Which component of Baddeley's working memory model is most directly disrupted by the repetition task?"
  type: multiple-choice
  options: ["The central executive", "The visuospatial sketchpad", "The episodic buffer", "The phonological loop"]
  answer: 3
  explanation: "Articulatory suppression (repeating a meaningless sound) occupies the phonological loop, which rehearses verbal and acoustic information. Because the loop is busy, it cannot also rehearse the phone number, disrupting verbal serial recall. This is a classic experimental demonstration that the phonological loop is a distinct, capacity-limited subsystem."

- question: "Working memory capacity is best measured by counting the total number of individual items (letters, digits, words) a person can recall, regardless of how familiar those items are."
  type: true-false
  answer: false
  explanation: "Capacity is measured in chunks, not raw items. A chess expert can encode a mid-game board position as a few meaningful chunks rather than 32 individual piece locations. Familiarity and expertise allow more information to be packed into each chunk, so raw item count conflates capacity with chunking efficiency."

- question: "How does expertise effectively expand a person's functional working memory capacity within their domain?"
  type: short-answer
  answer: "Experts chunk familiar patterns into single units stored as one slot rather than many. A chess master sees 'kingside castled position under attack' as one chunk; a novice sees 12 separate piece locations. By encoding more information per chunk, experts free up capacity for higher-level reasoning about the same situation."
  explanation: "Working memory capacity itself (roughly 4 chunks) does not change with expertise — the size and information density of each chunk does. This is why expertise feels like expanded capacity: the cognitive bottleneck shifts from storage to higher-level processing."
```

## Explainer

You already know from cognitive psychology that the mind does not record experience like a camera — it processes, selects, and constructs. Working memory is the system that holds the information currently being processed: the sentence you are reading, the number you are adding, the face you are comparing to a description. Baddeley and Hitch's model gave researchers a map of how this active holding and manipulation works, and it turns out to be considerably more structured than the older idea of a single "short-term memory."

The model has four components. The **phonological loop** holds verbal and acoustic information through subvocal rehearsal — the inner voice that repeats a phone number while you reach for a pen. It is time-limited rather than item-limited: long words are harder to rehearse than short ones (the word-length effect) because they take longer to cycle through. The **visuospatial sketchpad** holds visual and spatial information — the mental image of a map, or a chess position held in mind while planning. These two subsystems are relatively independent: you can simultaneously rehearse a word list (phonological loop) and rotate a shape in your mind (sketchpad) with less interference than when both tasks use the same subsystem.

The **episodic buffer** integrates information across subsystems and with long-term memory, allowing you to bind a face, a name, and a context into a single episode. The **central executive** is the attentional controller — it allocates resources, switches focus, and coordinates the subsystems. It is the most cognitively demanding component and the one that degrades most under dual-task conditions.

The capacity limit — famously described as roughly four chunks — applies to chunks, not to raw items. A chunk is whatever unit your long-term memory can recognize as a single pattern. A novice chess player sees 20 separate piece locations; an expert sees three familiar configurations. This is why expertise feels like expanded memory in a domain: it is not that the expert's working memory is larger, but that each slot in their working memory is doing more work, encoded against a richer library of long-term patterns.

The practical implication — developed into cognitive load theory, which you will encounter next — is that learning design should respect working memory limits. Presenting too many new elements simultaneously overwhelms the central executive and prevents integration. Instruction works best when it builds on existing chunks (minimizing the number of new elements), presents information in compatible subsystems (verbal explanation + spatial diagram rather than two verbal streams), and builds automaticity in subskills so they no longer require working memory at all.
