---
id: derivational-morphology-formal
title: Formal Analysis of Derivational Morphology
domain: language-and-communication
course: linguistics
prerequisites:
- id: derivational-morphology
  type: hard
builds-toward:
- lexical-organization-formal
tags:
- morphology
- derivation
- word-class-change
- semantics
stage: formal-systems
status: draft
---

# Formal Analysis of Derivational Morphology

## Core Idea
Derivational morphology creates new lexical entries with altered meaning or word class through affixation and reduplication. Unlike inflection, derivational rules are less productive and more semantically idiosyncratic ("run" + -er = "runner" is transparent, but "read" + -er is ambiguous). Distinguishing productive from unproductive rules explains why some derivations feel natural and others sound impossible.

## Explainer

From your prerequisite work on derivational morphology, you know that derivation creates new words by attaching affixes that often change the word class: *happy* (adjective) → *happiness* (noun), *dark* (adjective) → *darken* (verb). Formal analysis asks a harder question: what exactly are the rules governing which derivations are possible, and why do some perfectly well-formed derivations sound wrong?

The key concept is **productivity** — the degree to which a derivational rule can generate new words freely. The suffix *-er* (agentive nominalizer: turns verbs into "one who does") is highly productive: any verb can in principle become an *-er* noun — *runner*, *builder*, *compiler*, *blogger*. You can coin new *-er* words and native speakers immediately understand them. Contrast this with *-th* (forms nouns from adjectives: *warm* → *warmth*, *wide* → *width*) — this rule is nearly **unproductive**, frozen in a small set of lexical items. You cannot freely attach *-th* to new adjectives: "happyth" or "slowth" are impossible. The rule still exists in the lexicon (we can recognize its pattern), but it no longer generates new words.

What makes productivity vary? One factor is **blocking**: if a word already exists for the concept, a new derivation is blocked. You can say *runner* but not *\*runnist* — the *-ist* form is blocked because *runner* is already lexicalized. Similarly, *stole* (past tense of *steal*) blocks *\*stealed*. Blocking explains why derivational rules are more semantically **idiosyncratic** than inflectional rules: once a word exists in the lexicon, it occupies that semantic slot and prevents regular derivations from filling it.

A related asymmetry is **directionality and class-changing behavior**. Derivation typically proceeds in one direction only: *nation* → *national* → *nationality*, not *nationality* → *national* → *nation*. Each step changes word class and alters meaning in ways that are predictable in direction but not always in semantics. *Reader* from *read* is agentive and transparent; but *reader* can also mean a textbook anthology — the derivation has accumulated a second meaning through usage that formal rules cannot predict. This semantic drift distinguishes derivation from inflection, which is semantically transparent and completely regular.

Formally, derivational rules are represented in the lexicon as **word-formation rules** that specify input category, output category, the affix, and semantic content. The analysis of blocking, productivity, and semantic idiosyncrasy together explain a striking fact about natural language: speakers can generate thousands of novel words but still feel that some morphologically valid forms are impossible. The grammar that governs derivation is real — it has structure, constraints, and productive slots — but it is partial and exception-ridden in ways that purely inflectional morphology is not.
