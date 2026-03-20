---
id: cognitive-load-theory
title: Cognitive Load Theory
domain: psychology
course: cognitive-psychology
prerequisites:
- id: working-memory-model
  type: hard
- id: attention-selective
  type: hard
- id: attention-divided
  type: soft
builds-toward:
- metacognition
- expertise-and-chunking
tags:
- cognitive-load
- learning
- instructional-design
- working-memory
stage: advanced
status: validated
---

# Cognitive Load Theory

## Core Idea
Cognitive load theory (Sweller) proposes that learning is constrained by the limited capacity of working memory. Three types of load are distinguished: intrinsic load (from the inherent complexity of the material), extraneous load (from poorly designed instruction that wastes cognitive resources), and germane load (from effortful schema construction that benefits long-term learning). Effective instruction minimizes extraneous load, manages intrinsic load through careful sequencing, and optimizes germane load by actively promoting schema formation.

## How It's Best Learned
Compare learning from worked examples versus equivalent problem-solving in a complex domain at early learning stages — worked examples reduce extraneous load and demonstrate superior retention. The expertise reversal effect, where this advantage disappears as learners gain proficiency, shows that optimal load depends on the learner's current schema state.

## Common Misconceptions
- High cognitive load does not automatically produce poor learning — desirable difficulties that increase germane load can improve long-term retention despite slowing initial acquisition.
- Cognitive load theory applies broadly to any learning under resource constraints, not only to formal educational settings.

## Explainer

You already know from the working memory model that the phonological loop, visuospatial sketchpad, and central executive have strictly limited capacity. Cognitive load theory (Sweller, 1988) builds directly on this: if learning requires constructing new schemas in long-term memory, and if that construction must pass through working memory, then anything that wastes working memory capacity on *something other than schema formation* is directly reducing how much learning can occur. The theory's power comes from distinguishing precisely *where* the load is coming from — because only some types of load are unavoidable, and only some types benefit learning.

**Intrinsic load** is the load imposed by the material itself. It depends on **element interactivity** — how many information elements must be held in working memory simultaneously because they are meaningfully interrelated. Learning isolated vocabulary words has low element interactivity: each word can be learned independently. Learning to solve a multi-step algebra problem has high element interactivity: each step depends on the previous ones, so everything must be held together. Intrinsic load cannot be eliminated without changing the material itself, but it can be managed through sequencing — presenting simple cases first, building up complexity only after foundational schemas are formed.

**Extraneous load** is the load imposed by *how instruction is designed*, not by the content. It is cognitive effort that does not contribute to learning — effort spent searching for relevant information, integrating redundant materials, or processing decorative elements. Classic sources of extraneous load include the **split-attention effect** (diagrams separated from their explanatory text, requiring the learner to mentally integrate them), the **redundancy effect** (restating in words what is already fully conveyed by a diagram), and **seductive details** (interesting but irrelevant content that captures attention). Good instructional design systematically eliminates these waste sources — placing labels on the diagram rather than in a separate legend, removing decorative images from worked examples, cutting explanatory prose when a visual is already complete.

**Germane load** is the effortful cognitive processing that *directly produces* schema formation. It is sometimes described as good load — not all difficulty is wasteful. Generating an answer yourself (**the generation effect**), varying the context across practice problems (interleaving), and explaining material to others (the protégé effect) all impose additional processing demands while substantially improving long-term retention. These demands produce germane load because they force the learner to encode the underlying structure of the material rather than surface features. The **worked example effect** neatly illustrates the interplay: novice learners achieve better learning from studying worked examples (low extraneous and intrinsic load, freeing resources for schema formation) than from solving equivalent problems. But this reverses for experts — the **expertise reversal effect** — because the expert already has rich schemas and the worked example now creates redundancy (extraneous load), making self-directed problem-solving more efficient. Cognitive load theory thus makes precise, testable predictions about which instructional formats work best for which learners at which stages of expertise.
