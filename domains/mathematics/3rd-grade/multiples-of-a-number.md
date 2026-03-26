---
id: multiples-of-a-number
title: Multiples of a Number
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-within-100
  type: hard
- id: skip-counting-by-2s
  type: soft
- id: skip-counting-by-5s
  type: soft
builds-toward:
- factors-and-multiples
- prime-and-composite-numbers
- arithmetic-patterns-3rd
tags:
- multiples
- multiplication
- patterns
- number-theory
stage: concrete-operations
status: validated
---

# Multiples of a Number

## Core Idea
Multiples of a number are the products of that number and any whole number: the multiples of 4 are 4, 8, 12, 16, 20, … Listing multiples is equivalent to skip-counting by that number. Recognizing multiples builds fluency with multiplication facts and lays groundwork for later concepts like LCM.

## How It's Best Learned
Have students circle multiples on a hundreds chart for different numbers and look for patterns. Compare the charts for 2 and 4 — all multiples of 4 are also multiples of 2.

## Common Misconceptions
- Students confuse multiples with factors. A multiple is always greater than or equal to the original number (or equal if multiplied by 1).
- Zero is a multiple of every number (0×n = 0), which surprises students.

## Questions

```yaml
- question: "A student asked to list the multiples of 6 writes: 1, 2, 3, 6. What mistake did they make?"
  type: multiple-choice
  options:
    - "They forgot to include 0 and 12"
    - "They listed the factors of 6, not the multiples"
    - "They confused 6 with an even number"
    - "They counted backward instead of forward"
  answer: 1
  explanation: "The student listed the factors of 6 (the numbers that divide evenly into 6) rather than the multiples (the numbers you get by multiplying 6 by whole numbers). The multiples of 6 are 6, 12, 18, 24, 30... — found by skip-counting by 6 or computing 6×1, 6×2, 6×3, and so on. Factors and multiples are related but opposite: factors of a number are smaller or equal to it, while multiples are greater than or equal to it."

- question: "Which statement correctly describes the multiples of 7?"
  type: multiple-choice
  options:
    - "The list of multiples of 7 eventually ends when you run out of multiplication facts"
    - "All multiples of 7 are odd numbers"
    - "The multiples of 7 are 7, 14, 21, 28, 35... continuing without end"
    - "The multiples and factors of 7 are the same numbers"
  answer: 2
  explanation: "Multiples go on forever because you can always multiply 7 by a larger whole number to get another multiple — there is no largest one. Option A is wrong because multiplication facts are just a starting list; the concept extends infinitely. Option B is wrong because multiples of 7 include even numbers (14, 28, 42...). Option D confuses multiples with factors: the factors of 7 are only 1 and 7 (since 7 is prime), while its multiples are the infinite list 7, 14, 21..."

- question: "Every multiple of 6 is also a multiple of 3."
  type: true-false
  answer: true
  explanation: "True. Because 6 = 2 × 3, any number produced by multiplying 6 by a whole number automatically contains 3 as a factor. For example: 6×4 = 24, and 24 = 3×8. This is a general pattern: if one number is a multiple of another (6 is a multiple of 3), then all multiples of the larger number are also multiples of the smaller one. Exploring these patterns on a hundreds chart makes them visually obvious."

- question: "A multiple of a number is typically smaller than the number itself."
  type: true-false
  answer: false
  explanation: "False — it's the opposite. Multiples of a number are always greater than or equal to the number (the first multiple is n×1 = n itself, and all others are larger). It is *factors* that are smaller than or equal to the number. This is the most persistent confusion between factors and multiples: factors divide in, multiples build out."

- question: "12 is both a multiple of 4 and a multiple of 3. A student asks: 'Does that make 12 special?' How would you explain what this means mathematically?"
  type: short-answer
  answer: "12 is a common multiple of 4 and 3 — a number that appears in both their multiple lists. This is significant because it means 12 can be divided evenly by both 3 and 4. The smallest number that two numbers share as a multiple is called the least common multiple (LCM), which becomes important when adding fractions with different denominators."
  explanation: "When two numbers share a multiple, that shared value lies at an intersection of their multiplication patterns. For 3 and 4, the common multiples are 12, 24, 36... (every multiple of 12). Understanding common multiples is the foundation for finding least common denominators — so recognizing that 12 appears in both the 3-list and the 4-list is not trivial, but a preview of a core fractions skill."
```

## Explainer

You already know your multiplication facts and have practiced skip-counting by 2s and 5s. **Multiples** bring those two skills together under a single name: the multiples of a number are exactly the values you land on when skip-counting by that number, which are also exactly the entries in that number's row in the multiplication table.

Consider the number 4. Skip-count by fours: 4, 8, 12, 16, 20, 24... These are the multiples of 4. You can also find them from multiplication facts: 4×1=4, 4×2=8, 4×3=12, and so on. Both approaches produce the same list because skip-counting is just repeated addition, and multiplication is a compact way to express repeated addition. This means you have already memorized multiples for every number from 1 through 10 — they are your multiplication facts in disguise.

Multiples have one striking property: they go on forever. Unlike the factor list of a number (which is finite and eventually runs out), you can always find a larger multiple by multiplying by a bigger whole number. The multiples of 4 never stop at 40 or 400 — you can always multiply by a larger number to get another one.

Exploring patterns within multiple lists reveals something deeper about how numbers relate to each other. Notice that every multiple of 4 is also a multiple of 2: 4, 8, 12, 16 are all even. This makes sense because 4 = 2 × 2, so anything built by multiplying by 4 is automatically also divisible by 2. When two different numbers share multiples — like 4 and 6 both having 12 in their lists — those shared values are called **common multiples**, an idea you will use when working with fractions.
