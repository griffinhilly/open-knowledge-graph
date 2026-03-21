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

## Questions

```yaml
- question: "You are searching for an 8-character pattern in a text consisting entirely of the characters 'A' and 'B'. Which of the following best explains why Boyer-Moore performs poorly on this input?"
  type: multiple-choice
  options:
    - "Right-to-left comparison is less efficient than left-to-right for binary alphabets"
    - "The bad-character rule rarely allows large skips because the mismatched character almost always appears in the pattern, shrinking skip distances toward 1"
    - "The good-suffix rule does not apply when the alphabet has only two symbols"
    - "Boyer-Moore requires O(m²) preprocessing time for small alphabets"
  answer: 1
  explanation: "Boyer-Moore's advantage comes from the bad-character rule: when a mismatch occurs, if the mismatched text character does not appear in the pattern, the algorithm can skip the full pattern length. With a binary alphabet, almost every character in the text appears somewhere in the pattern, so skips shrink to 1 or 2 positions and worst-case O(n·m) behavior emerges. Large alphabets are what make Boyer-Moore shine — in natural language or DNA with 26 or 4 symbols, mismatches often allow full-length skips."

- question: "Which of Boyer-Moore's two heuristics requires preprocessing the pattern into a table of shift values based on what was already matched before the mismatch?"
  type: multiple-choice
  options:
    - "The bad-character rule, because it indexes every character in the pattern"
    - "The good-suffix rule, because it uses the already-matched suffix to determine the safe shift"
    - "Both rules require identical preprocessing tables"
    - "Neither rule requires preprocessing — shifts are computed at match time"
  answer: 1
  explanation: "The good-suffix rule handles the situation where some characters at the right end of the pattern already matched before a mismatch. It looks for another occurrence of that matched suffix earlier in the pattern, or a prefix of the pattern that matches a suffix of the good suffix, and shifts to align it. This requires O(m) preprocessing of the pattern into a shift table. The bad-character rule, in contrast, preprocesses a table of the rightmost position of each character in the pattern — a simpler lookup. In practice, the algorithm takes the maximum shift from both rules at each step."

- question: "Boyer-Moore compares the pattern against the text from left to right, just like the naive algorithm."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. Boyer-Moore's key innovation is comparing from RIGHT to LEFT within the pattern at each alignment position. This reversal is what enables the bad-character rule to produce large skips: when a mismatch occurs at the rightmost comparison, the mismatched text character immediately tells you how far ahead you can shift the entire pattern. Left-to-right comparison would only reveal mismatch information about the leftmost character, which is less useful for skipping."

- question: "Boyer-Moore generally achieves better best-case performance on inputs with larger alphabets than on inputs with smaller alphabets."
  type: true-false
  answer: true
  explanation: "This is true and is the central reason Boyer-Moore excels in practice for natural-language text. With a large alphabet (e.g., 26 English letters or 128 ASCII characters), mismatched text characters are unlikely to appear in the pattern, so the bad-character rule frequently allows skipping the full pattern length. For a 10-character English-language pattern, most mismatches allow a 10-position skip. With a binary alphabet, the skips collapse. This is why Boyer-Moore is excellent for DNA pattern matching (4-character alphabet of 'ACGT') only with longer patterns — the longer the pattern, the more characters become rare in it even with a small alphabet."

- question: "Why does Boyer-Moore's right-to-left comparison enable larger skips than left-to-right comparison, giving it sublinear best-case performance?"
  type: short-answer
  answer: "When you compare right-to-left and a mismatch occurs at the rightmost position, the mismatched text character has not yet been 'used' by any successful comparison. This tells you that no alignment that places the pattern over that text character (other than the alignments where it matches a pattern position containing that character) can succeed. If the mismatched character doesn't appear in the pattern at all, the entire pattern can be shifted past it — a skip equal to the full pattern length. The first comparison that fails can already rule out many candidate alignments at once. Left-to-right comparison would fail at the first character and shift by one, gaining nothing from the mismatch beyond the single position."
  explanation: "The insight is that information from a failure can be used to skip more than one position. In the naive algorithm, a failure shifts by exactly 1. In Boyer-Moore, the bad-character rule's skip is determined by how far ahead the mismatched character next appears in the pattern (or the full pattern length if it doesn't appear). Because the rightmost comparison is the one that mismatches, the algorithm can often jump forward by m positions — examining fewer characters than the text contains, hence O(n/m) best-case time."
```

## Explainer

From naive string matching, you know the brute-force approach: align the pattern at each position in the text, compare character by character from left to right, and shift by one position on failure. Boyer-Moore's first key innovation is reversing the comparison direction — it compares the pattern against the text **from right to left**. This seemingly small change unlocks a powerful ability: when a mismatch occurs, the algorithm can often skip ahead by much more than one position, because the mismatched character reveals information about multiple alignment positions at once.

The **bad-character rule** is the more intuitive of Boyer-Moore's two heuristics. When a mismatch occurs at some position and the text character is, say, 'X', the algorithm asks: does 'X' appear anywhere in the pattern? If not, the entire pattern can be shifted past that character — no alignment that includes 'X' can possibly match. If 'X' does appear in the pattern, the pattern is shifted to align its rightmost occurrence of 'X' with the text position. Consider searching for "EXAMPLE" in a long English text. If the rightmost character comparison reveals the text has a 'Z', and 'Z' does not appear in "EXAMPLE," the algorithm jumps forward by the full pattern length of 7 positions. This is why Boyer-Moore achieves **sublinear** best-case performance of O(n/m) — it can skip large portions of the text entirely, examining fewer characters than the text contains.

The **good-suffix rule** handles a subtler situation. When some characters at the right end of the pattern have already matched before a mismatch occurs, the matched portion (the "good suffix") constrains how far the pattern can safely shift. The algorithm looks for another occurrence of this suffix earlier in the pattern, or for a prefix of the pattern that matches a suffix of the good suffix, and shifts the minimum amount needed to align one of these with the text. This rule requires preprocessing the pattern into a table of shift values, which takes O(m) time. In practice, the algorithm takes the maximum of the shifts suggested by the bad-character rule and the good-suffix rule, ensuring the largest safe skip at each step.

Boyer-Moore excels in practice for natural-language text and DNA sequences — situations with reasonably large alphabets and patterns of moderate length. The larger the alphabet, the more likely a mismatched character does not appear in the pattern, leading to full-length skips. For a 26-character English alphabet and a 10-character pattern, most mismatches allow skipping 10 positions. However, on adversarial inputs with very small alphabets (like binary strings with repeated characters), the skip distances shrink and worst-case O(n·m) behavior can emerge. This is why the Galil variant and other refinements add worst-case linear guarantees. Understanding when Boyer-Moore shines and when it degrades helps you choose the right string matching algorithm for your specific domain.
