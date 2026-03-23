---
id: feature-matrices-phonology
title: Feature Matrices in Phonology
domain: language-and-communication
course: linguistics
prerequisites:
- id: typed-feature-structures
  type: soft
- id: phonological-features
  type: hard
builds-toward:
- formal-phonotactics
- feature-geometry-phonology
tags:
- phonology
- features
- formalism
stage: advanced
status: validated
---

# Feature Matrices in Phonology

## Core Idea
Sounds are formally represented as matrices of binary or multi-valued features (e.g., [+voice], [+anterior]). This allows systematic statement of which feature combinations form natural classes and how features change in phonological processes.

## Questions

```yaml
- question: "A phonological rule causes /p/, /t/, and /k/ to become voiced before a voiced consonant. Using feature notation, how should this rule be stated?"
  type: multiple-choice
  options:
    - "List all three sounds explicitly: /p/, /t/, /k/ → voiced / _[+voice]"
    - "Change [−voice] to [+voice] for all segments specified as [−voice, −continuant] (voiceless stops)"
    - "Add [+voice] to all consonants in the environment of a voiced segment"
    - "Use the feature [+labial] to capture the class of sounds that undergo this change"
  answer: 1
  explanation: "The rule applies to a natural class — voiceless stops, defined by [−voice, −continuant] — so the rule should reference those features, not list individual sounds. Feature notation reveals that only one feature value changes (voice: − → +) while all other feature values remain constant. This is both more general and more explanatory than a list. Option A is how rules were stated before feature theory; option C is too broad (it would apply to all consonants, including fricatives); option D is wrong because [+labial] only captures /p/, not /t/ and /k/."

- question: "A linguist proposes that /m/, /n/, and /ŋ/ form a natural class. Which feature best defines this class?"
  type: multiple-choice
  options:
    - "[+labial] — all are produced with the lips"
    - "[+voice] — all are voiced consonants"
    - "[+nasal] — all allow air to flow through the nasal cavity"
    - "[−continuant] — all are produced with complete oral closure"
  answer: 2
  explanation: "The feature [+nasal] uniquely defines the class {m, n, ŋ} — all three are nasal consonants in which the velum is lowered and air flows through the nose. [+labial] applies only to /m/; [+voice] includes many other consonants (b, d, g, v, z, etc.); [−continuant] includes all oral stops as well. A natural class must be the most restrictive (smallest) set of features that picks out exactly the sounds that behave together. The [+nasal] specification is both necessary and sufficient to identify this class."

- question: "Feature matrices reveal not just what changes in a phonological process but also what remains constant — and this is as analytically important as identifying the change."
  type: true-false
  answer: true
  explanation: "When a rule changes /t/ to /d/, the feature matrix shows that only [voice] changes from − to +. Every other feature — place of articulation, manner, nasality — remains identical. This is crucial: it shows the process is minimal (only one property is affected) and that the segment's identity is largely preserved. Symbol-based notation (/t/ → /d/) hides this; matrix notation makes it explicit. Identifying what stays constant is part of what distinguishes a voicing rule from an entirely different process."

- question: "Feature matrices are simply a more convenient notation for writing out individual sounds — any phonological rule that can be written with features could just as well be written by listing the affected segments individually."
  type: true-false
  answer: false
  explanation: "Feature matrices do more than provide notation — they reveal the underlying structure of natural classes and phonological processes. A list of affected sounds (/p/, /t/, /k/ → voiced) captures the facts but offers no explanation for why these sounds behave together or what changes. Feature notation shows that the sounds form a natural class (voiceless stops), that only one property changes (voicing), and that the rule generalizes to any new voiceless stop in the language. A list cannot predict behavior for novel sounds or across languages, while features can."

- question: "Why can't phonological rules be stated simply as lists of individual sounds? What does the feature matrix representation reveal that a list of symbols cannot?"
  type: short-answer
  answer: "A list of sounds captures which segments are affected but cannot explain why those segments pattern together or predict what other sounds should behave the same way. Feature matrices reveal the natural class membership — the shared features that define which sounds undergo the rule — and show exactly which property changes while others stay constant. This makes rules general, predictive, and explanatory rather than merely descriptive."
  explanation: "The point of feature theory is that phonological generalizations are not arbitrary lists — they reflect systematic properties of the articulatory-acoustic space. When a rule voices voiceless stops before a voiced consonant, the sounds affected are precisely those sharing [−voice, −continuant], not an arbitrary assortment. Feature notation encodes this systematicity. It also makes cross-linguistic comparison possible: the same rule, written in features, can be compared across languages, revealing universal tendencies in phonological processes."
```

## Explainer

From your work with **phonological features**, you know that sounds are not atomic — they are bundles of articulatory and acoustic properties. A **feature matrix** is simply the formal notation that makes this explicit: instead of writing a sound as a symbol (like /p/ or /d/), you write it as a column of feature-value pairs, each feature set to + or − depending on whether the sound has that property. The matrix for /b/, for example, would show [+voice], [+labial], [−nasal], [+stop] (in whatever feature system you're using). Together these values uniquely identify the segment.

The power of the matrix representation is what it reveals about groups of sounds. Consider the set {p, b, t, d, k, g} — these are English stops. What do they all share? In feature notation, they all have the value [+stop] (or [−continuant] in some frameworks). That shared feature is the formal definition of their **natural class**: a group of sounds that share one or more features and that behave as a unit in phonological rules. Rules can then be written with feature specifications rather than lists of individual sounds. Instead of saying "voicing assimilation affects /p/, /t/, /k/," you say it affects [−voice, +stop], which is both more general and more explanatory.

Feature matrices earn their complexity in the description of **phonological processes**. When a rule changes /t/ to /d/ before a voiced consonant, the matrix representation makes the process transparent: only the value of [voice] changes from − to +; every other feature value stays the same. This partial-change representation is impossible with symbols alone. The matrix shows you *exactly* what changes and what remains constant — which is the linguist's goal when writing a rule.

The **binary** (±) convention assumes that most phonological oppositions are two-way: a sound is either voiced or voiceless, either nasal or oral, either labial or not labial. Some modern frameworks use multi-valued or privative features (where a feature is either present or absent, rather than + or −), but binary features remain the standard starting point because they map cleanly onto articulatory contrasts. As you move toward feature geometry, you'll see how these feature values are organized hierarchically — not as a flat list in a matrix, but as a tree where some features depend on others. The matrix is the entry point to that richer representational world.
