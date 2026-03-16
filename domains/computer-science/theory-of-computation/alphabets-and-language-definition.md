---
id: alphabets-and-language-definition
title: Alphabets, Strings, and Language Definition
domain: computer-science
course: theory-of-computation
prerequisites:
- id: formal-languages-and-strings
  type: hard
builds-toward:
- regular-languages-fundamentals
- closure-properties-regular-languages
tags:
- formal-languages
- strings
- definitions
stage: abstract-reasoning
status: draft
---

# Alphabets, Strings, and Language Definition

## Core Idea
An alphabet Σ is a finite, non-empty set of symbols. A string (or word) is a finite sequence of symbols from Σ, and the empty string ε is the string of length zero. A formal language over Σ is any subset of Σ*, the set of all finite strings over Σ.

## Explainer

From your work with formal languages and strings, you have a general sense that computation involves processing sequences of symbols. This topic pins down the precise definitions that everything else in theory of computation builds upon. An **alphabet**, denoted Σ (sigma), is simply a finite, non-empty set of symbols. It could be as simple as Σ = {0, 1} for binary strings, Σ = {a, b, c} for a three-letter system, or Σ = {a, b, ..., z} for lowercase English. The key constraints are that the set must be finite (you cannot have infinitely many symbols) and non-empty (you need at least one symbol to work with).

A **string** (also called a **word**) over an alphabet Σ is a finite sequence of symbols drawn from Σ. Over the alphabet {0, 1}, the strings include `0`, `1`, `01`, `110`, `0000`, and so on. The length of a string is the number of symbols it contains: `|01| = 2`, `|110| = 3`. One special string deserves its own name: the **empty string** ε (epsilon) has length zero. It contains no symbols at all. Think of it as the string equivalent of the number zero — it seems trivial, but it turns out to be essential in formal definitions, just as zero is essential in arithmetic. Every alphabet has ε as a valid string over it.

The notation **Σ\*** (sigma star) denotes the set of *all* finite strings over Σ, including ε. If Σ = {a, b}, then Σ* = {ε, a, b, aa, ab, ba, bb, aaa, aab, ...} — an infinite set, even though Σ itself is finite. This is a crucial point: a finite alphabet generates infinitely many strings. A **formal language** over Σ is then defined as any subset of Σ*. The language could be finite (like {ab, ba}), infinite (like "all strings with equal numbers of a's and b's"), or even empty (the set ∅, containing no strings at all — distinct from {ε}, which contains one string, the empty string). This definition is extraordinarily broad: any collection of strings you can describe is a formal language. The entire study of automata and computability is about classifying which languages can be recognized by which kinds of machines.
