---
id: invariants-and-monovariants-intro
title: Invariants and Monovariants
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: direct-proof-introduction
    type: hard
  - id: proof-by-contradiction-introduction
    type: soft
  - id: conjectures-and-testing
    type: soft
builds-toward:
  - when-is-something-proven
  - loop-design-and-invariants
tags: [invariants, monovariants, problem-solving, proof]
stage: abstract-reasoning
status: validated
---

# Invariants and Monovariants

## Core Idea
An invariant is a quantity or property that never changes as a process runs, no matter what moves or steps are taken. A monovariant is a quantity that changes in only one direction — it can only increase, or only decrease, but never reverses. Both are powerful proof tools. If you can show an invariant has a certain value at the start and a different value at the proposed end, you have proven the end state is unreachable. If you can show a monovariant decreases with each step and is bounded below, you have proven the process must eventually stop. These concepts turn many "is it possible?" questions into clean proofs.

## How It's Best Learned
Start with the classic checkerboard puzzle: remove two opposite corners of an 8×8 board. Can you tile the remaining 62 squares with dominoes? Each domino covers one black and one white square, so the number of black minus white squares covered is always 0 — that is the invariant. But two opposite corners have the same color, so the remaining board has 30 of one color and 32 of the other. The invariant (equal coverage) cannot match the board (unequal colors), so tiling is impossible. For monovariants, use the Euclidean algorithm: at each step, the remainder decreases, and it cannot go below 0, so it must terminate.

## Common Misconceptions
- Confusing "I cannot see how to do it" with "it is impossible." Invariant arguments prove impossibility rigorously, not just by failure to find a solution.
- Thinking any quantity that happens to stay constant is a useful invariant. A useful invariant is one whose constancy (or one-directional change) actually constrains the problem. The challenge is identifying the right invariant.
- Assuming monovariants always decrease by 1. A monovariant can decrease by varying amounts — the key is that it always decreases and is bounded below (or always increases and is bounded above).

## Questions

```yaml
- question: "You start with a pile of 100 coins. At each step, you split any pile into two smaller piles and write down the product of the two pile sizes. After all splits, you have 100 piles of 1 coin each. What is the sum of all the products you wrote down?"
  type: multiple-choice
  options: ["99", "100", "4950", "5050"]
  answer: 2
  explanation: "The invariant is the sum of the squares of all pile sizes minus the sum of the products recorded. Or more directly: consider that the sum of all products always equals (100 choose 2) = 4950, regardless of how you split. You can verify with a small example: 3 coins, split into 2+1 (product 2), then split 2 into 1+1 (product 1). Total: 3. And (3 choose 2) = 3. The invariant ensures the answer is always 4950."

- question: "A monovariant is a quantity that can increase or decrease, but not both, during a process."
  type: true-false
  answer: true
  explanation: "A monovariant changes in only one direction. If it can only decrease, each step reduces it. If it can only increase, each step raises it. Combined with a bound (a floor for decreasing, a ceiling for increasing), this guarantees the process terminates — the monovariant can only change finitely many times before hitting the bound."

- question: "A 3×3 grid is filled with +1 and -1. At each step, you choose a row or column and flip all signs in it. Can you reach a grid where all entries are +1, starting from a grid with exactly one -1?"
  type: short-answer
  answer: "No. The invariant is the product of all nine entries. Initially, the product is -1 (eight +1s and one -1). Flipping a row or column flips 3 entries, which multiplies the product by (-1)³ = -1. So each step multiplies the total product by -1, alternating between -1 and +1. The all-+1 grid has product +1. Starting from -1, after any even number of steps the product is -1, and after any odd number it is +1. But we need the grid to be all +1s, which requires the product to be +1 AND all entries to be +1. However, having the right product does not guarantee the right configuration. The deeper invariant is that the product changes between -1 and +1, but reaching all +1s from a single -1 is impossible because the parity of the number of -1s changes by an odd number each step (1 or 3 entries flip), so the parity of the count of -1s changes at each step. Starting with 1 (odd), after one step you have 0 or 2 or 4 (even) negative entries, then odd again, etc. You need 0 (even) -1s. After an odd number of steps you have odd count, after even you have even. So it is possible after an even number of steps to have 0 negative entries — but the product invariant shows this is impossible since the product after an even number of steps is -1, which means an odd number of -1s. Contradiction. Therefore it is impossible."
  explanation: "The product of all entries is the key invariant. Each row/column flip changes exactly 3 signs, multiplying the total product by (-1)³ = -1. Starting at -1, the product alternates -1, +1, -1, +1, ... The target (all +1s) has product +1, achievable only after an odd number of steps. But to get all +1s, we also need every entry individually to be +1. The invariant narrows the search space and, combined with more detailed analysis, proves impossibility."
```

## Explainer

Some of the most satisfying proofs in mathematics answer the question "is this possible?" with a definitive no — and they do it by finding a quantity that constrains what can happen. That quantity is an invariant if it never changes, or a monovariant if it only moves in one direction.

Consider the classic mutilated checkerboard problem. An 8×8 checkerboard has 32 black squares and 32 white squares. Remove two opposite corners — both the same color, say both white. You are left with 30 white and 32 black squares. Can you tile the remaining 62 squares with 31 dominoes, each covering exactly two adjacent squares? The key observation: every domino, no matter how you place it, covers exactly one black square and one white square. So the number of black squares covered always equals the number of white squares covered. This is the invariant. But to tile the board, you would need to cover 32 black and 30 white — unequal numbers. The invariant makes this impossible. No amount of cleverness can overcome a mathematical invariant.

Monovariants solve a different type of problem: they prove that processes must terminate. The Euclidean algorithm for finding the greatest common divisor repeatedly replaces the larger number with the remainder when dividing. At each step, the remainder is smaller than the divisor, so the sequence of remainders is a monovariant — it strictly decreases. Since remainders are non-negative integers, the sequence cannot decrease forever. It must eventually reach 0, at which point the algorithm stops and the last non-zero remainder is the GCD.

Finding the right invariant or monovariant is the creative challenge. There is no algorithm for this — it requires insight about the problem's structure. Common places to look: parity (is a count even or odd?), sums, products, colorings, modular arithmetic (what is the quantity mod 2? mod 3?). The checkerboard problem uses a coloring invariant. The coin-splitting problem uses an algebraic invariant. The Euclidean algorithm uses a size monovariant. Each problem has its own natural invariant, and part of the art of mathematics is learning to see it.

The general principle is this: if you want to prove something is impossible, find a quantity that the rules of the problem prevent from changing (or only allow to change in one direction), and show that the start and end states disagree on that quantity. If the invariant says "this property stays the same forever" and the target state has a different value of that property, the target is unreachable — not because you tried and failed, but because the mathematics forbids it.
