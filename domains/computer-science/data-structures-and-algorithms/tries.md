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
status: draft
---

# Tries (Prefix Trees)

## Core Idea
A trie (prefix tree) is a tree-like data structure for storing strings where each node represents a single character and paths from root to a marked node spell out complete words. Lookup, insertion, and deletion each take O(m) time where m is the string length, independent of the number of stored strings. Tries excel at prefix-based operations like autocomplete, spell checking, and IP routing. Each node typically holds a dictionary of children (one per possible character) and a boolean marking whether it completes a valid word.

## How It's Best Learned
Implement a Trie class with insert, search, and startsWith methods, using a dictionary for children. Then implement autocomplete by collecting all words under a given prefix node using DFS.

## Common Misconceptions
- Tries consume more memory than hash tables when strings share few common prefixes; their advantage emerges when prefixes are shared heavily.
- A trie lookup for a word of length m is O(m), not O(1); however O(m) is often optimal since any lookup must read all m characters of the query.
