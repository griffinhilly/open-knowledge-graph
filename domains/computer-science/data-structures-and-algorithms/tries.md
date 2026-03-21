---
id: tries
title: Tries (Prefix Trees)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-trees
  type: hard
- id: hash-tables
  type: soft
- id: string-operations
  type: soft
tags:
- trie
- prefix-tree
- strings
- autocomplete
stage: formal-systems
status: validated
---

# Tries (Prefix Trees)

## Core Idea
A trie (prefix tree) is a tree-like data structure for storing strings where each node represents a single character and paths from root to a marked node spell out complete words. Lookup, insertion, and deletion each take O(m) time where m is the string length, independent of the number of stored strings. Tries excel at prefix-based operations like autocomplete, spell checking, and IP routing. Each node typically holds a dictionary of children (one per possible character) and a boolean marking whether it completes a valid word.

## How It's Best Learned
Implement a Trie class with insert, search, and startsWith methods, using a dictionary for children. Then implement autocomplete by collecting all words under a given prefix node using DFS.

## Common Misconceptions
- Tries consume more memory than hash tables when strings share few common prefixes; their advantage emerges when prefixes are shared heavily.
- A trie lookup for a word of length m is O(m), not O(1); however O(m) is often optimal since any lookup must read all m characters of the query.

## Questions

```yaml
- question: "A trie stores 1,000,000 words from a dictionary. How long does it take to look up whether the word 'algorithm' (10 characters) is present?"
  type: multiple-choice
  options:
    - "O(1,000,000) — the query must be compared against all stored words"
    - "O(log 1,000,000) ≈ O(20) — binary search over sorted dictionary entries"
    - "O(10) — one edge traversal per character in the query string"
    - "O(10 × 1,000,000) — each character must be checked against all stored strings"
  answer: 2
  explanation: "Trie lookup is O(m) where m is the length of the query string — independent of the number of stored strings. At each node you follow exactly one edge for the next character; if the edge is missing, the word is absent; if you reach the end with an end-of-word flag, the word is present. The dictionary size introduces no additional comparisons — this is the key advantage over sorted arrays or hash tables for string lookups."

- question: "Why are tries better than hash sets for autocomplete functionality?"
  type: multiple-choice
  options:
    - "Tries guarantee O(1) lookup while hash sets are O(m) for string keys"
    - "Tries store words in sorted alphabetical order, enabling binary search on suggestions"
    - "Tries support prefix queries natively — navigating to a prefix node puts you at the root of all matching completions"
    - "Tries use less memory than hash sets for large vocabularies with long strings"
  answer: 2
  explanation: "A hash set answers 'does this exact string exist?' efficiently but has no structural connection between 'pre-' and 'prefix', 'preview', 'prevent', etc. In a trie, navigating p→r→e puts you at a node whose entire subtree consists of words starting with 'pre'. Collecting completions is then a simple DFS from that node — an operation that has no efficient analog in a hash set."

- question: "A trie storing 10,000 words is slower to search than a trie storing 100 words, assuming the query string is the same length."
  type: true-false
  answer: false
  explanation: "Trie search time is O(m) — the length of the query — regardless of how many words are stored. Each step follows one labeled edge; the dictionary size adds no additional traversal steps. This dictionary-size independence is precisely what distinguishes trie lookup from hash-table lookup (which can degrade with collisions) and binary search (which is O(log n))."

- question: "In a trie, every node reachable from the root represents a complete stored word."
  type: true-false
  answer: false
  explanation: "Most nodes represent prefixes, not complete words. A trie storing 'car' and 'card' has nodes at c, ca, car, and card. The 'car' node is marked as a word end, but 'c' and 'ca' are purely intermediate — they may represent no stored word at all. The end-of-word boolean flag is what distinguishes complete words from intermediate prefix nodes."

- question: "Why does a trie consume more memory than a hash set when stored strings share few common prefixes, and when does the trade-off reverse?"
  type: short-answer
  answer: "Each trie node stores a dictionary (or fixed-size array) of potential child pointers — one slot per possible character. With few shared prefixes, most nodes have mostly-empty child slots: a lot of wasted space for each unique character path. A hash set stores only the full strings compactly. The trade-off reverses when strings heavily share prefixes: each shared prefix character is stored in one node rather than repeated in every string, making the trie more space-efficient. Autocomplete dictionaries (thousands of words sharing 'un-', 'pre-', 'com-' etc.) are the canonical case where tries win on both time and space."
  explanation: "The memory trade-off depends directly on prefix overlap in the data. The trie's structural advantage — shared storage for shared prefixes — only pays off when that sharing actually exists. This is why domain-specific knowledge (is this a natural-language word set or arbitrary strings?) informs which structure to choose."
```

## Explainer

You already know that binary trees organize data by making binary decisions at each node — go left or go right. A **trie** (pronounced "try," from re*trie*val) generalizes this idea for strings: instead of two children, each node can have up to one child per character in the alphabet. A path from the root down through the tree spells out a string, one character per level. Some nodes are marked as "end of word" to distinguish complete words from mere prefixes. For example, storing "cat," "car," and "card" would share the path c → a at the top, then branch to t (ending "cat") and r (ending "car"), with r having a further child d (ending "card").

This shared-prefix structure is what makes tries powerful. When you search for a string of length m, you follow exactly m edges from the root — one per character. If at any point the required child does not exist, the string is not in the trie. This gives O(m) lookup time regardless of how many strings are stored, which contrasts with a hash table where hash collisions can degrade performance and where prefix queries are not naturally supported. In a trie, answering "what words start with 'pre'?" is as simple as navigating to the node for 'p' → 'r' → 'e' and then collecting all complete words in that subtree using a depth-first traversal.

The typical implementation represents each node as a dictionary (or fixed-size array) mapping characters to child nodes, plus a boolean flag indicating whether this node marks the end of a valid word. **Insertion** walks down the trie character by character, creating new nodes as needed, and marks the final node. **Search** walks down similarly but returns false if a child is missing or the final node is not marked as a word end. **Prefix search** (`startsWith`) is identical to search except it does not require the end-of-word mark — any node reachable by the prefix characters is a valid match.

The main tradeoff with tries is **memory usage**. If your alphabet is large (say, all Unicode characters) and stored strings share few prefixes, each node's child dictionary is mostly empty, wasting space compared to a hash set. Tries shine when strings share heavy prefix overlap — autocomplete dictionaries, IP routing tables, and spell checkers are classic examples. Compressed variants like **radix trees** (Patricia tries) address the space issue by collapsing chains of single-child nodes into one node holding a multi-character string, but the core prefix-sharing principle remains the same.
