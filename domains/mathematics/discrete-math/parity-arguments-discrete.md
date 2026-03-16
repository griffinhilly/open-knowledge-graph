---
id: parity-arguments-discrete
title: Parity Arguments and Parity Invariants
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic
  type: hard
- id: even-and-odd-numbers
  type: hard
tags:
- number-theory
- parity
- proofs
stage: formal-systems
status: draft
---

# Parity Arguments and Parity Invariants

## Core Idea
Parity (even/odd) is invariant under certain operations, meaning it doesn't change. Parity arguments use this invariance to prove impossibility results. For example, showing a process cannot reach a goal state if the parity required differs from the parity achievable.

## Explainer

From your work with modular arithmetic, you know that every integer is congruent to either 0 or 1 modulo 2 — it is either even or odd. A **parity invariant** is a quantity whose parity doesn't change as a process unfolds. If you can show that (1) a quantity has even parity at the start, (2) every allowed operation preserves parity, and (3) the target state requires odd parity, then the target is unreachable — regardless of how clever the path is. This is one of the cleanest proof techniques in all of combinatorics.

The classic example is the mutilated chessboard: remove two diagonally opposite corners of an 8×8 board, leaving 62 squares. Can you tile it perfectly with 31 dominoes? A domino always covers exactly one black square and one white square. The two removed corners are both the same color (say, both white), leaving 32 black squares and 30 white squares. Since every domino covers one of each, after placing any number of dominoes the difference (black covered − white covered) changes by 1 each time. To cover all remaining squares, you'd need 32 black and 30 white covered — but you need 31 dominoes covering 31 black and 31 white. The **parity of the color imbalance** is invariant, and the target requires a different parity. Tiling is impossible.

Parity arguments also appear in puzzles involving state changes. Suppose you have 15 coins all showing heads, and each move flips exactly 3 coins. After any number of moves, has the parity of heads changed? Each move changes 3 coins: each flip toggles one coin, changing the count of heads by +1 or −1. Three such changes alter the total by an odd amount. So after each move, the parity of the number of heads flips. Starting from 15 (odd), after an even number of moves you have an odd number of heads, and after an odd number of moves an even number. You can never reach exactly 0 heads in an even number of moves.

The power of parity arguments is their simplicity: you don't need to enumerate possibilities or construct an impossibility proof by exhaustion. You identify the right invariant, verify it's truly preserved, and derive the contradiction in one step. The same idea scales to more general **monovariant** and **invariant** arguments — a foundational technique in combinatorics and algorithms.
