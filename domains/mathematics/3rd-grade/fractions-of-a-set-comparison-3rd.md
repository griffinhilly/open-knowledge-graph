---
id: fractions-of-a-set-comparison-3rd
title: Fractions of Sets and Comparing Non-Unit Fractions
domain: mathematics
course: 3rd-grade
prerequisites:
- id: fractions-of-a-set
  type: hard
- id: unit-fractions-halves-thirds-fourths-3rd
  type: soft
builds-toward:
- adding-fractions-like-denominators
tags:
- fractions
- sets
- comparing
stage: concrete-operations
status: validated
---

# Fractions of Sets and Comparing Non-Unit Fractions

## Core Idea
A fraction can describe a part of a group (set). For example, 2/3 of 6 objects means 4 objects. Comparing fractions with the same denominator (e.g., 2/4 vs. 3/4) is straightforward: the one with more parts is larger.

## Questions

```yaml
- question: "A student says '3/8 is bigger than 3/4 because 8 is bigger than 4.' What misunderstanding does this reveal?"
  type: multiple-choice
  options:
    - "The student forgot to find a common numerator before comparing"
    - "The student compared the denominators correctly but forgot to consider the numerators"
    - "The student confused the roles of numerator and denominator — a larger denominator means each piece is smaller, so 3/8 has smaller pieces than 3/4, making 3/8 the lesser fraction"
    - "The student made an arithmetic error in the comparison"
  answer: 2
  explanation: "This is the most common fraction misconception: treating a larger denominator as meaning a larger fraction. The denominator defines the size of each equal piece — dividing a whole into 8 parts gives smaller pieces than dividing it into 4 parts. So 3/8 means 3 small pieces, while 3/4 means 3 larger pieces. Since the numerators are equal, 3/4 is greater. The denominator is not a count; it is the unit size. Larger denominator = smaller unit size."

- question: "To find 3/4 of 20, which process correctly applies the two roles of the numerator and denominator?"
  type: multiple-choice
  options:
    - "Multiply 20 × 4, then divide by 3"
    - "Divide 20 by 3 to form groups, then multiply by 4"
    - "Divide 20 by 4 (the denominator sets the group size), then multiply by 3 (the numerator picks how many groups): 5 × 3 = 15"
    - "Subtract 4 from 20 and add 3 to the result"
  answer: 2
  explanation: "The two-step method follows directly from the two roles in a fraction. The denominator (4) tells you how many equal groups to create: 20 ÷ 4 = 5 per group. The numerator (3) tells you how many of those groups to take: 3 × 5 = 15. The denominator acts first as a divisor (it divides the set), and the numerator acts second as a multiplier (it selects how many parts). Option A reverses the roles, which happens to give the same arithmetic result here (60 ÷ 4 = 15 = 20 ÷ 4 × 3) but misrepresents the conceptual structure."

- question: "When two fractions have the same denominator, the fraction with the larger numerator is always the larger fraction."
  type: true-false
  answer: true
  explanation: "When denominators match, every piece in both fractions is the same size — the denominator has established an identical unit. The only remaining question is how many of those same-sized pieces each fraction has, which is exactly what the numerator counts. 5/8 > 3/8 because both fractions use eighth-sized pieces, and 5 eighths is more than 3 eighths. This comparison rule — 'same denominator, compare numerators' — is reliable precisely because the unit size is held constant."

- question: "In a fraction, the denominator tells you how many pieces you have, and the numerator tells you how big each piece is."
  type: true-false
  answer: false
  explanation: "This reverses the two roles. The denominator defines the unit — it tells you the size of each equal piece (how many equal parts the whole is divided into). The numerator counts how many of those units you have. Think of it as: denominator = size of piece, numerator = number of pieces. So in 3/4, the 4 means each piece is one-quarter-sized, and the 3 means you have three of those quarter-sized pieces. Keeping these roles distinct is foundational for all future fraction work, including addition and multiplication."

- question: "In the fraction 3/4, what does the denominator (4) tell you, and what does the numerator (3) tell you? How do these two roles work together when you find 3/4 of a set of 20 objects?"
  type: short-answer
  answer: "The denominator (4) defines the unit — it tells you to divide the set into 4 equal groups, making each group the 'one-fourth' unit. The numerator (3) counts how many of those units you take. Working together on 20 objects: first, 20 ÷ 4 = 5 objects per group (the denominator creates equal groups); then, 3 × 5 = 15 objects (the numerator selects 3 of those groups). The denominator answers 'how big is one part?'; the numerator answers 'how many parts do I want?'"
  explanation: "This two-role framework is the key insight that makes fractions logical rather than arbitrary. The denominator is always doing a dividing job (setting the unit), and the numerator is always doing a counting job (selecting units). When comparing fractions with equal denominators, the denominator has already fixed the unit — so you only need to compare numerators. When finding a fraction of a set, the denominator divides first, and the numerator multiplies second. Both operations follow from understanding these two distinct roles."
```

## Explainer

You've already worked with fractions of a set — finding 1/3 of 12 marbles by dividing the total into 3 equal groups and taking 1 of them. Now you're extending that to **non-unit fractions**: fractions where the numerator is greater than 1, like 2/3, 3/4, or 5/6. The process is the same — you still divide the set into equal groups first — but now you take more than one group.

Here's the two-step method. To find 2/3 of 12: first, the denominator (3) tells you how many equal groups to make — divide 12 into 3 groups of 4. Second, the numerator (2) tells you how many of those groups to take — take 2 groups of 4, which is 8. So 2/3 of 12 = 8. Notice that 1/3 of 12 is 4 (one group), and 2/3 is just double that — 8. The fraction acts like an instruction: split into this many groups, then select this many of them.

Comparing fractions with the **same denominator** is now straightforward because the denominator sets the "size" of each piece. If two fractions have the same denominator, every piece is the same size — the only difference is how many pieces you have. So 3/4 vs. 2/4: both use quarter-sized pieces; 3/4 just has one more piece, so it's larger. When denominators match, comparing numerators tells you everything.

This rule breaks down when denominators are different, which is why same-denominator comparison is the starting point rather than the whole story. But for now, the key idea to carry forward is that a fraction has two jobs: the **denominator** defines the unit (the size of each equal part), and the **numerator** counts how many of those units you have. Keeping those two roles distinct — size vs. count — is the foundation for all future fraction work.
