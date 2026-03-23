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
stage: expert
status: draft
---

# Discourse Coherence and Rhetorical Relations

## Core Idea
Discourse coherence is achieved through rhetorical relations (elaboration, contrast, causation, explanation) linking adjacent sentences into unified structures. Coherence requires recognizing often-implicit discourse relations; violations cause comprehension difficulty and signal discourse incoherence.

## How It's Best Learned
Annotate discourse texts with relation types; study how pronouns, tense, and connectives signal discourse relations; test comprehension of violating vs. coherent discourse.

## Common Misconceptions
Discourse coherence is not mere chronological ordering; it requires recognizing semantic/rhetorical relationships between propositions that may be implicit or signaled subtly.

## Questions

```yaml
- question: "Read the pair: 'She practiced violin every day for a year. Her audition was a disaster.' What coherence relation does a reader most naturally assign between these sentences?"
  type: multiple-choice
  options:
    - "Elaboration — the second sentence provides more detail about the practice sessions"
    - "Concession/contrast — the effort and outcome are in tension with expected results"
    - "Narration — the second event simply follows the first in time"
    - "Explanation — the audition failure explains why she practiced so much"
  answer: 1
  explanation: "The reader uses world knowledge (practice should lead to success) to detect a violation of expectations between the two sentences. This signals a concession or contrast relation — the expected causal chain (practice → success) is disrupted. No connective like 'but' or 'however' is present; the reader assigns the relation inferentially. Option C is too weak — mere temporal sequence doesn't capture the rhetorical tension. Option D reverses the causal direction."

- question: "Which of the following best demonstrates that discourse coherence is NOT simply a matter of topical relatedness between sentences?"
  type: multiple-choice
  options:
    - "A paragraph about photosynthesis becomes incoherent if a sentence about digestion is inserted"
    - "Two topically related sentences can feel incoherent if no inferrable rhetorical relation links them"
    - "A text loses coherence whenever connective words like 'therefore' or 'however' are removed"
    - "Coherence requires that all sentences refer to the same discourse referent throughout"
  answer: 1
  explanation: "Coherence requires that readers be able to construct a rhetorical relation between adjacent sentences, not merely that sentences share a topic. Consider: 'She was a brilliant chef. Her father had red hair.' Both sentences could be about the same person (topically related) yet the passage is incoherent because no plausible relation can be assigned. Option A describes topical incoherence, which is a necessary but insufficient condition. Option C is wrong — coherence relations are often conveyed without explicit connectives."

- question: "The sentence pair 'He ran a marathon. He was exhausted.' conveys a causal relation even though no causal connective appears in the text."
  type: true-false
  answer: true
  explanation: "This is a central finding in coherence theory: readers automatically assign coherence relations based on world knowledge and pragmatic inference, without requiring explicit connectives. The reader knows that running a marathon causes exhaustion, and uses this to construct a causal interpretation. This implicit coherence relation is just as real and deterministic as one signaled by 'therefore' or 'as a result.' RST and related frameworks document how such relations structure entire texts, mostly without explicit marking."

- question: "A text is coherent as long as each of its sentences is grammatically well-formed and addresses the same general topic."
  type: true-false
  answer: false
  explanation: "Grammaticality and topical unity are necessary but not sufficient for coherence. A sequence of grammatically perfect, topically related sentences can still feel incoherent if no rhetorical relation can be inferred between adjacent sentences. For example: 'The concert was on Friday. The piano has 88 keys. Mozart was born in 1756.' All three sentences are grammatically correct and loosely related to music, but no interpretable relation links them. Coherence requires that adjacent segments stand in a recognizable rhetorical relationship."

- question: "Explain why removing all explicit connective words (like 'because,' 'however,' 'therefore') from a paragraph does not necessarily destroy its coherence."
  type: short-answer
  answer: "Coherence relations can be conveyed implicitly through world knowledge, pragmatic inference, and contextual cues like tense and aspect. Readers actively construct the most salient relation between adjacent sentences, drawing on knowledge about causation, event sequences, and narrative norms. Connectives are signals that make relations explicit and easier to process, but they are not the source of the relations themselves — the underlying semantic and pragmatic relationships between the propositions are what create coherence."
  explanation: "This is the key theoretical point: connectives are surface-level cues, not the deep structure of coherence. A skilled writer can create a fully coherent text with minimal connectives by arranging propositions so that their relations are inferrable. Conversely, a text that uses many connectives incorrectly (e.g., 'therefore' between two unrelated claims) can be incoherent despite heavy explicit marking. Coherence is a property of the reader's ability to construct a consistent interpretation, not of the text's surface form."
```

## Explainer

From your study of discourse analysis, you know that language above the sentence level has structure — conversations, narratives, and arguments are not random sequences of utterances but organized wholes. From discourse representation theory (DRT), you know how pronouns and definite descriptions are resolved across sentences by tracking discourse referents in a dynamic representational structure. Discourse coherence adds a further layer: not just *what* entities sentences are talking about, but *how* adjacent sentences are rhetorically related to each other. Without coherence relations, a sequence of true sentences can feel like a broken text; with them, the same sentences feel like a unified argument or narrative.

Consider a simple pair: *"Mary dropped the vase. It shattered."* You automatically interpret these sentences as causally related — the dropping caused the shattering — even though no causal connective is present. This is a **coherence relation** doing implicit work. The **elaboration** relation links a general claim to supporting detail; the **contrast** relation juxtaposes two situations that differ in an expected dimension; **narration** relates sequential events as part of a story; **explanation** gives the reason for a prior claim. Frameworks like **Rhetorical Structure Theory (RST)**, developed by Mann and Thompson, provide a systematic taxonomy of these relations, annotating how each sentence segment functions as a satellite (supporting) or nucleus (central) contribution relative to others.

The key theoretical insight is that **coherence relations are not merely described by connectives but can be conveyed without them**. "He trained hard. He won the championship" conveys a result relation. "He trained hard, but he lost" triggers a contrast-concession reading. "He trained hard. His coach was skeptical" invites an elaboration or background reading. The reader or hearer draws on world knowledge, pragmatic inference, and local context to assign the most salient relation — which is why incoherent texts are disorienting: when no plausible relation can be assigned between two sentences, comprehension breaks down. Coherence is therefore not a property of sentences in isolation but of a reader's ability to construct a globally consistent interpretation.

Understanding coherence relations has practical applications in computational linguistics, reading comprehension research, and text generation. Automatic **discourse parsers** attempt to label relations between adjacent text spans, a task that remains challenging because the same surface form can realize multiple relations depending on context, and many relations are entirely implicit. In natural language generation, a system that produces coherent multi-sentence output must plan not just the propositional content of each sentence but how each one will relate rhetorically to the next — otherwise outputs feel list-like or fragmented. The linguistic phenomenon you are studying here sits at the boundary between semantics (propositional content) and pragmatics (speaker intent and contextual interpretation), which is what makes it both theoretically rich and empirically complex.
