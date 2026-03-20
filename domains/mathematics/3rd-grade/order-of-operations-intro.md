---
id: order-of-operations-intro
title: Order of Operations Introduction
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-threes-through-nines
  type: soft
builds-toward:
- order-of-operations
tags:
- operations
- order
- conventions
stage: concrete-operations
status: draft
---

# Order of Operations Introduction

## Core Idea
When expressions include multiple operations, a convention ensures everyone computes the same answer: multiplication and division before addition and subtraction, left to right. So 2 + 3 × 4 = 2 + 12 = 14, not 5 × 4 = 20.

## Questions

```yaml
- question: "What is the value of 2 + 3 × 4?"
  type: multiple-choice
  options:
    - "20 — add 2 + 3 first to get 5, then multiply by 4"
    - "14 — multiply 3 × 4 first to get 12, then add 2"
    - "24 — multiply all three numbers together"
    - "9 — add all three numbers: 2 + 3 + 4"
  answer: 1
  explanation: "The correct answer is 14. By convention, multiplication is performed before addition. So 3 × 4 = 12 first, then 2 + 12 = 14. Option A (20) is the result of adding first — the most common error, and the exact wrong answer the order-of-operations convention was created to prevent."

- question: "Why did mathematicians agree on an order of operations?"
  type: multiple-choice
  options:
    - "Because multiplication is more important than addition in real-world applications"
    - "So that everyone computes the same answer from the same expression — without a shared convention, the same problem has multiple 'correct' answers"
    - "Because calculators were invented and needed a built-in rule to follow"
    - "Because addition must always be done last so it can include all the multiplication results"
  answer: 1
  explanation: "Order of operations is a convention — an agreed-upon standard, not a mathematical law derived from deeper truths. Without it, 2 + 3 × 4 could legitimately equal either 14 or 20, depending on which operation you do first. The convention eliminates that ambiguity so that mathematical expressions communicate the same meaning to everyone."

- question: "In the expression 12 ÷ 4 × 3, you should divide first (left to right), giving 3 × 3 = 9."
  type: true-false
  answer: true
  explanation: "When operations have the same priority level (both multiplication and division, or both addition and subtraction), you evaluate left to right. So 12 ÷ 4 = 3, then 3 × 3 = 9. Doing the multiplication first (4 × 3 = 12, then 12 ÷ 12 = 1) gives the wrong answer. Left-to-right is the tiebreaker for equal-priority operations."

- question: "Parentheses in a math expression are optional — the answer is the same whether or not you include them."
  type: true-false
  answer: false
  explanation: "Parentheses override the default order of operations. (2 + 3) × 4 = 20, while 2 + 3 × 4 = 14. These are different expressions with different values. Parentheses are not decoration — they are punctuation that changes meaning, just as punctuation changes meaning in written language."

- question: "Why does 2 + 3 × 4 equal 14 and not 20? Explain the rule that determines which operation is done first."
  type: short-answer
  answer: "By the order-of-operations convention, multiplication is performed before addition. So in 2 + 3 × 4, you compute 3 × 4 = 12 first, then add 2 to get 14. If you added first (2 + 3 = 5, then 5 × 4 = 20), you would get a different answer. The convention ensures everyone computes the same result from the same expression."
  explanation: "The order of operations is a shared grammatical rule for mathematical expressions. Multiplication before addition is the convention, not a logical necessity — but it is universally agreed upon so that expressions are unambiguous. Parentheses can override this order when a different sequence is intended."
```

## Explainer

Here is a problem that seems simple: what is 2 + 3 × 4? If you add first, you get 5 × 4 = 20. If you multiply first, you get 2 + 12 = 14. Both paths follow the symbols on the page — yet they produce different answers. Mathematics cannot have two correct answers to the same question, so mathematicians agreed on a **convention**: an agreed-upon rule that everyone follows, not because one way is mathematically superior, but because having a shared standard makes communication unambiguous. The convention says: multiply and divide before you add and subtract.

The reason multiplication is prioritized over addition is partly historical convention and partly practical: multiplication is a form of repeated addition, and treating it as a single operation before combining with other additions keeps expressions compact and useful. When you write 3 + 4 × 2, you mean "3, plus 4 groups of 2," which is 3 + 8 = 11. Writing (3 + 4) × 2 means something different — add first, then double the result — and parentheses are available precisely for those situations. **Parentheses** override the default order: whatever is inside parentheses is computed first, regardless of the operations involved.

When expressions contain only addition and subtraction, or only multiplication and division, you evaluate left to right — just as you read. So 12 ÷ 4 × 3 = 3 × 3 = 9 (not 12 ÷ 12 = 1). Left-to-right evaluation is the tiebreaker when operations have the same priority level. At this introductory stage, most problems involve multiplication combined with addition or subtraction, so the essential rule is: find all the multiplications first, compute them, then handle the additions and subtractions.

Understanding order of operations is not about memorizing a mnemonic — it is about understanding that mathematical expressions are a language with grammar. Just as a sentence's meaning depends on word order and punctuation, an expression's value depends on the order operations are applied. This grammar becomes essential when you write and interpret algebraic expressions in later grades, where the conventions you learn now will be taken for granted.
