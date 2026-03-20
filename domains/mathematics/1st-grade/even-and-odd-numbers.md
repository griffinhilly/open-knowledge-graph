---
id: even-and-odd-numbers
title: Even and Odd Numbers
domain: mathematics
course: 1st-grade
prerequisites:
- id: skip-counting-by-2s
  type: hard
tags:
- number-properties
- patterns
stage: pre-formal
status: draft
---

# Even and Odd Numbers

## Core Idea
Even numbers (2, 4, 6, 8...) can be split into two equal groups; odd numbers (1, 3, 5, 7...) cannot. Recognizing this property helps with number classification and patterns.

## Questions

```yaml
- question: "You have 9 blocks and try to split them into two equal groups. What happens, and what does it tell you about 9?"
  type: multiple-choice
  options:
    - "You get two groups of 4 with 1 leftover — so 9 is odd"
    - "You get two groups of 4 and one group of 1 — so 9 is even"
    - "You can make two groups of 4.5, so 9 is even"
    - "You cannot tell whether 9 is even or odd without counting to 10 first"
  answer: 0
  explanation: "Even numbers split perfectly into two equal groups with nothing left over. Nine cannot do this — you get 4 and 4 with 1 block left without a partner. That leftover is the defining mark of an odd number. Option B describes the same result but misclassifies it; options C and D reflect confusion about what 'splitting into equal groups' means."

- question: "Sarah says: 'When I add two odd numbers, I should get an odd answer — because odd plus odd feels like it should stay odd.' Is she right?"
  type: multiple-choice
  options:
    - "Yes — odd + odd = odd, because odd numbers never become even"
    - "No — odd + odd = even, because each odd number's one leftover pairs up with the other's leftover"
    - "It depends on which odd numbers you pick"
    - "It alternates — sometimes odd, sometimes even"
  answer: 1
  explanation: "Every odd number has exactly one 'leftover' object that can't find a pair. When you add two odd numbers, their two leftovers pair with each other, leaving nothing unpaired — so the result is even. For example: 3 + 5 = 8 (even), 7 + 1 = 8 (even). The counterintuitive result follows directly from the 'leftover' definition."

- question: "The number 100 is even because when you split 100 objects into two groups, each group gets exactly 50 with none left over."
  type: true-false
  answer: true
  explanation: "This is exactly the definition of even. The 'ends in 0' shortcut also tells us 100 is even, but the underlying reason is the equal-pairing property. Any number that forms two perfectly equal groups with zero leftovers is even — and 50 + 50 = 100 with nothing remaining."

- question: "Zero is an odd number because there are no objects to pair up."
  type: true-false
  answer: false
  explanation: "Zero is even. The test is: can you split the objects into two equal groups with no leftovers? Zero objects split into two groups of zero — that's 0 + 0 = 0, with nothing left over. Zero fits the 'no leftovers' definition perfectly, so it is even. It also fits the last-digit rule: 0 ends in 0, which is on the even list."

- question: "Why is the sum of two odd numbers always even? Use the 'leftover' idea in your explanation."
  type: short-answer
  answer: "Every odd number has exactly one object that cannot find a partner when you try to split the group into pairs. When you add two odd numbers, each brings one 'lonely' leftover. Those two leftovers pair with each other, so the combined total has no unpaired objects remaining — making the sum even."
  explanation: "The leftover framework makes the result feel inevitable rather than arbitrary. A student who only memorized 'odd + odd = even' without understanding why will forget it or misapply it; a student who understands the pairing logic can reconstruct the rule from scratch."
```

## Explainer

You already know how to skip-count by 2s: 2, 4, 6, 8, 10... That counting pattern is exactly the list of **even numbers**. Every number you land on when you skip-count by 2s is even. The numbers you skip over — 1, 3, 5, 7, 9... — are **odd numbers**. So the two lists take turns: odd, even, odd, even, going up forever.

Here's the best way to understand what "even" really means: if you have an even number of things, you can split them into two perfectly equal groups with nothing left over. 8 apples split into two groups of 4 — no leftovers. 6 split into two groups of 3 — no leftovers. But try it with 7: you get two groups of 3 and one apple left over. That leftover is what makes 7 odd. **Even means pairs with no leftovers; odd means one is always left alone.**

You can use this idea to check any number. Take 10 objects and try pairing them up — do they all pair? Yes, 10 is even. Take 9 — one ends up without a partner. 9 is odd. Another quick trick: look at the last digit of any number. If it ends in 0, 2, 4, 6, or 8, the number is even. If it ends in 1, 3, 5, 7, or 9, it's odd. That's why 100 is even and 101 is odd, even though they're big numbers.

Even and odd numbers show up in patterns everywhere. When you add two even numbers, you always get an even number. When you add two odd numbers, you also get an even number. But when you add one even and one odd, you get an odd number. You don't have to memorize these rules — you can figure them out from the "leftover" idea. Two odd numbers each have one leftover, and those two leftovers pair up, leaving nothing extra. That's why odd + odd = even. Noticing patterns like this is what mathematics is really about.
