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

## Explainer

From your study of sentence parsing and garden-path effects, you know that the parser doesn't wait until a sentence ends to begin building structure — it commits to analyses incrementally as words arrive, sometimes wrongly, triggering reanalysis. That picture assumes a parser with some kind of **working memory**: a temporary storage system that holds partial analyses, pending structures, and already-integrated words while the sentence continues. This topic is about the limits of that memory and what happens when sentences push against them.

**Working memory**, in the psycholinguistic sense, is not simply a buffer for phonological sequences — it is a resource for maintaining and manipulating linguistic representations during real-time processing. The key type of memory demand in sentence comprehension comes from **long-distance dependencies**: constructions where an element in one position is grammatically related to a position elsewhere in the sentence. In "Which book did you think the author intended to write about?", *which book* is the object of *write about*, but those two elements are separated by an entire embedded clause. The parser must hold an active representation of *which book* — a **filler** — while processing all the intervening material, searching for the corresponding **gap** position. The longer and more complex the intervening material, the more memory load the dependency imposes and the slower and more error-prone comprehension becomes.

The classic demonstration of memory limits is the contrast between **center-embedding** and **right-branching** relative clauses. The sentence "The rat the cat chased died" is grammatically well-formed but extremely difficult to parse. Its right-branching equivalent — "The rat died, and it had been chased by the cat" — is trivially easy. The difference is structural: center-embedding requires you to maintain an incomplete noun phrase (*the rat*) while processing a complete embedded clause (*the cat chased*) before you can close the matrix clause (*died*). Doubly center-embedded sentences like "The rat the cat the dog bit chased died" are effectively incomprehensible to most readers despite being perfectly grammatical — a concrete demonstration that memory capacity, not grammatical competence, is the limiting factor. Your grammar "knows" these sentences are well-formed; your working memory cannot process them.

This has important theoretical implications. **Competence** (the abstract grammatical knowledge you possess) and **performance** (what you can actually process in real time) can systematically diverge. The grammar permits unlimited center-embedding; working memory does not. This divergence is why theoretical linguists can construct sentences that are grammatically valid but psychologically impossible — and why cognitive scientists care about the specific resource limits that shape actual language use. Models of sentence comprehension must therefore incorporate both the grammatical rules that define what counts as a legal structure and the memory architecture that determines which legal structures humans can actually process. The interaction between these two — grammar and memory — is where much of contemporary psycholinguistics lives.
