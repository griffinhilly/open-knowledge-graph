---
id: multiplication-facts-threes-through-nines
title: 'Multiplication Facts: 3s Through 9s'
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-twos-fives-tens
  type: hard
- id: multiplication-introduction-equal-groups
  type: hard
builds-toward:
- two-digit-by-one-digit-multiplication
- division-facts-within-100
tags:
- multiplication
- facts
- fluency
stage: concrete-operations
status: validated
---

# Multiplication Facts: 3s Through 9s

## Core Idea
Students master multiplication facts for 3s, 4s, 6s, 7s, 8s, and 9s through skip-counting, repeated addition, and arrays. Fluency with these facts (retrievable within 5 seconds) is essential for multi-digit multiplication and division.

## Questions

```yaml
- question: "You forget 8 × 7. Using the doubling strategy, which known fact gives you the most direct path to the answer?"
  type: multiple-choice
  options: ["4 × 7 = 28, then double it to get 56", "8 × 10 = 80, then subtract 8 + 8 + 8", "8 × 5 = 40, then add 8 + 8 + 8", "Skip-count by 8 seven times"]
  answer: 0
  explanation: "The doubling strategy says the 8s are the 4s doubled: since 4 × 7 = 28, then 8 × 7 = 56 (double 28). This requires knowing one simpler fact and performing one doubling — far faster than skip-counting. Options C and D work but are slower and more error-prone. Option B requires subtracting three 8s, which is harder than simply doubling 28."

- question: "A student uses the 9s digit pattern: 'The tens digit is one less than the factor, and the digits add up to 9.' She is solving 9 × 6. What is her answer?"
  type: multiple-choice
  options: ["54, because the tens digit is 5 (one less than 6) and 5 + 4 = 9", "63, because the tens digit is 6 and 6 + 3 = 9", "45, because the tens digit is 4 and 4 + 5 = 9", "56, because 9 is close to 10 and 10 × 6 = 60"]
  answer: 0
  explanation: "For 9 × 6: the tens digit is one less than the factor 6, which is 5. The ones digit must make the sum equal 9, so 9 − 5 = 4. Answer: 54. Option B applies the pattern incorrectly (using the factor itself as the tens digit). This pattern works for all 9× facts up to 9 × 9 — it's a reliable shortcut that doesn't require any other fact."

- question: "Knowing that 3 × 8 = 24 is enough to immediately find 6 × 8 using the doubling strategy."
  type: true-false
  answer: true
  explanation: "The 6s are the 3s doubled: 6 × 8 = 2 × (3 × 8) = 2 × 24 = 48. This works because multiplication distributes: 6 groups of 8 is the same as two sets of 3 groups of 8. The doubling strategy turns 6s into 3s, 4s into 2s, and 8s into 4s — meaning you can derive many unfamiliar facts from ones you already know."

- question: "A student who can always reconstruct 7 × 8 by skip-counting has achieved fluency with that fact."
  type: true-false
  answer: false
  explanation: "Fluency means automatic retrieval in 3–5 seconds — not reconstruction. Skip-counting by 7s to reach 56 takes considerably longer and demands significant working memory. Fluency matters because multiplication facts are used constantly inside larger procedures. If a student must reconstruct a basic fact mid-problem (e.g., during long division), it consumes cognitive resources that should go toward understanding the larger concept. The goal is instant recall, not the ability to derive."

- question: "What is 7 x 8? Show how you could figure it out if you forgot the answer."
  type: short-answer
  answer: "7 x 8 = 56. One way to figure it out: if you know 7 x 7 = 49, just add one more 7 to get 56. Another way: know that 4 x 8 = 32 and double it isn't right (that gives 64 which is 8 x 8), so instead use 7 x 4 = 28 and double it to get 56, since 7 x 8 = 7 x (4 x 2) = (7 x 4) x 2 = 28 x 2 = 56."
  explanation: "The best approach is to just know that 7 x 8 = 56 by heart. But when you forget, strategies help: you can build from a nearby fact you do know (like 7 x 7 = 49 + 7) or use doubling (7 x 4 = 28, doubled = 56). The goal is eventually to recall all multiplication facts automatically so you do not have to figure them out each time."
```

## Explainer

You already know the easiest multiplication facts: the 2s (doubles), the 5s (end in 0 or 5), and the 10s (append a zero). Those three families account for a large chunk of the multiplication table. Now you're filling in the rest — 3s, 4s, 6s, 7s, 8s, and 9s — and several of these can be learned by **building on facts you already know**, rather than memorizing each one from scratch.

The **doubling strategy** is the most powerful shortcut here. The 4s are just the 2s doubled: since 2 × 7 = 14, then 4 × 7 = 28 (double 14). The 6s are the 3s doubled: since 3 × 8 = 24, then 6 × 8 = 48. The 8s are the 4s doubled: since 4 × 6 = 24, then 8 × 6 = 48. If you're not sure of a fact, ask yourself: "Do I know half of this?" Double that answer. The **9s** have their own pattern: the digits of any 9× product (up to 9×9) always add up to 9, and the tens digit is always one less than the factor you multiplied by. So 9 × 7: the tens digit is 6 (one less than 7), and the ones digit is 3 (since 6 + 3 = 9), giving 63.

The 3s and 7s don't have as clean a pattern, but skip-counting and **arrays** still work. Visualize 3 × 6 as 3 rows of 6 dots — or count by 3s: 3, 6, 9, 12, 15, 18. For the 7s, if you know the commutative property (7 × 3 = 3 × 7), you already know most of the 7s from earlier fact families. The truly new facts in the 7s column are 7 × 7 = 49 and 7 × 8 = 56 — two that are worth extra practice.

The goal of this practice is genuine **fluency**: automatic recall within about 3–5 seconds, without needing to recount or reconstruct. This matters because multiplication facts are used constantly inside bigger procedures — multi-digit multiplication, long division, finding equivalent fractions, reducing fractions. Every moment you spend reconstructing a basic fact while doing a larger problem is cognitive energy that could go toward understanding the bigger idea. Fluency with these facts clears the way for everything that follows.
