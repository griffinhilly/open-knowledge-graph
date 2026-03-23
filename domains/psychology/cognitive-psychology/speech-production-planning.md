---
id: speech-production-planning
title: Speech Production and Articulation Planning
domain: psychology
course: cognitive-psychology
prerequisites:
- id: language-production
  type: hard
- id: primary-motor-cortex-motor-representation
  type: soft
tags:
- language
- speech
- production
- planning
stage: formal-systems
status: draft
---

# Speech Production and Articulation Planning

## Core Idea
Speech production requires planning at multiple levels: conceptual planning (what to say), grammatical encoding (how to structure it), and phonetic encoding (how to pronounce it). Speech errors like spoonerisms and malapropisms reveal distinct processing stages and the normal mechanisms by which sounds are selected and sequenced.

## Questions

```yaml
- question: "A person knows the meaning of the word they want to say, its grammatical category, and even its first letter and rough syllable count — but cannot retrieve the full pronunciation. Which stage of lexical access has succeeded and which has failed?"
  type: multiple-choice
  options:
    - "Both lemma and lexeme retrieval have succeeded; this is a working memory failure"
    - "Lemma retrieval has succeeded but lexeme retrieval has failed — the classic tip-of-the-tongue state"
    - "Lexeme retrieval has succeeded but lemma retrieval has failed, leaving an empty sound without meaning"
    - "Neither stage has completed; the word is simply not in the person's vocabulary"
  answer: 1
  explanation: "The tip-of-the-tongue phenomenon is the key evidence for a two-stage model. The lemma encodes meaning, syntactic properties, grammatical category, and partial phonological information (first letter, syllable count). When lemma retrieval succeeds but lexeme retrieval fails, exactly this partial information is available. Option C is the reverse — it describes retrieving a form without access to meaning, which is not what tip-of-the-tongue looks like."

- question: "A speaker says 'tips of the slung' instead of 'tips of the tongue.' What does this spoonerism reveal about speech planning?"
  type: multiple-choice
  options:
    - "Phonological encoding occurs word-by-word in strict sequence, and the error reflects an isolated encoding failure for 'tongue'"
    - "Speech is planned across multiple words simultaneously, allowing phonological segments from different words to interact and transpose"
    - "The speaker retrieved the wrong lemma, selecting a semantically related word"
    - "Articulation programs for 'sl-' and 'st-' are stored in adjacent locations in motor cortex and were co-activated"
  answer: 1
  explanation: "Spoonerisms — transpositions of sounds across words — are only possible if the phonological segments of multiple upcoming words are active in the planning buffer at the same time. If encoding proceeded strictly word-by-word, the segment from 'tongue' could not interfere with 'tips.' This is the primary evidence that speech planning has a multi-word window. Option C describes a semantic substitution (wrong lemma), not a spoonerism (transposed phonemes)."

- question: "Introducing an artificial delay or pitch shift in a speaker's auditory feedback disrupts speech fluency, demonstrating that auditory monitoring is integrated into articulatory control — not just a post-hoc check."
  type: true-false
  answer: true
  explanation: "The forward model of motor control predicts sensory consequences of planned movements before they occur. Speakers continuously compare predicted and actual auditory feedback. When the feedback is artificially delayed or shifted, the mismatch between prediction and input disrupts the ongoing motor control process, causing stuttering, prolonged sounds, or altered pitch — evidence that auditory prediction is embedded in real-time articulation, not merely reviewed after speech ends."

- question: "Malapropisms (e.g., substituting 'pacific' for 'specific') arise from the same level of processing as semantic substitutions (e.g., substituting 'cat' for 'dog')."
  type: true-false
  answer: false
  explanation: "Malapropisms occur at the lexeme level: a phonologically similar word is retrieved instead of the target, indicating competition among phonological neighbors in the sound-encoding stage. Semantic substitutions occur at the lemma level: a semantically related word wins the lexical selection competition before any phonological encoding occurs. The two error types reveal distinct processing stages — semantic substitutions tell us about meaning-based competition; malapropisms tell us about sound-form competition."

- question: "Why does the tip-of-the-tongue phenomenon support a two-stage model of lexical access rather than a single-stage model?"
  type: short-answer
  answer: "In a single-stage model, either you retrieve the word or you don't — there would be no intermediate state with partial information. Tip-of-the-tongue states show that speakers can successfully access a word's meaning, grammatical category, and partial phonological form (first letter, syllable count) while failing to retrieve the complete phonological form. This pattern of partial access — exactly the split predicted if lexical retrieval has two stages (lemma, then lexeme) — cannot be explained by a single unified retrieval step."
  explanation: "The tip-of-the-tongue phenomenon is one of the most powerful pieces of evidence in psycholinguistics because it is a naturally occurring experiment: it reveals which properties of a word are accessible without full retrieval. The lemma-lexeme distinction predicts exactly the pattern observed — semantic and grammatical properties (lemma) succeed while phonological form (lexeme) fails."
```

## Explainer

When you produce a sentence, you are not simply converting a thought into sound — you are executing a tightly coordinated cascade of planning operations, each operating at a different level of abstraction, on a timescale measured in hundreds of milliseconds. Levelt's influential model of speech production identifies three broad stages. **Conceptualization** produces a preverbal message: the intention and its propositional content, before any linguistic form is selected. **Formulation** translates the preverbal message into a linguistic plan, subdividing into grammatical encoding (selecting words and building syntactic structure) and phonological encoding (assembling the sound sequence). **Articulation** executes the motor plan. Your prior work on language production gives you the macro-level picture; what this topic adds is the fine-grained mechanisms within formulation and articulation planning, and the evidence from errors.

**Lexical selection** — choosing the right word — occurs in two steps. First, **lemma** retrieval: the appropriate word is identified at an abstract lexical level that captures its meaning and syntactic properties (its grammatical category, whether it is transitive, its gender in languages that have it) without yet specifying its phonological form. Then **lexeme** retrieval adds the phonological encoding. Evidence for this two-step architecture comes from the **tip-of-the-tongue phenomenon**: you know the word's meaning and syntactic properties, you may know its first letter and number of syllables — the lemma is retrieved — but the lexeme (full phonological form) is temporarily unavailable. The partial information that is accessible in tip-of-the-tongue states reflects exactly the properties associated with the lemma level.

Speech errors are the primary experimental tool for revealing the architecture of this planning process, because errors show which units can interact with which other units. **Spoonerisms** (transpositions of phonological segments: "tips of the slung" for "tips of the tongue") show that phonological segments are planned as units and that segments from different words can exchange with each other within a planning window — demonstrating that speech is planned ahead, across multiple words simultaneously. **Semantic substitutions** (substituting "table" for "chair" or "cat" for "dog") show that lexical retrieval involves competition among semantically related words, any of which can be incorrectly selected if the target is not sufficiently activated. **Malapropisms** (substituting a word with a similar sound: "for all intensive purposes") occur at the lexeme level, where phonological neighbors can be retrieved instead of the target.

Connecting to your knowledge of primary motor cortex, articulation planning involves not only the sequential ordering of phonological units but also the preparation of the motor programs that drive the vocal tract. The **forward model** of motor control — in which the brain predicts the sensory consequences of a planned movement and uses prediction error to update the motor command — applies here as much as in limb movements. Speakers continuously monitor their own speech output (both via auditory feedback and efference copy) and can detect and correct errors in real time. Disrupting auditory feedback (by introducing a delay or shift in the pitch of heard speech) characteristically disrupts speech fluency, demonstrating that auditory prediction is integrated into articulatory control, not merely a post-hoc check on what was said.

