---
id: division-introduction-grouping
title: 'Division: Grouping (Repeated Subtraction) Model'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: division-as-grouping
  type: hard
- id: repeated-addition-to-multiplication
  type: soft
builds-toward:
- division-facts-2nd-grade
tags:
- division
- grouping
- repeated-subtraction
stage: concrete-operations
status: draft
---

# Division: Grouping (Repeated Subtraction) Model

## Core Idea
Division by grouping answers: 'How many groups of this size can I make?' For example, 12 ÷ 4 asks 'How many groups of 4 are in 12?' The answer is 3 groups. This is the inverse of multiplication: 3 × 4 = 12, so 12 ÷ 4 = 3.

## How It's Best Learned
Make equal-sized groups until all objects are used, counting how many groups were made. Use arrays rotated to show grouping. Emphasize the connection to multiplication.

## Common Misconceptions
- Confusing the grouping model with the sharing model.
- Miscounting the number of groups created.
- Not recognizing that division undoes multiplication.

## Questions

```yaml
- question: "You have 20 stickers and want to put 5 stickers in each bag. Which question does this situation match?"
  type: multiple-choice
  options:
    - "How many stickers go in each bag? (sharing model — you know the number of bags)"
    - "How many bags can you fill? (grouping model — you know the group size)"
    - "How many stickers are left over after filling the bags?"
    - "How many bags do you need if each bag holds all 20 stickers?"
  answer: 1
  explanation: "This is the grouping model: you know how big each group is (5 stickers per bag) and want to find how many groups (bags) you can make. The sharing model works the opposite way — you know how many groups (bags) you want and divide evenly among them, asking 'how many per group?' Both models represent division, but the grouping model asks 'how many groups of this size can I make?' which is exactly the question here: 20 ÷ 5 = 4 bags."

- question: "Which multiplication fact most directly helps you solve 35 ÷ 7 = ?"
  type: multiple-choice
  options:
    - "7 + 5 = 12"
    - "35 − 7 = 28"
    - "7 × 5 = 35"
    - "7 × 35 = 245"
  answer: 2
  explanation: "Because division is the inverse of multiplication, 35 ÷ 7 = ? is the same question as 7 × ? = 35. If you know 7 × 5 = 35, then the answer is 5 immediately — no counting or subtracting needed. This is the key insight: every division problem has a corresponding multiplication equation, and knowing your multiplication facts gives you division facts for free. Option B (repeated subtraction) works but is slow; options A and D are unrelated."

- question: "The grouping model of division asks: 'How many groups of this size can be made?' — you know the group size and find the number of groups."
  type: true-false
  answer: true
  explanation: "This is the defining feature of the grouping model. You start with the total and the size of each group (e.g., groups of 4) and count how many complete groups you can form. This is different from the sharing model, where you start with the total and the number of groups, and find how many go in each group. Both are valid division, but they frame the question differently."

- question: "The grouping model and the sharing model of division always give different numerical answers for the same division problem."
  type: true-false
  answer: false
  explanation: "Both models always give the same quotient for the same division problem — they are two ways of understanding the same operation. For 12 ÷ 4: the grouping model says '4 items per group → 3 groups'; the sharing model says '4 groups → 3 items per group.' Both arrive at 3. The models differ in what you know and what you are finding, but the mathematics is identical. 12 ÷ 4 = 3 regardless of which model you use."

- question: "Explain the difference between the grouping model and the sharing model of division. Use 12 ÷ 4 to illustrate both."
  type: short-answer
  answer: "Grouping model: You know the group size (4) and find the number of groups. For 12 ÷ 4, you ask: 'How many groups of 4 can I make from 12?' Answer: 3 groups. Sharing model: You know the number of groups (4) and find the size of each. For 12 ÷ 4, you ask: 'If I share 12 equally among 4 groups, how many in each group?' Answer: 3 in each group. Both give 3, but they frame the question differently."
  explanation: "Understanding both models of division builds flexibility. Real-world situations call for different framings: 'How many bags of 4 can I fill?' is grouping; 'How do I share 12 cookies equally among 4 friends?' is sharing. Students who know only one model sometimes fail to recognize division in the other framing. Both models are also important for understanding why division is the inverse of multiplication."
```

## Explainer

You've learned that multiplication is repeated addition: 3 × 4 means "three groups of four," which equals 12. Division using the **grouping model** asks the reverse question: if you have 12 objects and want groups of 4, how many groups can you make? It's the same relationship, just run backwards — you start with the total and the group size, and find out how many groups fit.

Imagine you have 12 tiles and you want to make rows of 4. You lay out one row of 4, then a second, then a third — and you've used all 12 tiles in exactly 3 rows. You just showed that 12 ÷ 4 = 3. This is also called the **repeated subtraction** model: each time you subtract a group of 4 from your pile (12 → 8 → 4 → 0), you count one more group. When nothing remains, the count of groups is your quotient.

This grouping model is different from the **sharing model**, where you distribute objects one at a time into a fixed number of groups. In sharing, you know how many groups you want; in grouping, you know how big each group is. Both are valid division — they just answer different questions. Here you're asking "how many groups of this size?" rather than "how many in each group?"

The key insight is that multiplication and division are **inverse operations** — they undo each other. If 3 × 4 = 12, then 12 ÷ 4 = 3 and 12 ÷ 3 = 4. Recognizing this connection means you never have to start from scratch: instead of guessing how many groups of 7 fit into 35, you can ask "what number times 7 gives me 35?" and use what you know about multiplication to find the answer immediately.
