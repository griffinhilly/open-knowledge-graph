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

## Questions

```yaml
- question: "You have 15 coins all showing heads. Each move flips exactly 3 coins. Can you reach a state with exactly 0 coins showing heads? What does parity tell you?"
  type: multiple-choice
  options:
    - "Yes, with enough moves you can always reach any configuration"
    - "No — each move changes the count of heads by an odd amount, so the parity of heads alternates each move; starting from 15 (odd), 0 (even) is reachable only after an odd number of moves, and the arithmetic works out"
    - "No — each move flips exactly 3 coins, so the parity of heads is invariant and never changes from odd"
    - "No — each move changes the count of heads by exactly 3, so you can only reach 15, 12, 9, 6, 3, or 0"
  answer: 1
  explanation: "Each flip of a single coin changes the count of heads by +1 or −1. Three flips change the total by an odd amount (odd + odd + odd = odd, or various combinations summing to odd). So after each move, the parity of the number of heads changes: odd→even→odd→even. Starting from 15 (odd), after one move you have an even count, after two moves odd again, etc. Reaching 0 (even) requires an odd number of moves — which is consistent with this analysis, so 0 IS reachable in odd-move paths. (The more interesting version: can you reach 0 in exactly 6 moves? Since 6 is even, you'd need the count to be odd after 6 moves, but starting from odd and flipping parity 6 times gives odd — not 0. This is the nuance the invariant captures.)"

- question: "A mutilated chessboard has two corners removed. You want to tile it with dominoes (each covering exactly one black and one white square). The two removed corners are the same color. What does a parity argument tell you?"
  type: multiple-choice
  options:
    - "Tiling is impossible because the board no longer has enough squares for 31 dominoes"
    - "Tiling is impossible because removing same-colored corners creates a color imbalance that no domino arrangement can correct, since every domino covers exactly one of each color"
    - "Tiling is possible as long as you start from the corner and work inward systematically"
    - "The parity argument is inconclusive here; you'd need to try all possible arrangements to know"
  answer: 1
  explanation: "Every domino covers exactly one black and one white square — this is an invariant. After any number of placements, the number of covered black squares equals the number of covered white squares. But removing two same-colored corners (say, both white) leaves 32 black and 30 white squares. To tile all remaining squares you'd need to cover 32 black and 30 white — an unequal number. But dominoes always cover equal numbers. The parity argument rules out tiling immediately, without trying any arrangements."

- question: "A parity argument proves impossibility by finding a single path to the goal state that fails, then concluding all paths fail."
  type: true-false
  answer: false
  explanation: "This is the key misconception to avoid. A parity argument does not examine paths at all — it identifies a quantity whose parity is preserved by every allowed operation (an invariant), then shows that the starting state and the target state have different parities. Since no sequence of operations can change the invariant, the target is unreachable by *any* path, however clever. This is far more powerful than enumerating paths, which would be impossible for large configuration spaces."

- question: "If every allowed operation changes a quantity by an even amount, then that quantity's parity is an invariant of the process."
  type: true-false
  answer: true
  explanation: "Adding an even number to any integer does not change its parity: even + even = even, odd + even = odd. So if every operation changes the tracked quantity by an even amount, the quantity's even-or-odd character is preserved across all operations. This is exactly the condition required for a parity invariant to hold — and it directly licenses impossibility conclusions when start and target have different parities."

- question: "Why is a parity argument more powerful than attempting to show impossibility by trial and error or exhaustive search?"
  type: short-answer
  answer: "A parity argument proves impossibility in one step for all possible paths simultaneously. It does not matter how many paths exist or how complex they are — if the parity invariant is violated between the start state and the target state, no path can bridge the gap. Exhaustive search, by contrast, only proves impossibility if you can check every possible path, which becomes computationally infeasible (or literally infinite) for large configuration spaces. The invariant argument sidesteps the search entirely by identifying a structural property that no sequence of allowed operations can alter."
  explanation: "This is the core advantage of invariant-based proofs in combinatorics and algorithms. The mutilated chessboard has an astronomical number of possible domino-placement sequences; no one could check them all. The parity argument collapses that complexity to a single two-line observation. The same principle scales: parity invariants are a special case of general invariant and monovariant arguments used throughout competitive mathematics and the analysis of algorithms."
```

## Explainer

From your work with modular arithmetic, you know that every integer is congruent to either 0 or 1 modulo 2 — it is either even or odd. A **parity invariant** is a quantity whose parity doesn't change as a process unfolds. If you can show that (1) a quantity has even parity at the start, (2) every allowed operation preserves parity, and (3) the target state requires odd parity, then the target is unreachable — regardless of how clever the path is. This is one of the cleanest proof techniques in all of combinatorics.

The classic example is the mutilated chessboard: remove two diagonally opposite corners of an 8×8 board, leaving 62 squares. Can you tile it perfectly with 31 dominoes? A domino always covers exactly one black square and one white square. The two removed corners are both the same color (say, both white), leaving 32 black squares and 30 white squares. Since every domino covers one of each, after placing any number of dominoes the difference (black covered − white covered) changes by 1 each time. To cover all remaining squares, you'd need 32 black and 30 white covered — but you need 31 dominoes covering 31 black and 31 white. The **parity of the color imbalance** is invariant, and the target requires a different parity. Tiling is impossible.

Parity arguments also appear in puzzles involving state changes. Suppose you have 15 coins all showing heads, and each move flips exactly 3 coins. After any number of moves, has the parity of heads changed? Each move changes 3 coins: each flip toggles one coin, changing the count of heads by +1 or −1. Three such changes alter the total by an odd amount. So after each move, the parity of the number of heads flips. Starting from 15 (odd), after an even number of moves you have an odd number of heads, and after an odd number of moves an even number. You can never reach exactly 0 heads in an even number of moves.

The power of parity arguments is their simplicity: you don't need to enumerate possibilities or construct an impossibility proof by exhaustion. You identify the right invariant, verify it's truly preserved, and derive the contradiction in one step. The same idea scales to more general **monovariant** and **invariant** arguments — a foundational technique in combinatorics and algorithms.
