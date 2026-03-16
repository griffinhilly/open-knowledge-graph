---
id: formal-languages-and-strings
title: Formal Languages and Strings
domain: computer-science
course: theory-of-computation
prerequisites: []
builds-toward:
- alphabets-and-language-definition
- regular-languages-fundamentals
tags:
- foundations
- formal-languages
- definitions
stage: abstract-reasoning
status: draft
---

# Formal Languages and Strings

## Core Idea
A formal language is a set of strings over an alphabet, where an alphabet is a finite set of symbols. Strings are finite sequences of symbols from the alphabet. Formal language theory provides mathematical frameworks for reasoning about computational problems and their solvability.

## How It's Best Learned
Start with small concrete examples of alphabets and languages (binary strings, palindromes, arithmetic expressions). Work through closure operations and set-theoretic properties before moving to computational models.

## Common Misconceptions
- Confusing a language with a single string; a language is a set. - Assuming all formal languages are computable or decidable. - Mixing up the alphabet (the symbol set) with the language (the set of strings).

## Explainer

Before we can reason rigorously about what computers can and cannot do, we need a precise mathematical vocabulary for the objects computers operate on. At its core, every computational problem involves deciding whether some input — represented as a sequence of symbols — belongs to some well-defined collection. **Formal language theory** provides exactly this vocabulary, and it is simpler than it might first sound.

An **alphabet** (usually denoted Σ) is just a finite set of symbols. For binary computation, Σ = {0, 1}. For English text, Σ might be {a, b, c, ..., z, space}. A **string** over Σ is a finite sequence of symbols drawn from the alphabet. The string `0110` is a string over {0, 1}; the string `cat` is a string over {a, ..., z}. The **length** of a string is the number of symbols it contains — |0110| = 4. There is one special string that causes initial confusion: the **empty string** ε (epsilon), which has length zero and contains no symbols at all. It is the string analog of zero in arithmetic — it exists, it is valid, and it is the identity element for concatenation (gluing strings together).

A **formal language** is simply a set of strings over some alphabet. The language L = {0, 01, 011, 0111, ...} is the set of all binary strings starting with 0 followed by any number of 1s. The language of palindromes over {a, b} includes ε, a, b, aa, bb, aba, bab, and so on. A language can be finite (like {cat, dog}) or infinite (like the set of all binary strings). It can even be empty — the empty language ∅ contains no strings at all (note: ∅ is different from {ε}, which contains one string, the empty string). The set of *all possible strings* over Σ, including ε, is written **Σ\*** (Sigma star), and every language over Σ is a subset of Σ\*.

Why does this matter? Because virtually every computational problem can be reframed as a language membership question. "Is this number prime?" becomes "does this binary string belong to the language of binary representations of primes?" "Is this program syntactically valid?" becomes "does this character sequence belong to the language defined by the programming language's grammar?" This reframing is not just a notational trick — it lets us use set-theoretic tools (union, intersection, complement) and define a hierarchy of language classes (regular, context-free, decidable, recognizable) based on what kind of machine is needed to determine membership. Every topic that follows in this course builds on this foundation of alphabets, strings, and the languages they form.
