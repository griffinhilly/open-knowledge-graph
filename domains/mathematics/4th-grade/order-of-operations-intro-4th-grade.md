---
id: order-of-operations-intro-4th-grade
title: Introduction to Order of Operations
domain: mathematics
course: 4th-grade
prerequisites:
  - id: multi-digit-multiplication
    type: hard
  - id: multi-digit-addition
    type: hard
builds-toward:
  - order-of-operations
  - writing-numerical-expressions
tags: [arithmetic, algebra-readiness, operations]
stage: concrete-operations
status: validated
---

# Introduction to Order of Operations

## Core Idea
When an expression contains more than one operation, the order in which you perform them matters: 3 + 4 x 2 equals 11 (multiply first) not 14 (add first). The conventional order is: (1) parentheses first, (2) multiplication and division from left to right, (3) addition and subtraction from left to right. At fourth grade, students work primarily with the first three operations and parentheses, saving exponents for later grades. The key understanding is that order of operations is a convention that ensures everyone interprets the same expression the same way -- it is the "grammar" of mathematical notation.

## How It's Best Learned
Start by showing that different orders give different answers: "Does 2 + 3 x 4 equal 20 or 14?" Establish the need for a shared convention. Introduce parentheses as "do this first" markers. Practice evaluating expressions step by step, underlining or circling the operation to perform next. Avoid over-relying on mnemonics (PEMDAS) without understanding -- students often misinterpret them.

## Common Misconceptions
- Performing operations strictly left to right without regard to multiplication/division priority.
- Thinking multiplication always comes before division (they are equal priority, evaluated left to right).
- Similarly, thinking addition always comes before subtraction.
- Ignoring or misplacing parentheses.

## Questions

```yaml
- question: "Evaluate: 20 ÷ 4 × 2"
  type: multiple-choice
  options:
    - "2.5 — because PEMDAS puts multiplication before division, so compute 4 × 2 = 8 first, then 20 ÷ 8"
    - "10 — because division and multiplication have equal priority; evaluate left to right: (20 ÷ 4) × 2 = 5 × 2"
    - "40 — because you multiply all numbers together before dividing"
    - "5 — because division always comes first: 20 ÷ 4 = 5, then discard the × 2"
  answer: 1
  explanation: "Multiplication and division have equal priority — neither comes before the other. When both appear without parentheses, evaluate left to right: 20 ÷ 4 = 5, then 5 × 2 = 10. The most common mistake is reading PEMDAS as 'M before D always,' which gives the wrong answer of 2.5. The mnemonic lists M before D, but they are equal partners evaluated left to right."

- question: "A student means to compute (3 + 4) × 2 but accidentally writes 3 + 4 × 2. What does the written expression equal, and how does it differ from what the student intended?"
  type: multiple-choice
  options:
    - "Both expressions equal 14 — parentheses do not change the answer when addition and multiplication are involved"
    - "The written expression gives 11 (multiply first: 4 × 2 = 8, then 3 + 8 = 11); the intended expression gives 14 (add first: 3 + 4 = 7, then 7 × 2 = 14)"
    - "The written expression gives 14 (add first); the parentheses version gives 11"
    - "Both expressions give 11 — addition and multiplication can be performed in any order"
  answer: 1
  explanation: "Without parentheses, multiplication wins: 3 + 4 × 2 = 3 + 8 = 11. With parentheses, addition happens first: (3 + 4) × 2 = 7 × 2 = 14. The parentheses changed the answer by 3. This is precisely why parentheses exist — when you want addition done before multiplication, you must write the parentheses explicitly. Leaving them out changes the meaning of the expression."

- question: "Parentheses in a mathematical expression indicate that the operations inside them should be performed before following the standard order of operations."
  type: true-false
  answer: true
  explanation: "Parentheses are the tool for overriding default priority. Anything inside parentheses is evaluated first, regardless of what operations appear outside them. (5 + 3) × 4 means 'add first, then multiply' — the parentheses say so explicitly. Without them, multiplication would happen first by default, giving a different answer."

- question: "According to the order of operations, multiplication should generally be performed before division when both appear in an expression."
  type: true-false
  answer: false
  explanation: "Multiplication and division have equal priority. When both appear in an expression (without parentheses), they are evaluated left to right — whichever appears first from left to right is done first. In 20 ÷ 4 × 2, division comes first (left to right): 20 ÷ 4 = 5, then 5 × 2 = 10. Treating division as lower priority gives the wrong answer of 2.5. The same equal-priority rule applies to addition and subtraction."

- question: "Why does mathematics need a shared order of operations? What problem would arise without it?"
  type: short-answer
  answer: "Without a shared convention, the same expression could be correctly evaluated to different answers by different people. For example, 3 + 4 × 2 could equal 11 (multiply first) or 14 (add first) depending on which order someone chose. Math only works as a shared language when the same notation produces the same result for everyone."
  explanation: "Order of operations is fundamentally a social agreement — the grammar of mathematical notation. Just as grammatical rules ensure 'the cat ate the fish' and 'the fish ate the cat' mean different things, order of operations ensures 3 + 4 × 2 means exactly one thing. Without it, engineers, scientists, and students would get different answers from identical formulas, making mathematical communication impossible."
```

## Explainer

You know how to add, subtract, and multiply multi-digit numbers. Now imagine reading the expression 3 + 4 × 2. Two people could reasonably get different answers: one might add first to get 7, then multiply to get 14; another might multiply first to get 8, then add to get 11. Both followed valid arithmetic steps — but they got different answers from the same expression. This is a problem. Math only works as a shared language if everyone reads the same expression the same way.

**Order of operations** is the agreement mathematicians made to fix this ambiguity. The rule: multiplication and division are performed before addition and subtraction. So 3 + 4 × 2 means 3 + (4 × 2) = 3 + 8 = 11, always. Think of multiplication as "tighter binding" than addition — it grabs its neighbors first. Addition and subtraction are weaker ties; they connect whatever is left after multiplication and division have been resolved.

**Parentheses** let you override the default order. Writing (3 + 4) × 2 means "add first, then multiply" — the parentheses announce: do this part first. Result: 7 × 2 = 14. Parentheses are the tool for saying "I really do want the addition done first here." Without them, multiplication wins. With them, you're in charge. Whenever you want to force a different order, use parentheses.

The mnemonic PEMDAS (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) can help you remember the hierarchy, but it hides an important detail: M and D are equal partners, evaluated left to right, not M before D always. Same for A and S. So 20 ÷ 4 × 2 is done left to right: (20 ÷ 4) × 2 = 5 × 2 = 10, not 20 ÷ (4 × 2) = 20 ÷ 8 = 2.5. Work through expressions step by step — circle the operation to do next, evaluate it, rewrite, repeat — until you build the habit of seeing priority before calculating.
