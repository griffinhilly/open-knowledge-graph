---
id: context-dependent-interpretation
title: Context-Dependent Interpretation
domain: language-and-communication
course: linguistics
prerequisites:
- id: linguistic-pragmatics
  type: hard
- id: compositional-semantics
  type: soft
tags:
- pragmatic enrichment
- narrowing
- loose use
- speaker meaning
- sentence meaning
stage: formal-systems
status: validated
---

# Context-Dependent Interpretation

## Core Idea
Context-dependent interpretation addresses the systematic gap between what a sentence literally means (sentence meaning) and what a speaker communicates by uttering it (speaker meaning). Pragmatic enrichment fills in underspecified elements — "I've eaten" is understood as "I've eaten today/recently," not "at some point in my life." Narrowing restricts a word's denotation contextually — "drink" at a party means alcoholic beverages, not all liquids. Loose use extends meaning beyond its literal boundaries — "Holland is flat" communicates an approximation that is useful despite being technically false for every square meter. These processes are rapid, automatic, and essential: virtually no utterance in natural conversation communicates exactly and only its compositional semantic content.

## How It's Best Learned
Collect everyday utterances and identify the gap between what was literally said and what was communicated — "The ham sandwich wants his check" in a restaurant context is a classic example. Practice distinguishing enrichment, narrowing, and loose use on the same word in different contexts (e.g., "open" in "open the door" vs. "open the wine" vs. "open person"). Compare Gricean and Relevance Theory accounts of how these processes work.

## Common Misconceptions
- Context-dependent interpretation is not sloppy or imprecise communication; it is an efficient design feature that allows a finite vocabulary to express an infinite range of meanings.
- The literal meaning of a sentence is not always its "real" or "correct" meaning — in most conversational contexts, the pragmatically enriched interpretation is the intended one.
- These processes are not conscious or effortful; listeners perform enrichment, narrowing, and loose-use calibration automatically and typically without awareness.

## Questions

```yaml
- question: "Someone says 'I've eaten' and is understood to mean 'I've eaten today' — not 'at some point in my life,' which is what the sentence literally encodes. Which process best describes what is happening?"
  type: multiple-choice
  options:
    - "Narrowing, because 'eaten' is being restricted to a shorter time frame"
    - "Loose use, because the statement is technically false for anyone who has ever skipped a meal"
    - "Pragmatic enrichment, where an underspecified element of the sentence is resolved by context into a more specific proposition"
    - "Semantic ambiguity, because the perfective aspect of 'have eaten' has two distinct meanings"
  answer: 2
  explanation: "The sentence is not ambiguous — the grammar of the English perfect tense is doing its job correctly. But the semantic content is underspecified: it truly encodes 'at some point up to now.' Context — specifically the pragmatic assumption that the speaker is responding to a relevant here-and-now question about readiness to eat — enriches this to 'recently/today.' Enrichment fills the gap between the semantically encoded skeleton and the full proposition the speaker intends to communicate. Narrowing would restrict a word's denotation; loose use would extend it beyond its literal range. This is enrichment of a temporal implicit argument."

- question: "At a cocktail party, someone asks 'Would you like a drink?' — and both parties understand this to mean an alcoholic beverage, not any liquid. A language purist objects: 'This is sloppy usage; they should say alcoholic drink.' What is wrong with this objection?"
  type: multiple-choice
  options:
    - "Nothing — the purist is correct that speakers should be more precise to avoid miscommunication"
    - "The usage is sloppy, but it's so common that it has become an accepted idiom"
    - "Narrowing is an efficient design feature: a single lexical entry is contextually restricted without requiring separate stored meanings for every situation"
    - "The objection is correct, but only for formal contexts — casual speech is exempt from precision requirements"
  answer: 2
  explanation: "Context-dependent narrowing is not a failure of precision — it is a designed efficiency. If 'drink' required a separate lexical entry for every contextual restriction (alcoholic drink, hot drink, sports drink, etc.), the mental lexicon would be unmanageably large and language acquisition impossibly complex. Instead, a single underspecified entry is deployed with contextually-salient restrictions. The word is doing exactly what it is designed to do. The 'real meaning' is not the maximally general denotation; it is whatever the context makes it appropriate to communicate. At a party, 'drink' communicates 'alcoholic drink' just as precisely as the longer phrase would."

- question: "The literal compositional meaning of a sentence is its 'real' meaning — pragmatic enrichment mainly adds optional supplementary information on top of what was actually asserted."
  type: true-false
  answer: false
  explanation: "This is a fundamental misunderstanding of how context-dependent interpretation works. In most conversational contexts, the pragmatically enriched interpretation is the intended proposition — what the speaker is actually asserting, and what the listener evaluates for truth. When someone says 'I've eaten,' they are not asserting the bare semantic content ('at some point in my life') and then additionally implying 'today.' They are asserting 'I've eaten today.' The enriched proposition is the assertion; the semantic skeleton is an intermediate step in processing, not the final product. Treating literal meaning as more 'real' than speaker meaning inverts the communicative relationship."

- question: "Pragmatic enrichment, narrowing, and loose use operate automatically and without conscious awareness in ordinary conversation."
  type: true-false
  answer: true
  explanation: "These processes are rapid and pre-conscious — listeners do not pause to deliberately analyze sentences for underspecification, then consciously add context. Psycholinguistic evidence shows that enriched interpretations are computed in real time during comprehension, typically within milliseconds, with no measurable delay relative to literal interpretation. This automaticity is part of what makes natural language communication so efficient: the cognitive work of bridging sentence meaning to speaker meaning happens below the level of awareness, freeing attention for higher-level processing of content."

- question: "Why is context-dependent interpretation described as a designed feature of natural language rather than a failure of precision? What would communication look like if every utterance had to express exactly its compositional semantic content and nothing else?"
  type: short-answer
  answer: "Context-dependent interpretation is a feature because it allows a finite vocabulary and relatively sparse grammar to generate infinitely varied, contextually precise communications. A language in which every utterance had to explicitly encode all the information communicated would require vastly larger vocabularies (separate words for 'drink-at-a-party', 'drink-when-thirsty', 'drink-medicinally'), much longer utterances, and enormous redundancy. Enrichment, narrowing, and loose use exploit shared context and pragmatic inference to compress this information: speakers leave out what context makes obvious, restrict terms to contextually salient subsets, and use approximations where precision isn't needed. Communication would be impossibly verbose and brittle without these mechanisms — any ambiguity in context would produce miscommunication because there would be no inferential system to resolve it."
  explanation: "The deeper point is that these are not failures of language but evidence of its elegant design. Natural language is an efficient code that relies on shared context as part of its decoding mechanism. The sentence meaning is not the full message — it is a compressed signal that points toward the full message, which speakers and listeners jointly reconstruct using context. This is why pragmatics is not a repair system for a broken semantics but an essential component of how language works."
```

