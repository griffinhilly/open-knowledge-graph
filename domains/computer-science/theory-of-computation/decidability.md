---
id: decidability
title: Decidable Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: set-theory-basics
  type: soft
- id: cardinality-and-countability
  type: soft
- id: mathematical-induction
  type: soft
builds-toward:
- halting-problem
- recognizability-vs-decidability
- undecidability-reductions
tags:
- decidable
- Turing-decidable
- recognizable
- algorithms
stage: advanced
status: draft
---

# Decidable Languages

## Core Idea
A language is *Turing-decidable* (or just decidable) if some Turing machine halts on every input and correctly accepts or rejects. A language is *Turing-recognizable* if some TM halts and accepts on every string in the language, but may loop on strings outside it. Decidable languages are a proper subset of recognizable languages. Examples of decidable languages include all regular and context-free languages. The distinction between recognizable and decidable becomes crucial when studying the limits of computation: some problems can be semi-solved (recognized) but not fully solved (decided).

## How It's Best Learned
Build TMs that decide specific languages (e.g., ATM for the same-length palindrome) and contrast with TMs that only recognize. Understanding why a decider must *halt on rejection* — not just loop — is the key conceptual bridge to undecidability.

## Common Misconceptions
- Thinking 'recognizable' and 'decidable' are synonyms — a recognizer may loop forever on non-members.
- Assuming all natural computational problems are decidable — the halting problem proves this false.
