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

## Explainer

You already know that binary trees organize data by making binary decisions at each node — go left or go right. A **trie** (pronounced "try," from re*trie*val) generalizes this idea for strings: instead of two children, each node can have up to one child per character in the alphabet. A path from the root down through the tree spells out a string, one character per level. Some nodes are marked as "end of word" to distinguish complete words from mere prefixes. For example, storing "cat," "car," and "card" would share the path c → a at the top, then branch to t (ending "cat") and r (ending "car"), with r having a further child d (ending "card").

This shared-prefix structure is what makes tries powerful. When you search for a string of length m, you follow exactly m edges from the root — one per character. If at any point the required child does not exist, the string is not in the trie. This gives O(m) lookup time regardless of how many strings are stored, which contrasts with a hash table where hash collisions can degrade performance and where prefix queries are not naturally supported. In a trie, answering "what words start with 'pre'?" is as simple as navigating to the node for 'p' → 'r' → 'e' and then collecting all complete words in that subtree using a depth-first traversal.

The typical implementation represents each node as a dictionary (or fixed-size array) mapping characters to child nodes, plus a boolean flag indicating whether this node marks the end of a valid word. **Insertion** walks down the trie character by character, creating new nodes as needed, and marks the final node. **Search** walks down similarly but returns false if a child is missing or the final node is not marked as a word end. **Prefix search** (`startsWith`) is identical to search except it does not require the end-of-word mark — any node reachable by the prefix characters is a valid match.

The main tradeoff with tries is **memory usage**. If your alphabet is large (say, all Unicode characters) and stored strings share few prefixes, each node's child dictionary is mostly empty, wasting space compared to a hash set. Tries shine when strings share heavy prefix overlap — autocomplete dictionaries, IP routing tables, and spell checkers are classic examples. Compressed variants like **radix trees** (Patricia tries) address the space issue by collapsing chains of single-child nodes into one node holding a multi-character string, but the core prefix-sharing principle remains the same.