## Explainer

From your work in linguistic pragmatics, you know that what a sentence literally encodes and what a speaker communicates are regularly different — Grice's cooperative principle governs the inferential gap. From compositional semantics, you know that sentence meaning is built systematically from word meanings and syntactic structure. Context-dependent interpretation is the territory between these two: the mechanisms by which sentence meaning gets transformed into the richer, more specific communication that speakers actually intend and listeners actually receive.

**Pragmatic enrichment** is the most pervasive mechanism. Virtually every utterance contains underspecified elements that must be resolved by context to determine what was actually communicated. "She's ready" is semantically incomplete — ready for what? "I've had breakfast" communicates "today," not "at some point in my life," even though the tense is perfective, not bounded. "It's raining" is implicitly "here, now." The semantic content of these sentences is truth-conditionally complete, but the communicated proposition is more specific. Enrichment fills in the gap between the semantic skeleton and the full proposition the speaker intends. Crucially, the enriched proposition — not the semantic skeleton — is what the speaker is asserting and what the listener evaluates for truth.

**Narrowing** restricts a word's denotation to a contextually appropriate subset. The word "drink" denotes all liquids, but at a cocktail party "would you like a drink?" means an alcoholic beverage. "She ate the whole box" typically means the entire contents, not the cardboard packaging. "Cutting" in a kitchen context means with a knife; "cutting" in a conversation about surgery means with a scalpel. The lexicon does not store a separate entry for each contextual restriction — language would be unusable if it did. Instead, a single lexical entry is deployed with a narrowed range that context makes salient. This efficiency is not imprecision; it is the designed use of underspecification.

**Loose use** works in the opposite direction, extending meaning beyond its literal boundaries while communicating something approximately or schematically true. "Holland is flat" is technically false for every square meter of the Netherlands, but it communicates useful information about the region's topography relative to mountainous alternatives. "The ATM is on the corner" may be twenty meters from the actual corner. These are not lies or mistakes — they are calibrated approximations where the speaker signals that exact truth is not the goal, approximate truth is. Relevance Theory explains loose use through scales of approximation: the speaker communicates the loosest interpretation that is informative enough for the hearer's purposes.

Together, enrichment, narrowing, and loose use explain why natural language communication is so efficient and yet so reliable. A finite lexicon and a relatively sparse grammar generate infinitely varied, contextually precise communications because each utterance comes loaded with assumptions about the situation, the speaker's goals, and what the listener already knows. The core skill in pragmatics is learning to see these processes as systematic and analyzable — not as noise in the signal, but as the signal itself.
