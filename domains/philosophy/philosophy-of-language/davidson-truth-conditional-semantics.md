---
id: davidson-truth-conditional-semantics
title: Davidson's Truth-Conditional Semantics
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: reference-determination
  type: hard
builds-toward:
- compositionality-principle
- pragmatics-semantics-boundary
tags:
- Davidson
- truth-conditional
- semantics
- meaning
stage: abstract-reasoning
status: draft
---

# Davidson's Truth-Conditional Semantics

## Core Idea
Davidson proposed that the meaning of a sentence is its truth-condition—what would have to be the case for the sentence to be true. A sentence is meaningful if we can specify its truth-conditions. Understanding 'Snow is white' requires knowing that it's true iff snow is white. Truth-conditional semantics provides a systematic, compositional account of meaning, where sentence meaning is determined by the meanings of parts and their mode of combination.

## How It's Best Learned
Consider simple examples ('Snow is white,' 'The cat is on the mat') and specify their truth-conditions formally. Then see how truth-conditions compose from parts. Explore the limits: some sentences (commands, questions, moral claims) seem to have no truth-conditions.

## Common Misconceptions
Truth-conditional semantics is about what sentences express psychologically—it's about what sentences are true under, an objective relational fact. All meaningful sentences have truth-conditions—this is contentious for imperatives, questions, and non-factual discourse.

## Questions

```yaml
- question: "According to Davidson's truth-conditional semantics, what does it mean to understand the sentence 'The Eiffel Tower is in Paris'?"
  type: multiple-choice
  options:
    - "To know what mental images or feelings the sentence evokes in a competent speaker"
    - "To know the communicative intention behind the sentence in its context of use"
    - "To know under what conditions the sentence is true — that it is true if and only if the Eiffel Tower is in Paris"
    - "To be able to identify the reference of 'the Eiffel Tower' but not necessarily connect it to a truth condition"
  answer: 2
  explanation: "Davidson's core claim is that meaning = truth condition. To understand a sentence is to know its T-sentence: the biconditional specifying what worldly conditions make it true. Option A (mental images) is the psychological view Davidson explicitly rejects — truth-conditional semantics is about objective relational facts, not psychological states. Option B (communicative intention) is closer to Gricean pragmatics, not Davidsonian semantics."

- question: "Davidson's framework faces a challenge from imperative sentences like 'Close the door!' because they seem to lack truth-conditions. How should a truth-conditional theorist best respond?"
  type: multiple-choice
  options:
    - "Deny that imperatives are meaningful — only truth-apt sentences can have meaning"
    - "Argue that imperatives have truth-conditions: 'Close the door' is true when the door is closed"
    - "Either extend the framework creatively, argue imperatives reduce to truth-apt forms, or concede they fall outside the theory's scope"
    - "Abandon truth-conditional semantics entirely and adopt a purely pragmatic account of all meaning"
  answer: 2
  explanation: "Option C correctly identifies the theorist's options as Davidson's framework presents them: extend, reduce, or acknowledge scope limits. Option B commits a confusion — 'Close the door' is not true or false in the normal sense; a closed door fulfills the imperative but does not verify it as a proposition. Option A would wrongly exclude clearly meaningful speech acts. The limits of the theory are genuine, and acknowledging them clearly is more rigorous than pretending they don't exist."

- question: "Davidson's truth-conditional semantics holds that understanding a sentence requires knowing what mental state or psychological experience it expresses in a competent speaker."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic explicitly corrects. Truth-conditional semantics is NOT about psychological expression — the Core Idea states it directly: 'Truth-conditional semantics is about what sentences are true under, an objective relational fact.' A T-sentence like \"'Snow is white' is true iff snow is white\" makes no reference to mental states. Meaning is located in the condition under which the sentence holds, not in any speaker's psychology."

- question: "On Davidson's account, the truth-condition of a complex sentence like 'The cat is on the mat' is derived systematically from the meanings of its parts and how they are combined."
  type: true-false
  answer: true
  explanation: "This is compositionality — the key payoff of the Davidsonian framework. 'The cat is on the mat' is true iff the individual picked out by 'the cat' stands in the on-the-mat relation to the object picked out by 'the mat.' The truth-condition of the whole is built recursively from the references of its parts and the structure of the sentence, explaining how finite speakers can understand infinitely many sentences they have never encountered before."

- question: "What is a 'T-sentence' in Davidson's framework, and why does he use truth-conditions rather than ideas or images to explain meaning?"
  type: short-answer
  answer: "A T-sentence is a biconditional of the form: 'S' is true if and only if p — where p gives the worldly condition under which sentence S holds. Davidson uses truth-conditions because they are objective (not private to any speaker), compositional (derivable systematically from parts), and precise — they explain how finite learners master an infinite range of sentences."
  explanation: "Meaning as ideas or images would make semantics private and unverifiable — two speakers could never confirm they mean the same thing. Truth-conditions are publicly accessible: we can all observe whether the Eiffel Tower is in Paris. This objectivity is essential to Davidson's project of giving a rigorous, communicable theory of how language works. The T-sentence format also builds directly into compositionality, which is why it became the foundation for subsequent formal semantics."
```

## Explainer

You already understand reference determination — how names and terms latch onto things in the world. Davidson's truth-conditional semantics builds on this to answer the harder question: how does a whole sentence mean what it means? The key insight is that the meaning of a sentence just *is* the condition under which it is true. To understand "Snow is white" is to know that it is true if and only if snow is white. This seems trivially obvious — but Davidson's program makes it theoretically powerful by demanding that we explain, systematically, how the truth-condition of any sentence derives from the meanings of its parts.

The philosophical tool Davidson borrowed is Tarski's **Convention T**: an adequate theory of truth for a language must entail, for every sentence S, a biconditional of the form "'S' is true if and only if p" — where p is the translation of S into the language we're using to do theory. For English, this gives us: "'Snow is white' is true iff snow is white." Tarski intended this for formal languages; Davidson proposed using it as the core of a **meaning theory** for natural language. The radical idea is that knowing the meaning of a sentence is knowing its T-sentence: the biconditional that specifies under what worldly conditions the sentence holds. There is no further semantic entity — no meaning-object, no proposition in some Platonic realm — that the sentence "expresses." Meaning is fully explained by truth-conditions.

The payoff is **compositionality**. The truth-condition of a complex sentence is systematically derived from the truth-conditions of its parts and how they are combined. "The cat is on the mat" is true iff the individual referred to by "the cat" stands in the on-the-mat relation to the object referred to by "the mat." The semantics unfolds recursively: sentences build from predicates and names according to rules that preserve the truth-conditional output. This is why Davidson's framework plugs directly into the compositionality principle — the systematicity of language is explained by the compositional structure of truth-conditions.

The limits of the framework are instructive. **Imperatives** ("Close the door!"), **questions** ("Is the cat on the mat?"), and arguably **moral claims** ("You ought to keep your promise") don't seem to be true or false in the same way — they are not straightforwardly truth-apt. A strict truth-conditional semanticist must either extend the framework creatively, argue these reduce to truth-apt forms, or concede they fall outside the theory's scope. The boundary between semantics and pragmatics also comes under pressure: much of what a sentence communicates is not captured by its truth-condition alone — implicatures, presuppositions, and context-dependence all require additional explanation. Davidson's framework gives you the foundation; these challenges push you toward the frontiers of philosophy of language.
