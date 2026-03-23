---
id: prefix-suffix-affixation
title: Prefix and Suffix Affixation
domain: language-and-communication
course: linguistics
prerequisites:
- id: morpheme-types
  type: hard
- id: morphological-structure
  type: hard
builds-toward:
- derivational-morphology
tags:
- morphology
- affixes
- word-formation
- morphophonology
stage: formal-systems
status: validated
---

# Prefix and Suffix Affixation

## Core Idea
Prefix and suffix affixation are the two most common affix types, attaching to the beginning or end of roots or stems. Affixes interact with stress patterns, phonotactic constraints, and semantic/grammatical properties of bases. Prefixes and suffixes differ in productivity, multiple attachment, and semantic transparency across and within languages.

## Questions

```yaml
- question: "What is the correct morphological structure of the word 'unhappiness'?"
  type: multiple-choice
  options:
    - "[[un-happy]-ness] — un- attaches first, then -ness attaches to the adjective unhappy"
    - "[un-[happy-ness]] — -ness attaches first, then un- attaches to the noun unhappiness"
    - "[un-happy-ness] — all three morphemes attach simultaneously to the root"
    - "Either order is grammatical — prefixes and suffixes can attach in any sequence"
  answer: 0
  explanation: "The structure must be [[un-happy]-ness] because -ness selects for adjective bases. un- first attaches to the adjective happy to form the adjective unhappy; then -ness attaches to the adjective unhappy to form the noun unhappiness. The alternative [un-[happiness]] would require un- to attach to a noun, but un- does not productively attach to nouns in English — *unhappiness as an input to un- is ungrammatical. The category-changing property of -ness forces this inside-out ordering."

- question: "Which of the following best illustrates the key asymmetry between prefixes and suffixes in English?"
  type: multiple-choice
  options:
    - "Prefixes are always more productive than suffixes in generating new words"
    - "Suffixes typically change the grammatical category of the base; prefixes typically preserve it"
    - "Prefixes attach only to nouns; suffixes attach to verbs and adjectives"
    - "Suffixes are borrowed from Latin while prefixes are native Germanic morphemes"
  answer: 1
  explanation: "This is the core asymmetry: -ness turns dark (adjective) into darkness (noun) — a category change. un- turns happy (adjective) into unhappy (still an adjective) — category preserved. This asymmetry has deep consequences: suffixes do the syntactic heavy lifting in derivation, determining what grammatical role the new word plays in a sentence. Prefixes modify meaning while leaving the word's category — and therefore its syntactic behavior — unchanged. Option A is false: suffixes are generally more productive in English. Option C oversimplifies: both attach to multiple categories."

- question: "The productivity of an affix can be restricted by the phonological properties of the base it attaches to."
  type: true-false
  answer: true
  explanation: "This is correct and well-illustrated by the contrast between -ity and -ness. The suffix -ity strongly prefers Latinate bases (probability, felicity) and sounds unnatural with Germanic ones (*hardity, *sadity). The suffix -ness is productive across both Germanic and Latinate bases (hardness, sadness, brightness). These restrictions reflect the phonological contexts and etymological strata in which each affix originally developed. An affix's productivity is not uniform across all possible bases — it is shaped by both sound-structure requirements and the etymological history of the vocabulary."

- question: "Prefixes and suffixes are equally likely to change the grammatical category of the base they attach to."
  type: true-false
  answer: false
  explanation: "In English, this is clearly false: suffixes far more commonly change grammatical category (dark → darkness, adjective to noun; terror → terrify, noun to verb), while prefixes almost always preserve the category of the base (happy → unhappy, both adjectives; write → rewrite, both verbs). This asymmetry holds broadly across English derivational morphology. Suffixes are described as 'morphologically more powerful' precisely because they determine the syntactic category of the derived word — something prefixes typically do not do."

- question: "Why does the category-changing property of suffixes constrain the order in which multiple suffixes can be stacked?"
  type: short-answer
  answer: "Each suffix selects for a specific grammatical category in its base. Since suffixes change category, the output category of one suffix must match the input category requirement of the next, forcing strict inside-out ordering. For example, -ize attaches to nouns and adjectives to form verbs (modern → modernize); then -ation attaches to verbs to form nouns (modernize → modernization). The reverse order *-ation-ize would require -ize to attach to a noun, violating its selectional restrictions. Each suffix creates a category that determines what can attach next, forming a dependency chain that constrains the order of all further derivation."
  explanation: "This is why morphological structure must be analyzed hierarchically, not as a flat sequence. The brackets in [[modern-ize]-ation] encode the fact that -ize must apply first because -ation requires a verbal base that only -ize has created. Prefixes, being category-neutral, stack more freely — but suffix stacking order is determined by category dependencies at each step."
```

## Explainer

From your work on morpheme types and morphological structure, you know that words are built from smaller meaningful units — roots, stems, and bound morphemes — and that these units combine according to structural rules. Prefix and suffix affixation is the dominant mechanism by which English (and most languages with derivational morphology) builds new words: attaching bound morphemes to the **left edge** (prefix) or **right edge** (suffix) of a root or stem. The asymmetry between these two affix positions is more significant than it might first appear.

In English, **suffixes** are far more powerful morphologically because they typically change the **grammatical category** of the base. Adding *-ness* turns the adjective *dark* into the noun *darkness*; adding *-ify* turns the noun *terror* into the verb *terrify*; adding *-ly* turns adjectives into adverbs. This category-changing property means suffixes do most of the syntactic work in derivation — they determine what slot the new word fills in a sentence. **Prefixes**, by contrast, usually preserve the category of the base while shifting its meaning. *Un-* added to *happy* (adjective) yields *unhappy* (still an adjective); *re-* added to *write* (verb) yields *rewrite* (still a verb). There are exceptions, but the asymmetry holds broadly: suffixes change category, prefixes change meaning.

This asymmetry has consequences for **multiple attachment** — the stacking of affixes. Because suffixes change category, they interact with each other in constrained ways: you must build words from inside out, and each suffix attaches to a specific category. Consider *unhappiness*: the structure is [[un-[happy]]-ness], not *[un-[[happy]-ness]]*. The suffix *-ness* attaches to adjectives, so it must wait until *unhappy* (an adjective) is formed; then *-ness* attaches to produce the noun. Prefixes, being category-neutral, can stack more freely, but they still interact with the phonological and semantic properties of whatever they attach to.

A central property distinguishing affixes is **productivity** — the degree to which an affix actively generates new words in the current language. Some suffixes are highly productive: *-er* (agentive, "one who Xs") applies to almost any verb to form a noun (*writer*, *runner*, *compiler*). Others are **frozen**: the *-th* in *warmth* and *length* survives in inherited words but doesn't generate new forms (*coolth* is a nonce coinage, not a natural derivation). Productivity interacts with **phonotactic constraints** — the sound-shape requirements of the affix and the base. The suffix *-ity* strongly prefers Latinate bases (*probability*, *felicity*) and sounds awkward with Germanic ones (*\*hardity*), while *-ness* is productive across both (*hardness*, *brightness*). These selectional restrictions are not arbitrary; they reflect the etymological strata of English vocabulary and the phonological contexts each affix originally evolved in.
