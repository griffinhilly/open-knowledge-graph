---
id: boyer-moore-algorithm-details
title: Boyer-Moore String Matching Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: string-matching-naive-optimized
  type: hard
tags:
- strings
- matching
- algorithms
stage: formal-systems
status: draft
---

# Boyer-Moore String Matching Algorithm

## Core Idea
Boyer-Moore matches from right to left and uses two heuristics: the bad-character rule (skip based on the mismatched character) and the good-suffix rule (skip based on the matched suffix). Preprocessing is O(m + σ) where σ is alphabet size; matching is O(n/m) best-case and O(n·m) worst-case.

## How It's Best Learned
Trace Boyer-Moore by hand on a simple example, watching how right-to-left matching and the bad-character rule skip positions. Implement and compare performance to KMP on both best-case and worst-case inputs.

## Common Misconceptions
- Thinking Boyer-Moore is always faster than KMP; worst-case complexity can be poor on adversarial inputs.
- Forgetting that the good-suffix rule requires additional preprocessing; often only the bad-character rule is implemented.
- Not recognizing that Boyer-Moore's advantage grows with larger alphabets and longer patterns.

## Explainer

From naive string matching, you know the brute-force approach: align the pattern at each position in the text, compare character by character from left to right, and shift by one position on failure. Boyer-Moore's first key innovation is reversing the comparison direction — it compares the pattern against the text **from right to left**. This seemingly small change unlocks a powerful ability: when a mismatch occurs, the algorithm can often skip ahead by much more than one position, because the mismatched character reveals information about multiple alignment positions at once.

The **bad-character rule** is the more intuitive of Boyer-Moore's two heuristics. When a mismatch occurs at some position and the text character is, say, 'X', the algorithm asks: does 'X' appear anywhere in the pattern? If not, the entire pattern can be shifted past that character — no alignment that includes 'X' can possibly match. If 'X' does appear in the pattern, the pattern is shifted to align its rightmost occurrence of 'X' with the text position. Consider searching for "EXAMPLE" in a long English text. If the rightmost character comparison reveals the text has a 'Z', and 'Z' does not appear in "EXAMPLE," the algorithm jumps forward by the full pattern length of 7 positions. This is why Boyer-Moore achieves **sublinear** best-case performance of O(n/m) — it can skip large portions of the text entirely, examining fewer characters than the text contains.

The **good-suffix rule** handles a subtler situation. When some characters at the right end of the pattern have already matched before a mismatch occurs, the matched portion (the "good suffix") constrains how far the pattern can safely shift. The algorithm looks for another occurrence of this suffix earlier in the pattern, or for a prefix of the pattern that matches a suffix of the good suffix, and shifts the minimum amount needed to align one of these with the text. This rule requires preprocessing the pattern into a table of shift values, which takes O(m) time. In practice, the algorithm takes the maximum of the shifts suggested by the bad-character rule and the good-suffix rule, ensuring the largest safe skip at each step.

Boyer-Moore excels in practice for natural-language text and DNA sequences — situations with reasonably large alphabets and patterns of moderate length. The larger the alphabet, the more likely a mismatched character does not appear in the pattern, leading to full-length skips. For a 26-character English alphabet and a 10-character pattern, most mismatches allow skipping 10 positions. However, on adversarial inputs with very small alphabets (like binary strings with repeated characters), the skip distances shrink and worst-case O(n·m) behavior can emerge. This is why the Galil variant and other refinements add worst-case linear guarantees. Understanding when Boyer-Moore shines and when it degrades helps you choose the right string matching algorithm for your specific domain.
