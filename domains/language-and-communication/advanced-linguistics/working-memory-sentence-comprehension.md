---
id: working-memory-sentence-comprehension
title: Working Memory in Sentence Comprehension
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: sentence-parsing-garden-paths
  type: hard
- id: psycholinguistics-intro
  type: soft
tags:
- psycholinguistics
- memory
- comprehension
stage: advanced
status: draft
---

# Working Memory in Sentence Comprehension

## Core Idea
Comprehending sentences requires maintaining syntactic and semantic information in working memory. Long dependencies—gaps between fillers and positions, as in 'Which book did you think the author intended to write about?'—impose memory load. Comprehension difficulty increases with dependency length and multiplicity, explaining why center-embedded clauses are harder than right-embedding, revealing memory constraints on real-time processing.

## Questions

```yaml
- question: "A native English speaker reads 'The rat the cat chased died' slowly and carefully but still finds it difficult to parse. She reads 'The cat chased a rat, and it died' with no difficulty. Both sentences are grammatically correct and describe the same event. What best explains the processing difference?"
  type: multiple-choice
  options:
    - "The first sentence uses passive voice, which is harder to process than active voice"
    - "Center-embedding requires holding an incomplete noun phrase ('the rat') in working memory while processing a full embedded clause before the matrix verb can be resolved — exceeding normal working memory capacity"
    - "The first sentence contains a garden-path effect where 'chased' is initially misread as a past-tense main verb"
    - "The second sentence uses a simpler vocabulary, reducing lexical processing demands"
  answer: 1
  explanation: "Both sentences use active voice and identical vocabulary. The difference is structural: 'The rat the cat chased died' is a center-embedded relative clause — the relative clause ('the cat chased') is embedded inside the matrix clause ('The rat… died'), forcing the reader to hold an unresolved noun phrase in working memory while processing the embedded material. Right-branching constructions ('The cat chased a rat, and it died') resolve the matrix clause first, minimizing memory load. The difficulty is not about vocabulary, voice, or garden-path reanalysis — it is about working memory capacity under structural dependency."

- question: "In processing 'Which book did you think the author intended to write about?', what memory demand does 'which book' impose on the parser?"
  type: multiple-choice
  options:
    - "It must be stored as a semantic concept because its meaning is ambiguous until the end of the sentence"
    - "It functions as a filler that must be kept active in working memory while the parser searches through intervening embedded clauses for the corresponding gap position"
    - "It triggers a garden-path effect because 'which' initially signals a question about the subject rather than the object"
    - "No special memory demand — the parser resolves 'which book' immediately and moves on"
  answer: 1
  explanation: "Wh-movement constructions create long-distance filler-gap dependencies: 'which book' is the filler — a displaced element that must be linked to a gap elsewhere in the structure (the object position of 'write about'). The parser must keep an active representation of 'which book' throughout the entire intervening string ('did you think the author intended to write about') while scanning for where it semantically fits. The longer and more deeply embedded the intervening material, the greater the memory load and the slower/more error-prone comprehension becomes. This is a core finding in psycholinguistics: dependency length predicts processing difficulty."

- question: "Sentences that are difficult for native speakers to comprehend, such as doubly center-embedded sentences, reveal gaps in their grammatical competence — they don't know the rules for those constructions."
  type: true-false
  answer: false
  explanation: "False. This conflates competence with performance. Grammatical competence — the abstract internalized knowledge of a language's rules — is distinct from performance, which is what you can actually process under real-time cognitive constraints. When presented with 'The rat the cat the dog bit chased died,' most native speakers recognize upon analysis that it is grammatically well-formed and can identify the correct interpretation if given enough time. The difficulty is not ignorance of the rule; it is a working memory bottleneck that prevents real-time processing. The grammar permits unlimited center-embedding; working memory creates the ceiling."

- question: "Because working memory limits are universal cognitive constraints, the difficulty of center-embedded sentences is roughly equal across all languages and grammatical structures."
  type: true-false
  answer: false
  explanation: "False. While working memory capacity is a universal constraint, languages differ in how they organize dependencies, and the same memory load can be distributed differently across a sentence. Some languages allow pro-drop or use morphological marking that reduces the need to hold fillers actively; others have head-final structures that create different dependency profiles. The center-embedding vs. right-branching contrast is most striking in English and similarly structured languages. Psycholinguists study cross-linguistic variation in processing difficulty to understand exactly how grammar and memory interact — and languages with different word orders often show different processing profiles for structurally equivalent sentences."

- question: "What is the key theoretical distinction between linguistic competence and linguistic performance, and why does the study of working memory in sentence comprehension make this distinction unavoidable?"
  type: short-answer
  answer: "Linguistic competence is abstract knowledge — the internalized system of grammatical rules that defines which sentences are well-formed. Performance is the actual real-time processing of language under cognitive constraints including working memory limits, attention, and processing speed. The distinction is unavoidable in working memory research because center-embedded sentences are both grammatically well-formed (competence says 'legal') and effectively incomprehensible in real time (performance says 'fails'). A theory that conflates the two cannot explain this divergence. Any adequate theory of language must specify both the grammatical rules (what is legal) and the resource architecture (what is actually processable) — and account for cases where they come apart."
  explanation: "Chomsky's competence/performance distinction was originally motivated partly by observations like this: the grammatical system is idealized and unlimited, but actual speakers process under real constraints. Psycholinguistics lives in the performance space — it studies the mechanisms by which competence knowledge is deployed in real time. Working memory research has been particularly productive because it identifies a specific, measurable resource that creates systematic gaps between what the grammar allows and what humans can actually process."
```

