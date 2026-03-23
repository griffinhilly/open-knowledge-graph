---
id: working-backwards-strategy
title: Working Backwards
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: what-is-an-argument
    type: hard
  - id: direct-proof-introduction
    type: soft
  - id: if-then-thinking
    type: soft
builds-toward:
  - proof-by-contradiction-introduction
  - invariants-and-monovariants-intro
tags: [problem-solving, strategy, reverse-reasoning, heuristic]
stage: abstract-reasoning
status: draft
---

# Working Backwards

## Core Idea
Working backwards is a problem-solving strategy where you start from the desired end result and reason back toward the starting conditions. Instead of asking "what happens next?" you ask "what must have come before?" This strategy is especially useful when the end state is known and specific but the path forward from the start is unclear. In mathematics, working backwards is used to discover proof strategies, solve equations, and analyze puzzles where the final answer is given and you need to reconstruct the process.

## How It's Best Learned
Start with a simple puzzle: "I think of a number, double it, add 5, and get 17. What was the number?" Working forward is trial-and-error; working backward is systematic: 17 → subtract 5 → 12 → divide by 2 → 6. Then progress to multi-step problems. Emphasize the key technique: reverse each operation. If the forward step is "add 5," the backward step is "subtract 5." Connect to solving algebraic equations, where "undoing" operations is the standard method.

## Common Misconceptions
- Thinking working backwards always gives a proof. It gives a discovery strategy — you still need to verify the answer by checking it works forward. The backward reasoning reveals the answer; the forward check confirms it.
- Reversing operations incorrectly. The reverse of "multiply by 3 then add 2" is "subtract 2 then divide by 3" — the order of operations also reverses.
- Assuming the strategy applies to every problem. Working backwards is most effective when the end state is clearly defined. For open-ended problems or problems with multiple possible end states, other strategies may be better.

## Questions

```yaml
- question: "A student starts with a number, multiplies by 3, subtracts 4, and gets 20. Working backwards, what is the original number?"
  type: multiple-choice
  options: ["5", "7", "8", "24"]
  answer: 2
  explanation: "Working backwards: start from 20. The last forward step was 'subtract 4,' so reverse it: 20 + 4 = 24. The step before that was 'multiply by 3,' so reverse it: 24 ÷ 3 = 8. Check forward: 8 × 3 = 24, 24 - 4 = 20. Confirmed."

- question: "When using the working backwards strategy, the reverse of 'divide by 2 then add 7' is 'subtract 7 then multiply by 2.'"
  type: true-false
  answer: true
  explanation: "When reversing a sequence of operations, you reverse both the operations themselves AND their order. The last operation applied forward ('add 7') is the first to be undone ('subtract 7'). The first operation applied forward ('divide by 2') is the last to be undone ('multiply by 2'). This is the same principle as unwinding a stack of function calls."

- question: "In a tournament, the final winner beat the player who beat the player who beat Player A. If the tournament is single-elimination and you know the final winner, explain how working backwards helps identify who Player A lost to."
  type: short-answer
  answer: "Start from the final winner. The winner beat someone in the final — identify that opponent. That opponent beat someone in the semifinal — identify who. That person beat Player A. Working backwards through the bracket from the known winner traces the chain of results to find exactly who eliminated Player A."
  explanation: "The bracket structure makes working backwards natural: each match has a known winner, and you can trace connections backward through the results. The end state (final winner) is specific and known, while the forward question (who will Player A lose to?) depends on many unknowns. This asymmetry — specific end, uncertain start — is exactly when working backwards excels."
```

## Explainer

Most problem-solving advice tells you to start at the beginning and work forward. But sometimes the end is clearer than the beginning, and the most efficient strategy is to start from the answer you want and reason backward to figure out how to get there. This is working backwards, and it is a powerful heuristic used across mathematics and puzzle-solving.

The simplest examples are "mystery number" puzzles. "I think of a number, add 7, multiply by 2, and get 30. What was my number?" Working forward, you would guess and check. Working backward, you reverse each operation in reverse order: 30 ÷ 2 = 15, then 15 - 7 = 8. The original number was 8. You can verify: 8 + 7 = 15, 15 × 2 = 30. The backward reasoning gave you the answer; the forward check confirmed it.

The key technique is reversing operations. Addition reverses to subtraction. Multiplication reverses to division. Squaring reverses to taking a square root. And crucially, the order of operations also reverses: if you "added 3, then multiplied by 5" going forward, you "divide by 5, then subtract 3" going backward. The last operation applied is the first to be undone, like taking off your shoes and socks — you put on socks first and shoes second, but you take off shoes first and socks second.

Working backwards is not limited to arithmetic puzzles. In proof-writing, it is one of the most common discovery strategies. If you need to prove that some expression equals zero, you might start from "equals zero" and ask "what algebraic manipulation would produce this?" You work backward from the conclusion to find the chain of steps, then write the proof forward. The backward reasoning discovers the proof; the forward presentation justifies it.

An important caveat: working backwards is a strategy for finding answers, not a substitute for verification. Not every backward chain is valid — some steps might not be reversible (squaring is not perfectly reversible because both 3² and (−3)² equal 9). Always check your answer by plugging it back into the original problem and verifying it works going forward. The backward strategy is a scaffold; the forward verification is the proof.
