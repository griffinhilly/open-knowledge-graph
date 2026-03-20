---
id: commutative-property-multiplication-3rd
title: Commutative Property of Multiplication
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-introduction-equal-groups
  type: hard
- id: multiplication-introduction-arrays
  type: soft
builds-toward:
- associative-property-multiplication
- distributive-property
tags:
- multiplication
- properties
- commutative
stage: concrete-operations
status: draft
---

# Commutative Property of Multiplication

## Core Idea
The commutative property states that 3 × 4 = 4 × 3. The order of factors does not change the product. Visualized with arrays: a 3-by-4 rectangular arrangement rotated 90° becomes 4-by-3, containing the same number of squares.

## Questions

```yaml
- question: "You know that 7 × 9 = 63. Using only the commutative property, which other multiplication fact do you automatically know?"
  type: multiple-choice
  options:
    - "7 × 10 = 70, because 9 and 10 are close"
    - "9 × 7 = 63, because order of factors does not change the product"
    - "63 ÷ 7 = 9, because multiplication and division are related"
    - "14 × 9 = 126, because doubling one factor doubles the product"
  answer: 1
  explanation: "The commutative property states that a × b = b × a — switching the order of factors gives the same product. So knowing 7 × 9 = 63 immediately and automatically tells you 9 × 7 = 63. Option C is true but requires the inverse relationship between multiplication and division — a different property, not the commutative property alone."

- question: "A word problem says: 'There are 5 shelves, each holding 8 books.' A student writes 8 × 5 = 40 instead of 5 × 8 = 40. Is the student's answer correct?"
  type: multiple-choice
  options:
    - "No — the problem says 5 shelves with 8 books each, so only 5 × 8 is valid"
    - "Yes — the commutative property guarantees the product is the same regardless of order"
    - "No — 8 × 5 means 8 shelves with 5 books, which is a different total"
    - "Only if the student explains why the order was switched"
  answer: 1
  explanation: "The commutative property guarantees 5 × 8 = 8 × 5 = 40, so the numerical answer is correct either way. The physical setup described in the problem (5 groups of 8) is different from 8 groups of 5, but the total count is identical. The commutative property applies to the numerical product — the answer 40 is correct regardless of which order is written."

- question: "The commutative property of multiplication means that 3 × 4 and 4 × 3 describe the same physical situation."
  type: true-false
  answer: false
  explanation: "The commutative property guarantees the same *product* (3 × 4 = 4 × 3 = 12), but the two expressions can describe different physical situations. Three groups of four is a different arrangement than four groups of three — even though both total 12. In a word problem, the order of factors carries meaning about the real-world setup. The property is about numerical equality, not situational identity."

- question: "Because of the commutative property, a student who knows 8 × 6 = 48 automatically knows 6 × 8 = 48 without any extra work."
  type: true-false
  answer: true
  explanation: "This is precisely what the commutative property delivers. Every fact in the multiplication table appears twice — once as a × b and once as b × a — but both give the same product. Knowing one immediately gives you the other for free. This is why the commutative property effectively cuts the number of unique multiplication facts in half."

- question: "Why does the commutative property cut the number of multiplication facts you need to memorize roughly in half?"
  type: short-answer
  answer: "Because a × b = b × a, every fact in the times table appears twice — for example, 3 × 7 and 7 × 3 are the same fact written in a different order. Once you know one, you know the other automatically. So the multiplication table is symmetric: every entry above the diagonal mirrors one below it, and you only need to learn one of each pair."
  explanation: "This halving is why the commutative property is one of the most practically useful properties in arithmetic. A student who grasps this can approach an unfamiliar fact (like 9 × 4) by recalling the more familiar version (4 × 9 = 36) — then flip it. The property isn't just a rule to recite; it's a memory shortcut with real daily value."
```

## Explainer

You've seen multiplication as equal groups: 3 × 4 means three groups of four objects. Now consider arranging those 12 objects into a rectangle — three rows of four. If you turn that rectangle sideways, you see four rows of three. The rectangle hasn't changed size or shape, but now it looks like four groups of three instead of three groups of four. Both arrangements contain exactly 12 objects. That visual fact is the **commutative property**: switching the order of the two factors doesn't change the product.

Written as a rule: a × b = b × a for any whole numbers a and b. This has real practical value. If you've memorized that 8 × 3 = 24, you automatically know that 3 × 8 = 24 without any extra work. In fact, the commutative property is why the multiplication table is symmetric — every entry above the diagonal mirrors an entry below it. You only need to learn roughly half the unique facts.

The property also gives you flexibility when computing. If 9 × 2 feels unfamiliar, reframe it as 2 × 9 and skip-count by twos. If 7 × 4 seems hard, try 4 × 7 and count by fours instead. The commutative property is a license to pick whichever order is easier for your thinking in a given moment.

It's worth being precise about what the property says and doesn't say. It says the **product** is the same — not that the two expressions describe the same situation. Three groups of four kids is a different physical setup from four groups of three kids, even though both count to 12. In a word problem, the order of factors sometimes carries real-world meaning. But numerically, the result is always identical, and that's the property you'll use repeatedly when building fluency, simplifying expressions, and later working in algebra.