## Explainer

From your study of sentence parsing and garden-path effects, you know that the parser doesn't wait until a sentence ends to begin building structure — it commits to analyses incrementally as words arrive, sometimes wrongly, triggering reanalysis. That picture assumes a parser with some kind of **working memory**: a temporary storage system that holds partial analyses, pending structures, and already-integrated words while the sentence continues. This topic is about the limits of that memory and what happens when sentences push against them.

**Working memory**, in the psycholinguistic sense, is not simply a buffer for phonological sequences — it is a resource for maintaining and manipulating linguistic representations during real-time processing. The key type of memory demand in sentence comprehension comes from **long-distance dependencies**: constructions where an element in one position is grammatically related to a position elsewhere in the sentence. In "Which book did you think the author intended to write about?", *which book* is the object of *write about*, but those two elements are separated by an entire embedded clause. The parser must hold an active representation of *which book* — a **filler** — while processing all the intervening material, searching for the corresponding **gap** position. The longer and more complex the intervening material, the more memory load the dependency imposes and the slower and more error-prone comprehension becomes.

The classic demonstration of memory limits is the contrast between **center-embedding** and **right-branching** relative clauses. The sentence "The rat the cat chased died" is grammatically well-formed but extremely difficult to parse. Its right-branching equivalent — "The rat died, and it had been chased by the cat" — is trivially easy. The difference is structural: center-embedding requires you to maintain an incomplete noun phrase (*the rat*) while processing a complete embedded clause (*the cat chased*) before you can close the matrix clause (*died*). Doubly center-embedded sentences like "The rat the cat the dog bit chased died" are effectively incomprehensible to most readers despite being perfectly grammatical — a concrete demonstration that memory capacity, not grammatical competence, is the limiting factor. Your grammar "knows" these sentences are well-formed; your working memory cannot process them.

This has important theoretical implications. **Competence** (the abstract grammatical knowledge you possess) and **performance** (what you can actually process in real time) can systematically diverge. The grammar permits unlimited center-embedding; working memory does not. This divergence is why theoretical linguists can construct sentences that are grammatically valid but psychologically impossible — and why cognitive scientists care about the specific resource limits that shape actual language use. Models of sentence comprehension must therefore incorporate both the grammatical rules that define what counts as a legal structure and the memory architecture that determines which legal structures humans can actually process. The interaction between these two — grammar and memory — is where much of contemporary psycholinguistics lives.
