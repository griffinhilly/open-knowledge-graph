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
status: validated
---

# Formal Analysis of Derivational Morphology

## Core Idea
Derivational morphology creates new lexical entries with altered meaning or word class through affixation and reduplication. Unlike inflection, derivational rules are less productive and more semantically idiosyncratic ("run" + -er = "runner" is transparent, but "read" + -er is ambiguous). Distinguishing productive from unproductive rules explains why some derivations feel natural and others sound impossible.

## Questions

```yaml
- question: "Why is the form '*stealed' unacceptable as the past tense of 'steal,' even though the suffix -ed is a highly productive past-tense marker in English?"
  type: multiple-choice
  options:
    - "The -ed suffix cannot attach to monosyllabic verbs like 'steal'"
    - "The existing irregular form 'stole' blocks the regular derivation by already occupying that semantic slot"
    - "'Stealed' violates phonological rules because -ed cannot follow a liquid consonant like /l/"
    - "The -ed suffix is only productive for recently borrowed verbs, not native Germanic words"
  answer: 1
  explanation: "This is blocking. Once a lexical item ('stole') exists for a particular meaning (past tense of steal), a new derivation (*stealed) is blocked from filling that slot — two forms cannot compete for the same semantic position in a mature lexicon. The same principle explains '*goed' (blocked by 'went') and '*gooder' (blocked by 'better'). Blocking is the key mechanism explaining why derivational rules, even productive ones, are not freely applicable: existing lexical items preempt new derivations."

- question: "A linguist observes that the suffix -th (warm→warmth, wide→width) cannot be attached to new adjectives like 'happy' or 'slow' to form 'happyth' or 'slowth.' What does this illustrate?"
  type: multiple-choice
  options:
    - "The suffix -th is not a real derivational morpheme — 'warmth' and 'width' are monomorphemic"
    - "English phonology prevents -th from attaching to adjectives ending in vowels or certain consonants"
    - "-th is an unproductive derivational rule: its pattern is recognizable in the lexicon but it no longer generates new words"
    - "-th is blocked by competing suffixes like -ness and -ity, which are preferred for all new derivations"
  answer: 2
  explanation: "-th is a nearly frozen rule — its pattern is detectable (linguists can identify it as a nominalizing suffix), but it no longer generates new words freely. Productivity exists on a spectrum: -er (agentive) is highly productive and coins new words freely; -th is lexicalized in a small closed set. Phonological explanation is tempting but wrong: 'happy' and 'slow' have no phonological problem that would block -th attachment — the rule is simply unproductive. This spectrum of productivity is central to formal morphological analysis."

- question: "Because the suffix -er is highly productive, any word formed with it will have a predictable, transparent meaning: 'one who does X.'"
  type: true-false
  answer: false
  explanation: "False. High productivity means a rule can generate many new words, but it does not guarantee semantic transparency. 'Reader' can mean 'one who reads' (agentive, transparent) but also 'an anthology of assigned texts' — a meaning accumulated through usage that the derivational rule cannot predict. 'Programmer' may refer to a person or a software component. Semantic drift and idiosyncrasy accumulate as derived words become lexicalized. This is precisely what distinguishes derivation from inflection, which is semantically transparent and completely regular."

- question: "Blocking occurs when an existing lexical item occupies the semantic slot that a new derivation would fill, preventing the derived form from entering the language."
  type: true-false
  answer: true
  explanation: "True. Blocking is a key constraint on derivational productivity. The principle: two forms cannot coexist in competition for exactly the same meaning in a single lexicon. 'Stealer' is generable by the -er rule but competes with 'thief,' which already occupies much of that semantic space, limiting its use. More cleanly: '*goed' is blocked by 'went,' and '*betterness' is largely blocked by 'improvement.' Blocking explains much of the apparent irregularity in derivational morphology — not that rules fail, but that existing lexical items preempt them."

- question: "What is the key difference between inflectional morphology and derivational morphology in terms of productivity and semantic predictability, and what accounts for this difference?"
  type: short-answer
  answer: "Inflectional morphology is fully productive and semantically transparent: every eligible word takes every inflection (all regular verbs take -ed for past tense) and the meaning is always predictable. Derivational morphology is partially productive and semantically idiosyncratic: rules apply only to some words (blocked by existing lexical items), and derived words often accumulate meanings the rule cannot predict. The difference arises because derived words become independent lexical entries subject to semantic drift, while inflected forms remain functionally bound to their base."
  explanation: "The key mechanism is lexicalization: once a derived form enters the lexicon as an established word, it takes on a life of its own — accumulating new meanings, narrowing or broadening, and potentially blocking new derivations. Inflected forms don't do this: 'walked' never develops an independent meaning distinct from 'walk + past tense.' Derivation creates new words; inflection creates grammatical variants of the same word. This distinction means derivational rules must contend with the existing lexicon in ways inflectional rules do not, producing messier productivity patterns."
```

## Explainer

From your prerequisite work on derivational morphology, you know that derivation creates new words by attaching affixes that often change the word class: *happy* (adjective) → *happiness* (noun), *dark* (adjective) → *darken* (verb). Formal analysis asks a harder question: what exactly are the rules governing which derivations are possible, and why do some perfectly well-formed derivations sound wrong?

The key concept is **productivity** — the degree to which a derivational rule can generate new words freely. The suffix *-er* (agentive nominalizer: turns verbs into "one who does") is highly productive: any verb can in principle become an *-er* noun — *runner*, *builder*, *compiler*, *blogger*. You can coin new *-er* words and native speakers immediately understand them. Contrast this with *-th* (forms nouns from adjectives: *warm* → *warmth*, *wide* → *width*) — this rule is nearly **unproductive**, frozen in a small set of lexical items. You cannot freely attach *-th* to new adjectives: "happyth" or "slowth" are impossible. The rule still exists in the lexicon (we can recognize its pattern), but it no longer generates new words.

What makes productivity vary? One factor is **blocking**: if a word already exists for the concept, a new derivation is blocked. You can say *runner* but not *\*runnist* — the *-ist* form is blocked because *runner* is already lexicalized. Similarly, *stole* (past tense of *steal*) blocks *\*stealed*. Blocking explains why derivational rules are more semantically **idiosyncratic** than inflectional rules: once a word exists in the lexicon, it occupies that semantic slot and prevents regular derivations from filling it.

A related asymmetry is **directionality and class-changing behavior**. Derivation typically proceeds in one direction only: *nation* → *national* → *nationality*, not *nationality* → *national* → *nation*. Each step changes word class and alters meaning in ways that are predictable in direction but not always in semantics. *Reader* from *read* is agentive and transparent; but *reader* can also mean a textbook anthology — the derivation has accumulated a second meaning through usage that formal rules cannot predict. This semantic drift distinguishes derivation from inflection, which is semantically transparent and completely regular.

Formally, derivational rules are represented in the lexicon as **word-formation rules** that specify input category, output category, the affix, and semantic content. The analysis of blocking, productivity, and semantic idiosyncrasy together explain a striking fact about natural language: speakers can generate thousands of novel words but still feel that some morphologically valid forms are impossible. The grammar that governs derivation is real — it has structure, constraints, and productive slots — but it is partial and exception-ridden in ways that purely inflectional morphology is not.
