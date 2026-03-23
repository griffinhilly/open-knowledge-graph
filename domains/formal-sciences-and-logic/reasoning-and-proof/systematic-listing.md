---
id: systematic-listing
title: Systematic Listing
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: sorting-and-classifying
    type: soft
  - id: what-is-an-argument
    type: soft
  - id: number-sequences-patterns
    type: soft
builds-toward:
  - proof-by-exhaustion-intro
  - pigeonhole-principle-introduction
  - working-backwards-strategy
tags: [problem-solving, enumeration, systematic, organization]
stage: abstract-reasoning
status: draft
---

# Systematic Listing

## Core Idea
Systematic listing is the strategy of organizing all possible cases in a structured way to ensure nothing is missed. Rather than listing possibilities randomly and hoping to find them all, you follow a systematic rule — alphabetical order, increasing size, fixing one variable at a time — that guarantees completeness. This strategy is the foundation of proof by exhaustion (checking every case) and combinatorial reasoning (counting all possibilities). The key insight: if your listing method is systematic, you can be confident your enumeration is complete.

## How It's Best Learned
Start with a concrete problem: "How many ways can you make 25 cents using pennies, nickels, and dimes?" List systematically by starting with the largest coin: 2 dimes + 1 nickel, 2 dimes + 5 pennies, 1 dime + 3 nickels, ... down to 25 pennies. Then introduce tree diagrams for counting ordered outcomes (e.g., outfits from 3 shirts and 2 pants). Emphasize the discipline: fix one choice, list all options for the remaining choices, then change the fixed choice.

## Common Misconceptions
- Believing you can just "think of all the cases" without a system. For small problems this works, but for anything with more than a handful of cases, unsystematic listing misses possibilities.
- Counting the same case twice because it appears under different headings. A good systematic listing has non-overlapping categories.
- Confusing listing (writing out every case) with counting (determining how many cases exist). Listing is sometimes necessary, but often you can count without listing by using multiplication rules.

## Questions

```yaml
- question: "How many two-digit numbers can be formed using the digits {1, 2, 3} if digits can be repeated?"
  type: multiple-choice
  options: ["3", "6", "9", "12"]
  answer: 2
  explanation: "Systematically: fix the first digit and list all second digits. First digit 1: 11, 12, 13. First digit 2: 21, 22, 23. First digit 3: 31, 32, 33. That is 9 numbers total. Alternatively, 3 choices for the first digit × 3 choices for the second digit = 9. The systematic listing confirms the multiplication principle."

- question: "When listing all possible outcomes systematically, the order in which you list them affects whether the list is complete."
  type: true-false
  answer: false
  explanation: "Any systematic order (alphabetical, numerical, by fixed variable) will produce the same complete list — the order of listing does not change what is on the list. What matters is that the system covers every possibility without gaps or duplicates. Different orderings are equally valid as long as they are exhaustive."

- question: "List all subsets of {a, b, c} systematically."
  type: short-answer
  answer: "Systematically by size: Size 0: {}. Size 1: {a}, {b}, {c}. Size 2: {a,b}, {a,c}, {b,c}. Size 3: {a,b,c}. Total: 8 subsets."
  explanation: "Organizing by size guarantees completeness. Within each size, listing in alphabetical order ensures no subset is missed or duplicated. The total count 2³ = 8 confirms the listing is complete. This systematic approach — fix one organizing principle (size), then systematically vary within that (alphabetical order) — scales to larger sets."
```

## Explainer

Systematic listing is less a mathematical technique and more a mathematical habit of mind. It is the discipline of organizing possibilities so that you can be certain your enumeration is complete. In everyday life, you might list grocery items by wandering the aisles; in mathematics, you need a system that guarantees nothing is missed.

The simplest systematic strategy is fixing and varying. Suppose you want to list all two-letter "words" from the alphabet {A, B, C}. Fix the first letter as A and vary the second: AA, AB, AC. Fix the first letter as B: BA, BB, BC. Fix the first letter as C: CA, CB, CC. Nine words, systematically arranged, with no gaps and no duplicates. The key is that you exhausted all choices for the second letter before moving to the next choice for the first letter.

Tree diagrams make this strategy visual. Each branch of the tree represents a choice, and each path from root to leaf represents one complete outcome. For the two-letter words, the tree has three branches at the top level (A, B, C) and each branches into three again (A, B, C). The number of leaves — 3 × 3 = 9 — is the count of outcomes. Tree diagrams scale well because the branching structure automatically enforces the fix-and-vary strategy.

Why does this matter for reasoning and proof? Because proof by exhaustion requires checking every case, and you cannot check every case unless you can list every case. If someone asks "prove that no two-digit number formed from {1, 2, 3} with repeated digits is divisible by 7," your systematic listing gives you the nine candidates (11, 12, 13, 21, 22, 23, 31, 32, 33), and you can check each one. Without the systematic list, you might miss a case and leave a hole in your proof.

Systematic listing also reveals when counting shortcuts are available. If you have 5 shirts and 4 pants, listing all 20 outfits is tedious but possible. The multiplication principle (5 × 4 = 20) gives the count instantly. But the multiplication principle is trustworthy only because the underlying listing is systematic — each shirt pairs with each pair of pants exactly once. The shortcut works because the systematic structure guarantees it. As problems get larger, you will rely increasingly on counting principles rather than explicit listing, but the systematic listing remains the conceptual foundation that makes those principles valid.
