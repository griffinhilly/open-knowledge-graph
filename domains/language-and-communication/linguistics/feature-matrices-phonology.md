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
stage: formal-systems
status: draft
---

# Feature Matrices in Phonology

## Core Idea
Sounds are formally represented as matrices of binary or multi-valued features (e.g., [+voice], [+anterior]). This allows systematic statement of which feature combinations form natural classes and how features change in phonological processes.

## Explainer

From your work with **phonological features**, you know that sounds are not atomic — they are bundles of articulatory and acoustic properties. A **feature matrix** is simply the formal notation that makes this explicit: instead of writing a sound as a symbol (like /p/ or /d/), you write it as a column of feature-value pairs, each feature set to + or − depending on whether the sound has that property. The matrix for /b/, for example, would show [+voice], [+labial], [−nasal], [+stop] (in whatever feature system you're using). Together these values uniquely identify the segment.

The power of the matrix representation is what it reveals about groups of sounds. Consider the set {p, b, t, d, k, g} — these are English stops. What do they all share? In feature notation, they all have the value [+stop] (or [−continuant] in some frameworks). That shared feature is the formal definition of their **natural class**: a group of sounds that share one or more features and that behave as a unit in phonological rules. Rules can then be written with feature specifications rather than lists of individual sounds. Instead of saying "voicing assimilation affects /p/, /t/, /k/," you say it affects [−voice, +stop], which is both more general and more explanatory.

Feature matrices earn their complexity in the description of **phonological processes**. When a rule changes /t/ to /d/ before a voiced consonant, the matrix representation makes the process transparent: only the value of [voice] changes from − to +; every other feature value stays the same. This partial-change representation is impossible with symbols alone. The matrix shows you *exactly* what changes and what remains constant — which is the linguist's goal when writing a rule.

The **binary** (±) convention assumes that most phonological oppositions are two-way: a sound is either voiced or voiceless, either nasal or oral, either labial or not labial. Some modern frameworks use multi-valued or privative features (where a feature is either present or absent, rather than + or −), but binary features remain the standard starting point because they map cleanly onto articulatory contrasts. As you move toward feature geometry, you'll see how these feature values are organized hierarchically — not as a flat list in a matrix, but as a tree where some features depend on others. The matrix is the entry point to that richer representational world.
