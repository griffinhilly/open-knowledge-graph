---
id: canonic-writing-technique
title: Canon and Fugue Composition Basics
domain: music
course: composition
prerequisites:
- id: counterpoint-imitation
  type: hard
- id: canon-techniques-advanced
  type: soft
builds-toward:
- baroque-counterpoint-and-fugue
tags:
- counterpoint
- canon
- fugue
- imitation
stage: formal-systems
status: draft
---

# Canon and Fugue Composition Basics

## Core Idea
Canons are compositions where melodic material enters successively in different voices, creating strict imitative texture. Fugues extend this principle with multiple subjects, episodes, and complex contrapuntal development. Both forms demand careful voice leading to ensure harmonic coherence despite the strict imitative rules.

## Explainer

A canon is counterpoint taken to its logical extreme: the imitation is not just occasional but continuous throughout the entire piece. From your work on counterpoint imitation, you know how to write a phrase in one voice and echo it in another. A canon formalizes this into a governing rule — the **dux** (leader) states the melody, and the **comes** (follower) enters at a fixed time interval and pitch interval, reproducing every note exactly. The whole piece is one line heard against itself displaced in time, which means every measure of the leader is simultaneously in counterpoint with an earlier measure of the same melody in the follower.

The practical challenge is that you cannot write the dux without already thinking about how it will sound against itself. When you write bar 3, the comes is playing bar 1. Every vertical sonority must be consonant by the rules of counterpoint you already know — but now the two voices aren't independently composed, they are the same melody offset. This constraint is demanding and creative simultaneously: it forces economy and ingenuity in the melodic line, since every interval and rhythm must work both horizontally (as melody) and vertically (as counterpoint against itself).

Fugue extends the imitative principle but relaxes the strictness. A fugue opens with a **subject** — a melodic idea stated alone. The subject is then answered in another voice, typically at the pitch level of the dominant (the **answer**). After all voices have entered in this way, the opening **exposition** is complete. What follows alternates between full **entries** (where the complete subject returns, often in new keys) and **episodes** (transitional passages that develop fragments of the subject or a **countersubject** — a second melody that habitually accompanies the subject). Episodes are the fugue's connective tissue, and they typically use **sequence** (a pattern repeated at successive pitch levels) to drive harmonic motion between key areas.

The connecting thread between canon and fugue is that both turn a single melodic idea into a full multi-voice texture through imitative logic. Canon achieves this with mechanical precision; fugue achieves it with flexible developmental judgment. Both forms reward composers who invest in strong initial material, because the imitative machinery amplifies and exposes every melodic interval and rhythmic figure across the full texture — weakness in the subject becomes weakness everywhere.

## Questions

```yaml
- question: "In a two-voice canon, why must the composer think about counterpoint when writing the dux (leader) alone?"
  type: short-answer
  answer: "Because the comes (follower) will reproduce the dux exactly, offset in time. Every measure of the dux will sound simultaneously with an earlier measure of the same melody. So when writing bar 3 of the dux, the composer must ensure it forms good counterpoint with bar 1 — the two bars will be heard together. The single line is always in counterpoint with itself."
  explanation: "This is the defining constraint of canon writing. Unlike free counterpoint, where two independent lines are composed against each other, a canon forces the composer to write one line that works as both melody and counterpoint simultaneously. The time interval and pitch interval of the imitation determine which measures will be in contact, so the composer must plan ahead for every upcoming vertical collision."

- question: "What is the difference between a fugue exposition and a fugue episode?"
  type: multiple-choice
  options:
    - "An exposition uses the full subject; an episode develops fragments without a complete subject statement"
    - "An exposition is in the tonic; an episode is always in a minor key"
    - "An exposition uses all voices; an episode uses only two voices"
    - "An exposition is the second section of a fugue; an episode is the opening"
  answer: 0
  explanation: "The exposition is the opening section where the subject enters successively in each voice. Episodes are transitional passages between full subject entries; they develop motivic fragments (often from the subject's tail or from a countersubject) using sequential motion, but they do not present the complete subject. Episodes are the fugue's connective tissue, driving harmonic motion between the key areas where full subject entries occur."
```
