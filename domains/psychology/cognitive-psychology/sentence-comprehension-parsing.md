---
id: sentence-comprehension-parsing
title: Sentence Comprehension and Parsing
domain: psychology
course: cognitive-psychology
prerequisites:
- id: word-recognition-lexical-access
  type: hard
- id: syntax-and-grammar-acquisition
  type: hard
builds-toward:
- mental-model-construction
tags:
- language
- comprehension
- parsing
- syntax
stage: formal-systems
status: draft
---

# Sentence Comprehension and Parsing

## Core Idea
Sentence comprehension involves parsing grammatical structure and integrating meaning. Garden-path sentences reveal that parsing is not always optimal: readers initially commit to one structural interpretation, then must revise when encountering contradictory information. This demonstrates the role of expectancy and immediate processing in comprehension.

## Explainer

From your word recognition prerequisite, you know how the mind accesses individual words from the mental lexicon — recognizing form, retrieving meaning, and activating syntactic information within a few hundred milliseconds. But understanding language involves far more than recognizing words in sequence: the meaning of a sentence is not a sum of word meanings, but a function of *structure*. "The dog bit the man" and "The man bit the dog" use the same words to mean different things. **Parsing** is the process of assigning grammatical structure to incoming words — identifying which noun phrase is the subject, which verb is the main verb, which clause modifies which — and doing so incrementally as each word arrives, before the sentence is complete.

The **garden-path effect** is the signature phenomenon showing that parsing commits to one interpretation immediately rather than waiting for more information. Consider: *"The horse raced past the barn fell."* Most readers stumble at "fell" — this is a grammatically correct sentence (reduced relative clause: "The horse [that was] raced past the barn fell"), but the parser had committed to analyzing "raced" as the main verb, not as a participle. When "fell" arrives and is uninterpretable under the initial analysis, the parser must **reanalyze** — a cognitively effortful, time-consuming process that produces characteristic delays measurable in eye-tracking studies as longer fixation times and regressions (backward re-reading). The reader was led down the garden path by the parser's initial (wrong) commitment. Simple examples include: *"The old man the boats"* (where "man" is the verb) or *"Fat people eat accumulates"* (where "eat" is not the main verb).

The core theoretical debate is between **syntax-first (serial) models** and **interactive models**. Syntax-first models (Frazier's garden-path theory) claim that the parser uses only syntactic information to build an initial structure — it applies heuristics like "minimal attachment" (attach each new word with the fewest syntactic nodes) and ignores semantic plausibility and contextual information until structural analysis is complete. If the initial structure fails, reanalysis follows. Interactive models claim that the parser uses all available information simultaneously — syntax, semantics, plausibility, frequency of structural patterns, and discourse context — and so rarely commits to an unambiguously wrong interpretation when plausible alternatives are available. The evidence favors a nuanced middle ground: syntax does constrain early parsing, but discourse context and lexical probabilities (knowing that "raced" rarely introduces a relative clause) bias the initial analysis and can prevent garden-pathing in rich enough contexts.

Working memory plays a crucial role in parsing complex structures. **Center-embedded sentences** — those with a relative clause that interrupts the main clause, which can itself be interrupted — rapidly exceed parsing capacity: "The reporter [that the senator [that the lobbyist attacked] praised] wrote the story." Understanding this sentence requires keeping the first subject ("reporter") available across two interrupting clauses before the main verb ("wrote") finally arrives. Capacity-limited working memory is why center-embedding beyond one or two levels becomes nearly incomprehensible even for speakers who understand all the words and know the grammatical rules. This connects your syntax knowledge to the working memory model: parsing is an on-line process that must hold partially built structures in working memory while integrating each new word, and the same capacity constraints that limit other cognitive operations limit comprehension of structurally complex language.
