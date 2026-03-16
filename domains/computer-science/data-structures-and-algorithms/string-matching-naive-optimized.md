---
id: string-matching-naive-optimized
title: 'String Matching: Naive and Optimized Approaches'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
builds-toward:
- boyer-moore-algorithm-details
- trie-implementation-applications
tags:
- strings
- matching
- algorithms
stage: formal-systems
status: draft
---

# String Matching: Naive and Optimized Approaches

## Core Idea
Naive string matching checks the pattern at every position, achieving O((n-m+1)·m) worst-case time. Optimized algorithms like KMP and Boyer-Moore preprocess the pattern to skip redundant comparisons, achieving O(n+m) or O(n) average-case time.

## How It's Best Learned
Implement naive matching, then observe how repeated comparisons waste effort. Study KMP's failure function and how it avoids re-examining matched characters.

## Common Misconceptions
- Assuming naive matching is always sufficient; large texts and patterns demand optimized algorithms.
- Thinking KMP and Boyer-Moore have similar performance; Boyer-Moore is often faster in practice due to skipping.
- Not accounting for pattern preprocessing cost; amortized over multiple searches, it's worth the investment.

## Explainer

String matching asks a deceptively simple question: given a text of length n and a pattern of length m, where does the pattern appear in the text? You already know how arrays work, so you can think of both text and pattern as character arrays. The **naive algorithm** tries the pattern at every possible starting position in the text — positions 0 through n-m — and at each position compares characters one by one. If all m characters match, you've found an occurrence. If any character mismatches, you slide the pattern over by one position and start comparing from scratch.

The naive approach works, but it does a lot of redundant work. Consider searching for "AAAB" in "AAAAAAB". At position 0 you compare three A's successfully before failing on the B. At position 1 you compare the same three A's again. The naive algorithm doesn't remember anything from previous attempts — every new position restarts the comparison from zero. This gives a worst case of O((n-m+1)·m), which approaches O(nm) for pathological inputs.

The **Knuth-Morris-Pratt (KMP)** algorithm eliminates this redundancy by preprocessing the pattern into a **failure function** (also called the prefix function or partial match table). The failure function records, for each position in the pattern, the length of the longest proper prefix of the pattern that is also a suffix of the pattern up to that point. When a mismatch occurs at position j in the pattern, instead of restarting from the beginning, KMP shifts the pattern so that the already-matched prefix aligns with its corresponding suffix — effectively skipping over comparisons you know will succeed. This guarantees that each character in the text is examined at most twice, giving O(n+m) total time including the O(m) preprocessing.

**Boyer-Moore** takes a different approach that is often faster in practice. Instead of comparing left-to-right, it compares the pattern against the text from right to left. When a mismatch occurs, it uses two heuristics — the **bad character rule** and the **good suffix rule** — to decide how far to shift the pattern. The bad character rule looks at the mismatched text character and jumps the pattern forward to align with the last occurrence of that character in the pattern. The good suffix rule uses information about the matched suffix to skip even further. In the best case, Boyer-Moore examines only O(n/m) characters — it can skip entire chunks of the text without looking at them. This makes it the preferred choice for searching long texts with moderate-length patterns, such as searching through files or documents.
