---
id: probability-with-combinatorics-probability-and-statistics
title: Probability with Combinatorics
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: counting-principles
  type: hard
- id: sample-spaces-and-events
  type: hard
builds-toward:
- binomial-distribution
- poisson-distribution
tags:
- combinatorics
- probability
- counting
stage: formal-systems
status: draft
---

# Probability with Combinatorics

## Core Idea
When outcomes are equally likely, P(A) = (number of favorable outcomes) / (total number of outcomes). Combinatorial counting techniques (permutations, combinations) enable efficient calculation of outcome counts for complex scenarios. This approach is powerful for computing probabilities in problems involving selection, arrangement, and distribution.

## How It's Best Learned
Practice recognizing when permutations vs. combinations apply. Solve problems by first counting favorable outcomes, then total outcomes.

## Common Misconceptions
Using combinations when permutations are needed (or vice versa). Assuming all outcomes are equally likely in situations where they are not (non-uniform sample spaces).

## Questions

```yaml
- question: "A combination lock requires entering 3 digits from {1, 2, 3, 4, 5} in a specific order, with no repetition. How many valid codes are there, and which counting tool applies?"
  type: multiple-choice
  options:
    - "10, using combinations C(5,3) — because you're just choosing 3 digits from 5"
    - "60, using permutations P(5,3) — because a different sequence of the same digits opens a different lock"
    - "6, using 3! — because only the arrangements of 3 chosen digits matter"
    - "125, using 5³ — because each of 3 positions can independently be any of 5 digits"
  answer: 1
  explanation: "Order matters: the code 1-2-3 and 3-2-1 are different sequences that open different locks (or no lock). When order matters among distinct items selected without repetition, permutations apply: P(5,3) = 5×4×3 = 60. Combinations C(5,3) = 10 would count only the 10 distinct sets of digits, ignoring order — appropriate if the lock accepted any ordering of 3 chosen digits, which it does not. Option D ignores the no-repetition constraint."

- question: "A committee of 4 students is chosen at random from a class of 25. What is the correct count of possible committees, and why?"
  type: multiple-choice
  options:
    - "P(25,4) = 303,600 — because who holds which committee role matters"
    - "C(25,4) = 12,650 — because the committee has no ordered roles; any group of 4 people is one committee regardless of selection order"
    - "25⁴ = 390,625 — because each of 4 positions can be filled by any of 25 students"
    - "25! — because all arrangements of the class must be considered"
  answer: 1
  explanation: "A committee is an unordered group — {Alice, Bob, Carol, Dan} is the same committee regardless of who was chosen first. When order does not matter, combinations apply: C(25,4) = 25!/(4! × 21!) = 12,650. Permutations P(25,4) would be correct if the 4 positions were distinguishable (president, vice-president, etc.), but a generic committee has no such ordering. This is the most common error in probability with combinatorics: using permutations when the selection is inherently unordered."

- question: "The probability formula P(A) = (number of favorable outcomes)/(total number of outcomes) is valid for any sample space, regardless of whether the outcomes are equally likely."
  type: true-false
  answer: false
  explanation: "This formula is valid only when all outcomes in the sample space are equally likely. For a fair die, each face has probability 1/6, so counting faces works. But a weighted die, or a sample space where outcomes have different probabilities (e.g., drawing from a bag with different numbers of colored balls and counting by color), requires assigning individual probabilities rather than counting uniformly. Applying the counting formula to a non-uniform space produces wrong answers. Recognizing when the equally-likely assumption holds is as important as knowing how to count."

- question: "Choosing a 5-card poker hand from a deck of 52 and arranging 5 people in a row for a photograph both involve selecting 5 items from a larger set, so both problems use the same counting formula."
  type: true-false
  answer: false
  explanation: "The distinction is whether order matters. For a poker hand, {A♠, K♠, Q♠, J♠, 10♠} dealt in any order is the same hand — combinations apply: C(52,5) = 2,598,960. For a photograph, the arrangement matters: Alice-Bob-Carol-Dan-Eve in a row is different from Eve-Alice-Bob-Carol-Dan. This requires permutations: P(52,5) or equivalently C(52,5) × 5! when selecting and then arranging. The surface similarity ('choose 5 from a set') conceals whether the order of selection or arrangement is meaningful."

- question: "You want to find the probability of being dealt a 5-card hand with exactly two aces from a standard 52-card deck. Describe the counting approach: what goes in the numerator, what goes in the denominator, and why combinations are used rather than permutations."
  type: short-answer
  answer: "Denominator: C(52,5) = 2,598,960 — the total number of possible 5-card hands, where order doesn't matter. Numerator: C(4,2) × C(48,3) — choose exactly 2 of the 4 aces (C(4,2) = 6 ways), then choose 3 non-ace cards from the remaining 48 (C(48,3) = 17,296 ways). Combinations are used because a hand is an unordered set: the same 5 cards constitute the same hand regardless of the order they were dealt. P(exactly two aces) = (6 × 17,296) / 2,598,960 ≈ 0.0399."
  explanation: "The structure of the problem is: count favorable outcomes (hands with exactly 2 aces) divided by total outcomes (all 5-card hands). Breaking the numerator into two independent choices — which 2 aces, and which 3 non-aces — and multiplying uses the multiplication principle. Combinations appear throughout because card hands are inherently unordered; permutations would overcount by treating each ordering of the same 5 cards as a distinct hand."
```
