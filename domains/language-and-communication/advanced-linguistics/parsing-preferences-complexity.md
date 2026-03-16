---
id: parsing-preferences-complexity
title: Parsing Preferences and Computational Complexity
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: psycholinguistics-intro
  type: hard
- id: sentence-parsing-garden-paths
  type: soft
tags:
- parsing
- preferences
- complexity
stage: advanced
status: draft
---

# Parsing Preferences and Computational Complexity

## Core Idea
Parsers exhibit biases toward simpler structures and frequent constructions. Minimal attachment (attaching phrases as low as possible) and late closure (attaching new material to recent constituents) govern initial parsing. Working memory limitations affect how many open dependencies can be maintained; high dependencies (long-distance relative clauses) are harder than low dependencies. Parsing preferences interact with grammatical constraints and input frequency to determine comprehension difficulty.

## How It's Best Learned
Predict parsing preferences for ambiguous sentences and test with reading-time experiments. Manipulate complexity factors (embedding depth, number of dependencies) and measure comprehension difficulty.

## Common Misconceptions
- Parsing preferences are not hard constraints; they bias initial analysis but can be overcome by strong cues.
- Working memory limitations are not absolute; they vary by individual and interact with linguistic factors.

## Explainer

From your psycholinguistics background and work with garden-path sentences, you know that parsing is not a neutral process of recovering structure — the parser has preferences, and those preferences create predictable patterns of difficulty. The study of parsing preferences and computational complexity maps those patterns systematically: why are some sentences easy to understand even when they are long, while others are difficult even when they are short?

The two most studied parsing preferences are **minimal attachment** and **late closure**. Minimal attachment means the parser attaches incoming material using the fewest additional syntactic nodes possible — preferring to extend an existing phrase rather than open a new one. Late closure means the parser prefers to attach new words to the most recently opened syntactic constituent rather than closing it and opening a new phrase. These are both efficiency heuristics: they minimize the structural complexity the parser must track at any moment. The preferences usually produce correct results, but when they lead to the wrong analysis (as in garden paths), the parser must revise — and the cost of revision is what makes complexity measurable.

**Working memory** is the resource constraint that underlies many complexity effects. Parsing requires simultaneously maintaining an incomplete structure in memory while integrating new words into it. The key variable is **dependency distance**: how far apart are the words that must be linked for the sentence to be understood? In a simple sentence (*The cat chased the mouse*), the verb and its arguments are close together. In a **center-embedded** clause (*The reporter that the senator that the lobbyist attacked accused ran*), the main verb *ran* is separated from its subject *reporter* by two intervening clauses — the dependency must be held open across multiple intervening words. Sentences with long, overlapping dependencies are dramatically harder to process than sentences where dependencies are short and resolved quickly, even when both are grammatical.

This explains an otherwise puzzling asymmetry: **subject relative clauses** (*The reporter who attacked the senator*) are consistently easier than **object relative clauses** (*The reporter that the senator attacked*), even though both are grammatical. In the subject relative, the relativized element (*reporter*) is in the same position it would occupy in a simple sentence (subject). In the object relative, the relativized element is in the object position while the subject of the relative clause intervenes — creating a longer dependency and a less frequent structural pattern. Processing difficulty tracks both **dependency length** (how long a gap must be held in memory) and **frequency** (how often this structure type appears in input). High-frequency structures are faster because the parser has acquired stronger expectations for them. This interaction between memory constraints and input statistics makes parsing complexity a window into both the architecture of the parsing system and the statistical structure of the language learner's environment.
