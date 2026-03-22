---
id: independence-and-multiplication-rule
title: Independence and the Multiplication Rule
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
- id: probability-axioms
  type: hard
builds-toward:
  - binomial-distribution
  - random-variables-intro
tags:
- independence
- multiplication-rule
- dependent-events
stage: formal-systems
status: draft
---
# Independence and the Multiplication Rule

## Core Idea
Two events A and B are independent if P(A|B) = P(A), meaning knowledge of B does not change the probability of A. For independent events, P(A ∩ B) = P(A) × P(B). The multiplication rule generalizes to: P(A ∩ B) = P(A) × P(B|A) for any events, which is essential for computing probabilities of sequences of outcomes.

## How It's Best Learned
Contrast independent scenarios (flipping two coins) with dependent ones (drawing cards without replacement). Verify independence by checking if P(A|B) = P(A).

## Common Misconceptions
Assuming events are independent when they are not (e.g., weather today and tomorrow). Confusing 'mutually exclusive' with 'independent'.

## Questions

```yaml
- question: "A student draws one card from a shuffled 52-card deck, notes it is a king, and does not replace it. What is the probability that the second card drawn is also a king?"
  type: multiple-choice
  options:
    - "4/52, because each draw is an independent event"
    - "3/51, because knowledge of the first draw changes the probability for the second"
    - "1/13, because kings always appear at a fixed rate"
    - "0, because two kings cannot be drawn in sequence"
  answer: 1
  explanation: "Because the card is not replaced, the two draws are dependent: knowing the first card was a king changes the composition of the remaining deck (51 cards, 3 kings). So P(2nd king | 1st king) = 3/51 ≠ 4/52. Option A is the misconception — treating draws without replacement as independent. Independence requires that P(A|B) = P(A), which fails here."

- question: "Events A and B satisfy P(A ∩ B) = 0, and both P(A) > 0 and P(B) > 0. Which of the following must be true?"
  type: multiple-choice
  options:
    - "A and B are independent"
    - "A and B are mutually exclusive and therefore not independent"
    - "A and B are independent because they share no outcomes"
    - "A and B are both equally probable"
  answer: 1
  explanation: "P(A ∩ B) = 0 means A and B are mutually exclusive — they cannot both occur. But this makes them maximally dependent, not independent: if A occurs, you know with certainty that B did not (P(B|A) = 0 ≠ P(B)). Mutual exclusivity and independence are essentially opposite concepts. Independence requires that P(A|B) = P(A), which is violated whenever two positive-probability events are mutually exclusive."

- question: "If two events are independent, they cannot both occur at the same time."
  type: true-false
  answer: false
  explanation: "That describes mutual exclusivity, not independence. Independent events can absolutely co-occur — flipping heads on a coin and rolling an even number on a die are independent, and both happen 25% of the time. Independence means P(A|B) = P(A): knowing one event occurred gives no information about the other. Mutual exclusivity means P(A ∩ B) = 0: knowing one occurred tells you the other definitely did not."

- question: "Two mutually exclusive events with positive probability are independent."
  type: true-false
  answer: false
  explanation: "If A and B are mutually exclusive, P(A ∩ B) = 0. But P(A) · P(B) > 0 since both events have positive probability. Therefore P(A ∩ B) ≠ P(A) · P(B), which means A and B are not independent. Equivalently, P(B|A) = 0 ≠ P(B), so knowing A occurred tells you B definitely did not — the opposite of independence."

- question: "Why does the formula P(A ∩ B) = P(A) · P(B) only work when A and B are independent, and what formula applies in the general case?"
  type: short-answer
  answer: "P(A) · P(B) is derived from the definition of independence: P(A|B) = P(A). Substituting into the definition of conditional probability gives P(A ∩ B) = P(A) · P(B). When events are dependent, P(A|B) ≠ P(A), so this simplification is invalid. The general multiplication rule — P(A ∩ B) = P(A) · P(B|A) — applies whether or not events are independent; when they are independent, P(B|A) = P(B) and it reduces to the product formula."
  explanation: "The product rule is a special case, not the general rule. The mistake of applying P(A) · P(B) to dependent events (like card draws without replacement) gives wrong answers because it ignores how the occurrence of A changes the probability of B. The general multiplication rule forces you to account for that dependency explicitly."
```

## Explainer

You've studied conditional probability: P(A|B) = P(A ∩ B)/P(B) tells you how the probability of A changes when you learn B occurred. **Independence** is the special case where learning B tells you nothing new about A — P(A|B) = P(A). Plugging this into the definition of conditional probability immediately gives P(A ∩ B) = P(A) · P(B). This elegant formula is both the formal definition of independence and its most useful computational tool: to find the probability that two independent events both occur, simply multiply their individual probabilities.

The most persistent confusion is between **independence** and **mutual exclusivity**. Mutually exclusive events cannot both occur: P(A ∩ B) = 0, which means if P(A) and P(B) are both positive, knowing A occurred tells you with certainty that B did not — they are maximally dependent. Truly independent events can absolutely both occur: flipping heads on two successive coin flips are independent events that both happen 25% of the time. If two events are mutually exclusive and have positive probability, they are *not* independent. The two concepts are almost opposites.

For sequences of outcomes, the **general multiplication rule** P(A ∩ B) = P(A) · P(B|A) applies whether or not A and B are independent. When they are independent, P(B|A) = P(B) and the formula simplifies to the product rule. When they are dependent, the conditional probability must be carried explicitly. Drawing cards without replacement is the canonical dependent example: P(first card is an ace) = 4/52; P(second card is an ace | first was an ace) = 3/51, not 4/52. The joint probability is (4/52)(3/51) ≠ (4/52)². Replacing the card between draws restores independence.

Independence extends to multiple events: A₁, A₂, ..., Aₙ are **mutually independent** if every subset satisfies the product formula — not just pairs. Pairwise independence is not enough to guarantee mutual independence (there are mathematical counterexamples). For mutually independent events, P(A₁ ∩ A₂ ∩ ... ∩ Aₙ) = P(A₁) · P(A₂) · ... · P(Aₙ), which you'll use constantly: in the binomial distribution (each trial independent), in computing probabilities of repeated experiments, and across all of statistical modeling where the i.i.d. (independent and identically distributed) assumption is the foundation of inference.
