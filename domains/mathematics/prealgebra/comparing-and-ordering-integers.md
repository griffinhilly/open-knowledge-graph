---
id: comparing-and-ordering-integers
title: Comparing and Ordering Integers
domain: mathematics
course: prealgebra
prerequisites:
  - id: integers-and-number-line
    type: hard
builds-toward:
  - absolute-value
  - one-step-inequalities
tags: [integers, comparing, ordering, number-line]
stage: abstract-reasoning
status: validated
---

# Comparing and Ordering Integers

## Core Idea
Comparing integers means determining which is greater, lesser, or if they are equal using the symbols <, >, and =. On the number line, the number further to the right is always greater. This is straightforward for positive numbers but requires careful reasoning with negatives: −2 > −8 because −2 is to the right of −8 on the number line, even though 2 < 8. Ordering integers means arranging a set from least to greatest (or greatest to least). This skill is prerequisite for understanding inequalities, number line representations of solutions, and data ordering for statistics.

## How It's Best Learned
Always reference the number line when comparing negatives. Use temperature analogies: −2 degrees is warmer than −8 degrees, so −2 > −8. Practice ordering mixed sets of positive and negative integers. Include zero in comparisons. Use inequality symbols and verbal descriptions interchangeably.

## Common Misconceptions
- Thinking −8 > −2 because 8 > 2 — students apply whole-number thinking to negative numbers.
- Confusing the direction of inequality symbols (the "alligator mouth" opens toward the larger number).
- Forgetting that zero is greater than all negative numbers.

## Questions

```yaml
- question: "A student claims that −8 > −2 because 8 is greater than 2. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is using the wrong inequality symbol"
    - "The student is applying whole-number magnitude thinking to negative numbers, which reverses the actual comparison"
    - "The student forgot that negative numbers cannot be compared with inequality symbols"
    - "Nothing — the student is actually correct"
  answer: 1
  explanation: "This is the most common misconception when comparing negative integers. On the number line, −2 is to the RIGHT of −8, which means −2 is greater. 'Greater' means 'further right on the number line,' not 'larger absolute value.' With negative numbers, the one closer to zero (smaller absolute value) is the greater number. Temperature is a good check: −2°F is warmer than −8°F, so −2 > −8."

- question: "Which of the following correctly orders the set {−3, 4, −7, 0, −1} from least to greatest?"
  type: multiple-choice
  options:
    - "4, 0, −1, −3, −7"
    - "−7, −3, −1, 0, 4"
    - "−1, −3, −7, 0, 4"
    - "−7, −1, −3, 0, 4"
  answer: 1
  explanation: "Least to greatest means moving from left to right on the number line. Among negatives, the most negative (furthest left) comes first: −7 is furthest left, then −3, then −1. Zero is in the middle. Then positive numbers: 4. The key is that among negatives, the one with the largest absolute value is the LEAST. Option B (−7, −3, −1, 0, 4) is correct."

- question: "On the number line, −5 is to the right of −9, so −5 > −9."
  type: true-false
  answer: true
  explanation: "This is correct. The number line rule is simple and absolute: whichever number is further to the right is greater. −5 is closer to zero than −9, placing it to the right of −9. So −5 > −9, even though 5 < 9 in terms of absolute value. Using the number line as a visual anchor eliminates the confusion that comes from thinking about magnitude alone."

- question: "Among negative integers, the one with the larger absolute value is the greater number."
  type: true-false
  answer: false
  explanation: "This is the central misconception for negative number comparisons. Among negatives, larger absolute value means further from zero, which means further LEFT on the number line — which means LESS, not greater. −8 has a larger absolute value than −2, but −8 < −2. The correct rule: among negatives, the one with the SMALLER absolute value (closer to zero) is the greater number."

- question: "Explain why −2 > −8, even though 2 < 8. Use the number line in your explanation."
  type: short-answer
  answer: "On the number line, −2 is closer to zero and sits to the RIGHT of −8. 'Greater' means 'further right,' not 'larger absolute value.' With negative numbers, being closer to zero means being less negative — which is higher on the scale. A useful analogy: −2°F is warmer (closer to freezing) than −8°F. The absolute values follow the opposite order of the numbers themselves when both are negative."
  explanation: "This question targets the core insight: the number line gives meaning to 'greater than' that the absolute-value intuition reverses for negative numbers. Students who can explain this in their own words genuinely understand the concept rather than having memorized a rule."
```

## Explainer

You already know how to place integers on the number line — positives to the right of zero, negatives to the left. Comparing integers is simply reading that number line: whichever number sits further to the right is **greater**. The symbols < (less than) and > (greater than) record which direction you would travel to get from one number to the other. If you're at −3 and need to move right to reach 5, then −3 < 5.

The tricky part is applying this to two negative numbers. Take −2 and −8. On the number line, −2 is closer to zero — it's further to the right. So −2 > −8, even though 2 < 8. The key insight: with negative numbers, the one with the smaller absolute value (closer to zero) is the greater number. Temperature is a perfect analogy — −2 degrees is warmer (closer to freezing) than −8 degrees. "Greater" doesn't mean "bigger absolute value"; it means "further right on the number line."

Zero occupies a special role: it is greater than every negative number and less than every positive number. This means when ordering a mixed set like {−5, 3, 0, −1, 7}, you can use zero as an anchor. All negatives go left of zero, all positives go right, and you order within each group by magnitude going outward: −5, −1, 0, 3, 7.

To order a large set efficiently, try this approach: first separate negatives from positives, then order the positives by size (smallest to largest), then order the negatives by reversing their size (largest absolute value is least). Finally, place zero in the middle. Combining these into a single sorted list gives you the ordering from least to greatest. The inequality symbols then let you express any comparison: −5 < −1 < 0 < 3 < 7 reads as a chain, each number less than the next.
