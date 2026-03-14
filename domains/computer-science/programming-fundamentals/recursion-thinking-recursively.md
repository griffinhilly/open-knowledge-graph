---
id: recursion-thinking-recursively
title: 'Recursion: Thinking Recursively'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: recursion-basics
  type: hard
- id: function-design-and-contracts
  type: soft
builds-toward:
- tail-recursion-and-iterative-thinking
tags:
- recursion
- functions
- design
stage: abstract-reasoning
status: draft
---

# Recursion: Thinking Recursively

## Core Idea
Recursion solves a problem by having a function call itself on a smaller problem. Every recursive function needs a base case (when to stop) and a recursive case (how to reduce the problem). Recursion mirrors the structure of recursive data (trees, lists).

## How It's Best Learned
Trace recursive calls by hand; draw the call stack; convert simple loops to recursion and back; test base cases thoroughly.

## Common Misconceptions
That recursion is inherently inefficient (some problems are naturally recursive); that base cases are optional (they're essential—without them, infinite recursion); that tail recursion requires special syntax (some languages optimize it automatically).
