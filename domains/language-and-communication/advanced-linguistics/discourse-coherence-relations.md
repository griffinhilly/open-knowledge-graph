---
id: discourse-coherence-relations
title: Discourse Coherence and Rhetorical Relations
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: discourse-analysis
  type: hard
- id: discourse-representation-theory
  type: hard
tags:
- discourse
- coherence
- pragmatics
stage: advanced
status: draft
---

# Discourse Coherence and Rhetorical Relations

## Core Idea
Discourse coherence is achieved through rhetorical relations (elaboration, contrast, causation, explanation) linking adjacent sentences into unified structures. Coherence requires recognizing often-implicit discourse relations; violations cause comprehension difficulty and signal discourse incoherence.

## How It's Best Learned
Annotate discourse texts with relation types; study how pronouns, tense, and connectives signal discourse relations; test comprehension of violating vs. coherent discourse.

## Common Misconceptions
Discourse coherence is not mere chronological ordering; it requires recognizing semantic/rhetorical relationships between propositions that may be implicit or signaled subtly.

## Explainer

From your study of discourse analysis, you know that language above the sentence level has structure — conversations, narratives, and arguments are not random sequences of utterances but organized wholes. From discourse representation theory (DRT), you know how pronouns and definite descriptions are resolved across sentences by tracking discourse referents in a dynamic representational structure. Discourse coherence adds a further layer: not just *what* entities sentences are talking about, but *how* adjacent sentences are rhetorically related to each other. Without coherence relations, a sequence of true sentences can feel like a broken text; with them, the same sentences feel like a unified argument or narrative.

Consider a simple pair: *"Mary dropped the vase. It shattered."* You automatically interpret these sentences as causally related — the dropping caused the shattering — even though no causal connective is present. This is a **coherence relation** doing implicit work. The **elaboration** relation links a general claim to supporting detail; the **contrast** relation juxtaposes two situations that differ in an expected dimension; **narration** relates sequential events as part of a story; **explanation** gives the reason for a prior claim. Frameworks like **Rhetorical Structure Theory (RST)**, developed by Mann and Thompson, provide a systematic taxonomy of these relations, annotating how each sentence segment functions as a satellite (supporting) or nucleus (central) contribution relative to others.

The key theoretical insight is that **coherence relations are not merely described by connectives but can be conveyed without them**. "He trained hard. He won the championship" conveys a result relation. "He trained hard, but he lost" triggers a contrast-concession reading. "He trained hard. His coach was skeptical" invites an elaboration or background reading. The reader or hearer draws on world knowledge, pragmatic inference, and local context to assign the most salient relation — which is why incoherent texts are disorienting: when no plausible relation can be assigned between two sentences, comprehension breaks down. Coherence is therefore not a property of sentences in isolation but of a reader's ability to construct a globally consistent interpretation.

Understanding coherence relations has practical applications in computational linguistics, reading comprehension research, and text generation. Automatic **discourse parsers** attempt to label relations between adjacent text spans, a task that remains challenging because the same surface form can realize multiple relations depending on context, and many relations are entirely implicit. In natural language generation, a system that produces coherent multi-sentence output must plan not just the propositional content of each sentence but how each one will relate rhetorically to the next — otherwise outputs feel list-like or fragmented. The linguistic phenomenon you are studying here sits at the boundary between semantics (propositional content) and pragmatics (speaker intent and contextual interpretation), which is what makes it both theoretically rich and empirically complex.
