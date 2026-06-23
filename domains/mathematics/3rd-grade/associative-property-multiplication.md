---
id: associative-property-multiplication
title: Associative Property of Multiplication
domain: mathematics
course: 3rd-grade
prerequisites:
- id: commutative-property-multiplication
  type: hard
- id: multiplication-facts-within-100
  type: hard
- id: commutative-property-multiplication-3rd
  type: soft
builds-toward:
- two-digit-by-one-digit-multiplication
- multi-digit-multiplication
tags:
- associative
- properties
- multiplication
- grouping
stage: concrete-operations
status: validated
---

# Associative Property of Multiplication

## Core Idea
The associative property of multiplication states that grouping factors differently does not change the product: (2×3)×4 = 2×(3×4) = 24. This allows students to choose the most convenient grouping when multiplying three or more numbers. It is the foundation for mental multiplication strategies.

## How It's Best Learned
Use volume or 3D arrays — a 2×3×4 box of unit cubes can be grouped as (2×3) layers of 4, or 2 slabs of (3×4). Numerical examples with three small factors work well before formalizing.

## Common Misconceptions
- Students confuse associative (regrouping) with commutative (reordering).
- Some students think the parentheses must always be evaluated first and don't see that they can choose a more convenient grouping.

## Questions

```yaml
- question: "A student needs to multiply 4 × 5 × 7. She groups it as (4 × 5) × 7 = 20 × 7 = 140, choosing to multiply 4 and 5 first because 20 is easy to work with. Which property justifies this choice?"
  type: multiple-choice
  options:
    - "Commutative property — she swapped two of the numbers"
    - "Associative property — she chose which pair of numbers to multiply first, without changing their positions"
    - "Distributive property — she split one number into smaller parts"
    - "Identity property — she multiplied by 1"
  answer: 1
  explanation: "The associative property says that the grouping of factors (which two you multiply first) does not change the product. She didn't swap any numbers' positions — 4 still comes before 5, which comes before 7. She only changed which multiplication to perform first by choosing the parentheses. That is exactly what associativity permits."

- question: "What is the key difference between the commutative property and the associative property of multiplication?"
  type: multiple-choice
  options:
    - "Commutative applies to addition; associative applies only to multiplication"
    - "Commutative lets you reorder factors (swap their positions); associative lets you regroup factors (choose which to multiply first, without swapping)"
    - "Commutative works with two factors; associative only works with four or more"
    - "There is no real difference — both say you can rearrange numbers freely"
  answer: 1
  explanation: "Commutative: 3 × 4 = 4 × 3 — the numbers swap positions. Associative: (2 × 3) × 4 = 2 × (3 × 4) — the numbers stay in the same order, but the parentheses move to show a different pairing. Confusing them is the most common error with this property. In practice you often use both together, but they are logically distinct operations."

- question: "The associative property of multiplication says that you can swap the positions of two factors without changing the product."
  type: true-false
  answer: false
  explanation: "Swapping the positions of factors is the commutative property (3 × 4 = 4 × 3). The associative property is about regrouping — changing which pair of factors you multiply first — without moving any factor to a different position. (2 × 3) × 4 = 2 × (3 × 4): the order left-to-right is identical in both; only the parentheses (the grouping) changed."

- question: "Using the associative property to compute 4 × 5 × 7 as (4 × 5) × 7 = 20 × 7 = 140 gives the same answer as (4 × 7) × 5 = 28 × 5 = 140."
  type: true-false
  answer: true
  explanation: "The associative property guarantees that any grouping produces the same product. Both computations yield 140, even though (4 × 5) × 7 is typically easier because multiplying by 20 is simpler than multiplying by 28. The property gives you the freedom to pick the most convenient grouping — that freedom is its practical value."

- question: "Explain in your own words how the associative property lets you choose the most convenient grouping when multiplying three numbers, and give an example where a strategic choice makes the calculation significantly easier."
  type: short-answer
  answer: "The associative property says that when multiplying three numbers, it doesn't matter which two you multiply first — the product will always be the same. This means you can look for a pair that produces a round number or a fact you know well. For example, to compute 2 × 7 × 5: multiplying left to right gives (2 × 7) × 5 = 14 × 5 = 70, which works but requires a two-digit multiplication. Instead, group the 2 and 5 first: 2 × (7 × 5) — wait, that's still 2 × 35. Better: (2 × 5) × 7 = 10 × 7 = 70. Multiplying by 10 is trivial, making the calculation much easier."
  explanation: "The strategic value of the associative property is that it turns a potentially hard calculation into an easy one by choosing a grouping that produces a round number (multiples of 10, 100, etc.). This is the engine behind many mental multiplication tricks: look for pairs that make friendly products, then multiply by the third factor."
```

## Explainer

You already know the **commutative property**: 3 × 4 = 4 × 3 — the order of two factors does not matter. The **associative property** extends this idea to three or more factors: when you multiply three numbers, it does not matter which two you multiply first. (2 × 3) × 4 gives the same result as 2 × (3 × 4). Both equal 24. The parentheses tell you which multiplication to do first, but the final product is unchanged no matter how you group them.

The cleanest way to see why this is true is with a three-dimensional array — a box of unit cubes. Imagine a box that is 2 layers high, 3 rows wide, and 4 cubes deep. You can count those cubes by slicing the box different ways. Slice into 2 horizontal layers, each containing a 3-by-4 grid of 12 cubes: 2 × 12 = 24. Or slice into 4 depth layers, each containing a 2-by-3 grid of 6 cubes: 4 × 6 = 24. The same 24 cubes appear regardless of how you cut. The associative property is not a rule you memorize — it is a physical fact about how groups-within-groups combine.

The real power of the associative property is **choosing a convenient grouping**. Suppose you need to compute 4 × 7 × 5. Multiplying left to right gives (4 × 7) × 5 = 28 × 5 = 140. That is correct but requires you to multiply 28 × 5. Regroup instead: 4 × (7 × 5) = 4 × 35 = 140. Still correct, but harder. Try: (4 × 5) × 7 = 20 × 7 = 140. Multiplying by 20 is easy because 20 is a round number. The associative property gave you the freedom to pick the easiest path.

Notice the difference between associative and commutative: commutative lets you **reorder** (swap two factors' positions), while associative lets you **regroup** (change which multiplication you do first, without swapping anything). In practice, you use both together — commutativity lets you move the 5 next to the 4, then associativity lets you group them first. The two properties work as a team whenever you multiply three or more numbers, and that team is the engine behind mental multiplication strategies you will use throughout math.

